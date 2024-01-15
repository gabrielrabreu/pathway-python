import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40]}

df = pd.DataFrame(data)

# Display the DataFrame
print("Sample DataFrame:")
print(df)

# Perform some basic operations
average_age = df['Age'].mean()
oldest_person = df['Name'][df['Age'].idxmax()]

# Display the results
print(f"\nAverage Age: {average_age}")
print(f"Oldest Person: {oldest_person}")
