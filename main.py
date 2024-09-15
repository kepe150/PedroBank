from flask import Flask, render_template, request
import configManager    

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/config', methods=['POST', 'GET'])
def config():
    if request.method == 'POST':


        configManager.setConfig(value=request.form.to_dict()['value'], type=request.form.to_dict()['porcentageType'])
        return render_template('config.html', values=configManager.getConfig(), chaged=True)
    
    values = configManager.getConfig()
    return render_template('config.html', values=values)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
