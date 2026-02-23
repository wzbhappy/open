from open_app import get_status


def test_status_message() -> None:
    assert get_status() == "open-app is ready"
