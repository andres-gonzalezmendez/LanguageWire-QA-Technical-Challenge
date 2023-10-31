Given our translation site LWT, which is designed for text and document translations, we need to test that the application meets the following criteria.

ACCEPTANCE CRITERIA:
- Text and document translation works for all languages available in API.
- The UI navigation and looks are correct on desktop and mobile.
- UI based on the API results.
- The system supports 10 concurrent users doing text translation.

NOTES:
- Token: `3iMj9mqMVteYCbXDREbZdXWmdbTQ8vPfOMUQzLHsngk%3D.eyJOb25jZSI6ICJOb25jZSIsICJGaXJzdE5hbWUiOiAiRmlyc3ROYW1lIiwgIkxhc3ROYW1lIjogIkxhc3ROYW1lIiwgIlBob3RvRnNlSWQiOiAiUGhvdG9Gc2VJZCIsICJVc2VySWQiOiAxMTA1Njg5LCAiRGVmYXVsdENvbXBhbnlJZCI6IDEsICJMd3RTdWJzY3JpcHRpb25JZCI6IG51bGwsICJQZXJtaXNzaW9ucyI6IFszMDkyXSwgIkV4cGlyYXRpb25UaW1lIjogIi9EYXRlKDE2OTkyNTg3OTY5NzYpLyJ9`
- URL for Frontend: `https://demo-qa-lwt.staging.lw-ml.net/?token={TOKEN}`
- API: `https://demo-qa-lwt.api.staging.lw-ml.net/docs`
- TokenAuthentication for API: `Agito {TOKEN}`

# Question 1
Could you tell what kind of data is contained in the token?

# Question 2
Can you find any errors in the LWT API documentation? 

# Question 3
Could you write unit tests for this function? It would be preferable if you use Python, but pseudocode is acceptable as well. Private functions are not included on purpose, their behaviour is not expected to be written, just mocked.

```
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
```
