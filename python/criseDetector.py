import requests
import pandas as pd

data = requests.get('http://localhost:8080/getDetectedCrise').json()
df = pd.json_normalize(data)
print(df)
