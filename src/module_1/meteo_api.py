import requests 
import matplotlib.pyplot  as plt 

def get_data_meteo_api(api_url: str, city: dict, parameters: str, t: list): 

    url = f"{API_URL}latitude={city['latitude']}&longitude={city['longitude']}&variables={VARIABLES}&start={t[0]}&end={t[1]}"  # Format??

    response = requests.get(url)  


    if response.status_code == 200:
        data = response.json()  # Format?
        print(data)  

    else:
        print(f'Error {response.status_code}: {response.text}')

    return data

def transform_data_meteo(data): 

    a = 0

    # MEAN

    # VARIANZA

    # RESOLUTION


def plot_data_meteo(clean_data): 

    b = 0

    # PLOTS

   

API_URL = "https://climate-api.open-meteo.com/v1/climate?" 

COORDINATES = {    
    "Madrid": {"latitude": 40.416775, "longitude": -3.703790},    
    "London": {"latitude": 51.507351, "longitude": -0.127758},    
    "Rio": {"latitude": -22.906847, "longitude": -43.172896}, 
}

VARIABLES = "temperature_2m_mean,precipitation_sum,soil_moisture_0_to_10cm_mean" 


timespan = [1950, 2050]

def main():    

    print("testing")
    
    madrid_raw_data = get_data_meteo_api(API_URL, (COORDINATES["Madrid"]), timespan , VARIABLES)
    




if __name__ == "__main__":    
    main()