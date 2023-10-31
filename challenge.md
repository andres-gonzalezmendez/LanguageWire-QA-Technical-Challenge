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

See function [here](function.py)
