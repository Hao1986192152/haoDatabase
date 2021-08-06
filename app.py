# -*- coding: utf-8 -*
from flask import Flask, render_template, request, make_response, g, jsonify, redirect, url_for, session
from redis import Redis
import redis
import os
import socket
import random
import json
import uuid
import sys
import string


def get_redis():
	if not hasattr(g, 'redis'):
		g.redis = Redis(host="127.0.0.1", port=6379, db=0, socket_timeout=5)
	return g.redis


option_a = os.getenv('OPTION_A', "空气滤芯")
option_b = os.getenv('OPTION_B', "汽车电瓶")
option_c = os.getenv('OPTION_C', "刹车片")
option_d = os.getenv('OPTION_D', "汽油滤芯")
option_e = os.getenv('OPTION_E', "电瓶搭火线")
option_f = os.getenv('OPTION_F', "刹车钳")
option_g = os.getenv('OPTION_G', "机器学习")
option_h = os.getenv('OPTION_H', "C++ Primer")
option_i = os.getenv('OPTION_I', "Python可以这样学")

hostname = socket.gethostname()
print("您的主机名为：", hostname)

redis = redis.Redis(host="127.0.0.1", port=6379, db=0, socket_timeout=5)
redis.hset("product", "product1", json.dumps({"price": 45, "name": "空气滤芯"}))
redis.hset("product", "product2", json.dumps({"price": 258, "name": "汽车电瓶"}))
redis.hset("product", "product3", json.dumps({"price": 198, "name": "刹车片"}))
redis.hset("product", "product4", json.dumps({"price": 69, "name": "汽油滤芯"}))
redis.hset("product", "product5", json.dumps({"price": 39, "name": "电瓶搭火线"}))
redis.hset("product", "product6", json.dumps({"price": 369, "name": "刹车钳"}))
redis.hset("product", "product7", json.dumps({"price": 76, "name": "机器学习"}))
redis.hset("product", "product8", json.dumps({"price": 92, "name": "C++ Primer"}))
redis.hset("product", "product9", json.dumps({"price": 51, "name": "Python可以这样学"}))

redis.hset("shopping", "test", json.dumps(
	{"product1": 0, "product2": 0, "product3": 0, "product4": 0, "product5": 0,
	 "product6": 0, "product7": 0, "product8": 0, "product9": 0}))
redis.save()

app = Flask(__name__, static_folder='assets', template_folder='templates')


@app.route("/", methods=['GET'])
def entrance():
	return redirect(url_for('hello'))


