from flask import Flask, jsonify

app = Flask(_name_)

@app.route('/sayHello', methods=['GET'])
def say_hello():
    return jsonify({'message': 'Hello User.'})

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=80)
