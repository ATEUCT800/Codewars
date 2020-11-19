import json

def json_decorator(json_file):
    def inner_decorator(cls):
        def wrapper(*args, **kwargs):
            if not args and not kwargs:
                with open(json_file, 'r') as jf:
                    arguments = json.load(jf)
                return cls(**arguments)
            return cls(*args, **kwargs)
        return wrapper
    return inner_decorator

@json_decorator('Codewars\\Json decorator\\arguments.json')
class Ship:
    
    def __init__(self, weight = None, crew = None):
        self.weight = weight
        self.crew = crew
    
    # def __str__(self):
    #     return f'Ship args:\n weight = {self.weight}\n crew = {self.crew}'

ship1 = Ship(14, 10)
print(ship1)

ship2 = Ship()
print(ship2)
