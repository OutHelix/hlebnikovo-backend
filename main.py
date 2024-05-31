from flask import Flask, render_template, request, redirect
import datbase
app = Flask(__name__)
@app.route("/", methods = ("POST", "GET"))
@app.route("/home", methods = ("POST", "GET"))
def index():
    if request.method == "POST":
        username = request.form["username"]
        phone = request.form["phonenumber"]
        qtext = request.form["question"]
        datbase.writeQ(username, phone, qtext)
    return render_template("index.html")


@app.route("/carehorse")
def carehorse():
    return render_template("care_of_horses.html")


#Страницы Цены и дочерние
@app.route("/price/", methods = ["POST", "GET"])
def price():
    if request.method == "POST":
        date = request.form["selected_date"]
        time = request.form["selected_time"]
        fullname = request.form["fullname"]
        phone = request.form["phone"]
        numofpeople = request.form["numofpeople"]
        datbase.writePeople(date, time, fullname, phone, numofpeople)
        return redirect("/price/")
    dates = datbase.getDateList()
    times = datbase.getTimeList()
    number = datbase.getDataTime(dates)
    return render_template('price.html', number = number, dates = dates, times = times)


@app.route("/getname", methods = ["POST"])
def getname():
    datbase.horsename = request.form["horsename"]
    dates = datbase.getDateList()
    number = datbase.getDataTime(dates)
    times = datbase.getTimeList()
    return render_template('price.html', number = number, dates = dates, times = times)



@app.route("/price/certificates")
def certificates():
    return render_template('certificates.html')


@app.route("/price/sales")
def sales():
    return render_template('sales.html')


#Страница О Нас и дочерние
@app.route("/about/")
def about():
     return render_template('aboutus.html')


@app.route("/about/coaches")
def coaches():
    return render_template('coaches.html')


@app.route("/about/otherstaff")
def otherstaff():
    return render_template("otherstaff.html")


@app.route("/about/volunteer")
def volunteer():
    return render_template("volunteer.html")


@app.route("/news")
def news():
    return render_template('news.html')


@app.route("/photogallery")
def photogallery():
    return render_template('photogallery.html')


#Страница Лошади и все лошади
@app.route("/horses/")
def horses():
    return render_template("horses.html")


@app.route("/horses/<string:namehorse>", methods = ("POST", "GET"))
def showHorse(namehorse):
    horseinfo = datbase.getInfo(namehorse)
    return render_template("horse_template.html", horseinfo = horseinfo)


if __name__ == "__main__":
     app.run(debug = True)
app.config['DEBUG'] = True
