from pprint import pprint
from http import HTTPStatus
from featurizer_api_client import FeaturizerApiClient


def featurize():
    """Example code: calls .featurize(...) on an injected features extractor"""

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

    # TODO: prepare data for request authorization (access token and refresh token)
    access_token = "<TODO: FILL-IN>"
    refresh_token = "<TODO: FILL-IN>"

    # TODO: prepare pipeline of features
    #
    # Example:
    # features_pipeline = [
    #     {
    #         "name": "feature 1",
    #         "args": {"abc": 123, "def": 456}
    #     },
    #     {
    #         "name": "feature 2",
    #         "args": {"ghi": "simple", "jkl": False}
    #     },
    #     {
    #         "name": "feature 3",
    #         "args": {}
    #     }
    # ]
    features_pipeline = "<TODO: FILL-IN>"

    # TODO: prepare feature extractor configuration
    extractor_configuration = "<TODO: FILL-IN>"

    # TODO: prepare featurizer data (sample values/labels)
    #
    # ----------------------------------------------------- #
    # Must meet the data requirements of the Featurizer API #
    # ----------------------------------------------------- #
    #
    # Example (10 subjects, each having 100 1-D samples):
    # sample_values = numpy.random.rand(10, 1, 100)
    # sample_labels = None
    sample_values = "<TODO: FILL-IN>"
    sample_labels = None

    print("\n-- [04] example --")
    print(f"Calling .featurize(...) on a feature extractor\n")

    # Call .featurize(...) on a feature extractor
    response, status_code = client.featurize(
        features_pipeline=features_pipeline,
        sample_values=sample_values,
        sample_labels=sample_labels,
        extractor_configuration=extractor_configuration,
        access_token=access_token,
        refresh_token=refresh_token)

    # Check the output
    if status_code == HTTPStatus.OK:
        print("Successfully called .featurize(...)")
    else:
        print(f"The request was unsuccessful ({status_code}): {response}")

    print("Response:")
    pprint(response)


if __name__ == "__main__":
    featurize()
