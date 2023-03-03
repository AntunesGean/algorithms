from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():

    assert encrypt_message("abcabc", 3) == "cba_cba"
    assert encrypt_message("abcabc", 4) == "cb_acba"
    assert encrypt_message("abcabc", 9) == "cbacba"

    with pytest.raises(TypeError):
        encrypt_message(3, "abcabc")
