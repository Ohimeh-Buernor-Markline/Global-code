import pyowm
 
apiKey = 'bf45390a352169d3a24e4ea5363c3c49'
owm = pyowm.OWM(apiKey)
observation = owm.weather_at_place('Accra,Ghana')
w = observation.get_weather()
 
print(w.get_wind())
print("Humidity = ",w.get_humidity())