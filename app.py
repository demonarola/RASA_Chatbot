import os
from flask import Flask
from flask import render_template
from flask_cors import CORS, cross_origin
from flask import request
from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "customer.db"))

app = Flask(__name__, static_url_path='',
            static_folder='static', template_folder='templates')


app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String, nullable=False)
    customer_address = db.Column(db.String, nullable=False)
    customer_number = db.Column(db.String, nullable=False)
    pizza_type = db.Column(db.String)
    pizza_sub_type = db.Column(db.String)
    customize_details = db.Column(db.String)
    pizza_size = db.Column(db.String)
    delivery_time = db.Column(db.String)

    def __init__(self, customer_name, customer_address, customer_number, pizza_type, pizza_sub_type, customize_details, pizza_size, delivery_time):
        self.customer_name = customer_name
        self.customer_address = customer_address
        self.customer_number = customer_number
        self.pizza_type = pizza_type
        self.pizza_sub_type = pizza_sub_type
        self.customize_details = customize_details
        self.pizza_size = pizza_size
        self.delivery_time = delivery_time


@app.route('/', methods=['GET', 'POST', 'OPTIONS'])
def index():
    return render_template('index.html')

@app.route('/customer')
def show_all():
   return render_template('show_all.html', User = User.query.all() )


if __name__ == '__main__':
    db.create_all()
    db.session.commit()
    app.run(host="0.0.0.0", port="5010", debug=True)
