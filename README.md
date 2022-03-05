# Media-Storage-Service

### About
A demo media storage webapp to explore AWS services like S3, Lambda and add CI/CD with Github Actions

### DIR Structure 
```
├── LICENSE
├── README.md
├── app
│   ├── __init__.py
│   ├── api
│   │   ├── __init__.py
│   │   ├── endpoint
│   │   │   ├── models.py
│   │   │   └── router.py
│   │   └── upload
│   │       ├── __init__.py
│   │       ├── config.py
│   │       └── helper.py
│   ├── config.py
│   ├── main.py
│   └── tests
│       ├── __init__.py
│       └── test.py
└── frontend
    ├── index.html
    └── upload.js
```