from flask import Flask,render_template



app =Flask(__name__)




@app.route('/')
def home():
    return render_template('/index/index.html')

@app.route('/contact',  methods=['GET', 'POST'])
def contact():
    
    
    return render_template('/contact/index.html')

@app.route('/about')
def about():
    languages = ("Javascript","HTML","CSS","C#","Python","SQL Server")
    return render_template('/about-me/index.html',languages=languages)

if __name__=='__main__':
    app.run(debug=True, port=8000)