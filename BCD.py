def hotel_names_loop(hotels):
    hotel_names = []
    for i in range(len(hotels)):
        key = hotels[i].get("name")
        hotel_names.append(key)
    return hotel_names

def hotel_names_compr(hotels):
    return [hotel.get("name") for hotel in hotels]

def hotel_names_map():
    def names(hotel):
        return hotel.get("name")
    return list(map(names, hotels))

def word_count(words):
    words_dict = {}
    words_list = words.split()
    for i in range(len(words_list)):
        frequency = words_list.count(words_list[i])
        words_dict[words_list[i]] = frequency
    return words_dict

def flip_flop(**kwargs):
    new_dict = {}
    keys = list(kwargs.keys())
    values = list(kwargs.values())
    for i in range(len(keys)):
        new_dict[values[i]] = keys[i]
    return new_dict

def remove_dublicates(amenities):
    for i in range(len(amenities)-1):
        frequency_from_beginning = amenities[:i+1].count(amenities[i])
        if frequency_from_beginning > 1:
            amenities.pop(i)
    return amenities

def multiply_with_exception_current(given):
    multiply_value = 1
    new_list = []
    for i in range(len(given)):
        given.append(given[0])
        given.pop(0)
        for j in range(len(given)-1):
            multiply_value *= given[j]
        new_list.append(multiply_value)
        multiply_value = 1
    return new_list



given = [2, 5, 3, 4, 1]
amenities = ['free wifi', 'breakfast', 'gym', 'breakfast', 'pool', 'restaurant']
words = "any type type of words of"
hotels = [{'name': 'Hilton', 'locations': 2345}, {'name': 'Accor', 'locations':789}, {'name': 'W', 'locations':678}]
print(f'hotel_names_loop {hotel_names_loop(hotels)}')
print(f'hotel_names_compr {hotel_names_compr(hotels)}')
print(f'hotel_names_map {hotel_names_map()}')
print(f'word_count {word_count(words)}')
print(f'flip_flop {flip_flop(a=1,b=2)}')
print(f'remove_dublicates {remove_dublicates(amenities)}')
print(f'multiply_with_exception {multiply_with_exception_current(given)}')