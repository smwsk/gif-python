from flask import *
from model.gif_info import gifInfo
gif = Blueprint('gif', __name__)

# 查询gif列表
@gif.route("/list")
def list_gif_info():
    list = gifInfo.query([gifInfo],filter=[])
    return jsonify(gifInfo.list_model_serialize(list))

# 跳转到制作界面
@gif.route('/to_make_gif/<name>')
def to_make_gif(name='sorry'):
    gif_info = gifInfo.query([gifInfo], filter=[gifInfo.name == name])
    return render_template('/gif/make.html',gif=gif_info[0].model_serialize())

# 制作
@gif.route('/make', methods=['POST', 'GET'])
def tplmake(name="sorry"):
    if request.method == 'POST':
        name = request.args.get("name")
        a = request.get_data()
        dict1 = json.loads(a)

        sentences = list(dict1.keys())
        for k, v in dict1.items():
            sentences[int(k)] = v

        app.logger.debug(json.dumps(sentences, ensure_ascii=False))
        from utils import render
        path = render.render_gif(name, sentences)
        app.logger.debug(path)
        return '<p><a href="/{path}" target="_blank"><p>点击下载</p></a></p>'.format(path=path)
    else:
        return '<h1>只接受post请求！</h1>'