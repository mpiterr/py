def person_print(name, last_name, *others, age):
    formatted_data = 'Imię: {}, nazwisko: {}, wiek: {}'.format(name, last_name, age)
    others_str = ' '
    for arg in others:
        others_str += arg + ' '
    print(formatted_data + others_str)


def args_kwargs_print(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print("{}:{}".format(key, value))


args_kwargs_print("arg0", "arg1", key0="value0", key1="value1", key2="value2")

person_print("Piotr", "Mąkosa", "Kraków", "Polska", "Europa", age=23)
# warunkimem koniecznym jest wypisanie age=23 przypisane liczbie
# wypisanie wszystkich kluczy nie jest konieczne