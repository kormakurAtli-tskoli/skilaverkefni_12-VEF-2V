# Kormákur Atli Unnþórsson
# 11.11.2017
# Skilaverkefni 12

from bottle import *
from sanitize import sanitize
import pymysql

#static files route
@route("/static/<filename>")
def staticFile(filename):
    return static_file(filename, root="./static/")

run(host="0.0.0.0", port="argv[1]")
