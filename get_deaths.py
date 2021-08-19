import pandas as pd

def get_country_deaths(country):
    pop = pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/scripts/input/un/population_2020.csv')
    country = country.title()
    country = country.replace('And', 'and')
    country = country.replace('Of', 'of')
    country = country.replace("D'Ivoire", "d'Ivoire")
    country = country.replace('Sint Maarten (Dutch Part)', 'Sint Maarten (Dutch part)')
    data = pd.read_csv(f'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/jhu/biweekly_deaths_per_million.csv', sep=',')
    data = data[['date', country]]
    data['date_dt'] = pd.to_datetime(data['date'], format='%Y-%m-%d')
    data['date_dt'] = data['date_dt'].dt.date
    country_pop = int(pop['population'].loc[pop['entity'] == country])
    data['population'] = country_pop
    data.rename(columns={country:'deaths'}, inplace=True)
    return data