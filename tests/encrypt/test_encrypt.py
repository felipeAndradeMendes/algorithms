from challenges.challenge_encrypt_message import encrypt_message
# import pytest


# def test_encrypt_message_incorrect_message_type():
#     with pytest.raises(TypeError, match="tipo inválido para message"):
#         encrypt_message(12, 3)


# def test_encrypt_message_incorrect_key_type():
#     with pytest.raises(TypeError, match="tipo inválido para key"):
#         encrypt_message("message", "key")


def test_encrypt_message_negative_key():
    assert encrypt_message('amaral', -1) == 'larama'


def test_encrypt_message_key_odd():
    assert encrypt_message("amaral", 3) == "ama_lar"


def test_encrypt_message_key_even():
    assert encrypt_message("amaral", 4) == "la_rama"
