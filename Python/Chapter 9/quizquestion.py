cities = {
    'GA': 'Atlanta'
}

if 'FL' in cities:
    del cities['FL']

    cities['FL'] = 'Tallahassee'

print(cities)