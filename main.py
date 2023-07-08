# Задание 1:
# Создайте класс «Город». Необходимо хранить в полях класса: название города, название региона, название страны, количество жителей в городе, почтовый индекс города, телефонный код города. Реализуйте доступ к отдельным полям через методы класса.
# get and set (по примеру на уроке)
#
class City:
    def __init__(self, name, region, country, population, postal_code, tel_code):
        self.name = name
        self.region = region
        self.country = country
        self.population = population
        self.postal_code = postal_code
        self.tel_code = tel_code


# setting up a class - City for Dnepr
city_dnepr = City("Dnepr", "Dneprovsky", "Ukraine", 1000000, 49000, "056")

# setting up a class - City for Kiyv
city_kiev = City("Kiev", "Kievsky", "Ukraine", 3000000, 51000, "044")

# Make a choice
user_choice = input("Choose the city (Dnepr or Kiev): ")

# Info output
if user_choice.lower() == "dnepr":
    print("Info about city Dnepr:")
    print("City name:", city_dnepr.name)
    print("Region name:", city_dnepr.region)
    print("Country name:", city_dnepr.country)
    print("Population:", city_dnepr.population)
    print("Zip code:", city_dnepr.postal_code)
    print("Tel code:", city_dnepr.tel_code)
elif user_choice.lower() == "kiev":
    print("Info about city Kiev:")
    print("City name:", city_kiev.name)
    print("Region name:", city_kiev.region)
    print("Country name:", city_kiev.country)
    print("Population:", city_kiev.population)
    print("Zip code:", city_kiev.postal_code)
    print("Tel code:", city_kiev.tel_code)
else:
    print("Choose Dnepr or Kiev")
#
# Задание 2:
# Создайте класс «Страна». Необходимо хранить в полях класса: название страны, название континента, количество жителей в стране, телефонный код страны, название столицы, название городов страны. Реализуйте доступ к отдельным полям через методы класса.
# get and set (по примеру на уроке)
#
class Country:
    def __init__(self, name, continent, population, tel_code, capital, cities):
        self._name = name
        self._continent = continent
        self._population = population
        self._phone_code = tel_code
        self._capital = capital
        self._cities = cities

    def get_name(self):
        return self._name

    def get_continent(self):
        return self._continent

    def get_population(self):
        return self._population

    def get_phone_code(self):
        return self._phone_code

    def get_capital(self):
        return self._capital

    def get_cities(self):
        return self._cities


# Setting up class Country
country = Country("Ukraine", "Europe", 45000000, 38, "Kiev", ["Kiev", "Dnepr", "Kharkiv", "Lviv", "And others"])

# Getting request from a user
field = input("Enter value to get info (name, continent, population, tel_code, capital, cities): ")

# Output for a user
if field.lower() == "name":
    print("Country name:", country.get_name())
elif field.lower() == "continent":
    print("Continent name:", country.get_continent())
elif field.lower() == "population":
    print("Population:", country.get_population())
elif field.lower() == "tel_code":
    print("Tel code of a country:", country.get_phone_code())
elif field.lower() == "capital":
    print("Name of a capital:", country.get_capital())
elif field.lower() == "cities":
    print("Names of several cities:", ", ".join(country.get_cities()))
else:
    print("Something went wrong. Try again")
