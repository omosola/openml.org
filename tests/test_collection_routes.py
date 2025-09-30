import os

import pytest
import utils

@pytest.fixture(scope="function", autouse=True)
def setup(session, test_client, valid_user):
    session.add(valid_user)
    session.commit()
    utils.login(test_client, valid_user.email, "abcabc")
    yield


def test_upload_collection_runs(test_client):
    access_token = str(os.environ.get("TEST_ACCESS_TOKEN"))
    headers = {"Authorization": "Bearer {}".format(access_token)}
    json_obj = {
        "run_ids": "1,2,3,4",
        "collectionname": "test",
        "description": "test desc",
        "benchmark": "23",
    }
    response = test_client.post(
        "/upload-collection-runs", headers=headers, json=json_obj
    )

    assert response.json["msg"] == "collection uploaded"
    assert response.status_code == 200


def test_upload_collection_tasks(test_client):
    access_token = str(os.environ.get("TEST_ACCESS_TOKEN"))
    headers = {"Authorization": "Bearer {}".format(access_token)}
    json_obj = {
        "taskids": "1,2,3,4",
        "collectionname": "test",
        "description": "test desc",
    }
    response = test_client.post(
        "/upload-collection-tasks", headers=headers, json=json_obj
    )

    assert response.json["msg"] == "collection uploaded"    
    assert response.status_code == 200
