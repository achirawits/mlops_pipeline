import pandas as pd

df = pd.read_csv(r"C:\Users\chi\Desktop\chichi\mlops_pipeline\processed_data\test.csv")

min_max = pd.DataFrame({
    "Min": df.min(),
    "Max": df.max()
})

print(min_max)
