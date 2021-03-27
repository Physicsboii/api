from flask import Flask,request, jsonify,render_template

app = Flask(__name__)

app.config["DEBUG"] = True


    


@app.route('/', methods=['GET'])
def api_id():
    
    if 'length' in request.args:
        length = int(request.args['length'])
        
    if 'depth' in request.args:
        depth = int(request.args['depth'])
    
    if depth < 16.4:
        breed = "gentoo"
    else:
        if length > 42.35:
           breed = "chinstrap"
        else:
            breed = "adelie"
    
    
    return render_template('index.html',length = length , depth = depth , breed = breed)

   
app.run()