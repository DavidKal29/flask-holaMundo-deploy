from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

app=Flask(__name__)

@app.route('/')
def index():
    USERNAME=os.getenv('USER')
    EMAIL=os.getenv('EMAIL')
    PASSWORD=os.getenv('PASSWORD')

    print(USERNAME,EMAIL,PASSWORD)

    return '<h1>Hola Mundo, esta es mi primera app deployada en render. Mis datos:<br> {}<br> {}<br> {}</h1>'.format(USERNAME,EMAIL,PASSWORD)

def status_404(error):
    return '<h1>Pagina no encontrada, error 404, not found, salir de aqui que no hay nada, fuera</h1>'

if __name__=='__main__':
    app.register_error_handler(404,status_404)
    app.run(debug=True)