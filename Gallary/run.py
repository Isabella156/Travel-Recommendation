from app import app, db

db.create_all()
app.run(debug=True, port=5002)