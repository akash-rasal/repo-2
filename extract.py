import pandas as pd

print("Extract Data")

data= {
    "id": [1, 2, 3],
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35]
}

df=pd.DataFrame(data)
print(df)
