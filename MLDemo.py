import pandas as pd

resources_data_file_path = "resources/data/" # this allows us to access multiple files from the same location easily
melb_file_path = resources_data_file_path + "melb_data.csv"

melbourne_data = pd.read_csv(melb_file_path)

print(melbourne_data.describe())

# perform calculations
avg_lot_size = melbourne_data["Landsize"].mean()
newest_home = melbourne_data["YearBuilt"].min()


# generate output
print("The average lot size is " + str(avg_lot_size))
print("The newest home age is " + str(newest_home))


