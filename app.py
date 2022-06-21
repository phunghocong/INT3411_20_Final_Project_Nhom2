from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

app = Flask(__name__)
# khởi tạo và xây dựng trang web demo để hiện thị index.html
# sử dụng Flask để tạo ra một ứng dụng web
@app.route('/')
def index():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)