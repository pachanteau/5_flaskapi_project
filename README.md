
### Serve your model with API

## ML in production project

### ML in production

Wine-o-meter is a future unicorn application. It allows wine producers to predict the quality score of their wine based on physicochemical inputs. The startup behind this innovation is convinced about its ability to disrupt the world of wine. 🍷


## Project 🚧
The data-science team has worked together on creating the best model predicting the quality score (from 0 to 10) of multiple wines. The next step is to include this model into the mobile application. The development team is expecting an API endpoint in order to request the model and display the result inside the application.

Your job is to put the trained model into production. Hopefully, the team provided you their work:

a model.joblib which is the trained model pickled (saved using joblib library),
the notebook used to train the model (Model_Training.ipynb) and the dataset (winequality.csv), so you can have a look,
a test notebook (Test_Endpoint.ipynb) so you can assert that your endpoint is meeting the requirements.


## Goals 🎯

Your mission is to put this model into production by building an API. To succeed you need to:

provide a /predict endpoint,
provide a small documentation for the developer team at the index of your website.
In the following text, we describe the technical expectations:

/predict endpoint
You should provide at least one endpoint /predict. The full URL would look like something like this: https://your-url.com/predict.

This endpoint accepts POST method with JSON input data and it should return the predictions. We assume inputs will be always well formatted. It means you do not have to manage errors. We leave the error handling as a bonus.

Input example:

{
  "input": [[7.0, 0.27, 0.36, 20.7, 0.045, 45.0, 170.0, 1.001, 3.0, 0.45, 8.8], [7.0, 0.27, 0.36, 20.7, 0.045, 45.0, 170.0, 1.001, 3.0, 0.45, 8.8]]
}
The response should be a JSON with one key prediction corresponding to the prediction.

Response example:

{
  "prediction":[6,6]
}


## Documentation page

You need to provide the users with a small HTML page documentation about your API.

It has to be located at the index of your website. If we take the URL example above, it should be located directly at https://your-url.com).

This small documentation should at least include:

An h1 title: the title is up to you.
A description of every endpoints the user can call with the endpoint name, the HTTP method, the required input and the expected output (you can give example).
You are free to add other any other relevant informations and style your HTML as you wish.


## Online production

You have to host your API online. We recommend you to use Heroku as it is free of charge. But you are free to choose any other hosting provider.


## Deliverable 📬

To complete this project, you should deliver:

The whole code stored in a Github repository. You will include the repository's URL.
An online API on Heroku server (or any other provider you choose) with an HTML page documentation at the website index and one /predict endpoint at least that respect the technical description above. We should be able to request the API endpoint /predict using curl:
$ curl -i -H "Content-Type: application/json" -X POST -d '{"input": [[7.0, 0.27, 0.36, 20.7, 0.045, 45.0, 170.0, 1.001, 3.0, 0.45, 8.8]]}' http://your-url/predict
Or Python:

import requests

response = requests.post("https://your-url/predict", json={
    "input": [[7.0, 0.27, 0.36, 20.7, 0.045, 45.0, 170.0, 1.001, 3.0, 0.45, 8.8]]
})
print(response.json())
