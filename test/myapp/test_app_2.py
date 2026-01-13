from myapp.app import lambda_handler


def test_lambda_handler(mocker):
    mock_s3_client = mocker.Mock()
    mock_body = mocker.Mock()
    mock_body.read.return_value = b"DB_HOST=test-host\nDB_USER=test-user\n"
    mock_s3_client.get_object.return_value = {"Body": mock_body}
    mocker.patch("myapp.app.s3_client", mock_s3_client)

    response = lambda_handler({}, None)

    assert response["statusCode"] == 200
    assert response["db_host"] == "test-host"