@app.route("/hello", methods=['POST', 'GET'])
def hello():
	vote_a = int(redis.get("a"))
	vote_b = int(redis.get("b"))
	vote_c = int(redis.get("c"))
	vote_d = int(redis.get("d"))
	vote_e = int(redis.get("e"))
	vote_f = int(redis.get("f"))
	vote_g = int(redis.get("g"))
	vote_h = int(redis.get("h"))
	vote_i = int(redis.get("i"))

	user_info = redis.hget("product", "product1")
	user_dict = json.loads(user_info)
	price1 = user_dict["price"]
	user_info = redis.hget("product", "product2")
	user_dict = json.loads(user_info)
	price2 = user_dict["price"]
	user_info = redis.hget("product", "product3")
	user_dict = json.loads(user_info)
	price3 = user_dict["price"]
	user_info = redis.hget("product", "product4")
	user_dict = json.loads(user_info)
	price4 = user_dict["price"]
	user_info = redis.hget("product", "product5")
	user_dict = json.loads(user_info)
	price5 = user_dict["price"]
	user_info = redis.hget("product", "product6")
	user_dict = json.loads(user_info)
	price6 = user_dict["price"]
	user_info = redis.hget("product", "product7")
	user_dict = json.loads(user_info)
	price7 = user_dict["price"]
	user_info = redis.hget("product", "product8")
	user_dict = json.loads(user_info)
	price8 = user_dict["price"]
	user_info = redis.hget("product", "product9")
	user_dict = json.loads(user_info)
	price9 = user_dict["price"]

	user_info = redis.hget("shopping", "test")
	user_dict = json.loads(user_info)
	amount1 = user_dict["product1"]
	amount2 = user_dict["product2"]
	amount3 = user_dict["product3"]
	amount4 = user_dict["product4"]
	amount5 = user_dict["product5"]
	amount6 = user_dict["product6"]
	amount7 = user_dict["product7"]
	amount8 = user_dict["product8"]
	amount9 = user_dict["product9"]

	username = request.args.get("username")
	if username is None:
		username = "登录"
	elif username == "登录":
		pass
	else:
		vote_aU = int(redis.hget(username, "a"))
		vote_bU = int(redis.hget(username, "b"))
		vote_cU = int(redis.hget(username, "c"))
		vote_dU = int(redis.hget(username, "d"))
		vote_eU = int(redis.hget(username, "e"))
		vote_fU = int(redis.hget(username, "f"))
		vote_gU = int(redis.hget(username, "g"))
		vote_hU = int(redis.hget(username, "h"))
		vote_iU = int(redis.hget(username, "i"))

	vote = None

	if request.method == 'POST':
		vote = request.form['vote']
		print(vote)
		if username != "登录":
			if vote == "a":
				vote_a += 1
				vote_aU += 1
				redis.set(vote, vote_a)
				redis.hset(username, vote, vote_aU)
			elif vote == "b":
				vote_b += 1
				vote_bU += 1
				redis.set(vote, vote_b)
				redis.hset(username, vote, vote_bU)
			elif vote == "c":
				vote_c += 1
				vote_cU += 1
				redis.set(vote, vote_c)
				redis.hset(username, vote, vote_cU)
			elif vote == "d":
				vote_d += 1
				vote_dU += 1
				redis.set(vote, vote_d)
				redis.hset(username, vote, vote_dU)
			elif vote == "e":
				vote_e += 1
				vote_eU += 1
				redis.set(vote, vote_e)
				redis.hset(username, vote, vote_eU)
			elif vote == "f":
				vote_f += 1
				vote_fU += 1
				redis.set(vote, vote_f)
				redis.hset(username, vote, vote_fU)
			elif vote == "g":
				vote_g += 1
				vote_gU += 1
				redis.set(vote, vote_g)
				redis.hset(username, vote, vote_gU)
			elif vote == "h":
				vote_h += 1
				vote_hU += 1
				redis.set(vote, vote_h)
				redis.hset(username, vote, vote_hU)
			elif vote == "i":
				vote_i += 1
				vote_iU += 1
				redis.set(vote, vote_i)
				redis.hset(username, vote, vote_iU)
			else:
				pass
		else:
			pass
		redis.save()

	resp = make_response(render_template(
		'index.html',
		option_a=option_a,
		option_b=option_b,
		option_c=option_c,
		option_d=option_d,
		option_e=option_e,
		option_f=option_f,
		option_g=option_g,
		option_h=option_h,
		option_i=option_i,
		hostname=hostname,
		username=username,
		vote_a=vote_a,
		vote_b=vote_b,
		vote_c=vote_c,
		vote_d=vote_d,
		vote_e=vote_e,
		vote_f=vote_f,
		vote_g=vote_g,
		vote_h=vote_h,
		vote_i=vote_i,
		vote=vote,
		price1=price1,
		price2=price2,
		price3=price3,
		price4=price4,
		price5=price5,
		price6=price6,
		price7=price7,
		price8=price8,
		price9=price9,
		amount1=amount1,
		amount2=amount2,
		amount3=amount3,
		amount4=amount4,
		amount5=amount5,
		amount6=amount6,
		amount7=amount7,
		amount8=amount8,
		amount9=amount9
	))
	redis.set("currentUser", username)
	redis.save()
	return resp


@app.route('/login', methods=['GET'])
def loginInfo():
	return render_template('login.html')


@app.route('/api/login', methods=['POST', 'GET'])
def login():
	dict_new = None
	if request.method == "POST":
		username = request.form.get("username")
		password = request.form.get("password")
		if username == "" or password == "":
			dict_new = "用户名或密码不能为空！请重新输入"
			return render_template("login.html", dict_new=dict_new)
		elif redis.hget(username, "username") is None:
			dict_new = "该用户不存在！请重新输入"
			return render_template("login.html", dict_new=dict_new)
		elif str(redis.hget(username, "password"), 'utf-8') != password:
			dict_new = "密码错误！请重新输入"
			return render_template("login.html", dict_new=dict_new)
		else:
			print("登录成功")
			return redirect(url_for('hello', username=username))

	if request.method == "GET":
		dict_new = {"message": "tean"}
		return jsonify(dict_new)
	else:
		return jsonify(dict_new)


@app.route('/register', methods=['GET'])
def registerInfo():
	return render_template('register.html')


