from myapp.app import lambda_handler

import pytest


@pytest.fixture
def mock_load_config(mocker):
    mock_s3 = mocker.Mock()
    mocker.patch("myapp.app.s3_client", mock_s3)

    return mocker.patch(
        "myapp.app.load_config",
        return_value={
            "DB_HOST": "fixture-host",
            "DB_USER": "fixture-user"
        }
    )


def test_lambda_handler(mock_load_config):
    response = lambda_handler({}, None)

    assert response["statusCode"] == 200
    assert response["db_host"] == "fixture-host"
