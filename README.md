# TropiPay Fraud Detection System 


## Skeleton 

```plain
- bin: Binaries
- cfg: Configurations
- src: Source Code
    - eda: Exploratory Data Analysis
    - lsc: Learning Classifier System
```

## Requirements 
- python v3.8.3
- pip v20.1.1

## Install
- pip install -r requirements.txt
- pip list

## Run 1
- heroku local web -f Procfile.win2
- http://127.0.0.1:8000/

## Run 2
- python bin/server.py 
- http://127.0.0.1:8000/

## Endpoints 
- POST http://127.0.0.1:8000/api/lcs/generate
- POST http://127.0.0.1:8000/api/lcs/traing
- POST http://127.0.0.1:8000/api/lcs/classify

