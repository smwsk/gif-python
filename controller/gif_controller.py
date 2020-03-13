from flask import *
from model.gif_info import gifInfo
from model.gif_info_template import gifInfoTemplate
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
    # 获取模板信息
    template_list = gifInfoTemplate.query([gifInfoTemplate],filter=[gifInfoTemplate.gif_name == name],group_by=[],order_by=gifInfoTemplate.index.asc())
    return render_template('/gif/make.html',gif=gif_info[0].model_serialize(), template_list= gifInfoTemplate.list_model_serialize(template_list))


# 制作
@gif.route('/make/<name>', methods=['POST', 'GET'])
def tplmake(name="sorry"):
    result = {
        'flag': True,
        'object': None
    }
    gif_info = gifInfo.query([gifInfo], filter=[gifInfo.name == name])
    if request.method == 'POST':
        a = request.get_data()
        dict1 = json.loads(a)
        sentences = list(dict1.keys())
        for k, v in dict1.items():
            sentences[int(k)] = v

        current_app.logger.debug(json.dumps(sentences, ensure_ascii=False))
        from utils import render
        path = render.render_gif(name, sentences,gif_info[0])
        current_app.logger.debug(path)
        result['object'] = path
        return jsonify(result)
    else:
        result['object'] = '只接受post请求'
        result['flag'] = False
        return jsonify(result)