@app.route('/api/register', methods=['POST', 'GET'])
def register():
	if request.method == "POST":
		username = request.form.get("username")
		password = request.form.get("password")
		rePassword = request.form.get("rePassword")
		if username == "":
			dict_old = "用户名不能为空！请重新输入"
			return render_template("register.html", dict_old=dict_old)
		elif password == "":
			dict_old = "密码不能为空！请重新输入"
			return render_template("register.html", dict_old=dict_old)
		elif password != rePassword:
			dict_old = "两次输入的密码不一致！请重新输入"
			return render_template("register.html", dict_old=dict_old)
		elif redis.hget(username, "username") is not None:
			dict_old = "该用户名已存在！请重新输入"
			return render_template("register.html", dict_old=dict_old)
		else:
			redis.hmset(username, {"username": username, "password": password,
								   "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0,
								   "g": 0, "h": 0, "i": 0})
			redis.save()
			print("数据库添加成功！")
			dict_new = "注册成功！请登录"
			return render_template("login.html", dict_new=dict_new)
		pass

@app.route('/favourite', methods=['POST', 'GET'])
def favourite():
	username = str(redis.get("currentUser"), 'utf-8')
	print(username)
	if username != "登录":
		vote_aU = int(redis.hget(username, "a"))
		vote_bU = int(redis.hget(username, "b"))
		vote_cU = int(redis.hget(username, "c"))
		vote_dU = int(redis.hget(username, "d"))
		vote_eU = int(redis.hget(username, "e"))
		vote_fU = int(redis.hget(username, "f"))
		vote_gU = int(redis.hget(username, "g"))
		vote_hU = int(redis.hget(username, "h"))
		vote_iU = int(redis.hget(username, "i"))
		return render_template('favourite.html',
							   vote_aU=vote_aU,
							   vote_bU=vote_bU,
							   vote_cU=vote_cU,
							   vote_dU=vote_dU,
							   vote_eU=vote_eU,
							   vote_fU=vote_fU,
							   vote_gU=vote_gU,
							   vote_hU=vote_hU,
							   vote_iU=vote_iU, )
	else:
		msg = "请登陆后使用该功能！"
		return render_template('favourite.html', msg=msg)


@app.route("/back", methods=['POST', 'GET'])
def back():
	username = str(redis.get("currentUser"), 'utf-8')
	print(username)
	return redirect(url_for('hello', username=username))


@app.route("/quite")
def quite():
	return redirect(url_for('hello'))


@app.route('/clear', methods=['GET'])
def clearGoods():
	redis.hset("shopping", "test", json.dumps(
		{"product1": 0, "product2": 0, "product3": 0, "product4": 0, "product5": 0,
		 "product6": 0, "product7": 0, "product8": 0, "product9": 0}))
	redis.save()
	return redirect(url_for('hello'))


@app.route('/add1', methods=['GET'])
def add1():
	user_info = redis.hget("shopping", "test")
	user_dict = json.loads(user_info)
	amount1 = int(user_dict["product1"]) + 1
	amount2 = int(user_dict["product2"])
	amount3 = int(user_dict["product3"])
	amount4 = int(user_dict["product4"])
	amount5 = int(user_dict["product5"])
	amount6 = int(user_dict["product6"])
	amount7 = int(user_dict["product7"])
	amount8 = int(user_dict["product8"])
	amount9 = int(user_dict["product9"])
	redis.hset("shopping", "test", json.dumps(
		{"product1": amount1, "product2": amount2, "product3": amount3, "product4": amount4,
		 "product5": amount5, "product6": amount6, "product7": amount7, "product8": amount8,
		 "product9": amount9}))
	redis.save()
	return redirect(url_for('hello'))


@app.route('/add2', methods=['GET'])
def add2():
	user_info = redis.hget("shopping", "test")
	user_dict = json.loads(user_info)
	amount1 = int(user_dict["product1"])
	amount2 = int(user_dict["product2"]) + 1
	amount3 = int(user_dict["product3"])
	amount4 = int(user_dict["product4"])
	amount5 = int(user_dict["product5"])
	amount6 = int(user_dict["product6"])
	amount7 = int(user_dict["product7"])
	amount8 = int(user_dict["product8"])
	amount9 = int(user_dict["product9"])
	redis.hset("shopping", "test", json.dumps(
		{"product1": amount1, "product2": amount2, "product3": amount3, "product4": amount4,
		 "product5": amount5, "product6": amount6, "product7": amount7, "product8": amount8,
		 "product9": amount9}))
	redis.save()
	return redirect(url_for('hello'))


