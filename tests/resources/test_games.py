import requests
from pytest import mark


"""these tests verify http responses for the OCS API
Games resource uri
"""

@mark.games
class GamesTests:
    def test_can_get_all_games_in_no_order(self, games_route):
        response = requests.get(games_route)
        assert response.status_code == 200
        for games in response.json():
            assert 'game_id' in games
            assert 'city' in games
            assert 'year' in games

    def test_can_return_participating_athletes_by_id(self, games_route):
        game_id = '2'
        games_route = games_route + '/' + game_id + '/athletes'
        response = requests.get(games_route)
        assert response.status_code == 200