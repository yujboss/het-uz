Hududiy Elektr Tarmoqlari - Telegram Scraper Bot
This bot scrapes electricity consumption data from the "Hududiy Elektr Tarmoqlari" AJ web portal. It automates login, fetches billing and usage stats, and delivers them via the Telegram Bot API, helping you monitor your usage effortlessly.

<!-- It's a good idea to add a screenshot of your bot in action here! -->

✨ Features
Automated Scraping: Logs in and fetches your latest electricity usage data automatically.

Daily Reports: Sends an automated report every day at a scheduled time (default is 12:00 PM).

On-Demand Fetching: Instantly get the latest reading with a simple /get command.

Usage Graphs: Visualize your consumption for the current month with the /graph command.

Secure: Keeps your credentials separate from the main codebase and out of version control.

🚀 Setup and Installation
Follow these steps to get the bot up and running on your own server.

1. Clone the Repository
First, clone this repository to your local machine or server:

git clone https://github.com/yujboss/het-uz.git
cd het-uz

2. Install Dependencies
It's recommended to use a Python virtual environment.

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install the required Python packages
pip install -r requirements.txt

(Note: You will need to create a requirements.txt file. You can do this by running pip freeze > requirements.txt in your current setup.)

3. Install Google Chrome
The scraper uses Selenium to control a headless instance of Google Chrome. You must have it installed on your system. For Debian/Ubuntu:

# Download the installer
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

# Install the package and its dependencies
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt-get install -f

4. Configure the Bot
All configuration is handled in the config.py file. A dummy file is provided to help you get started.

Rename the example file:

mv config.py.example config.py

Edit config.py with your favorite text editor (like nano or vim) and fill in your details:

HET_USERNAME & HET_PASSWORD: Your login credentials for the het.uz portal.

TELEGRAM_BOT_TOKEN: Your token from BotFather.

TELEGRAM_CHAT_ID: Your personal chat ID.

▶️ Running the Bot
Once everything is configured, you can start the bot with this command:

python3 bot.py

The bot will now be running continuously, listening for commands and sending scheduled reports. It's recommended to run this inside a screen or tmux session to keep it active after you disconnect.

🤖 Bot Commands
/start - Displays a welcome message.

/get - Fetches and displays the current electricity reading.

/graph - Generates and sends a graph of the current month's usage.