@app.route('/add3', methods=['GET'])
def add3():
	user_info = redis.hget("shopping", "test")
	user_dict = json.loads(user_info)
	amount1 = int(user_dict["product1"])
	amount2 = int(user_dict["product2"])
	amount3 = int(user_dict["product3"]) + 1
	amount4 = int(user_dict["product4"])
	amount5 = int(user_dict["product5"])
	amount6 = int(user_dict["product6"])
	amount7 = int(user_dict["product7"])
	amount8 = int(user_dict["product8"])
	amount9 = int(user_dict["product9"])
	redis.hset("shopping", "test", json.dumps(
		{"product1": amount1, "product2": amount2, "product3": amount3, "product4": amount4,
		 "product5": amount5, "product6": amount6, "product7": amount7, "product8": amount8,
		 "product9": amount9}))
	redis.save()
	return redirect(url_for('hello'))


@app.route('/add4', methods=['GET'])
def add4():
	user_info = redis.hget("shopping", "test")
	user_dict = json.loads(user_info)
	amount1 = int(user_dict["product1"])
	amount2 = int(user_dict["product2"])
	amount3 = int(user_dict["product3"])
	amount4 = int(user_dict["product4"]) + 1
	amount5 = int(user_dict["product5"])
	amount6 = int(user_dict["product6"])
	amount7 = int(user_dict["product7"])
	amount8 = int(user_dict["product8"])
	amount9 = int(user_dict["product9"])
	redis.hset("shopping", "test", json.dumps(
		{"product1": amount1, "product2": amount2, "product3": amount3, "product4": amount4,
		 "product5": amount5, "product6": amount6, "product7": amount7, "product8": amount8,
		 "product9": amount9}))
	redis.save()
	return redirect(url_for('hello'))


@app.route('/add5', methods=['GET'])
def add5():
	user_info = redis.hget("shopping", "test")
	user_dict = json.loads(user_info)
	amount1 = int(user_dict["product1"])
	amount2 = int(user_dict["product2"])
	amount3 = int(user_dict["product3"])
	amount4 = int(user_dict["product4"])
	amount5 = int(user_dict["product5"]) + 1
	amount6 = int(user_dict["product6"])
	amount7 = int(user_dict["product7"])
	amount8 = int(user_dict["product8"])
	amount9 = int(user_dict["product9"])
	redis.hset("shopping", "test", json.dumps(
		{"product1": amount1, "product2": amount2, "product3": amount3, "product4": amount4,
		 "product5": amount5, "product6": amount6, "product7": amount7, "product8": amount8,
		 "product9": amount9}))
	redis.save()
	return redirect(url_for('hello'))


@app.route('/add6', methods=['GET'])
def add6():
	user_info = redis.hget("shopping", "test")
	user_dict = json.loads(user_info)
	amount1 = int(user_dict["product1"])
	amount2 = int(user_dict["product2"])
	amount3 = int(user_dict["product3"])
	amount4 = int(user_dict["product4"])
	amount5 = int(user_dict["product5"])
	amount6 = int(user_dict["product6"]) + 1
	amount7 = int(user_dict["product7"])
	amount8 = int(user_dict["product8"])
	amount9 = int(user_dict["product9"])
	redis.hset("shopping", "test", json.dumps(
		{"product1": amount1, "product2": amount2, "product3": amount3, "product4": amount4,
		 "product5": amount5, "product6": amount6, "product7": amount7, "product8": amount8,
		 "product9": amount9}))
	redis.save()
	return redirect(url_for('hello'))


@app.route('/add7', methods=['GET'])
def add7():
	user_info = redis.hget("shopping", "test")
	user_dict = json.loads(user_info)
	amount1 = int(user_dict["product1"])
	amount2 = int(user_dict["product2"])
	amount3 = int(user_dict["product3"])
	amount4 = int(user_dict["product4"])
	amount5 = int(user_dict["product5"])
	amount6 = int(user_dict["product6"])
	amount7 = int(user_dict["product7"]) + 1
	amount8 = int(user_dict["product8"])
	amount9 = int(user_dict["product9"])
	redis.hset("shopping", "test", json.dumps(
		{"product1": amount1, "product2": amount2, "product3": amount3, "product4": amount4,
		 "product5": amount5, "product6": amount6, "product7": amount7, "product8": amount8,
		 "product9": amount9}))
	redis.save()
	return redirect(url_for('hello'))


