import requests
from pytest import mark

"""these tests verify http responses for the OCS API
Photo resource uri
"""


@mark.photo
class PhotoTests:
    def test_can_get_athlete_photo(self, all_athletes_route):
        athlete_photo_route = all_athletes_route + '2/photo'
        response = requests.get(athlete_photo_route)
        assert response.status_code == 200
