from flask import request, jsonify,Flask
app = Flask(__name__)
import json
# from recommendBySelection import recommendBySelection s
# import recommendBySelection.recommendBySelection


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
def get_data1():
    # 假设有如下 URL
    # http://10.8.54.48:5000/index?name=john&age=20

    #可以通过 request 的 args 属性来获取参数
    lat = request.args.get("lat")
    lon = request.args.get("lon")
    text = request.args.get("text")
    time = request.args.get("time")
    cuisines = request.args.get("cuisines")
    categories = request.args.get("categories")
    
    res = recommendBySelection.requestForResult(lat, lon,text,time,cuisine,categorie)
    
    # 将数据再次打包为 JSON 并传回
    resp = json.dumps(res)
    # resp = '{{"obj": {} }}'.format(res.to_json(orient = "records", force_ascii = False))
    return resp


def test(lat, lon, text, time): 
    content = {
                "name":"Humbles Ray",
                "cuisines": ["Chinese", "Asian Fusin"],
                "highlights": ['take Away Available', 'breakfast', 'dinner'],
                "thumb": "https://media.licdn.com/dms/image/C5603AQEH5JqXT-IE2Q/profile-displayphoto-shrink_200_200/0?e=1574294400&v=beta&t=9i-nhnn7zTOqQKGV4Dj15u5kwHwe8vELttNkusGBhBE",
                "userRating": 4.4,
                "phoneNumbers": "0321321",
                "lon": -37.802518,
                "lat":144.959633,
            }


    res = {"restaurants": [content,content]}


    return res


if __name__ == "__main__":
    app.run(host='0.0.0.0')