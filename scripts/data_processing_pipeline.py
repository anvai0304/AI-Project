import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from datetime import datetime, timedelta
import logging
import os

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Database connection (adjust as needed)
DB_USER = "postgres"
DB_PASSWORD = "your_password_here"  # Replace with your actual password
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "forest_ecosystem"

engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

def load_data():
    """Load data from the database"""
    query = """
    SELECT fp.id, fp.plot_name, fp.latitude, fp.longitude, fp.area_hectares,
           td.species, td.height_meters, td.diameter_cm, td.measurement_date
    FROM forest_plots fp
    JOIN tree_data td ON fp.id = td.plot_id
    """
    df = pd.read_sql(query, engine)
    logging.info(f"Loaded {len(df)} records from the database")
    return df

def process_data(df):
    """Process the loaded data"""
    # Calculate average tree height and diameter for each plot
    plot_stats = df.groupby('plot_name').agg({
        'height_meters': 'mean',
        'diameter_cm': 'mean',
        'species': 'nunique'
    }).rename(columns={
        'height_meters': 'avg_height',
        'diameter_cm': 'avg_diameter',
        'species': 'species_count'
    })
    
    # Calculate tree density (trees per hectare)
    tree_counts = df.groupby('plot_name').size().rename('tree_count')
    plot_areas = df.groupby('plot_name')['area_hectares'].first()
    plot_stats['tree_density'] = tree_counts / plot_areas
    
    logging.info(f"Processed data for {len(plot_stats)} plots")
    return plot_stats

def save_results(df, output_path):
    """Save the processed data"""
    df.to_csv(output_path)
    logging.info(f"Saved results to {output_path}")

def main():
    logging.info("Starting data processing pipeline")
    
    # Create 'outputs' directory if it doesn't exist
    os.makedirs('outputs', exist_ok=True)
    
    # Generate output filename with current date
    output_filename = f"plot_stats_{datetime.now().strftime('%Y%m%d')}.csv"
    output_path = os.path.join('outputs', output_filename)
    
    try:
        # Load data
        df = load_data()
        
        # Process data
        results = process_data(df)
        
        # Save results
        save_results(results, output_path)
        
        logging.info("Data processing pipeline completed successfully")
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()