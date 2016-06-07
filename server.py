from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'my_secret_key'

if __name__ == '__main__':
  app.run(debug = True)
