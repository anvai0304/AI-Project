import pandas as pd
from sqlalchemy import create_engine
from db_connection import engine, ForestPlot, Session

def ingest_forest_plots():
    # Read the CSV file
    df = pd.read_csv('../data/sample_forest_plots.csv')
    
    # Create a database session
    session = Session()
    
    try:
        # Iterate through the dataframe and add each row to the database
        for index, row in df.iterrows():
            plot = ForestPlot(
                plot_name=row['plot_name'],
                latitude=row['latitude'],
                longitude=row['longitude'],
                area_hectares=row['area_hectares']
            )
            session.add(plot)
        
        # Commit the changes
        session.commit()
        print(f"Successfully ingested {len(df)} forest plots.")
    except Exception as e:
        print(f"An error occurred during data ingestion: {e}")
        session.rollback()
    finally:
        session.close()

if __name__ == "__main__":
    ingest_forest_plots()