@app.route('/add8', methods=['GET'])
def add8():
	user_info = redis.hget("shopping", "test")
	user_dict = json.loads(user_info)
	amount1 = int(user_dict["product1"])
	amount2 = int(user_dict["product2"])
	amount3 = int(user_dict["product3"])
	amount4 = int(user_dict["product4"])
	amount5 = int(user_dict["product5"])
	amount6 = int(user_dict["product6"])
	amount7 = int(user_dict["product7"])
	amount8 = int(user_dict["product8"]) + 1
	amount9 = int(user_dict["product9"])
	redis.hset("shopping", "test", json.dumps(
		{"product1": amount1, "product2": amount2, "product3": amount3, "product4": amount4,
		 "product5": amount5, "product6": amount6, "product7": amount7, "product8": amount8,
		 "product9": amount9}))
	redis.save()
	return redirect(url_for('hello'))


@app.route('/add9', methods=['GET'])
def add9():
	user_info = redis.hget("shopping", "test")
	user_dict = json.loads(user_info)
	amount1 = int(user_dict["product1"])
	amount2 = int(user_dict["product2"])
	amount3 = int(user_dict["product3"])
	amount4 = int(user_dict["product4"])
	amount5 = int(user_dict["product5"])
	amount6 = int(user_dict["product6"])
	amount7 = int(user_dict["product7"])
	amount8 = int(user_dict["product8"])
	amount9 = int(user_dict["product9"]) + 1
	redis.hset("shopping", "test", json.dumps(
		{"product1": amount1, "product2": amount2, "product3": amount3, "product4": amount4,
		 "product5": amount5, "product6": amount6, "product7": amount7, "product8": amount8,
		 "product9": amount9}))
	redis.save()
	return redirect(url_for('hello'))


@app.route('/clear1', methods=['GET'])
def clear1():
	user_info = redis.hget("shopping", "test")
	user_dict = json.loads(user_info)
	amount1 = int(user_dict["product1"])
	amount2 = int(user_dict["product2"])
	amount3 = int(user_dict["product3"])
	amount4 = int(user_dict["product4"])
	amount5 = int(user_dict["product5"])
	amount6 = int(user_dict["product6"])
	amount7 = int(user_dict["product7"])
	amount8 = int(user_dict["product8"])
	amount9 = int(user_dict["product9"])
	amount1 = 0

	redis.hset("shopping", "test",json.dumps(
		{"product1": amount1, "product2": amount2, "product3": amount3, "product4": amount4,
		 "product5": amount5, "product6": amount6, "product7": amount7, "product8": amount8,
		 "product9": amount9}))
	redis.save()
	return redirect(url_for('hello'))


@app.route('/clear2', methods=['GET'])
def clear2():
	user_info = redis.hget("shopping", "test")
	user_dict = json.loads(user_info)
	amount1 = int(user_dict["product1"])
	amount2 = int(user_dict["product2"])
	amount3 = int(user_dict["product3"])
	amount4 = int(user_dict["product4"])
	amount5 = int(user_dict["product5"])
	amount6 = int(user_dict["product6"])
	amount7 = int(user_dict["product7"])
	amount8 = int(user_dict["product8"])
	amount9 = int(user_dict["product9"])
	amount2 = 0

	redis.hset("shopping", "test",json.dumps(
		{"product1": amount1, "product2": amount2, "product3": amount3, "product4": amount4,
		 "product5": amount5, "product6": amount6, "product7": amount7, "product8": amount8,
		 "product9": amount9}))
	redis.save()
	return redirect(url_for('hello'))

@app.route('/clear3', methods=['GET'])
def clear3():
	user_info = redis.hget("shopping", "test")
	user_dict = json.loads(user_info)
	amount1 = int(user_dict["product1"])
	amount2 = int(user_dict["product2"])
	amount3 = int(user_dict["product3"])
	amount4 = int(user_dict["product4"])
	amount5 = int(user_dict["product5"])
	amount6 = int(user_dict["product6"])
	amount7 = int(user_dict["product7"])
	amount8 = int(user_dict["product8"])
	amount9 = int(user_dict["product9"])
	amount3 = 0

	redis.hset("shopping", "test",json.dumps(
		{"product1": amount1, "product2": amount2, "product3": amount3, "product4": amount4,
		 "product5": amount5, "product6": amount6, "product7": amount7, "product8": amount8,
		 "product9": amount9}))
	redis.save()
	return redirect(url_for('hello'))

