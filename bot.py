import logging
from datetime import datetime
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, ContextTypes
from apscheduler.schedulers.background import BackgroundScheduler

# Import your custom modules
import config
import scraper
import data_manager
import graph_generator

# --- Basic Logging Setup ---
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# --- Telegram Bot Command Handlers ---
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm ready to fetch your electricity usage. Use /get for the latest reading or /graph for this month's usage graph.")

async def get_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Fetching the latest reading, please wait...")
    value = scraper.get_current_reading(config)
    
    if value:
        now = datetime.now()
        date_str = now.strftime("%A, %d %B")
        message = f"Date: {date_str}\nkVt·s: *{value}*"
        await update.message.reply_text(message, parse_mode='Markdown')
        data_manager.save_reading_to_csv(config.CSV_FILE, value)
    else:
        await update.message.reply_text("Sorry, I couldn't fetch the reading. An error occurred.")

async def graph_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Generating graph for the current month...")
    graph_file = graph_generator.generate_usage_graph(config.CSV_FILE)
    
    if graph_file:
        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(graph_file, 'rb'))
    else:
        await update.message.reply_text("Not enough data to generate a graph for this month. Use /get to add today's reading.")

# --- Scheduled Job ---
async def daily_report_job():
    logger.info("Running scheduled daily report job...")
    bot = Bot(token=config.TELEGRAM_BOT_TOKEN)
    value = scraper.get_current_reading(config)
    
    if value:
        data_manager.save_reading_to_csv(config.CSV_FILE, value)
        now = datetime.now()
        date_str = now.strftime("%A, %d %B")
        message = f"📅 Daily Report\nDate: {date_str}\nkVt·s: *{value}*"
        await bot.send_message(chat_id=config.TELEGRAM_CHAT_ID, text=message, parse_mode='Markdown')
    else:
        logger.warning("Scheduled job failed to get reading.")
        await bot.send_message(chat_id=config.TELEGRAM_CHAT_ID, text="⚠️ Scheduled job failed to get the daily reading.")

# --- Main Bot Execution ---
def main():
    if config.TELEGRAM_BOT_TOKEN == "YOUR_TELEGRAM_BOT_TOKEN" or config.TELEGRAM_CHAT_ID == "YOUR_TELEGRAM_CHAT_ID":
        logger.error("Please fill in your TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID in config.py")
        return

    application = Application.builder().token(config.TELEGRAM_BOT_TOKEN).build()
    
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("get", get_command))
    application.add_handler(CommandHandler("graph", graph_command))

    scheduler = BackgroundScheduler()
    scheduler.add_job(daily_report_job, 'cron', hour=12, minute=0)
    scheduler.start()
    
    logger.info("Bot started and scheduler is running...")
    application.run_polling()

if __name__ == '__main__':
    main()
