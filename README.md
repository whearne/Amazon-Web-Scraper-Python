# Amazon Web Scraper Project
This project is an Amazon web scraper built using Python. It allows you to track the price and availability of products on Amazon and sends you notifications when certain conditions are met (e.g., price drops). This script utilizes the BeautifulSoup and requests libraries for web scraping and the smtplib library for email notifications.

## Features
- Scrapes product data from Amazon, including:
    - Product title
    - Price
    - Availability status
- Tracks price changes over time.
- Sends email notifications if the product price falls below a specified threshold.
- Logs data with timestamps for future reference and analysis.
## Getting Started
### Prerequisites
- Python 3.x
- Required libraries: BeautifulSoup, requests, smtplib
You can install the required libraries using the following command:

pip install beautifulsoup4 requests

### Installation
1. Clone the repository or download the script directly:

    git clone https://github.com/whearne/amazon-web-scraper-python.git

2. Navigate to the project directory:

    cd amazon-web-scraper-project

3. Install the necessary Python libraries if you haven't already.

### Usage
1. Open the script (Amazon Web Scraper Project.py) in your favorite code editor.

2. Update the URL variable in the script with the Amazon product link you want to track. For example:

    URL = 'https://www.amazon.co.uk/Data-Analytics-Engineering-Business-Intelligence/dp/B0922P1MN8/ref=sr_1_1?crid=19WJCTPZACH5J'

3. Update the headers dictionary with your user agent string. This helps to mimic a legitimate browser request to Amazon.


    headers = {"User-Agent": "your-user-agent-string"}

4. Set up your email server and recipient email in the script to receive notifications when the product's price drops:

    server = smtplib.SMTP('smtp.gmail.com', 587)
    sender_email = 'your-email@gmail.com'
    recipient_email = 'recipient-email@gmail.com'
  
5. Run the script:


    python Amazon\ Web\ Scraper\ Project.py
### Scheduled Execution
To run the script automatically at regular intervals, you can use a task scheduler (e.g., cron on Linux/Mac or Task Scheduler on Windows).

### License
This project is licensed under the MIT License - see the LICENSE file for details.
