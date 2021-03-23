def make_country(country_name, capital_name):
    try:
        if type(country_name) != str or type(capital_name) != str:
            raise TypeError
        my_dictionary = {'country': country_name, 'capital': capital_name}
        return my_dictionary
    except TypeError:
        print('TypeError')
        raise


def show_country_info(country_dict):
    try:
        if type(country_dict) != dict:
            raise ValueError
        return f"Country: {country_dict.get('country')}, Capital: {country_dict.get('capital')}."
    except ValueError:
        print ('ValueError')
        raise

# your code goes here
print(show_country_info(make_country("Gondor", "Minas Tirith")))