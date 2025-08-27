# Hududiy Elektr Tarmoqlari - Telegram Scraper Bot

This bot scrapes electricity consumption data from the "Hududiy Elektr Tarmoqlari" AJ web portal. It automates login, fetches billing and usage stats, and delivers them via the Telegram Bot API, helping you monitor your usage effortlessly.

<!-- It's a good idea to add a screenshot of your bot in action here! -->

## ✨ Features

* **Automated Scraping**: Logs in and fetches your latest electricity usage data automatically.

* **Daily Reports**: Sends an automated report every day at a scheduled time (default is 12:00 PM).

* **On-Demand Fetching**: Instantly get the latest reading with a simple `/get` command.

* **Usage Graphs**: Visualize your consumption for the current month with the `/graph` command.

* **Secure**: Keeps your credentials separate from the main codebase and out of version control.

* **Dockerized**: Easy to deploy and run anywhere with Docker.

## 🚀 Setup and Deployment

This project is designed to be run with Docker and Docker Compose, which is the recommended method.

### Docker Setup (Recommended)

This is the simplest and most reliable way to run the bot. It packages the application and all its dependencies into a single container.

**Prerequisites:**

* [Docker](https://docs.docker.com/get-docker/) installed.

* [Docker Compose](https://docs.docker.com/compose/install/) installed.

**Steps:**

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/yujboss/het-uz.git](https://github.com/yujboss/het-uz.git)
   cd het-uz
   ```

2. **Create Your Configuration File:**
   Rename the example config file and fill in your credentials.
   ```bash
   mv config.py.example config.py
   ```
   Now, edit `config.py` with your details (`HET_USERNAME`, `HET_PASSWORD`, `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`).

3. **Build and Run the Bot:**
   Use Docker Compose to build the image and start the container in the background.
   ```bash
   docker-compose up --build -d
   ```
   Your bot is now running!

**Managing the Bot with Docker:**

* **View Logs:** `docker-compose logs -f`

* **Stop the Bot:** `docker-compose down`

* **Start the Bot:** `docker-compose up -d`

### Manual Setup (Legacy)

This method is for running the bot directly on a machine without Docker.

1. **Install Dependencies:**
   It's recommended to use a Python virtual environment.
   ```bash
   # Create and activate a virtual environment
   python3 -m venv venv
   source venv/bin/activate
   
   # Install the required Python packages
   pip install -r requirements.txt
   ```

2. **Install Google Chrome:**
   The scraper uses Selenium to control a web browser. For Debian/Ubuntu systems:
   ```bash
   wget [https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb](https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb)
   sudo dpkg -i google-chrome-stable_current_amd64.deb
   sudo apt-get install -f
   ```

3. **Configure and Run:**
   Follow Step 2 from the Docker setup to create and edit your `config.py` file. Then, run the bot:
   ```bash
   python3 bot.py
   ```

## 🤖 Bot Commands

* `/start` - Displays a welcome message and confirms the bot is running.

* `/get` - Fetches and displays the current electricity reading instantly.

* `/graph` - Generates and sends a graph of the current month's usage.
