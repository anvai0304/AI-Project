import os
from sqlalchemy import create_engine, Column, Integer, String, Numeric, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from geoalchemy2 import Geometry

# Database connection settings
DB_USER = "postgres"
DB_PASSWORD = "anvai0304"  # Replace with your actual password
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "forest_ecosystem"

# Create the database engine
engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

# Create a base class for declarative models
Base = declarative_base()

# Define the ForestPlot model
class ForestPlot(Base):
    __tablename__ = 'forest_plots'

    id = Column(Integer, primary_key=True)
    plot_name = Column(String(100))
    location = Column(Geometry('POINT', srid=4326))
    area_hectares = Column(Numeric)

# Define the TreeData model
class TreeData(Base):
    __tablename__ = 'tree_data'

    id = Column(Integer, primary_key=True)
    plot_id = Column(Integer, ForeignKey('forest_plots.id'))
    species = Column(String(100))
    height_meters = Column(Numeric)
    diameter_cm = Column(Numeric)
    measurement_date = Column(Date)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Test the connection by querying the forest_plots table
try:
    result = session.query(ForestPlot).first()
    if result:
        print(f"Successfully connected to the database. First plot name: {result.plot_name}")
    else:
        print("Successfully connected to the database, but the forest_plots table is empty.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    session.close()

if __name__ == "__main__":
    # Here you can add code to insert sample data or perform other operations
    pass