@app.route('/clear4', methods=['GET'])
def clear4():
	user_info = redis.hget("shopping", "test")
	user_dict = json.loads(user_info)
	amount1 = int(user_dict["product1"])
	amount2 = int(user_dict["product2"])
	amount3 = int(user_dict["product3"])
	amount4 = int(user_dict["product4"])
	amount5 = int(user_dict["product5"])
	amount6 = int(user_dict["product6"])
	amount7 = int(user_dict["product7"])
	amount8 = int(user_dict["product8"])
	amount9 = int(user_dict["product9"])
	amount4 = 0

	redis.hset("shopping", "test",json.dumps(
		{"product1": amount1, "product2": amount2, "product3": amount3, "product4": amount4,
		 "product5": amount5, "product6": amount6, "product7": amount7, "product8": amount8,
		 "product9": amount9}))
	redis.save()
	return redirect(url_for('hello'))

@app.route('/clear5', methods=['GET'])
def clear5():
	user_info = redis.hget("shopping", "test")
	user_dict = json.loads(user_info)
	amount1 = int(user_dict["product1"])
	amount2 = int(user_dict["product2"])
	amount3 = int(user_dict["product3"])
	amount4 = int(user_dict["product4"])
	amount5 = int(user_dict["product5"])
	amount6 = int(user_dict["product6"])
	amount7 = int(user_dict["product7"])
	amount8 = int(user_dict["product8"])
	amount9 = int(user_dict["product9"])
	amount5 = 0

	redis.hset("shopping", "test",json.dumps(
		{"product1": amount1, "product2": amount2, "product3": amount3, "product4": amount4,
		 "product5": amount5, "product6": amount6, "product7": amount7, "product8": amount8,
		 "product9": amount9}))
	redis.save()
	return redirect(url_for('hello'))

@app.route('/clear6', methods=['GET'])
def clear6():
	user_info = redis.hget("shopping", "test")
	user_dict = json.loads(user_info)
	amount1 = int(user_dict["product1"])
	amount2 = int(user_dict["product2"])
	amount3 = int(user_dict["product3"])
	amount4 = int(user_dict["product4"])
	amount5 = int(user_dict["product5"])
	amount6 = int(user_dict["product6"])
	amount7 = int(user_dict["product7"])
	amount8 = int(user_dict["product8"])
	amount9 = int(user_dict["product9"])
	amount6 = 0

	redis.hset("shopping", "test",json.dumps(
		{"product1": amount1, "product2": amount2, "product3": amount3, "product4": amount4,
		 "product5": amount5, "product6": amount6, "product7": amount7, "product8": amount8,
		 "product9": amount9}))
	redis.save()
	return redirect(url_for('hello'))

@app.route('/clear7', methods=['GET'])
def clear7():
	user_info = redis.hget("shopping", "test")
	user_dict = json.loads(user_info)
	amount1 = int(user_dict["product1"])
	amount2 = int(user_dict["product2"])
	amount3 = int(user_dict["product3"])
	amount4 = int(user_dict["product4"])
	amount5 = int(user_dict["product5"])
	amount6 = int(user_dict["product6"])
	amount7 = int(user_dict["product7"])
	amount8 = int(user_dict["product8"])
	amount9 = int(user_dict["product9"])
	amount7 = 0

	redis.hset("shopping", "test",json.dumps(
		{"product1": amount1, "product2": amount2, "product3": amount3, "product4": amount4,
		 "product5": amount5, "product6": amount6, "product7": amount7, "product8": amount8,
		 "product9": amount9}))
	redis.save()
	return redirect(url_for('hello'))

@app.route('/clear8', methods=['GET'])
def clear8():
	user_info = redis.hget("shopping", "test")
	user_dict = json.loads(user_info)
	amount1 = int(user_dict["product1"])
	amount2 = int(user_dict["product2"])
	amount3 = int(user_dict["product3"])
	amount4 = int(user_dict["product4"])
	amount5 = int(user_dict["product5"])
	amount6 = int(user_dict["product6"])
	amount7 = int(user_dict["product7"])
	amount8 = int(user_dict["product8"])
	amount9 = int(user_dict["product9"])
	amount8 = 0

	redis.hset("shopping", "test",json.dumps(
		{"product1": amount1, "product2": amount2, "product3": amount3, "product4": amount4,
		 "product5": amount5, "product6": amount6, "product7": amount7, "product8": amount8,
		 "product9": amount9}))
	redis.save()
	return redirect(url_for('hello'))

