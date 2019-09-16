from flask import Flask
app = Flask(__name__)


@app.route('/res', methods = ["GET"])   # GET 和 POST 都可以
def get_data():
    # 假设有如下 URL
    # http://10.8.54.48:5000/index?name=john&age=20

    #可以通过 request 的 args 属性来获取参数
    lat = request.args.get("lat")
    lon = request.args.get("lon")
    text = request.args.get("text")
    category = request.args.get("category")
    

    
    # 经过处理之后得到要传回的数据
    res= some_function(name, age)
    
    # 将数据再次打包为 JSON 并传回
    resp = '{{"obj": {} }}'.format(res.to_json(orient = "records", force_ascii = False))
    
    return resp


if __name__ == "__main__":
    app.run()