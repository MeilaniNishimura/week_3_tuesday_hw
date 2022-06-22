# lambda homework
# question 1
places = [' ', 'Argentina', '  ', 'San Diego', '', '   ', '', 'Boston', 'New York']
new_places=list(filter(lambda x: x.strip(), places))
print(new_places)

# question 2
authors = ["Connor Milliken", "Victor aNisimov", "Andrew P. Garfield", "David HassELHOFF", "Oprah wInfrey"]
new_list=[a.split(",") for a in authors]
new_list.sort(key=lambda x: x[-1])
print(new_list)

# question 3
places = [('Nassau', 32), ('Boston', 12), ('Los Angeles', 44), ('Miami', 29)]
def celcius(places):
    return(places[0], places[1] * 9/5 +32)
cel = list(map(celcius, places))
print(list(cel))

# question 4
# I could not accomplish this whatsoever I'm so sorry 