def kwargs_length(**kwargs):
    return len(kwargs)


dictionary = {'first_level': 'Peter', 'age': 25}

print(kwargs_length(**dictionary))
