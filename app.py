from flask import Flask,render_template,request,session,redirect,url_for
app = Flask(__name__)
app.config['SECRET_KEY']='dfasgfdasyilfhadsilhil'
user_details = {'samarth':'vaibav','admin':'user'}

@app.route('/home')
def home():
    return '<h3>Hello World</h3>'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/how_to_play')
def howtoplaychess():
    return render_template('how_to_play.html')

@app.route('/regi')
def registration():
    return render_template('register.html')

@app.route('/verify_register',methods = ['POST'])
def verify_register():
    username = request.form.get('username') 
    password = request.form.get('password')
    email = request.form.get('email')
    user_details[username]=password
    print(user_details)
    return render_template('registation_successful.html')
@app.route('/login',methods=['get','POST'])
def login():
    if session.get('authenticated') == True:
        return render_template('login_sucsessful.html')
    else:
        return render_template('login.html')

@app.route('/user_validation',methods=["POST"])
def validate():
    username=request.form.get('username')
    print(username)
    password=request.form.get('password')
    return_value = login_sucsess(user_details,username,password)
    if return_value == True:
        session['authenticated'] = True
        return render_template('login_sucsessful.html',username=username)
    else:
        session['authenticated'] = False
        return render_template('login_failed.html')
def login_sucsess(dictionary,username,password):
    if dictionary.get(username,"User Not Found")==password:
        return True
    else:
        return False
@app.route('/quiz')
def quiz():
    return render_template('quiz.html')


@app.route('/mquiz')
def mquiz():
    return render_template('mathquiz.html')

@app.route('/mlion')
def mlion():
    return render_template('mountain_lion.html')

@app.route('/feed')
def feed():
    return render_template('feedback.html')

@app.route('/qu1', methods = ['POST'])
def qu1():
    return render_template('quiz1.html')

@app.route('/qu2',methods = ["POST"])
def qu2():
    return render_template('quiz2.html')

@app.route('/qu3',methods = ["POST"])
def qu3():
    return render_template('quiz3.html')

@app.route('/q1')
def q1():
    return render_template('q1.html', score = 0)
@app.route('/calc')
def calc():
    return render_template('calc.html')

@app.route('/q2',methods = ["POST"])
def q2():
    p_score = session.get("score", 0)
    c_score = p_score
    s_answer = request.form.get('callTime')
    c_answer = request.form.get("ca")
    if s_answer == c_answer:
        marks = 10
        c_score = p_score+marks
        session["score"] = c_score
    return render_template('q2.html',score = c_score)

@app.route('/q3',methods = ["POST"])
def q3():
    p_score = session.get("score", 0)
    c_score = p_score
    s_answer = request.form.get('callTime')
    c_answer = request.form.get("ca")
    if s_answer == c_answer:
        marks = 10
        c_score = p_score+marks
        session["score"] = c_score
    return render_template('q3.html',score = c_score)


@app.route('/q4',methods = ["POST"])
def q4():
    p_score = session.get("score", 0)
    c_score = p_score
    s_answer = request.form.get('callTime')
    c_answer = request.form.get("ca")
    if s_answer == c_answer:
        marks = 10
        c_score = p_score+marks
        session["score"] = c_score
    return render_template('q4.html',score = c_score)

@app.route('/q5',methods = ["POST"])
def q5():
    p_score = session.get("score", 0)
    c_score = p_score
    s_answer = request.form.get('callTime')
    c_answer = request.form.get("ca")
    if s_answer == c_answer:
        marks = 10
        c_score = p_score+marks
        session["score"] = c_score
    return render_template('q5.html',score = c_score)

@app.route('/miq1')
def miq1():
    return render_template('age7_9q1.html', score1 = 0)

@app.route('/miq2', methods = ["POST"])
def miq2():
    p_score = session.get("score1", 0)
    c_score = p_score
    s_answer = request.form.get('callTime')
    c_answer = request.form.get("ca")
    if s_answer == c_answer:
        marks = 10
        c_score = p_score+marks
        session["score1"] = c_score
    return render_template('age7_9q2.html',score1 = c_score)

@app.route('/miq3', methods = ["POST"])
def miq3():
    p_score = session.get("score1", 0)
    c_score = p_score
    s_answer = request.form.get('callTime')
    c_answer = request.form.get("ca")
    if s_answer == c_answer:
        marks = 10
        c_score = p_score+marks
        session["score1"] = c_score
    return render_template('age7_9q3.html', score1 = c_score)    

