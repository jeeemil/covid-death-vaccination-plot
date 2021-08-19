import pandas as pd

def get_country_vaccine_data(country):
    pop = pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/scripts/input/un/population_2020.csv')
    country = country.title()
    country = country.replace('And', 'and')
    country = country.replace('Of', 'of')
    country = country.replace("D'Ivoire", "d'Ivoire")
    country = country.replace('Sint Maarten (Dutch Part)', 'Sint Maarten (Dutch part)')
    country_pop = int(pop['population'].loc[pop['entity'] == country])
    if ' ' in country:
        country = country.replace(' ', '%20')
    data = pd.read_csv(f'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/country_data/{country}.csv')
    data['date_dt'] =  pd.to_datetime(data['date'], format='%Y-%m-%d')
    data['date_dt'] = data['date_dt'].dt.date
    
    data['population'] = country_pop
    data['vaccine_share_1'] = (data['people_vaccinated'] / data['population']) * 100
    data['vaccine_share_2'] = (data['people_fully_vaccinated'] / data['population']) * 100
    return data