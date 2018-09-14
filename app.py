from flask import *
app = Flask(__name__)
from models.order import Trasua, User
import mlab
mlab.connect()

@app.route('/')
def index():
    return render_template('index.htm')


#############
app.secret_key = "132465"
#
@app.route("/login", methods = ["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.htm")
    elif request.method == "POST":
        form = request.form
        username = form['user']
        password = form['password']
        # print(user, password)
        user_data = User.objects(username = username, password = password)
        # print(user_data)
        # return "abc"
        if len(user_data) == 1:
            session['logged_in'] = True
            session['user_id'] = str(user_data[0].id)
            print(session['user_id'])
            session['username'] = user_data[0].fullname
            # print(session['fullname'])
            return redirect (url_for('index'))
        else:
            error = "Sai tên đăng nhập hoặc mật khẩu"
            return render_template("login.htm", error=error)
@app.route("/logout")
def logout():
    try:
        del session["user_id"]
        del session["logged_in"]
        ##redirect(url_for("function"))
        return redirect(url_for("index"))
    except BaseException:
        return redirect(url_for("index"))        

@app.route('/about')
def about():
    return render_template('about.htm')

@app.route('/menu', methods = ['GET', 'POST'])
def menu():
    special_drinks = [
        {
            "name":"Trà Đen Milkfoam",
            "link": "https://scontent.fhan3-2.fna.fbcdn.net/v/t1.0-9/41495206_1080923838733350_1780323704366956544_n.jpg?_nc_cat=0&oh=ad8d999951f3d5e3ba880de1f3d7d0f4&oe=5C2F85F4"
        },
        {
            "name":"Trà Bí Đao Milkfoam",
            "link": "https://scontent.fhan3-2.fna.fbcdn.net/v/t1.0-9/41608644_1080923778733356_9216964602779140096_n.jpg?_nc_cat=0&oh=35f25d790b06a5eeff8e538278c83907&oe=5C2E1120",
        },
        {
            "name":"Trà Alisan Milkfoam",
            "link":"https://scontent.fhan3-2.fna.fbcdn.net/v/t1.0-9/41554488_1080923825400018_5565966544019652608_n.jpg?_nc_cat=0&oh=3b6e35760b7ff0474f355596707a7b96&oe=5C2CB054",
        }
    ]
    trasuas = [
        {
            "name":"Trà sữa Oolong",
            "link": "https://scontent.fhan3-2.fna.fbcdn.net/v/t1.0-9/41669931_1080923902066677_4705469781841543168_n.jpg?_nc_cat=0&oh=0b7e21d87582773fe6dd4b3904d23763&oe=5C208A64"
        },
        {
            "name":"Trà sữa Chocolate",
            "link": "https://scontent.fhan3-2.fna.fbcdn.net/v/t1.0-9/41413750_1080923845400016_8612472656224059392_n.jpg?_nc_cat=0&oh=f9c0a4a306a134db3104abf0d8a1bdef&oe=5C1E0870  ",
        },
        {
            "name":"Trà sữa Khoai môn",
            "link":"https://scontent.fhan3-2.fna.fbcdn.net/v/t1.0-9/41598590_1080923908733343_4690689781468758016_n.jpg?_nc_cat=0&oh=a12829fb58c6e862b546081fdbe9f21c&oe=5C2D524A",
        }
    ]
    teas = [
        {
            "name":"Trà Alisan",
            "link": "https://scontent.fhan3-2.fna.fbcdn.net/v/t1.0-9/41514497_1080923765400024_7872533298172395520_n.jpg?_nc_cat=0&oh=cf19b28e7fa07ce957be3fdd73f4ec0a&oe=5C3101CC"
        },
        {
            "name":"Trà bí đao Alisan",
            "link": "https://scontent.fhan3-2.fna.fbcdn.net/v/t1.0-9/41647135_1080923768733357_6677417351949844480_n.jpg?_nc_cat=0&oh=bde799759faa9c914f96d402d9d4f724&oe=5C1B92AC",
        },
        {
            "name":"Trà Ô long ",
            "link":"https://scontent.fhan3-2.fna.fbcdn.net/v/t1.0-9/41514497_1080923765400024_7872533298172395520_n.jpg?_nc_cat=0&oh=cf19b28e7fa07ce957be3fdd73f4ec0a&oe=5C3101CC",
        }
    ]
    if request.method == 'GET':
        return render_template('menu.htm', special_drinks = special_drinks, trasuas = trasuas, teas = teas)    
    elif request.method == 'POST':
        form = request.form
        name = form['tra']
        # return "form"
        # return name 
        return redirect(url_for('order', name=name))
@app.route('/customerinfo')
def customerinfo():
    return render_template('customerinfo.htm')

@app.route("/contact")
def contact():
    return render_template("contact.htm")

@app.route("/signup", methods=["GET","POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.htm")
    elif request.method == "POST":
        form = request.form
        surname = form["surname"]
        full_name = form['name']
        email = form['email']
        phone = form['phone']
        username = form['user']
        password = form['password']
        address = form['address']
        new_user = User(
            surname = surname,
            fullname = full_name,
            username = username,
            email = email,
            password = password,
            phone = phone,
            address = address,
            trasua_id = []
        )
        new_user.save()
        return redirect(url_for('login'))

@app.route('/finishpage')
def finishpage():
    return render_template('finishpage.htm')  

@app.route('/order/<name>', methods = ["GET", "POST"])
def order(name):
    if request.method == "GET":
        if 'user_id' not in session:
            return redirect(url_for('login'))
        else:
            return render_template('order.htm')
    elif request.method == "POST":
        form = request.form 
        sugar = form['radiogroup1']
        ice = form['radiogroup']
        list_topping = form.getlist('topping')
        topping = ", ".join(list_topping)
        size = form['size']

        new_trasua=Trasua(
            name = name,
            sugar = sugar,
            ice = ice,
            topping = topping,
            size = size
        )
       
        new_trasua.save()
        user_id = session['user_id']
        user = User.objects.with_id(user_id)
        user.update(push__trasua_id = new_trasua)
        import time
        time.sleep(60)
        return redirect(url_for('menu'))

@app.route('/profile')
def profile():
    user_id = session['user_id']
    user = User.objects.with_id(user_id)
    tra_sua = user.trasua_id
    return render_template('profile.htm', user = user, tra_sua = tra_sua)
    # return "abc"

if __name__ == '__main__':
    app.run(debug=True)
 