from flask import Flask, render_template,jsonify
app = Flask(__name__)

THEMES =[
    {
    'id' :1,
    'title':'lifestyle',
    'about': 'Fashion,Beauty,Travel,Food,Home Decor'
    },
    {'id' :2,
    'title':'Personal Development',
    'about': 'Mindfullness,Productivity,Self Care, Mental Health'
    },
    {'id' :3,
    'title':'Technology',
    'about': 'Latest Gadgets, Software, Trends in Tech Industry'
    },
    {'id' :4,
    'title':'Business and Entrepreneurship',
    'about': 'Startup Advice, Marketing Strategies'
    },
    {'id' :5,
    'title':'Finance',
    'about': 'Budgeting, Investing'
    }
]

@app.route("/")
def home():
    return render_template('home.html', Themes=THEMES)

@app.route("/Themes")
def list_Themes():
    return jsonify(THEMES)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)