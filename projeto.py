import pandas as pd
from geopy import Nominatim
from geopy.extra.rate_limiter import RateLimiter


x = pd.read_excel(r'C:\Users\muniz\Documents\ENDERECO.xlsx', engine='openpyxl')


geolocator = Nominatim(user_agent="myGeocoder")

geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1
                      )
x['point'] = x['COMPLETO'].apply(geocode).apply(lambda loc: tuple(loc.point) if loc else None)

x.to_excel('teste1.xlsx', sheet_name='teste', na_rep='#N/A', header=True, index=False)


