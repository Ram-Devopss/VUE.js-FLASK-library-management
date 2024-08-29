from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
CORS(app)  # Enable CORS
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'  # Use SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

CORS(app, resources={r"/*":{'origins':"*"}})


# Create database tables
with app.app_context():
    db.create_all()




#################################### Start Books Model #######################################################

class Books(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(120), nullable=True)
    genre = db.Column(db.String(250),nullable=False)
    image = db.Column(db.String(250),nullable=True)
    access = db.Column(db.Boolean, default=False, nullable=False)





@app.route('/VIEWBOOKS', methods=['GET'])
def VIEWBOOKS():
    books = Books.query.all()
    books_data = [
        {
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "genre": book.genre,
            "image": book.image,
        }
        for book in books
    ]
    return jsonify({"books": books_data}), 200


@app.route('/TOTALBOOKS', methods=['GET'])
def TOTALBOOKS():
    # Query the database to get the latest book
    latest_book = Books.query.order_by(Books.id.desc()).first()

    if latest_book:
        # Return the ID of the latest book
        return jsonify({"final_id": latest_book.id}), 200
    else:
        # If there are no books in the database
        return jsonify({"message": "0"}), 404


@app.route('/ADDBOOKS', methods=['POST'])
def ADDBOOKS():
    data = request.json
    title = data.get('title')
    author = data.get('author')
    genre = data.get('genre')
    image = data.get('image')

    # Simple validation
    if not title or not genre:
        return jsonify({"message": "Invalid Book"}), 400

    # Check if user already exists
    existing_user = Books.query.filter_by(title=title).first()
    if existing_user:
        return jsonify({"message": "Books already exists"}), 400

    # Create new user
    new_user = Books(title=title.upper(), author=author.upper(),genre=genre.upper(),image=image)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "Books registered successfully"}), 201



#################################### End Books Model #######################################################


#################################### Start Librarian Model #######################################################



class Librarian(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(250),nullable=False)





@app.route('/Librarian_login', methods=['POST'])
def Librarian_login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Simple validation
    if not username or not password:
        return jsonify({"message": "Invalid data"}), 400

    # Check if user exists
    user = Librarian.query.filter_by(username=username, password=password).first()
    if not user:
        return jsonify({"message": "Invalid username or password"}), 401

    return jsonify({"message": "Login successful"}), 200


@app.route('/Librarian_register', methods=['POST'])
def Librarian_register():
    data = request.json

    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    # Simple validation
    if not username or not password or not email:
        return jsonify({"message": "Invalid data"}), 400

    # Check if user already exists
    existing_user = Librarian.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({"message": "Management already exists"}), 400

    # Create new user
    new_user = Librarian(username=username, password=password,email=email)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "Management registered successfully"}), 201


#################################### End Librarian Model #######################################################

#################################### Start Student Model #######################################################

# Define Students model
class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(250),nullable=False)
    



@app.route('/TOTALSTUDENTS', methods=['GET'])
def TOTALSTUDENTS():
        # Query the database to get the latest book
    latest_student = Students.query.order_by(Students.id.desc()).first()

    if latest_student:
        # Return the ID of the latest book
        return jsonify({"final_id": latest_student.id}), 200
    else:
        # If there are no books in the database
        return jsonify({"message": "0"}), 404



@app.route('/student_register', methods=['POST'])
def student_register():
    data = request.json

    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    # Simple validation
    if not username or not password:
        return jsonify({"message": "Invalid data"}), 400

    # Check if user already exists
    existing_user = Students.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({"message": "Students already exists"}), 400

    # Create new user
    new_user = Students(username=username, password=password,email=email)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "Students registered successfully"}), 201


@app.route('/student_login', methods=['POST'])
def student_login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Simple validation
    if not username or not password:
        return jsonify({"message": "Invalid data"}), 400

    # Check if user exists
    user = Students.query.filter_by(username=username, password=password).first()
    if not user:
        return jsonify({"message": "Invalid username or password"}), 401

    return jsonify({"message": "Login successful"}), 200

############################# End Student Model ########################################################

#################################### Start Request Model #######################################################


class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, nullable=False)
    student_name = db.Column(db.String(120), nullable=False)
    access = db.Column(db.Boolean, default=False, nullable=False)
    request_time = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)



# UPDATE_ACCESS

@app.route('/UPDATE_ACCESS',methods=['POST'])
def UPDATE_ACCESS():
    data = request.json
    book_id = data.get('book_id')
    student_name = data.get('student_name')

    if not book_id or not student_name:
        return jsonify({"message": "Book ID and Student ID are required"}), 400

    request_record = Request.query.filter_by(book_id=book_id, student_name=student_name).first()

    if not request_record:
        return jsonify({"message": "Request not found"}), 404

    # Update the access status
    request_record.access = True

    try:
        db.session.commit()
        return jsonify({"message": "Access granted"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Failed to update access", "error": str(e)}), 500
    

@app.route('/VIEWREQUEST', methods=['GET'])
def VIEWREQUEST():
    request_list = Request.query.all()
    request_data = [
        {
            "id": req.id,
            "book_id": req.book_id,
            "student_name": req.student_name,
            "access":req.access,
            "request_time": req.request_time,
        
        }
        for req in request_list
    ]
    return jsonify({"books": request_data}), 200



@app.route('/OURBOOKS', methods=['POST'])
def OURBOOKS():
    data = request.json
    student_name = data.get('student_name')

    if not student_name:
        return jsonify({"message": "Username is required"}), 400

    request_records = Request.query.filter_by(student_name=student_name).all()

    if not request_records:
        return jsonify({"message": "Request not found"}), 404

    request_data = [
        {
            "id": req.id,
            "book_id": req.book_id,
            "student_name": req.student_name,  # Assuming `student_id` is the correct field
            "access": req.access,
            "request_time": req.request_time.isoformat(),
        }
        for req in request_records
    ]

    return jsonify({"books": request_data}), 200

    


@app.route('/TOTALREQUEST')
def TOTALREQUEST():
          # Query the database to get the latest book
    latest_student = Request.query.order_by(Request.id.desc()).first()

    if latest_student:
        # Return the ID of the latest book
        return jsonify({"final_id": latest_student.id}), 200
    else:
        # If there are no books in the database
        return jsonify({"message": "0"}), 404





@app.route('/REQUEST_SENDS', methods=['POST'])
def REQUEST_SENDS():
    data = request.json

    username = data.get('student_name')
    book_id = data.get('book_id')

    # Simple validation
    if not username or not book_id:
        return jsonify({"message": "Invalid data"}), 400

    # Check if user already exists
    existing_user = Request.query.filter_by(book_id=book_id,student_name=username).first()
    if existing_user:
        return jsonify({"message": "Students Already Requested"}), 400

    # Create new user
    new_user = Request(book_id=book_id,student_name=username)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "Students Requested successfully"}), 201


#################################### End Request Model #######################################################

if __name__ == '__main__':
    app.run(debug=True)


