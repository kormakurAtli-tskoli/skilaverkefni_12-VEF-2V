# Kormákur Atli Unnþórsson
# 11.11.2017
# Skilaverkefni 12

from bottle import *
import os

@route("/")
def index():
    return "Kormákur er kominn á Heroku."
    
run(host='0.0.0.0', port=os.environ.get('PORT'))
