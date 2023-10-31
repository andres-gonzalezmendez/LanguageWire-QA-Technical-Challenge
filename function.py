# We want to reuse the same exception as pyjwt so that it would be easier
# to switch to it afterwards if needed.
class PyJWTError(Exception):
"""Base class for all token exceptions."""

class InvalidTokenError(PyJWTError):
"""Token has invalid structure."""

class DecodeError(InvalidTokenError):
"""Base class for exceptions when decoding."""

class InvalidSignatureError(DecodeError):
"""Signature does not match."""

class InvalidAlgorithmError(DecodeError):
"""The specified alg value is not allowed."""

class ExpiredSignatureError(InvalidTokenError):
"""Token/signature has expired."""

class InvalidExpireError(InvalidTokenError):
"""Expiration time has an invalid format."""

class InvalidAudienceError(InvalidTokenError):
"""The audience is invalid."""

class InvalidKeyError(PyJWTError):
"""Key used for signature is invalid."""

def decode(token: str, key: str) -> dict:
   """Decode the token using the given key.
   :param token: the token to decode
   :param key: the key used to sign the token
   :raises InvalidKeyError: if the given key is None
   :raises InvalidTokenError: if the token has an invalid structure
   :raises InvalidSignatureError: if the actual signature doesn't match with the given
   :raises ExpiredSignatureError: if the token has expired
   :raises InvalidExpireError: if the expiration time is invalid
   :return: decoded token payload
   """
   if key is None:
       raise InvalidKeyError("Key must be provided")

   parts = token.split(".")
   if len(parts) != 2:
       raise InvalidTokenError(
           f"Invalid token structure. Expected 2 parts, got {len(parts)}."
       )

   # will raise DecodeError if wrong
   decoded_token_data = _base64url_decode(parts[1])

   # will raise InvalidSignatureError if wrong
   _verify_signature(decoded_token_data, key)

   try:
       token_data = json.loads(decoded_token_data.decode())
   except UnicodeDecodeError as ex:
       raise DecodeError("Invalid JSON payload string") from ex

   # will raise ExpiredSignatureError or InvalidExpireError if wrong
   _verify_expiration(token_data)
   return token_data
