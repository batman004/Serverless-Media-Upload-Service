# Media-Storage-Service

### About
A demo media storage webapp to explore and learn about AWS services like S3, Lambda and add CI/CD with Github Actions

### DIR Structure 
```
├── LICENSE
├── README.md
├── app   
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
│       ├── test.txt
│       └── test_main.py
├── frontend
│   ├── assets
│   │   ├── css
│   │   │   └── styles.css
│   │   └── media
│   │       └── logo.png
│   ├── js
│   │   └── upload.js
│   └── templates
│       ├── index.html
│       └── signup.html
└── requirements.txt
```

### High-Level System Design

![System Design](https://user-images.githubusercontent.com/58564635/156899246-80606234-1c13-4062-8d76-7cb181078121.png)
