import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sqlalchemy import create_engine

# Database connection (update with your credentials)
engine = create_engine('postgresql://postgres:anvai0304@localhost:5433/forest_ecosystem')

# Load data from database
forest_plots = pd.read_sql_table('forest_plots', engine)
tree_data = pd.read_sql_table('tree_data', engine)

# Merge datasets
merged_data = pd.merge(tree_data, forest_plots, left_on='plot_id', right_on='id', suffixes=('_tree', '_plot'))

# Basic statistics
print(merged_data.describe())

# Distribution of tree species
plt.figure(figsize=(12, 6))
sns.countplot(y='species', data=merged_data, order=merged_data['species'].value_counts().index)
plt.title('Distribution of Tree Species')
plt.tight_layout()
plt.savefig('species_distribution.png')
plt.close()

# Relationship between tree height and diameter
plt.figure(figsize=(10, 6))
sns.scatterplot(x='diameter_cm', y='height_meters', hue='species', data=merged_data)
plt.title('Tree Height vs Diameter')
plt.tight_layout()
plt.savefig('height_vs_diameter.png')
plt.close()

# Average tree height by plot
avg_height_by_plot = merged_data.groupby('plot_name')['height_meters'].mean().sort_values(ascending=False)
plt.figure(figsize=(12, 6))
avg_height_by_plot.plot(kind='bar')
plt.title('Average Tree Height by Plot')
plt.ylabel('Average Height (meters)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('avg_height_by_plot.png')
plt.close()

# Correlation heatmap
numeric_columns = merged_data.select_dtypes(include=[np.number]).columns
correlation_matrix = merged_data[numeric_columns].corr()
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap of Numeric Features')
plt.tight_layout()
plt.savefig('correlation_heatmap.png')
plt.close()

print("EDA completed. Check the generated PNG files for visualizations.")