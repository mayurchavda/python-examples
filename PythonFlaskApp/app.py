from flask import Flask, render_template, jsonify, json, request, session
from pymongo import MongoClient
from bson.objectid import ObjectId
from fabric.api import *

app = Flask(__name__)

client = MongoClient('localhost:27017')
db = client.MachineData

@app.route('/')
def showMachineList():
	return render_template('list.html')

@app.route('/addMachine', methods=['POST'])
def addMachine():
	try:
		json_data = request.json['info']
		deviceName = json_data['device']
		ipAddress = json_data['ip']
		userName = json_data['username']
		password = json_data['password']
		portNumber = json_data['port']
		db.Machines.insert_one({
			'device': deviceName,'ip': ipAddress, 'username':userName,'password':password,'port':portNumber	})
		return jsonify(status='OK', message='inserted successfully')
	except Exception as e:
		return jsonify(status='ERROR', message=str(e))

@app.route("/getMachineList",methods=['POST'])
def getMachineList():
	try:
		machines = db.Machines.find()

		machineList = []
		for machine in machines:
			print(machine)
			machineItem = {
				'device': machine['device'],
				'ip': machine['ip'],
				'username': machine['username'],
				'password': machine['password'],
				'port': machine['port'],
				'id': str(machine['_id'])
			}
			machineList.append(machineItem)
	except Exception as e:
		return str(e)
	return json.dumps(machineList)


@app.route('/updateMachine', methods=['POST'])
def updateMachine():
	try:
		machineInfo = request.json['info']
		machineId = machineInfo['id']
		device = machineInfo['device']
		ip = machineInfo['ip']
		username = machineInfo['username']
		password = machineInfo['password']
		port = machineInfo['port']

		db.Machines.update_one({ '_id': ObjectId(machineId)},{'$set':{'device':device,'ip':ip,'username':username,'password':password,'port':port}})

		return jsonify(status='OK', message='updated successfully')
	except Exception as e:
		return jsonify(status='ERROR', message=str(e))

@app.route('/deleteMachine', methods=['POST'])
def deleteMachine():
	try:
		machineId = request.json['id']
		db.Machines.remove({'_id': ObjectId(machineId)})
		return jsonify(status='OK', message='deletion successfully')
	except Exception as e:
		return jsonify(status='ERROR',message=str(e))

@app.route('/getMachine', methods=['POST'])
def getMachine():
	try:
		machineId = request.json['id']
		#print (machineId)
		machine = db.Machines.find_one({'_id':ObjectId(machineId)})
		#print (machine)
		machineDetail = {
			'device': machine['device'],
			'ip': machine['ip'],
			'username': machine['username'],
			'password': machine['password'],
			'port': machine['port'],
			'id': str(machine['_id'])
		}
		return json.dumps(machineDetail)
	except Exception as e:
		return str(e)

@app.route("/execute", methods=['POST'])
def execute():
	try:
		machineInfo = request.json['info']
		ip=machineInfo['ip']
		username=machineInfo['username']
		password=machineInfo['password']
		command=machineInfo['command']
		isRoot=machineInfo['isRoot']

		env.host_string = username + '@' + ip
		env.password = password
		resp = ''
		with settings(warn_only=True):
			if isRoot:
				resp = sudo(command)
			else:
				resp = run(command)

		return jsonify(status='OK', message=resp)

	except Exception as e:
		print ('Error is' + str(e))
		return jsonify(status='ERROR', message=str(e))

if __name__ == '__main__':
	app.run(host='0.0.0.0')