@app.route('/clear9', methods=['GET'])
def clear9():
	user_info = redis.hget("shopping", "test")
	user_dict = json.loads(user_info)
	amount1 = int(user_dict["product1"])
	amount2 = int(user_dict["product2"])
	amount3 = int(user_dict["product3"])
	amount4 = int(user_dict["product4"])
	amount5 = int(user_dict["product5"])
	amount6 = int(user_dict["product6"])
	amount7 = int(user_dict["product7"])
	amount8 = int(user_dict["product8"])
	amount9 = int(user_dict["product9"])
	amount9 = 0

	redis.hset("shopping", "test",json.dumps(
		{"product1": amount1, "product2": amount2, "product3": amount3, "product4": amount4,
		 "product5": amount5, "product6": amount6, "product7": amount7, "product8": amount8,
		 "product9": amount9}))
	redis.save()
	return redirect(url_for('hello'))

@app.route('/payment', methods=['GET'])
def payment():
	user_info = redis.hget("product", "product1")
	user_dict = json.loads(user_info)
	name1 = user_dict["name"]
	price1 = user_dict["price"]
	user_info = redis.hget("product", "product2")
	user_dict = json.loads(user_info)
	name2 = user_dict["name"]
	price2 = user_dict["price"]
	user_info = redis.hget("product", "product3")
	user_dict = json.loads(user_info)
	name3 = user_dict["name"]
	price3 = user_dict["price"]
	user_info = redis.hget("product", "product4")
	user_dict = json.loads(user_info)
	name4 = user_dict["name"]
	price4 = user_dict["price"]
	user_info = redis.hget("product", "product5")
	user_dict = json.loads(user_info)
	name5 = user_dict["name"]
	price5 = user_dict["price"]
	user_info = redis.hget("product", "product6")
	user_dict = json.loads(user_info)
	name6 = user_dict["name"]
	price6 = user_dict["price"]
	user_info = redis.hget("product", "product7")
	user_dict = json.loads(user_info)
	name7 = user_dict["name"]
	price7 = user_dict["price"]
	user_info = redis.hget("product", "product8")
	user_dict = json.loads(user_info)
	name8 = user_dict["name"]
	price8 = user_dict["price"]
	user_info = redis.hget("product", "product9")
	user_dict = json.loads(user_info)
	name9 = user_dict["name"]
	price9 = user_dict["price"]

	user_info = redis.hget("shopping", "test")
	user_dict = json.loads(user_info)
	amount1 = user_dict["product1"]
	amount2 = user_dict["product2"]
	amount3 = user_dict["product3"]
	amount4 = user_dict["product4"]
	amount5 = user_dict["product5"]
	amount6 = user_dict["product6"]
	amount7 = user_dict["product7"]
	amount8 = user_dict["product8"]
	amount9 = user_dict["product9"]

	total1 = price1 * amount1
	total2 = price2 * amount2
	total3 = price3 * amount3
	total4 = price4 * amount4
	total5 = price5 * amount5
	total6 = price6 * amount6
	total7 = price7 * amount7
	total8 = price8 * amount8
	total9 = price9 * amount9

	total = total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9
	redis.set("total_price", total)
	redis.save()
	return render_template('payment.html', name1=name1, price1=price1, amount1=amount1, total1=total1,
						   name2=name2, price2=price2, amount2=amount2, total2=total2
						   , name3=name3, price3=price3, amount3=amount3, total3=total3
						   , name4=name4, price4=price4, amount4=amount4, total4=total4
						   , name5=name5, price5=price5, amount5=amount5, total5=total5
						   , name6=name6, price6=price6, amount6=amount6, total6=total6
						   , name7=name7, price7=price7, amount7=amount7, total7=total7
						   , name8=name8, price8=price8, amount8=amount8, total8=total8
						   , name9=name9, price9=price9, amount9=amount9, total9=total9
						   , total=total)

@app.route('/pay', methods=['GET'])
def pay():
	total_price = int(redis.get("total_price"))
	return render_template('pay.html', total_price=total_price)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8088, debug=True, threaded=True)
