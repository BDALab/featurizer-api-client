from pprint import pprint
from http import HTTPStatus
from featurizer_api_client import FeaturizerApiClient


def example_sign_up_user():
    """Example code: sign-up a new user"""

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

    # TODO: prepare data for a new user (see the API's requirements on the password)
    #
    # 1. username
    # 2. password (e.g. can be generated with https://passwordsgenerator.net/)
    username = "<TODO: FILL-IN>"
    password = "<TODO: FILL-IN>"

    print("\n-- [01] example --")
    print(f"Signing-up a new user with username: {username} and password: {password}\n")

    # Sign-up a new user
    response, status_code = client.sign_up(username, password)

    # Check the output
    if status_code == HTTPStatus.OK:
        print("Successfully signed-up a new user")
    else:
        print(f"The request was unsuccessful ({status_code}): {response}")

    print("Response:")
    pprint(response)


if __name__ == "__main__":
    example_sign_up_user()
