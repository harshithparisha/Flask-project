from flask import Flask, render_template, jsonify

app = Flask(__name__)



@app.route('/')

def employee_list():
    employees = [
        {
            'id':'1',
            'title':'Software developer',
            'name':'Parisha Harshith',
            'location':'Bangalore',
            'Salary':'24,00,000'
        },
        {
            'id':'2',
            'title':'Associate Software developer',
            'name':'James Alex',
            'location':'Bangalore',
            'Salary':'25,00,000'
        }
    ]

    return render_template('index.html',employees=employees)



if __name__=="__main__":
    app.run(debug=True,port=8002)    