# LanguageWire - QA Technical Challenge

By: Andrés González Méndez

Date: Oct 31, 2023

View challenge [here](challenge.md).

## Results
### Question 1

- I open the API documentation page: `https://demo-qa-lwt.api.staging.lw-ml.net/docs`

- I add the `TokenAuthentication` that was provided.

- I make the following request:
    ```
    curl -X 'POST' \
        'https://demo-qa-lwt.api.staging.lw-ml.net/api/v1/auth/token-info' \
        -H 'accept: application/json' \
        -H 'Authorization: Agito 3iMj9mqMVteYCbXDREbZdXWmdbTQ8vPfOMUQzLHsngk=.eyJOb25jZSI6ICJOb25jZSIsICJGaXJzdE5hbWUiOiAiRmlyc3ROYW1lIiwgIkxhc3ROYW1lIjogIkxhc3ROYW1lIiwgIlBob3RvRnNlSWQiOiAiUGhvdG9Gc2VJZCIsICJVc2VySWQiOiAxMTA1Njg5LCAiRGVmYXVsdENvbXBhbnlJZCI6IDEsICJMd3RTdWJzY3JpcHRpb25JZCI6IG51bGwsICJQZXJtaXNzaW9ucyI6IFszMDkyXSwgIkV4cGlyYXRpb25UaW1lIjogIi9EYXRlKDE2OTkyNTg3OTY5NzYpLyJ9' \
        -d ''
    ```

- The API response is as follows:
    ```
    {
        "exp": 1699258796,
        "subscriptionId": null
    }
    ```
- The token contains information about its expiration date (timestamp), and a subscription identifier.


### Question 2

- In the Auth section, there is this action to get information from the token: `POST api/v1/auth/token-info`

- As per the documentation, the request should include the header `X-LWT-Locale`.

- But current behaviour is that you don't actually need to include this header to get a response.


### Question 3

- I know there is a Python module called `unittest` that offers some help to write the unit tests, but I preferred to use the classic try-except formula.

- See python file [here](test.py)
