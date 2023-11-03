# LanguageWire - QA Technical Challenge

By: Andrés González Méndez

Date: Oct 31, 2023

View challenge [here](challenge.md).

## Results

First thing I do:

- I open the API documentation page: `https://demo-qa-lwt.api.staging.lw-ml.net/docs`

- I add the `TokenAuthentication` that was provided.

### Question 1
**Criteria 1: Text and document translation works for all languages available in API.**

API:

- I make the following request:
    ```
    curl -X 'GET' \
        'https://demo-qa-lwt.api.staging.lw-ml.net/api/v1/language-pairs?includeVariants=true' \
        -H 'accept: application/json' \
        -H 'Authorization: Agito 3iMj9mqMVteYCbXDREbZdXWmdbTQ8vPfOMUQzLHsngk%3D.eyJOb25jZSI6ICJOb25jZSIsICJGaXJzdE5hbWUiOiAiRmlyc3ROYW1lIiwgIkxhc3ROYW1lIjogIkxhc3ROYW1lIiwgIlBob3RvRnNlSWQiOiAiUGhvdG9Gc2VJZCIsICJVc2VySWQiOiAxMTA1Njg5LCAiRGVmYXVsdENvbXBhbnlJZCI6IDEsICJMd3RTdWJzY3JpcHRpb25JZCI6IG51bGwsICJQZXJtaXNzaW9ucyI6IFszMDkyXSwgIkV4cGlyYXRpb25UaW1lIjogIi9EYXRlKDE2OTkyNTg3OTY5NzYpLyJ9'
    ```

- The API response is a JSON file with all possible combinations of source and target language

Frontend app:

- Text translation:

    - I open the app
    
    - I select the first source language and target language provided in the response

    - I enter a text in the source language

    - I wait for the app to offer a translation

    - I verify the translation corresponds to the target language

    - I repeat for all combinations of source and target language

- Document translation:

    - I open the app
    
    - I select the first source language and target language provided in the response

    - I click on Browse button and select a document in the source language (or drag and drop to the source language section)

    - I click on the "Translate to `target language`" button

    - I wait for the app to offer a translation

    - I save the document in my computer

    - I verify the translation corresponds to the target language

    - I repeat for all combinations of source and target language

**Criteria 2: The UI navigation and looks are correct on desktop and mobile.**

Both desktop and mobile:

- I open the app

- I verify all elements on screen

- I expand all menus and select all possible options

- I verify all navigation patterns work correct

**Criteria 3: UI based on the API results.**

API:

- I make the following request:
    ```
    curl -X 'POST' \
        'https://demo-qa-lwt.api.staging.lw-ml.net/api/v1/translations/text' \
        -H 'accept: application/json' \
        -H 'Authorization: Agito 3iMj9mqMVteYCbXDREbZdXWmdbTQ8vPfOMUQzLHsngk%3D.eyJOb25jZSI6ICJOb25jZSIsICJGaXJzdE5hbWUiOiAiRmlyc3ROYW1lIiwgIkxhc3ROYW1lIjogIkxhc3ROYW1lIiwgIlBob3RvRnNlSWQiOiAiUGhvdG9Gc2VJZCIsICJVc2VySWQiOiAxMTA1Njg5LCAiRGVmYXVsdENvbXBhbnlJZCI6IDEsICJMd3RTdWJzY3JpcHRpb25JZCI6IG51bGwsICJQZXJtaXNzaW9ucyI6IFszMDkyXSwgIkV4cGlyYXRpb25UaW1lIjogIi9EYXRlKDE2OTkyNTg3OTY5NzYpLyJ9' \
        -H 'Content-Type: application/json' \
        -d '{
        "sourceLanguage": "es",
        "targetLanguage": "en",
        "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "sourceText": "Hola, esto es una prueba de traducción de español a inglés. ¡Gracias!"
        }'
    ```

- Translation provided by API: `Hello, this is a Spanish to English translation test. Thanks a lot!`

Frontend:

- I open the app
    
- I select `Spanish` as source language and `English` as target language

- I enter the text `Hola, esto es una prueba de traducción de español a inglés. ¡Gracias!` in the source language section

- I wait for the app to offer a translation

- I verify the translation is the same translation provided by API: `Hello, this is a Spanish to English translation test. Thanks a lot!`

**Criteria 4: The system supports 10 concurrent users doing text translation.**

For this test I can only think of a program that sends multiple concurrent requests to a server and verifies the responses obtained. 

I first thought on Postman, but as far as I know it can only send sequential requests, so I googled for a solution and I found out that Apache JMeter is able to do this.

I have never used this software though, but I guess this would be the best way to test this.

### Question 2

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


### Question 3

- In the Auth section, there is this action to get information from the token: `POST api/v1/auth/token-info`

- As per the documentation, the request should include the header `X-LWT-Locale`.

- But current behaviour is that you don't actually need to include this header to get a response.


### Question 4

- I know there is a Python module called `unittest` that offers some help to write the unit tests, but I preferred to use the classic try-except formula.

- See python file [here](test.py)
