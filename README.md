# Fizz Buzz classifier
Demo Fizz Buzz classifier base on Python with sklearn

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

## 
- git clone https://github.com/ameksike/kdd.fizz.buzz.classifier.git
- pip install -r requirements.txt
- pip list

## Run 1
- heroku local web -f Procfile.win2
- http://127.0.0.1:8000/

## Run 2
- python bin/server.py 
- http://127.0.0.1:8000/

### Endpoint Generate

Request:
```
POST http://127.0.0.1:8000/api/lcs/generate
{
    "size": 10
}
```
response: 
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

### Endpoint Traing
```
POST http://127.0.0.1:8000/api/lcs/traing
```
Response:
```json
{ 
    "accuracy_score": 1.0, 
    "classifer_name": "data/classifier_100_data_model.pkl", 
    "cross_validation_score_mean": 0.9375, 
    "cross_validation_scores": [ 1.0, 1.0, 1.0, 1.0, 0.875, 0.875, 0.875, 0.875, 0.875, 1.0 ], 
    "f1_score": 1.0, "precision_score": 1.0, 
    "recall_score": 1.0 
}
```

### Endpoint Classify
```
POST http://127.0.0.1:8000/api/lcs/classify
```

