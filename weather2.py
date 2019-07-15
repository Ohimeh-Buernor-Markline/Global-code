import pyowm
 
apiKey = 'bf45390a352169d3a24e4ea5363c3c49'
owm = pyowm.OWM(apiKey)
obs = owm.weather_at_place('Hong kong,Hong kong')
w = obs.get_weather()

print("Hong Kong")
print("---------")
print("Humidity = ",w.get_humidity())

print(" ")
print(" ")

obs = owm.weather_at_place('Iceland')
v = obs.get_weather()

print("Iceland")
print("---------")
print("Humidity = ",v.get_humidity())

print(" ")
if (w.get_humidity() > v.get_humidity()):
    print("The humidity is Hong Kong is worst than that in Ghana")
    print("The humidity for Hong Kong is ", w.get_humidity())
else:
    print("The humidity in Ghana is worst than that of Hong Kong")

