from flask import Flask  
app = Flask(__name__)    
@app.route('/')          
def hello_world():
    return 'Hello World!'  

@app.route('/dojo')          
def dojo():
    return 'dojo'  

@app.route('/say/<name>')          
def say(name):
    return 'Hello ' + name

@app.route('/repeat/<num>/<namee>')          
def repeat(num, namee):
    return str(namee)*int(num) 




if __name__=="__main__":  
    app.run(debug=True)    
