import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1: Loading the CSV file
file_path = 'mtcars.csv'  # A sample csv file I had used for this project
data = pd.read_csv(file_path)

# 2: Basic Data Analysis 
# Calculating the average mpg
average_mpg = data['mpg'].mean()
print(f"Average MPG: {average_mpg:.2f}")

# 3: Visualizations
# Bar Chart: MPG by Car Model
plt.figure(figsize=(10, 6))
plt.bar(data['model'], data['mpg'], color='skyblue')
plt.xticks(rotation=90)
plt.xlabel('Car Model')
plt.ylabel('Miles Per Gallon (MPG)')
plt.title('Miles Per Gallon (MPG) by Car Model')
plt.tight_layout()
plt.show()

# Scatter Plot: Horsepower vs. MPG (column 1 vs column 2)
plt.figure(figsize=(8, 6))
plt.scatter(data['hp'], data['mpg'], color='green', alpha=0.7)
plt.xlabel('Horsepower (HP)')
plt.ylabel('Miles Per Gallon (MPG)')
plt.title('Horsepower vs. Miles Per Gallon')
plt.grid(True)
plt.show()

# Heatmap: Correlation Matrix 
plt.figure(figsize=(10, 8))
correlation_matrix = data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation Matrix')
plt.show()

# 4: Insights and Observations I found
print("\nInsights and Observations:")
print("- Our average MPG indicates general fuel efficiency.")
print("- Our bar chart shows varying fuel efficiency among car models.")
print("- Our scatter plot indicates a negative correlation between horsepower and MPG.")
print("- The heatmap highlights key correlations, such as weight and MPG.")
