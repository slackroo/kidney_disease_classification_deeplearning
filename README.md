# kidney_disease_classification_deeplearning MLflow and DVC
...
## Workflows

1. Update config.yaml
2. update secret.yaml [not added currently]
3. update params.yaml
4. update the entity
5. update the configuration manager in src config
6. update components
7. update pipeline
8. update main.py
9. update dvc.yaml 
10. update app.py

...
### Dataset link 
````
https://www.kaggle.com/datasets/nazmul0087/ct-kidney-dataset-normal-cyst-tumor-and-stone
````
Islam MN, Hasan M, Hossain M, Alam M, Rabiul G, Uddin MZ, Soylu A. Vision transformer and explainable transfer learning models for auto detection of kidney cyst, stone and tumor from CT-radiography. Scientific Reports. 2022 Jul 6;12(1):1-4.


# How to run?

### Steps:

Clone the repository 

````bash
https://github.com/slackroo/kidney_disease_classification_deeplearning
````
### Step1 - Create a virtual environment after downloading the repository
I am using pycharm, when opening the project select create new virtual environment with python3.8 python interpreter

### Step2 - Install the requirement packages
````bash
pip install requirements.txt
````
## MLflow

- [Documentation](https://mlflow.org/docs/latest/index.html)

- [MLflow tutorial](https://www.youtube.com/watch?v=daBTYQP23-A&ab_channel=DagsHub)

##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

Everytime the project is closed, We need to add the below 3 lines on the terminal to re-establish the connection to dagshub

MLFLOW_TRACKING_URI=https://dagshub.com/slackroo/kidney_disease_classification_deeplearning.mlflow\
MLFLOW_TRACKING_USERNAME=slackroo\
MLFLOW_TRACKING_PASSWORD=e383057a1f050e672c874aef175d897f88ad2ea2\
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/slackroo/kidney_disease_classification_deeplearning.mlflow

export MLFLOW_TRACKING_USERNAME=slackroo 

export MLFLOW_TRACKING_PASSWORD=e383057a1f050e672c874aef175d897f88ad2ea2

```

### DVC cmd
1. dvc init
2. dvc repro
3. dvc dag


### Flask cmd
To run the flask app I have created a index.html from bootstrap template 
We can run  the app with command

````bash
python app.py
````

 