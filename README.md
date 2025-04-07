# 📊 Purchase Suggestion System: Inventory Automation with Python
Hey there! I’m Ygor Caixeta, and this is my **Purchase Suggestion System** project—an automation tool I built with a ton of passion for my data analyst and automation portfolio. 🚀 If you’re here, you probably love Python, data, and turning repetitive tasks into smart solutions. Let’s dive in—I’m excited to show you what this project is all about!

## 🌟 About the Project
This project came to life because I wanted to solve a real-world challenge: how can a company manage its inventory smarter and avoid running out of stock? I used Python to create an automation script that predicts product consumption, forecasts needs for 7 days and 3 months, and suggests how much to buy based on current stock levels. My goal was to take raw data and turn it into actionable insights—all with a few lines of code!

Here’s what you’ll find in this project:
- **Key Metrics**: Daily consumption averages, 7-day and 3-month forecasts, and purchase recommendations.
- **Detailed Analysis**: For example, if a product like "Produto_1" has a 3-month forecast of 499.88 units but only 297 in stock, it’ll suggest buying 202.88 more.
- **Automation**: It processes Excel data and spits out a ready-to-use purchase plan.

I wanted to build something practical—not just cool code, but a tool that could help spot inventory gaps and optimize stock management.

## 🎯 Why I Built This Project
I’m obsessed with data and how it can simplify life through automation. As a data analyst with a love for coding, I focus on turning numbers into solutions. This project let me flex my Python skills while showing what I can do: from handling data with Pandas to automating decisions that save time and effort.

This is part of my portfolio for data analyst and automation roles. I wanted to prove I can:
- Build efficient automation scripts with Python.
- Extract actionable insights (e.g., “Produto_19 needs 256 units to meet demand—time to reorder!”).
- Work with tools like Pandas and NumPy to process data smoothly.

## 📈 What You’ll Find in the Project
Here’s a sneak peek of what the script does:
- **Daily Consumption**: Calculates average daily usage per product (e.g., 5.55 units for Produto_1).
- **Forecasts**: Predicts needs for 7 days (e.g., 38.88 units) and 3 months (e.g., 499.88 units).
- **Stock Check**: Compares forecasts to current stock (e.g., 297 units for Produto_1).
- **Purchase Suggestions**: Outputs how much to buy (e.g., 202.88 units for Produto_1).
- **Excel Output**: Saves everything in a neat file (`previsao_estoque.xlsx`) for easy use.

**Example Insight**:  
“Produto_19’s 3-month forecast is 351.29 units, but we only have 95 in stock. Ordering 256 more units could prevent a shortage!”

## 🛠️ How I Used Python
Here’s a bit about the process—I think the “how” is just as exciting as the result:
- **Data Input**: I used Pandas to read inventory data from an Excel file (`estoque_aleatorio.xlsx`).
- **Simulation**: With NumPy, I simulated 90 days of consumption based on initial stock levels (randomized with a normal distribution for realism).
- **Calculations**: I calculated averages, forecasts, and purchase needs with simple Python logic.
- **Output**: The script saves the results back to Excel—ready for action!

The script is flexible too—you can tweak the input and output paths via command-line arguments.

## 🚀 How to Use the Project
Want to try it out? It’s super simple:
1. **Clone the Repository**:
  
   git clone https://github.com/ygorcaixeta/purchase-suggestion-system.git

2. **Install Dependencies**:
   Make sure you have Python 3.x, then run:

   pip install -r requirements.txt

3. **Run the Script**:
   Place your `estoque_aleatorio.xlsx` file in the folder, then:

   python main.py --input estoque_aleatorio.xlsx --output previsao_estoque.xlsx

4. **Check the Output**:
   Open `previsao_estoque.xlsx` to see the purchase plan!

If you don’t want to run it, I’ve included a sample input file in the repo so you can see how it works. 😊

## 💡 What I Learned
This project was a blast to build! Here’s what I took away:
- **Python Automation**: I got better at scripting with Pandas and NumPy to handle data efficiently.
- **Problem-Solving**: I learned to turn inventory challenges into automated solutions.
- **Code Flexibility**: Adding command-line arguments made the script way more user-friendly.
- **Data Insights**: I practiced digging into numbers to find practical takeaways.

## 🌱 How This Project Can Evolve
There’s always room to grow, and I’ve got some ideas:
- Add real consumption data instead of simulated values.
- Build a simple GUI with Tkinter for non-coders to use it.
- Include cost estimates for purchase suggestions.
Got feedback or ideas? I’d love to hear them—drop me a message or open an issue here!

## 📬 Get in Touch
If you enjoyed this project or want to talk about Python, data, or automation, here’s where to find me:
- **LinkedIn**: [Ygor de Freitas Caixeta](https://www.linkedin.com/in/ygor-de-freitas-caixeta-a0soowkskso/)
- **Email**: [ygorcaixeta@gmail.com](mailto:ygorcaixeta@gmail.com)

This project is a glimpse of what I can do with data and code. I’m pumped to keep learning, grow as an analyst and automator, and help businesses work smarter. Thanks for checking it out! 💙
