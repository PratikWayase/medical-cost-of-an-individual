
import os
import pandas as pd
from sklearn.model_selection import train_test_split

def process_insurance_data():
    """Process the Medical insurance dataset and split into train/test sets"""
    try:
        # Define paths using your specific directory structure
        base_path = r"D:\Users\Desktop\insurance\insurance"
        input_path = os.path.join(base_path, "data", "raw", "Medical_insurance.csv")
        train_path = os.path.join(base_path, "data", "processed", "train.csv")
        test_path = os.path.join(base_path, "data", "processed", "test.csv")
        
        # Load the dataset
        print("Loading dataset...")
        data = pd.read_csv(input_path)
        
        # Split the dataset into 80% training and 20% testing
        print("Splitting dataset...")
        train_data, test_data = train_test_split(
            data, 
            test_size=0.2, 
            random_state=42
        )
        
        # Save the datasets
        print("Saving split datasets...")
        train_data.to_csv(train_path, index=False)
        test_data.to_csv(test_path, index=False)
        
        print("\nSuccess! Data has been split and saved:")
        print(f"Total samples: {len(data)}")
        print(f"Training samples: {len(train_data)}")
        print(f"Testing samples: {len(test_data)}")
        print(f"\nFiles are saved in: {os.path.join(base_path, 'data', 'processed')}")
        
    except FileNotFoundError:
        print("Error: Unable to find the file. Please check if the path is correct:")
        print(input_path)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    process_insurance_data()