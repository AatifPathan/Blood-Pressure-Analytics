import pandas as pd
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/AatifPathan/Python-Project/main/Blood_pressure_data.csv'

def load_data():
    try:
        data = pd.read_csv(url)
        return data
    except Exception as e:
        print("Error loading data:", e)
        print("Creating a new data file.")
        data = pd.DataFrame(columns=['Age', 'Systolic', 'Diastolic'])
        data.to_csv('Blood_pressure_data.csv', index=False)
        return data

def add_data(data):
    ages = []
    systolic = []
    diastolic = []
    num_entries = int(input("Enter the number of blood pressure entries: "))
    for i in range(num_entries):
        age = int(input(f"Enter age for entry {i + 1} (40-80): "))
        sys = float(input(f"Enter systolic pressure for entry {i + 1}: "))
        dia = float(input(f"Enter diastolic pressure for entry {i + 1}: "))
        ages.append(age)
        systolic.append(sys)
        diastolic.append(dia)
    new_data = pd.DataFrame({'Age': ages, 'Systolic': systolic, 'Diastolic': diastolic})
    data = pd.concat([data, new_data], ignore_index=True)
    data.to_csv('Blood_pressure_data.csv', index=False)
    print("New data has been added and saved.")
    return data

def view_analytics(data):
    print("\nBlood Pressure Analytics:")
    print("Average Systolic Pressure:", data['Systolic'].mean())
    print("Average Diastolic Pressure:", data['Diastolic'].mean())
    age_bins = [40, 45, 50, 55, 60, 65, 70, 75, 80]
    age_labels = [f"{age}-{age + 4}" for age in age_bins[:-1]]
    data['Age Group'] = pd.cut(data['Age'], bins=age_bins, labels=age_labels, right=False)
    age_group_analysis = data.groupby('Age Group').agg({'Systolic': 'mean', 'Diastolic': 'mean', 'Age': 'count'}).rename(columns={'Age': 'Count'}).reset_index()
    print("\nAverage Blood Pressure by Age Group:")
    print(age_group_analysis)
    plt.figure(figsize=(10, 5))
    plt.plot(data.index, data['Systolic'], label='Systolic BP', color='red')
    plt.plot(data.index, data['Diastolic'], label='Diastolic BP', color='blue')
    plt.title('Blood Pressure Over Time')
    plt.xlabel('Entry Index')
    plt.ylabel('Blood Pressure (mmHg)')
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()

def main():
    data = load_data()
    while True:
        print("\nMenu:")
        print("1. Add Blood Pressure Data")
        print("2. View Blood Pressure Analytics")
        print("3. Exit")
        choice = input("Select an option (1-3): ")
        if choice == '1':
            data = add_data(data)
        elif choice == '2':
            view_analytics(data)
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please select again.")

if __name__ == "__main__":
    main()
