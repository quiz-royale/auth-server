from db import DummyDbService


def test_dummy_db(mocker):
    db = DummyDbService()
    u1 = mocker.sentinel.u1
    u2 = mocker.sentinel.u2
    db._USERS = [u1, u2]

    users = db.get_users()

    assert users == [u1, u2]
