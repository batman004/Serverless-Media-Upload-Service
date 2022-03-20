# Media-Upload-Service

### About
A highly optimized media upload web-service which increases upload speeds and reduces throttling while handling multiple API requests.

### Tools and Technologies used

- Python (FastAPI) to write the API 
- AWS Lambda to allow auto-scaling and load balancing
- AWS API Gateway to expose the Lambda function via a known URL
- AWS S3 Bucket as storage for media
- HTML, CSS and JavaScript to create a simple UI, add styling and run client side scripts respectively

### Installation

#### Requirements

* Python 3.8 or above
* An IDE/editor of your choice
* Dependencies installed
* Environment secrets

#### Steps to run

* Clone this repository locally by opening up your terminal and running the command 

```
git clone https://github.com/batman004/Media-Storage-Service.git
``` 
* CD into the project folder and create a virtual environment by executing 

```
virtualenv env
```
* Next install all the dependencies by running 

```
pip install -r requirements.txt
```

* Fill in the environement secrets :
    create a file called `.env` at the root of the app DIR and fill in the following values

```
AWS_ACCESS_KEY_ID = 
AWS_SECRET_ACCESS_KEY = 
AWS_DEFAULT_REGION = 
DB_URL = 
DB_NAME = 
JWT_SECRET_KEY = 
ALGORITHM = HS256
```
* now cd into the app folder and run the api with `python main.py` which will spin up a uvicorn sever which listens to requests on 
```port:8000```
* Go to `http://localhost:8000/docs` to see the automated swagger docs and explore the API endpoints

### DIR Structure 
```
├── LICENSE
├── README.md
├── api
│   ├── __init__.py
│   ├── auth
│   │   ├── auth_bearer.py
│   │   ├── auth_handler.py
│   │   ├── hashing.py
│   │   └── helper.py
│   ├── config.py
│   ├── endpoints
│   │   ├── models.py
│   │   └── router.py
│   ├── main.py
│   └── upload
│       ├── __init__.py
│       ├── config.py
│       └── helper.py
├── requirements.txt
└── tests
    ├── __init__.py
    ├── test.txt
    └── test_main.py
```

### High-Level System Design

![System Design](https://user-images.githubusercontent.com/58564635/159136643-81b1559e-ec96-408d-97e4-fbeb69a8ed5d.png)
