from flask import Flask,render_template,request
import sqlite3
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///to_do_list.db'
app.secret_key = 'MY_KEY_SECRET'
db = SQLAlchemy(app)

class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200),nullable=False)


with app.app_context():
    db.create_all()



@app.route("/",methods= ['GET','POST'])
def home():
    if request.method == "POST":
        title = request.form.get('title')
        todo = ToDo(title.title)
        db.session.add(todo)
        db.session.commit()
    
    todos = ToDo.query.order_by(ToDo.id.desc()).all()
    return render_template('home.html',todos = todos)



if __name__ == '__main__':
    app.run(debug=True,port=8086)