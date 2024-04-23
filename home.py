from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)

# Database Configuration
DB_USER = 'root'
DB_PASSWORD = '1234'
DB_HOST = '127.0.0.1'
DB_PORT = '3306'
DB_NAME = 'DCC_Assignment_4'

app.config['MYSQL_HOST'] = DB_HOST
app.config['MYSQL_USER'] = DB_USER
app.config['MYSQL_PASSWORD'] = DB_PASSWORD
app.config['MYSQL_DB'] = DB_NAME

# Connect to the database using SQLAlchemy
connection_string = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(connection_string, echo=True)

# MySQL object for Flask app
mysql = MySQL(app)

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/bond", methods=['GET', 'POST'])
def home():
    per_page = 10  # Number of records per page

    if request.method == "POST":
        bond_number = request.form.get('Bond_number')
        company_name = request.form.get('Company_name')

        try:
            cursor = mysql.connection.cursor()
            
            if bond_number:  
                cursor.execute("SELECT * FROM purchase_details WHERE `Bond Number` = %s", (bond_number,))
                
            fetchdata = cursor.fetchall()
            column_headers = [i[0] for i in cursor.description]
            cursor.close()
            
            if fetchdata:
                return render_template("home.html", responsive_data=fetchdata, static_data=None, headers=column_headers)
            else:
                return render_template("home.html", responsive_data=None, static_data=None, bond_number=bond_number, company_name=company_name)
            
        except SQLAlchemyError as e:
            return render_template("error.html", error=str(e))
        except Exception as e:
            return render_template("error.html", error=str(e))

    else:
        return render_template("home.html")
    

@app.route('/purchaser',methods=["GET","POST"])
def purchaser():
    cursor=mysql.connection.cursor()
    cursor.execute("select distinct Name of the Purchaser from eb_purchase_details")
    data=cursor.fetchall()
    dropdown_options=[row[0] for row in data]
    cursor.close()

    if request.method=="POST":
        if 'dropdown' in request.form:  
            selected_option=request.form["dropdown"]
            cursor=mysql.connection.cursor()
            cursor.execute(f"select * from eb_purchase_details where Name of the Purchaser = '{selected_option}'")
            data_a2=cursor.fetchall()
            cursor.close()
            return render_template('purchaser.html', dropdown_options=dropdown_options,data_a2=data_a2,selected_option=selected_option)
        
    return render_template('purchaser.html', dropdown_options=dropdown_options)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
