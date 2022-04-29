# Serverless-Media-Upload-Service

### About
A highly optimized media upload web-service which increases upload speeds and reduces latency while handling multiple API requests.
(see [System Design](#high-level-system-design) below) 

### Motivation

Typically, in a server-based environment, the process of uploading media is as follows:

![](https://user-images.githubusercontent.com/58564635/159216309-71b205b5-297b-4f46-86c9-544f6f3a6f83.png)


While the procedure is straightforward, it can have a considerable impact on the web server's speed in high-volume applications. Because media uploads are often huge, they can consume a significant amount of network I/O and server CPU time. You must also keep track of the transfer's progress to verify that the entire item is uploaded successfully, as well as retries and mistakes. If thousands of users attempt to upload media around the same time, this requires you to scale out the application server and ensure that there is sufficient network bandwidth available.

### Methodology

- **Directly publishing files to Amazon S3** can help your application server manage additional requests during busy moments by **reducing network traffic and server CPU use**. S3 is also extremely accessible and long-lasting, making it an excellent long-term storage option for user uploads.

- This is primarily achieved by transferring the upload latency dependency completely on the client side. I have used a [Pre-Signed URL](https://docs.aws.amazon.com/AmazonS3/latest/userguide/PresignedUrlUploadObject.html) recieved from the S3 Bucket which allows public read/write access to it. 
Once the client recieves the Pre-signed URL, they can run a script to upload the desired files without any permissions. This is why protecting the `api/services/upload` endpoint is of great importance.
I have used JWT tokens which would be required as a part of the headers while sending an upload request to the server to verify a given user, apart from getting authenticated by querying user data from a database.

- Another reason why I call this service optimized is that I have tried to mitigate issues such as API throttling and slow response times by deploying my API as an edge function through AWS Lambda. this was 

### Tools and Technologies used

- Python (FastAPI) to write the REST-API 
- AWS Lambda for deploying our API and to allow auto-scaling and load balancing
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

# activate the env
source env/bin/activate (Linux/MacOS)
env\Scripts\activate (Windows)
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

### High Level System Design

![System Design](https://user-images.githubusercontent.com/58564635/159136643-81b1559e-ec96-408d-97e4-fbeb69a8ed5d.png)
