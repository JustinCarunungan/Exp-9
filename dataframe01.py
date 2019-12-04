import pandas as pd
cars = pd.read_csv("cars.csv")
print("First Five Rows")
print()
print(cars.iloc[:5])
print()
print("Last Five Rows")
print()
print(cars.iloc[-5:])
input()

