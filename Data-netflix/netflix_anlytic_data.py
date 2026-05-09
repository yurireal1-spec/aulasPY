import pandas as pd

# Ler o CSV
df = pd.read_csv("netflix_titles.csv")

# Converter para JSON
df.to_json("netflix_titles1.json", orient="records",  indent=4, force_ascii=False)

print("ok")