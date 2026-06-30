# 🕷️ Automated Web Scraper with Scheduler

An automated web scraping application built with Python that periodically collects data from websites. The scraper supports dynamic web pages using Selenium, extracts data with BeautifulSoup, stores it in an SQLite database, and exports the collected data to CSV for further analysis.

---

## 📌 Features

- 🌐 Scrape data from dynamic websites
- 🤖 Automate browser interactions using Selenium
- 📝 Parse HTML content with BeautifulSoup
- 💾 Store scraped data in SQLite
- ⏰ Schedule scraping tasks using Celery
- 📤 Export scraped data to CSV
- 🚫 Prevent duplicate entries
- 📋 Logging and error handling
- 🧩 Modular and maintainable project structure

---

## 🛠️ Tech Stack

- Python 3.x
- Selenium
- BeautifulSoup4
- Celery
- SQLite
- CSV
- ChromeDriver

---

## 📂 Project Structure

```
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
├── logs/
│   └── scraper.log
│
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/AutomatedWebScraper.git
cd AutomatedWebScraper
```

### 2. Create a Virtual Environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install ChromeDriver

Download the ChromeDriver version that matches your installed Google Chrome browser and add it to your system PATH.

---

## 🚀 Usage

### Run the scraper

```bash
python app.py
```

### Start Celery Worker

```bash
celery -A tasks worker --loglevel=info
```

### Export Data to CSV

```bash
python export_csv.py
```

---

## 🗄️ Database Schema

```sql
CREATE TABLE scraped_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    price TEXT,
    url TEXT,
    scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## 🔄 Workflow

```
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
```

---

## 📊 Sample Output

### SQLite Database

| ID | Title | Price | Scraped At |
|----|-------|--------|------------|
| 1 | Laptop | ₹55,000 | 2026-06-30 |
| 2 | Phone | ₹25,000 | 2026-06-30 |

### CSV Output

```csv
Title,Price,Scraped At
Laptop,55000,2026-06-30
Phone,25000,2026-06-30
```

---

## 🎯 Learning Outcomes

This project demonstrates:

- Web Scraping
- Selenium Browser Automation
- HTML Parsing with BeautifulSoup
- SQLite Database Operations
- Task Scheduling using Celery
- Data Export to CSV
- Python Automation
- Error Handling and Logging
- Modular Software Design

---

## 🚀 Future Enhancements

- Flask or Django Dashboard
- Support for multiple websites
- Email notifications after scraping
- JSON and Excel export
- Docker deployment
- PostgreSQL/MySQL integration
- REST API for accessing scraped data
- Proxy and CAPTCHA handling

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push the branch
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👩‍💻 Author

**Shrimayee Pattanaik**

GitHub: https://github.com/YOUR_GITHUB_USERNAME

---



