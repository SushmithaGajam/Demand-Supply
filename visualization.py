import pandas as pd
import matplotlib.pyplot as plt

# Load your data from CSV (make sure path is correct)
data = pd.read_csv('clothing_data.csv')

def plot_data(df):
    plt.figure(figsize=(12,6))
    plt.plot(df['Month'], df['Demand'], marker='o', label='Demand')
    plt.plot(df['Month'], df['Supply'], marker='o', label='Supply')
    plt.title('Monthly Demand & Supply of Clothes in Telangana')
    plt.xlabel('Month')
    plt.ylabel('Units')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_data(data)
