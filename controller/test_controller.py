from model.test_model import Test
from model.category import Category
import json
from flask import *
test = Blueprint('test', __name__)
category = Blueprint('category',__name__)

@test.route('add')
def test_model_add():
    t = Test(tid=1, name='test')
    t.add()
    return jsonify(t.model_serialize())

@test.route('list')
def test_model_list():
    list = Test.query([Test],filter=[])
    return jsonify(Test.list_model_serialize(list))

@test.route('get')
def test_model_get():
    list = Test.query([Test],filter=[Test.tid == 1])
    return jsonify(Test.list_model_serialize(list))

@test.route('category')
def test_model_list_category():
    list = Category.query([Category]);
    return jsonify(Test.list_model_serialize(list))