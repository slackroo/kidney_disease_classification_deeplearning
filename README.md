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

## About MLflow & DVC

MLflow

 - Its Production Grade
 - Trace all of your expriements
 - Logging & taging your model


DVC 

 - Its very lite weight for POC only
 - lite weight expriements tracker
 - It can perform Orchestration (Creating Pipelines)




# AWS CI/CD Deployment with GitHub Actions

## About MLflow & DVC

### MLflow

- Production Grade
- Trace all of your experiments
- Logging & tagging your model

### DVC

- Very lightweight for POC only
- Lightweight experiments tracker
- It can perform Orchestration (Creating Pipelines)

## Deployment Steps

### 1. Login to AWS Console

### 2. Create IAM User for Deployment

#### With Specific Access

- EC2 access: It is a virtual machine
- ECR: Elastic Container registry to save your Docker image in AWS

#### Description: About the Deployment

1. Build a Docker image of the source code
2. Push your Docker image to ECR
3. Launch Your EC2
4. Pull Your image from ECR in EC2
5. Launch your Docker image in EC2

#### Policies

1. AmazonEC2ContainerRegistryFullAccess
2. AmazonEC2FullAccess

### 3. Create ECR repo to store/save Docker image
- Save the URI: `566373416292.dkr.ecr.us-east-1.amazonaws.com/chicken`

### 4. Create EC2 machine (Ubuntu)

### 5. Open EC2 and Install Docker in EC2 Machine

#### Optional

```bash
sudo apt-get update -y
sudo apt-get upgrade
```
#### Required
```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
```

### 6. Configure EC2 as self-hosted runner:

    Go to setting>actions>runner>new self hosted runner> choose os> then run command one by one


### 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-so