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
    sample_size = request.json.get("size", 100)
    result = srvEtl.generate(sample_size)
    resp = make_response(result.to_csv(index=False))
    resp.headers["Content-Disposition"] = "attachment; filename=sample_data_" + str(sample_size) +".csv"
    resp.headers["Content-Type"] = "text/csv"
    return resp

@app.route("/api/lcs/traing", methods=["POST"])
def traing():
    path = os.path.dirname(__file__) + "../../../../data/"
    filename = path + request.form.get("modelname", 'sample_data_100') + ".csv"
    filename = os.path.abspath(filename)

    cross_validation_scores, cross_validation_score_mean, accuracy_score, precision_score, recall_score, f1_score, classifer_name = \
        srvMl.train(filename)

    payload = {
        "cross_validation_scores": cross_validation_scores.tolist(),
        "cross_validation_score_mean": cross_validation_score_mean,
        "accuracy_score": accuracy_score,
        "precision_score": precision_score,
        "recall_score": recall_score,
        "f1_score": f1_score,
        "classifer_name": classifer_name
    }
    return jsonify(payload)

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


