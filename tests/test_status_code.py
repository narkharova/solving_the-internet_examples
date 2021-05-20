import requests
import pytest
from core.browser_helper import BrowserHelpers


@pytest.mark.parametrize('status_code', [200, 301, 404, 500])
def test_status_code(status_code):
    get_response = requests.get(BrowserHelpers().base_url + '/status_codes/' + str(status_code))
    assert get_response.status_code == status_code
