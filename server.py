# -*- coding: utf-8 -*-

from flask import request, jsonify,Flask
app = Flask(__name__)
import json
# from recommendBySelection import recommendBySelection s
import recommendBySelection
import sentimentRecommendation

@app.route('/restaurant/recommendation/', methods = ["GET"])   # GET 和 POST 都可以
def get_data():
    # 假设有如下 URL
    # http://10.8.54.48:5000/index?name=john&age=20

    #可以通过 request 的 args 属性来获取参数
    lat = request.args.get("lat")
    lon = request.args.get("lon")
    text = request.args.get("text")
    time = request.args.get("time")

    # lat = -37.813629
    # lon = 144.963058
    # time = 14
    # text = "I am happy with chinese food."
    print("lat: ",lat, ", lon:",lon," ,text:",text,",time", time)
    res = sentimentRecommendation.sentiment_recommendation().request_for_result(lat, lon, text, time)

    # 将数据再次打包为 JSON 并传回
    resp = json.dumps(res)
    print(resp)
    # resp = '{{"obj": {} }}'.format(res.to_json(orient = "records", force_ascii = False))
    return resp




@app.route('/restaurant/selectionbased/', methods = ["GET"])   # GET 和 POST 都可以
def get_data1():

    #可以通过 request 的 args 属性来获取参数
    lat = request.args.get("lat")
    lon = request.args.get("lon")
    text = request.args.get("text")
    time = request.args.get("time")
    cuisine = request.args.get("cuisine")
    category = request.args.get("categorie")

    print("lat: ",lat, ", lon:",lon," ,cuisine:",cuisine,",category", category)
    categoryDict = {
        "Breakfast":8,
        "Lunch":9,
        "Dinner":10,
        "Cafes":6,
    }

    cuisineDict = {
        "Chinese":25,
        "Korean":67,
        "Australia":201,
        "Japanese":60,

    }
    cuisine = cuisineDict[cuisine]
    category = categoryDict[category]

    res = recommendBySelection.recommendBySelection().requestForResult(lat,lon,text,time,cuisine,category)

    # 将数据再次打包为 JSON 并传回
    resp = json.dumps(res)
    # print(resp)
    return resp



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=None, debug=True)
