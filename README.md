🚀 Indian Startup Analysis

This project is all about exploring and analyzing the Indian startup ecosystem.
It takes raw data of startups and transforms it into a structured format for insights, while also allowing additional enrichment like adding founder information.

📂 Project Structure

app.py → Python script for running analysis/visualization

startup_cleaned_new.csv → Cleaned dataset of Indian startups

(Optional future file) startup_with_founder.csv → Dataset with founder names included

✨ Features

✔️ Cleaned dataset of Indian startups
✔️ Analysis-ready CSV file
✔️ Easy to enrich with additional details like founders, funding, investors
✔️ Python-based workflow (Pandas, etc.)

⚙️ How to Use

Clone this repository:

git clone https://github.com/vedantbhavsar17/indian-startup-analysis.git
cd indian-startup-analysis


Install required dependencies (if any):

pip install pandas


Run the analysis script:

python app.py


(Optional) Add founder data by preparing a CSV like this:

startup,founder
Ola,Bhavish Aggarwal
Paytm,Vijay Shekhar Sharma
Flipkart,Sachin Bansal & Binny Bansal


Then merge it with the main dataset using Pandas.

📊 Example Output

The enriched dataset (startup_with_founder.csv) will look like this:

startup,industry,investors,amount,date,founder
Ola,Transport,SoftBank,1000000,2015-01-01,Bhavish Aggarwal
Paytm,Fintech,Alibaba,500000,2016-05-12,Vijay Shekhar Sharma
Flipkart,Ecommerce,Tiger Global,2000000,2014-07-10,Sachin Bansal & Binny Bansal

🤝 Contributing

If you’d like to add more data (like founders, industries, or investors), feel free to fork the repo and create a pull request!

📌 Future Plans

Add more startup metadata (like location, sector, funding stage)

Build dashboards for visualization

Automate founder enrichment from APIs

👨‍💻 Author

Made with ❤️ by Vedant Bhavsar

Would you like me to generate a ready README.md file for you (so you can directly upload it to your repo), or do you just want this text to copy-paste?

You said:
yes
ChatGPT said:

Got it 👍 Since your project is about startup funding analysis with Streamlit, I’ll draft a clean README.md for you that explains how to set up, run, and use your app.

Here’s a first version:

Startup Funding Analysis

An interactive Streamlit dashboard to explore and analyze startup funding data. This project provides insights into investors, sectors, funding trends, and more.

📊 Features

Filter and analyze funding data by year, sector, city, and investor.

Visualize trends using interactive charts and tables.

Identify top investors and funding rounds.

Easy-to-use sidebar filters for custom exploration.

🛠️ Tech Stack

Python 3.8+

Streamlit for the interactive dashboard

Pandas for data manipulation

Matplotlib for visualization

🚀 Installation

Clone this repository:

git clone https://github.com/your-username/startup-funding-analysis.git
cd startup-funding-analysis


Create a virtual environment (recommended):

python -m venv venv
source venv/bin/activate   # On Mac/Linux  
venv\Scripts\activate      # On Windows  


Install dependencies:

pip install -r requirements.txt


Add your CSV dataset (e.g., startup_cleaned_new.csv) in the project folder.

▶️ Running the App

Start the Streamlit server:

streamlit run app.py

Then open your browser at http://localhost:8501
 to interact with the dashboard.

📂 Project Structure
startup-funding-analysis/
│-- app.py                  # Main Streamlit app  
│-- startup_cleaned_new.csv # Dataset  
│-- requirements.txt        # Python dependencies  
│-- README.md               # Project documentation  

📈 Example Insights

Top sectors receiving investments

Active investors and their portfolios

Yearly trends in funding rounds

📝 Notes

Make sure the dataset is clean and formatted correctly before running.

You can update the CSV with newer data for fresh insights.
