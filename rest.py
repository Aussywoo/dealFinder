import urllib3
import urllib.parse

user_agent_str: str = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0'


# TODO What is the return type????
def make_request_urllib3(method: str, endpoint: str, headers: dict[str, str] , queries: dict[str, str]):
    url = f"{endpoint}?{urllib.parse.urlencode(queries)}"
    with urllib3.PoolManager() as http:
        response = http.request(method, url, headers=headers)
    # print(response.data)
    return response