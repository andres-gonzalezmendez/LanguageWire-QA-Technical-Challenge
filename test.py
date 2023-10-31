from function import (
    decode,
    InvalidTokenError,
    DecodeError,
    InvalidSignatureError,
    ExpiredSignatureError,
    InvalidExpireError,
    InvalidKeyError,
    )

class TestDecodeMethod():
    """All methods in this class should return True to verify the correct behaviour of the decode method"""

    def test_decode(self):
        token = "this_is_a_valid_token"
        key = "this_is_a_valid_key"
        decoded_token = {"expected": "this_is_the_expected_decoded_token"}

        assert decode(token, key) is decoded_token
    
    def test_invalid_token_error(self):
        token = "this_is_a_token_with_just_one_part"
        key = "any_key"

        try:
            decode(token, key)
        except InvalidTokenError:
            return True
        else:
            return False
        
    def test_decode_error(self):
        token="this_is_a_token_encoded_with_an_encoding_other_than_base64url_which_is_not_supported"
        key = "any_key"

        try:
            decode(token, key)
        except DecodeError:
            return True
        else:
            return False
        
    def test_invalid_signature_error(self):
        token="this_is_a_token_that_will_fail_to_verify_the_signature_with_the_key_below"
        key = "this_key"

        try:
            decode(token, key)
        except InvalidSignatureError:
            return True
        else:
            return False
        
    def test_expired_signature_and_invald_expire_error(self):
        token="this_is_a_token_with_an_outdated_expiration_date"
        key = "the_key"

        try:
            decode(token, key)
        except (ExpiredSignatureError, InvalidExpireError):
            return True
        else:
            return False
        
    def test_invalid_key_error(self):
        token="this_is_a_valid_token"
        key = None

        try:
            decode(token, key)
        except InvalidKeyError:
            return True
        else:
            return False
