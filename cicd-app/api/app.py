from flask import Flask, jsonify
import os
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    try:
        conn = mysql.connector.connect(
            host=os.environ.get('DB_HOST', 'db'),
            user=os.environ.get('DB_USER', 'appuser'),
            password=os.environ.get('DB_PASSWORD', 'apppassword'),
            database=os.environ.get('DB_NAME', 'appdb')
        )
        conn.close()
        return "Conexión exitosa a la base de datos"
    except Exception as e:
        return f"Error de conexión a la base de datos: {str(e)}", 500

@app.route('/db-test')
def db_test():
    return home()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
# CI/CD activado Thu Aug 20 22:31:40 UTC 2026
