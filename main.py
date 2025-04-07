import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import argparse

# Set up command-line arguments
parser = argparse.ArgumentParser(description="Purchase Suggestion System")
parser.add_argument("--input", default="estoque_aleatorio.xlsx", help="Path to input Excel file")
parser.add_argument("--output", default="previsao_estoque.xlsx", help="Path to output Excel file")
args = parser.parse_args()

# Load data from Excel file
df = pd.read_excel(args.input)

# Simulate 90-day consumption history for each product
historico_consumo = []
num_dias = 90  # Analysis period (3 months)
for _, row in df.iterrows():
    nome_produto = row["nome_produto"]
    quantidade_inicial = row["quantidade_inicial"]
    # Generate random daily consumption based on initial stock
    consumo_diario = np.abs(np.random.normal(loc=quantidade_inicial/num_dias, scale=5, size=num_dias))
    datas = [datetime.now() - timedelta(days=i) for i in range(num_dias)]
    for data, consumo in zip(datas, consumo_diario):
        historico_consumo.append([nome_produto, data.strftime('%Y-%m-%d'), consumo])

# Create DataFrame for consumption history
df_consumo = pd.DataFrame(historico_consumo, columns=["nome_produto", "data", "consumo_diario"])

# Calculate average daily consumption per product
media_consumo = df_consumo.groupby("nome_produto")["consumo_diario"].mean().reset_index()

# Forecast consumption for 7 days and 3 months
media_consumo["previsao_7_dias"] = media_consumo["consumo_diario"] * 7
media_consumo["previsao_3_meses"] = media_consumo["consumo_diario"] * 90

# Merge with current stock data
media_consumo = media_consumo.merge(df[["nome_produto", "quantidade_atual"]], on="nome_produto")

# Calculate purchase needs (only positive values)
media_consumo["necessidade_compra"] = np.maximum(media_consumo["previsao_3_meses"] - media_consumo["quantidade_atual"], 0)

# Save results to Excel
media_consumo.to_excel(args.output, index=False)
print(f"File saved to {args.output}")