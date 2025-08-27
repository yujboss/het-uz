# Hududiy Elektr Tarmoqlari - Telegram Scraper Bot

This bot scrapes electricity consumption data from the "Hududiy Elektr Tarmoqlari" AJ web portal. It automates login, fetches billing and usage stats, and delivers them via the Telegram Bot API, helping you monitor your usage effortlessly.

<!-- It's a good idea to add a screenshot of your bot in action here! -->

## ✨ Features

-   **Automated Scraping**: Logs in and fetches your latest electricity usage data automatically.
-   **Daily Reports**: Sends an automated report every day at a scheduled time (default is 12:00 PM).
-   **On-Demand Fetching**: Instantly get the latest reading with a simple `/get` command.
-   **Usage Graphs**: Visualize your consumption for the current month with the `/graph` command.
-   **Secure**: Keeps your credentials separate from the main codebase and out of version control.

## 🚀 Setup and Installation

Follow these steps to get the bot up and running on your own server.

### 1. Clone the Repository
First, clone this repository to your local machine or server:
```bash
git clone [https://github.com/yujboss/het-uz.git](https://github.com/yujboss/het-uz.git)
cd het-uz
```

### 2. Install Dependencies
It's recommended to use a Python virtual environment to keep your project's dependencies organized.
```bash
# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install the required Python packages
pip install -r requirements.txt
```
*(Note: A `requirements.txt` file is included in the repository. If you add new packages, you can update it by running `pip freeze > requirements.txt`.)*

### 3. Install Google Chrome
The scraper uses **Selenium** to control a web browser. This script is configured to use Google Chrome, so it must be installed on the system where you run the bot.

**Why is this needed?** Selenium automates a real browser to log in and navigate the website just like a human would. The script runs Chrome in "headless mode," meaning it does all its work in the background without needing a graphical display, which is perfect for servers.

To install it on a Debian/Ubuntu system, run the following commands:
```bash
# Download the installer
wget [https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb](https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb)

# Install the package and any missing dependencies
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt-get install -f
```

### 4. Configure the Bot
All configuration is handled in the `config.py` file. A template is provided to make this easy.

1.  **Rename the example file:**
    ```bash
    mv config.py.example config.py
    ```
2.  **Edit `config.py`** with a text editor (like `nano` or `vim`) and fill in your details:
    -   `HET_USERNAME` & `HET_PASSWORD`: Your login credentials for the het.uz portal.
    -   `TELEGRAM_BOT_TOKEN`: Your unique token from Telegram's BotFather.
    -   `TELEGRAM_CHAT_ID`: Your personal chat ID, so the bot knows where to send messages.

## ▶️ Running the Bot
Once everything is configured, you can start the bot with this command:
```bash
python3 bot.py
```
The bot will now run continuously, listening for commands and sending scheduled reports. For long-term use, it's recommended to run this process in the background using a tool like `screen` or `tmux` to ensure it stays active even after you disconnect from the server.

## 🤖 Bot Commands

-   `/start` - Displays a welcome message and confirms the bot is running.
-   `/get` - Fetches and displays the current electricity reading instantly.
-   `/graph` - Generates and sends a graph of the current month's usage.
