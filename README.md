🕷️ Automated Web Scraper with Scheduler
An automated web scraping application built with Python that periodically collects data from dynamic websites using Selenium and BeautifulSoup. The scraped data is stored in an SQLite database and can be exported to CSV for further analysis.

📌 Features
Scrape data from static and dynamic websites
Handle JavaScript-rendered pages with Selenium
Parse HTML using BeautifulSoup
Store scraped data in SQLite
Schedule automatic scraping tasks using Celery
Export data to CSV
Prevent duplicate entries
Error handling and logging
Modular and easy-to-maintain code structure
🛠️ Tech Stack
Python 3.x
Selenium
BeautifulSoup4
Celery
SQLite
Flask (Optional)
ChromeDriver
CSV
📂 Project Structure
AutomatedWebScraper/
│
├── app.py
├── scraper.py
├── database.py
├── scheduler.py
├── tasks.py
├── export_csv.py
├── config.py
├── requirements.txt
├── scraped_data.db
│
├── data/
│   └── output.csv
│
├── templates/
│   └── index.html
│
├── static/
│
└── README.md
⚙️ Installation
1. Clone the repository
git clone https://github.com/your-username/AutomatedWebScraper.git
cd AutomatedWebScraper
2. Create a virtual environment
Windows

python -m venv venv
venv\Scripts\activate
macOS/Linux

python3 -m venv venv
source venv/bin/activate
3. Install dependencies
pip install -r requirements.txt
🚀 Usage
Start the scraper
python app.py
Run scheduled scraping
celery -A tasks worker --loglevel=info
Export data to CSV
python export_csv.py
🗄️ Database Schema
CREATE TABLE scraped_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    price TEXT,
    link TEXT,
    scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
🔄 Workflow
Website
    │
    ▼
Selenium
    │
    ▼
BeautifulSoup
    │
    ▼
SQLite Database
    │
    ▼
Celery Scheduler
    │
    ▼
CSV Export
📸 Sample Output
SQLite
ID	Title	Price	Scraped At
1	Laptop	₹55,000	2026-06-30
CSV
Title,Price,Scraped At
Laptop,55000,2026-06-30
Phone,25000,2026-06-30
💡 Future Enhancements
Web dashboard using Flask
Support multiple websites
Email notifications
Excel and JSON export
Docker deployment
PostgreSQL/MySQL integration
REST API for scraped data
🎯 Learning Outcomes
This project demonstrates:

Web Scraping
Selenium Automation
BeautifulSoup Parsing
Task Scheduling with Celery
SQLite Database Operations
CSV Data Export
Python Automation
Error Handling
Modular Project Design
🤝 Contributing
Contributions are welcome!

Fork the repository
Create a new branch
Commit your changes
Push the branch
Open a Pull Request
📄 License
This project is licensed under the MIT License.

👩‍💻 Author
Tripti Bharadwaj Pandey

If you found this project helpful, consider giving it a ⭐ on GitHub!

About
No description, website, or topics provided.
Resources
 Readme
 Activity
Stars
 0 stars
Watchers
 0 watching
Forks
 0 forks
Releases
No releases published
Create a new release
Packages
No packages published
Publish your first package
Contributors
1
@pandeytriptibharadwaj-code
pandeytriptibharadwaj-code
Languages
Python
100.0%
Suggested workflows
Based on your tech stack
SLSA Generic generator logo
SLSA Generic generator
Generate SLSA3 provenance for your existing release workflows
Python application logo
Python application
Create and test a Python application.
Python Package using Anaconda logo
Python Package using Anaconda
Create and test a Python package on multiple Python versions using Anaconda for package management.
More workflows
Footer
© 2026 GitHub, Inc.
