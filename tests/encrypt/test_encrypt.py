from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    assert encrypt_message("amaral", -1) == "larama"

    assert encrypt_message("amaral", 3) == "ama_lar"

    assert encrypt_message("amaral", 4) == "la_rama"

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message(12, "key")
