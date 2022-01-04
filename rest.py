"""REST related functions"""
import urllib3
import urllib.parse

user_agent_str: str = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0'


# TODO What is the return type????
def make_request_urllib3(method: str, endpoint: str, headers: dict[str, str] , queries: dict[str, str]):
    """
    Makes a REST request using urllib3
    :param method: The REST method to use
    :param endpoint: The endpoint URL to send the request to
    :param headers: The headers to attach to the request
    :param queries: The information to query the endpoint with
    :return: The Response from urllib3
    """
    url = f"{endpoint}?{urllib.parse.urlencode(queries)}"
    with urllib3.PoolManager() as http:
        response = http.request(method, url, headers=headers)
    # print(response.data)
    return response
