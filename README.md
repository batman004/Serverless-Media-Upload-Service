# Media-Upload-Service

### About
A highly optimized media upload web-service which increases upload speeds and reduces throttling while handling multiple API requests.

### Tools and Technologies used

- Python (FastAPI) to write the API 
- AWS Lambda to allow auto-scaling and load balancing
- AWS API Gateway to expose the Lambda function via a known URL
- AWS S3 Bucket as storage for media
- HTML, CSS and JavaScript to create a simple UI, add styling and run client side scripts respectively

### DIR Structure 
```
├── LICENSE
├── README.md
├── app
│   ├── api
│   │   ├── __init__.py
│   │   ├── auth
│   │   │   ├── auth_bearer.py
│   │   │   ├── auth_handler.py
│   │   │   ├── hashing.py
│   │   │   └── helper.py
│   │   ├── endpoints
│   │   │   ├── models.py
│   │   │   └── router.py
│   │   └── upload
│   │       ├── __init__.py
│   │       ├── config.py
│   │       └── helper.py
│   ├── config.py
│   ├── main.py
│   └── tests
│       ├── __init__.py
│       ├── test.txt
│       └── test_main.py
├── frontend
│   ├── css
│   │   └── styles.css
│   ├── js
│   │   └── upload.js
│   └── templates
│       ├── index.html
│       ├── login.html
│       └── signup.html
└── requirements.txt
```

### High-Level System Design

![System Design](https://user-images.githubusercontent.com/58564635/159136643-81b1559e-ec96-408d-97e4-fbeb69a8ed5d.png)
