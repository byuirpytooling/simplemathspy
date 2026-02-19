from simplemathspy.mitch import duplicate_mitch


def test_duplicate_mitch():
    duplicated = duplicate_mitch(2)
    assert duplicated == "mitchmitch"
