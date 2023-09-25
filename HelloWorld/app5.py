# IF STATEMENTS

temperature = float(input("Input Temp. Readings in Celsius: "))
temperatureF = (temperature * 9 / 5) + 32  # Convert to F

if temperature > 60:
    print("C Temperature: " + str(temperature))
    print("F Temperature: " + str(temperatureF))
    print("How are you alive")
elif temperature > 40:
    print("C Temperature: " + str(temperature))
    print("F Temperature: " + str(temperatureF))
    print("Woah that's really hot")
elif temperature > 30:
    print("C Temperature: " + str(temperature))
    print("F Temperature: " + str(temperatureF))
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature > 20:  # (20, 30]
    print("C Temperature: " + str(temperature))
    print("F Temperature: " + str(temperatureF))
    print("It's a nice day")
elif temperature > 10:  # (10, 20]
    print("C Temperature: " + str(temperature))
    print("F Temperature: " + str(temperatureF))
    print("It's a bit cold")
else:
    print("C Temperature: " + str(temperature))
    print("F Temperature: " + str(temperatureF))
    print("It's cold")
    print("Stay warm! :)")
print("Done")
