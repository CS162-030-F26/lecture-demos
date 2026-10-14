# Define your City class up here
class City:
    name: str
    population: int

def main() -> None:
    with open('data.txt', 'r') as my_file:
        for line in my_file:
            # Split the line by commas
            # (.split() method)
            # Create a City object
            # Store the name in the_city.name
            # Type-cast the population to an
            # int, and store it in
            # the_city.population
            the_city = City()
            tokens = line.split(',').strip()
            the_city.name = tokens[0]
            the_city.population = int(tokens[1])


if __name__ == '__main__':
    main()
