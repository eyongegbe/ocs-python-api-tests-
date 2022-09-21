import requests
from pytest import mark


"""these tests verify http responses for the OCS API
Results resource uri
"""


@mark.results
class ResultsTests:

    def test_can_return_all_results_for_an_athlete(self, all_athletes_route):
        athlete_id = '20'
        response = requests.get(all_athletes_route + athlete_id + '/results')
        assert response.status_code == 200
        for result in response.json():
            assert 'city' in result
            assert 'year' in result
            assert 'gold' in result
            assert 'silver' in result
            assert 'bronze' in result
            assert 'Fourths' in result
