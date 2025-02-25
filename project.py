import json
import random
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Step 1: Generate Dataset
def create_dataset(num_samples=500):
    dataset = []
    for _ in range(num_samples):
        sample = {
            "fan_in": random.randint(5, 50),
            "fan_out": random.randint(3, 30),
            "gate_count": random.randint(20, 200),
            "path_length": random.randint(5, 50),
            "logic_depth": random.randint(8, 25)  # Target variable
        }
        dataset.append(sample)

    with open("dataset.json", "w") as f:
        json.dump(dataset, f, indent=4)

    print(f"✅ Dataset with {num_samples} samples created successfully!")

# Step 2: Train the Model
def train_model():
    data = pd.read_json("dataset.json")
    X = data.drop(columns=["logic_depth"])
    y = data["logic_depth"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=100)
    model.fit(X_train, y_train)
    
    joblib.dump(model, "model.pkl")
    print("✅ Model trained and saved as 'model.pkl'!")

# Step 3: Prediction Function
def predict_logic_depth():
    model = joblib.load("model.pkl")
    feature_names = ["fan_in", "fan_out", "gate_count", "path_length"]

    # Get user inputs
    print("\n🔹 Enter Circuit Parameters:")
    fan_in = int(input("Fan In: "))
    fan_out = int(input("Fan Out: "))
    gate_count = int(input("Gate Count: "))
    path_length = int(input("Path Length: "))

    features = pd.DataFrame([[fan_in, fan_out, gate_count, path_length]], columns=feature_names)
    prediction = model.predict(features)[0]
    
    print(f"\n🟢 Predicted Logic Depth: {prediction:.2f}")

# Main Menu
if __name__ == "__main__":
    while True:
        print("\n🔹 Select an option:\n")
        print("1️⃣  Create Dataset")
        print("2️⃣  Train Model")
        print("3️⃣  Predict Logic Depth")
        print("4️⃣  Exit\n")

        choice = input("Enter your choice (1/2/3/4): ").strip()

        if choice == "1":
            num_samples = int(input("Enter number of samples for dataset: "))
            create_dataset(num_samples)
        elif choice == "2":
            train_model()
        elif choice == "3":
            predict_logic_depth()
        elif choice == "4":
            print("🚀 Exiting the program. Have a great day!")
            break
        else:
            print("❌ Invalid choice! Please enter 1, 2, 3, or 4.")
