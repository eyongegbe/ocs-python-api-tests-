import requests
from pytest import mark

"""these tests verify http responses for the OCS API
Athletes resource uri
"""


@mark.athletes
class AthletesTests:

    def test_all_records_have_expected_fields(self, all_athletes_route):
        response = requests.get(all_athletes_route)
        assert response.status_code == 200
        for athlete in response.json():
            assert 'athlete_id' in athlete
            assert 'name' in athlete
            assert 'surname' in athlete
            assert 'dateOfBirth' in athlete
            assert 'bio' in athlete
            assert 'weight' in athlete
            assert 'height' in athlete
            assert 'photo_id' in athlete

    def test_can_return_specific_athlete_data(self, all_athletes_route):
        athlete_id = '8'
        response = requests.get(all_athletes_route + athlete_id)
        assert response.status_code == 200
        data = response.json()
        assert 'athlete_id' in data
        assert 'name' in data
        assert 'surname' in data
        assert 'dateOfBirth' in data
        assert 'bio' in data
        assert 'weight' in data
        assert 'height' in data
        assert 'photo_id' in data