@app.route('/miq4', methods = ["POST"])
def miq4():
    p_score = session.get("score1", 0)
    c_score = p_score
    s_answer = request.form.get('callTime')
    c_answer = request.form.get("ca")
    if s_answer == c_answer:
        marks = 10
        c_score = p_score+marks
        session["score1"] = c_score
    return render_template('age7_9q4.html', score1 = c_score)    

@app.route('/miq5', methods = ["POST"])
def miq5():
    p_score = session.get("score1", 0)
    c_score = p_score
    s_answer = request.form.get('callTime')
    c_answer = request.form.get("ca")
    if s_answer == c_answer:
        marks = 10
        c_score = p_score+marks
        session["score1"] = c_score
    return render_template('age7_9q5.html', score1 = c_score)    

@app.route('/hiq1')
def hiq1():
    return render_template('age10_14q1.html', score2 = 0)

@app.route('/hiq2',methods = ["POST"])
def hiq2():
    p_score = session.get("score2", 0)
    c_score = p_score
    s_answer = request.form.get('callTime')
    c_answer = request.form.get("ca")
    if s_answer == c_answer:
        marks = 10
        c_score = p_score+marks
        session["score2"] = c_score
    return render_template('age10_14q2.html', score2 = c_score)

@app.route('/hiq3',methods = ["POST"])
def hiq3():
    p_score = session.get("score2", 0)
    c_score = p_score
    s_answer = request.form.get('callTime')
    c_answer = request.form.get("ca")
    if s_answer == c_answer:
        marks = 10
        c_score = p_score+marks
        session["score2"] = c_score
    return render_template('age10_14q3.html', score2 = c_score)

@app.route('/hiq4',methods = ["POST"])
def hiq4():
    p_score = session.get("score2", 0)
    c_score = p_score
    s_answer = request.form.get('callTime')
    c_answer = request.form.get("ca")
    if s_answer == c_answer:
        marks = 10
        c_score = p_score+marks
        session["score2"] = c_score
    return render_template('age10_14q4.html', score2 = c_score)

@app.route('/hiq5',methods = ["POST"])
def hiq5():
    p_score = session.get("score2", 0)
    c_score = p_score
    s_answer = request.form.get('callTime')
    c_answer = request.form.get("ca")
    if s_answer == c_answer:
        marks = 10
        c_score = p_score+marks
        session["score2"] = c_score
    return render_template('age10_14q5.html', score2 = c_score)

@app.route('/end_quiz', methods = ["POST"])
def end_quiz():
    p_score = session.get("score", 0)
    c_score = p_score
    s_answer = request.form.get('callTime')
    c_answer = request.form.get("ca")
    if s_answer == c_answer:
        marks = 10
        c_score = p_score+marks
        session["score"] = c_score
    return render_template('end_quiz.html', score = c_score)

@app.route('/end_quiz1', methods = ["POST"])
def end_quiz1():
    p_score = session.get("score1", 0)
    c_score = p_score
    s_answer = request.form.get('callTime')
    c_answer = request.form.get("ca")
    if s_answer == c_answer:
        marks = 10
        c_score = p_score+marks
        session["score1"] = c_score
    return render_template('end_quiz1.html', score1 = c_score)


@app.route('/end_quiz2', methods = ["POST"])
def end_quiz2():
    p_score = session.get("score2", 0)
    c_score = p_score
    s_answer = request.form.get('callTime')
    c_answer = request.form.get("ca")
    if s_answer == c_answer:
        marks = 10
        c_score = p_score+marks
        session["score2"] = c_score
    return render_template('end_quiz2.html', score2 = c_score)

@app.route('/end_quiz3', methods = ["POST"])
def end_quiz3():
    p_score = session.get("score", 0)
    c_score = p_score
    s_answer = request.form.get('callTime')
    c_answer = request.form.get("ca")
    if s_answer == c_answer:
        marks = 10
        c_score = p_score+marks
        session["score"] = c_score
    return render_template('end_quiz3.html', score = c_score)


@app.route('/logout')
def logout():
    session.pop("username", None)
    session.clear()
    return redirect(url_for("index"))
if __name__ == '__main__':
    app.run(debug=True)