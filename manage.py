from flask import Flask, request, render_template
from flask_bcrypt import Bcrypt

# Create a Flask application
app = Flask(__name__) 

# Initialize bcrypt
bcrypt = Bcrypt(app)

# Create route for registration page
@app.route('/register', methods=['POST'])
def register():
    # Get form values
    username = request.form.get('username')
    password = request.form.get('password')

    # Encrypt the password using bcrypt
    encrypted_password = bcrypt.generate_password_hash(password).decode('utf-8')

    # Store the username and encrypted password in the database

    # Render a success message
    return render_template('register_success.html')

# Create route for login page
@app.route('/login', methods=['POST'])
def login():
    # Get form values
    username = request.form.get('username')
    password = request.form.get('password')

    # Look up the username in the database
    # Get the encrypted password associated with the username

    # Encrypt the submitted password using bcrypt
    encrypted_password = bcrypt.generate_password_hash(password).decode('utf-8')

    # Compare the encrypted passwords
    if bcrypt.check_password_hash(encrypted_password, password):
        # Grant access
        return render_template('login_success.html')
    else:
        # Display error message
        return render_template('login_error.html')

if __name__ == '__main__':
    app.run()