import pandas as pd


data = pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.csv')
country_list = list(data.location.unique())
print(country_list)
