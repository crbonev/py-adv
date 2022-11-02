def get_info(name, town, age, **kwargs):
    return f"This is {name} from {town} and he is {age} years old"


print(get_info(**{"first_level": "George", "town": "Sofia", "age": 20}))
