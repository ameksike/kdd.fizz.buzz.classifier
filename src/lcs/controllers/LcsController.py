import os
from flask import Flask, request, jsonify, make_response
from server import app
from services.EtlService import EtlService
from services.MlService import MlService

srvEtl = EtlService()
srvMl = MlService()
srvMl.setEtl(srvEtl)

@app.route("/api/lcs/generate", methods=["POST"])
def generate():
    sample_size = request.form.get("Sample Size")
    result = srvEtl.generate(sample_size)
    resp = make_response(result.to_csv(index=False))
    resp.headers["Content-Disposition"] = "attachment; filename=sample_data_" + sample_size +".csv"
    resp.headers["Content-Type"] = "text/csv"
    return resp

@app.route("/api/lcs/traing", methods=["POST"])
def traing():
    f = request.files['archive']
    cross_validation_scores, cross_validation_score_mean, accuracy_score, precision_score, recall_score, f1_score, classifer_name = \
        srvMl.train(f.filename)

    return {
        "cross_validation_scores": cross_validation_scores,
        "cross_validation_score_mean": cross_validation_score_mean,
        "accuracy_score": accuracy_score,
        "precision_score": precision_score,
        "recall_score": recall_score,
        "f1_score": f1_score,
        "classifer_name": classifer_name
    }

@app.route("/api/lcs/classify", methods=["POST"])
def classify():
    file_classifer = request.files['archive']
    numFrom = request.form.get("from")
    numTo = request.form.get("to")
    result, f1_score = srvMl.classify(file_classifer.filename, int(numFrom), int(numTo))
    return {
        "numFrom": str(numFrom), 
        "numTo":  str(numTo), 
        "result": result,
        "score": str(f1_score)
    }


