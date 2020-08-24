# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 14:48:42 2020

@author: Madhan Kumar Selvaraj
"""


from flask import Flask, render_template

server = Flask(__name__)
server.debug = True
@server.route('/')
def landing_page():
    return render_template('index.html')
    
if __name__ == '__main__':
    server.run(debug=True)
