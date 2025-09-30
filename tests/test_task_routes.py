import os

import pytest
import utils


@pytest.fixture(scope="function", autouse=True)
def setup(session, valid_user):
    session.add(valid_user)
    session.commit()
    yield


def test_upload_task(test_client, valid_user):
    utils.login(test_client, valid_user.email, "abcabc")

    access_token = str(os.environ.get("TEST_ACCESS_TOKEN"))
    headers = {"Authorization": "Bearer {}".format(access_token)}
    json_obj = {
        "dataset_id": "128",
        "task_type": "classification",
        "target_name": "class",
        "evaluation_measure": "predictive_accuracy",
    }
    response = test_client.post("/upload-task", headers=headers, json=json_obj)
    print(response)

    assert response.status_code == 200
