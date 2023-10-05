from flask import Flask, render_template, request
import os
from prediction import Prediction

app = Flask(__name__, template_folder="templates")

extra_dirs = ['templates', 'static']
extra_files = extra_dirs[:]
for extra_dir in extra_dirs:
    for dirname, dirs, files in os.walk(extra_dir):
        for filename in files:
            filename = os.path.join(dirname, filename)
            if os.path.isfile(filename):
                extra_files.append(filename)

JR = Prediction()

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        data = request.form.get('text')
        print(f"The user entered: {data}")

        if data != '':
            suggested_titles, result = JR.recommend(data)

            if len(result) != 0:
                return render_template('main.html', user_input=data, suggested_titles=suggested_titles, results=result)
            else:
                return render_template('main.html', error='true')

            
    return render_template('main.html')


if __name__ == '__main__':
    app.run(debug=True, extra_files=extra_files)
