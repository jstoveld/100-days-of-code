import pandas as pd
from tabulate import tabulate

url = "https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data/Pennsylvania_medical_cases_by_county"
table = pd.read_html(url)[0]
print(table)