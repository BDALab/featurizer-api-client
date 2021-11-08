from pprint import pprint
from http import HTTPStatus
from featurizer_api_client import FeaturizerApiClient


def refresh_access_token():
    """Example code: refresh an expired access token"""

    # Prepare the featurizer API client settings
    #
    # ---------------------------------------------- #
    # Must be same as for the running Featurizer API #
    # ---------------------------------------------- #
    #
    # 1. host (IP address)
    # 2. port (port number)
    # 3. request verification
    # 4. request timeout in seconds
    host = "http://127.0.0.1"
    port = 5000
    verify = True
    timeout = 2

    # Instantiate the featurizer API client
    client = FeaturizerApiClient(host=host, port=port, verify=verify, timeout=timeout)

    # TODO: prepare data for request authorization (refresh token from: ./02_log_in_user.py)
    refresh_token = "<TODO: FILL-IN>"

    print("\n-- [03] example --")
    print("Refreshing an expired access token\n")

    # Refresh an expired access token
    response, status_code = client.refresh_access_token(refresh_token)

    # Check the output
    if status_code == HTTPStatus.OK:
        print("Successfully refreshed an expired access token")
    else:
        print(f"The request was unsuccessful ({status_code}): {response}")

    print("Response:")
    pprint(response)


if __name__ == "__main__":
    refresh_access_token()
