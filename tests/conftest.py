from pytest import fixture

'''
A store for fixtures that are used
for initializing tests
'''

uri = "http://localhost:3000"

@fixture(scope='function')
def all_athletes_route():
    return f"{uri}/athletes/"

@fixture(scope='function')
def games_route():
    return f"{uri}/games"

