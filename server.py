from flask import request, jsonify,Flask
app = Flask(__name__)
import json


@app.route('/restaurant/recommendation/', methods = ["GET"])   # GET 和 POST 都可以
def get_data():
    # 假设有如下 URL
    # http://10.8.54.48:5000/index?name=john&age=20

    #可以通过 request 的 args 属性来获取参数
    lat = request.args.get("lat")
    lon = request.args.get("lon")
    text = request.args.get("text")
    time = request.args.get("time")
    
    res= test(lat, lon,text,time)
    
    # 将数据再次打包为 JSON 并传回
    resp = json.dumps(res)
    # resp = '{{"obj": {} }}'.format(res.to_json(orient = "records", force_ascii = False))
    return resp

@app.route('/restaurant/selectionbased/', methods = ["GET"])   # GET 和 POST 都可以
def get_data():
    # 假设有如下 URL
    # http://10.8.54.48:5000/index?name=john&age=20

    #可以通过 request 的 args 属性来获取参数
    lat = request.args.get("lat")
    lon = request.args.get("lon")
    text = request.args.get("text")
    time = request.args.get("time")
    cuisines = request.args.get("cuisines")
    categories = request.args.get("categories")
    
    res= test(lat, lon,text,time)
    
    # 将数据再次打包为 JSON 并传回
    resp = json.dumps(res)
    # resp = '{{"obj": {} }}'.format(res.to_json(orient = "records", force_ascii = False))
    return resp


def test(lat, lon, text, time):
    return {
        "lat": lat,
        'lon':lon,
        'text':text,
        'time':time
    }


if __name__ == "__main__":
    app.run()