import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import logging

# This line helps confirm that the correct file is being imported.
print("DEBUG: graph_generator.py module has been loaded.")

logger = logging.getLogger(__name__)

def generate_usage_graph(filepath):
    """Generates a PNG graph of the current month's usage."""
    if not os.path.exists(filepath):
        logger.warning(f"Data file not found at {filepath}. Cannot generate graph.")
        return None
        
    try:
        df = pd.read_csv(filepath, parse_dates=['date'])
        # Handle potential non-numeric values in the 'reading' column
        df['reading'] = pd.to_numeric(df['reading'].astype(str).str.replace(',', ''), errors='coerce')
        df.dropna(subset=['reading'], inplace=True) # Drop rows where conversion failed
        
        if df.empty:
            logger.warning("CSV file is empty after cleaning. Cannot generate graph.")
            return None

        current_month = datetime.now().month
        current_year = datetime.now().year
        monthly_data = df[(df['date'].dt.month == current_month) & (df['date'].dt.year == current_year)]
        
        if monthly_data.empty:
            logger.info("No data available for the current month to generate a graph.")
            return None

        plt.figure(figsize=(10, 6))
        plt.plot(monthly_data['date'], monthly_data['reading'], marker='o', linestyle='-', color='b')
        plt.title(f'Electricity Usage for {datetime.now().strftime("%B %Y")}')
        plt.xlabel('Date')
        plt.ylabel('kVt·s')
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        graph_path = 'usage_graph.png'
        plt.savefig(graph_path)
        plt.close()
        
        logger.info(f"Successfully generated graph at {graph_path}")
        return graph_path
    except Exception as e:
        logger.error(f"Failed to generate graph: {e}")
        return None
