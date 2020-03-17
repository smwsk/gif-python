from flask import *
from model.gif_info import gifInfo
from model.api_gif_info import ApiGifInfo
from model.gif_info_template import gifInfoTemplate
api = Blueprint('api', __name__)

# api接口首页
@api.route("/index",methods=['GET','POST'])
def api_index():
    list = ApiGifInfo.query([ApiGifInfo],filter=[])
    banner_list = ApiGifInfo.query([ApiGifInfo],order_by=gifInfo.tid.asc(),limit=3, offset=0)
    result = {
        'gif_list': ApiGifInfo.list_model_serialize(list),
        'banner_list': ApiGifInfo.list_model_serialize(banner_list)
    }
    return jsonify(result)

@api.route('/listGifInfo',methods=['GET','POST'])
def listGifInfo():
    params = request.get_data()
    params_json = json.loads(params)
    name = params_json['name']
    gif_list = ApiGifInfo.query([ApiGifInfo],filter=[ApiGifInfo.name == name])
    return jsonify(ApiGifInfo.list_model_serialize(gif_list))


@api.route('/templateList/<name>',methods=['GET','POST'])
def template_list(name='sorry'):
    # 获取模板信息
    template_list = gifInfoTemplate.query([gifInfoTemplate], filter=[gifInfoTemplate.gif_name == name], group_by=[],
                                          order_by=gifInfoTemplate.index.asc())
    return jsonify(gifInfoTemplate.list_model_serialize(template_list))

# 制作
@api.route('/make/<name>', methods=['POST', 'GET'])
def make_gif(name="sorry"):
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