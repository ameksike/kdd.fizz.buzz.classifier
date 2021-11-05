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



### 

```
2,3,5,7,11,13,Class 
0,0,0,0,0,0,4 
1,1,0,0,0,0,3 
0,0,0,0,0,0,4 
1,0,0,0,0,1,4 
0,1,1,1,0,0,1 
1,0,0,0,0,0,4 
0,0,0,0,0,0,4 
1,1,0,0,0,0,3 
0,0,0,0,0,0,4 
1,0,1,0,1,0,2
```