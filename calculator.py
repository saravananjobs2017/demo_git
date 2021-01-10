from flask import *

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def welcome():
    if request.method == 'GET':
        return render_template('button.html')
    elif request.method == 'POST':
        if request.form.get('submit_button') == 'Addition':
            final = add()
            return 'the value:%s' % final
        elif request.form.get('submit_button') == 'Subtraction':
            final=sub()
            return 'the value:%s' % final
        elif request.form.get('submit_button') == 'Multiply':
            final=mul()
            return 'the value:%s' % final
        elif request.form.get('submit_button') == 'Division':
            final=div()
            return 'the value:%s' % final
def add():
    val1 = int(request.form.get('first_value'))
    val2 = int(request.form.get('second_value'))
    result = int(val1 + val2)
    return 'the value:%s' % result
def sub():
    val1 = int(request.form.get('first_value'))
    val2 = int(request.form.get('second_value'))
    result = int(val1 - val2)
    return 'the value:%s' % result
def mul():
    val1 = int(request.form.get('first_value'))
    val2 = int(request.form.get('second_value'))
    result = int(val1 * val2)
    return 'the value:%s' % result
def div():
    val1 = int(request.form.get('first_value'))
    val2 = int(request.form.get('second_value'))
    result = int(val1 / val2)
    return 'the value:%s' % result


if __name__ == '__main__':
    app.run(debug=True)
