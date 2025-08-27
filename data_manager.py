import os
import pandas as pd
from datetime import datetime
import logging

# This line helps confirm that the correct file is being imported.
print("DEBUG: data_manager.py module has been loaded.")

logger = logging.getLogger(__name__)

def save_reading_to_csv(filepath, value):
    """Saves the date and reading to a CSV file, avoiding duplicates."""
    # Create the file with headers if it doesn't exist
    if not os.path.exists(filepath):
        df = pd.DataFrame(columns=['date', 'reading'])
        df.to_csv(filepath, index=False)
    
    # Read the existing data
    df = pd.read_csv(filepath)
    
    # Get today's date as a string
    today_str = datetime.now().strftime('%Y-%m-%d')
    
    # Create a new entry to be added
    new_entry = pd.DataFrame([{'date': today_str, 'reading': value}])
    
    # Remove today's entry if it already exists to prevent duplicates
    if not df.empty and 'date' in df.columns:
        df = df[df.date != today_str]
    
    # Append the new, updated entry and save the file
    df = pd.concat([df, new_entry], ignore_index=True)
    df.to_csv(filepath, index=False)
    logger.info(f"Saved reading for {today_str}: {value}")

