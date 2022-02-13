from flask import Flask, render_template, request, jsonify


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
@app.route('/', methods=['GET'])

def index():
    height = request.args.get('weight', type = float)
    weight = request.args.get('height', type = float)
    if not(weight<=0 or height<=0):
        bmi =calc_bmi(weight, height)
        label = check_label(float(bmi))
        return jsonify({"bmi": bmi, "label":label})
    elif (weight is None or height is None):
        return jsonify({"Error Message":'Invalid Input: Only Numbers are allowed'})  
    else:
        return jsonify({"Error Message":'Invalid Input: weight/height should be more than 0 and positive'})

def calc_bmi(weight, height):
    BMI=format(float(weight / (height/100)**2), ".2f")
    return(BMI) 

def check_label(bmis):
    if float(bmis) <= 18.49:  
        label="underweight"  
    elif 18.50 <= float(bmis) <= 24.9:  
        label= "normal"  
    else:  
        label= "overweight"  
    return(label)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
