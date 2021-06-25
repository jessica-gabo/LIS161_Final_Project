from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return ""
# Since granted is set to default as False, the grant method then overrides the set granted value to true
granted = False


def grant():
    global granted
    granted = True


# this login method is used to check the username and passwords stored in the user_details.txt file and allows the
# user to login if username and password match
def login(name, password):
    success = False
    file = open("user_details.txt", "r")
    for i in file:
        a, b = i.split(",")
        b = b.strip()
        if (a == name and b == password):
            success = True
            break
            file.close()

            if (success):
                print("Login Succesful!")
                grant()
            else:
                print("Incorrect username or password! Please Try again!")


# this register method enables to user to register a username and password and store it to the user_details.txt file
def register(name, password):
    file = open("user_details.txt", "a")
    file.write("\n" + name + "," + password)
    file.close()


# this code allows the user to login and register. if the user succesfully logs in it pull up the main ordering system code while if he/she chooses to register it asks of rthe desired username and password and automatically appends it to the txt file by calling the regioster method defined above
def access(option):
    global name
    if option == "login":
        name = input("Enter username: ")
        password = input("Enter password: ")
        login(name, password)
        print("Login Successful!")
        grant()  # changes the value of the granted varaible to tru which triggers a series of codes to run
    else:
        print("Enter desired username and password to register.")
        name = input("Enter desired username: ")
        password = input("Enter desired password: ")
        print("Register Successful!")
        register(name, password)


# this begin method is the opening method and allows the user to pull up the login and register menu
def begin():
    # declared globally to ensure that the variable option can ba accessed and manipulated all throughout the code
    # without it needing to be defined again and again
    global option
    print("Welcome to our restaurant!")
    option = input("login or register? (Enter word of choice use small letters): ")
    if option != "login" and option != "register":
        begin()


# the main body of the code
begin()  # calls the begin function
access(option)  # calls the access funtion which is for the login and register
if granted:  # after value of the grant granted value changes to true with the help of the grant function it then runs the codes below which contains the ordering system of our project
    # declares the menu lists which holds the menu that can be purchased by the customer
    menu_list = [
        {"id": 1, "name": "1. Blueberry Cheesecake", "price": 450, "$": "pesos"},
        {"id": 2, "name": "2. Strawberry Cheesecake", "price": 430, "$": "pesos"},
        {"id": 3, "name": "3. Mango Cheesecake", "price": 450, "$": "pesos"},
        {"id": 4, "name": "4. Basque Burnt Cheesecake", "price": 500, "$": "pesos"},
        {"id": 5, "name": "5. Assorted Mini Cheesecake", "price": 300, "$": "pesos"}]
    # this list will hold the orders that the customer will be ordering
    Order_list = []
    print(
        '========================== Welcome to Simply Dahlicious, I wish you a happy meal ============ '
        '======================== ')
    print("Today's menu:")
    for menu in menu_list:
        print(menu.get('name'), menu.get('price'), menu.get('$'))
    while True:
        print('=' * 50)
        print("1. User order \ n2. Cancel order \ n3. Confirm menu \ n4. Checkout")
        server = int(input("Please select service:"))

        # conditional statements for the choices which basically enters what the customer orders, their value and adds them to the order list
        if server == 1:
            while True:
                menu_add = input("Please enter the dish number or enter X to finish ordering:")
                if menu_add.upper() != 'X':
                    for m in menu_list:
                        if m.get('id') == int(menu_add):
                            Order_list.append(m)
                            break
                else:
                    print('================== Ordered =====================')
                    total_price = 0
                    for order in Order_list:
                        print(order.get('name'), order.get('price'), order.get('$'))
                        total_price += int(order.get('price'))
                    print('Subtotal: {} pesos'.format(total_price))
                    break
            # removes the order
        elif server == 2:
            menu_del = input("Please enter the number of the dish you want to remove:")
            for order in Order_list:
                if order.get('id') == int(menu_del):
                    Order_list.remove(order)

            print('================== Ordered =====================')
            total_price = 0
            for order in Order_list:
                print(order.get('name'), order.get('price'), order.get('$'))
                total_price += int(order.get('price'))
            print('Subtotal: {} pesos'.format(total_price))

        # shows the ordered items again
        elif server == 3:
            print('================== Ordered =====================')
            total_price = 0
            for order in Order_list:
                print(order.get('name'), order.get('price'), order.get('$'))
                total_price += int(order.get('price'))
            print('Subtotal: {} pesos'.format(total_price))
        # computes the total order by adding all the value of the items ordered then terminates the code
        elif server == 4:
            print('================= Your total order =======================')
            total_price = 0
            for order in Order_list:
                print(order.get('name'), order.get('price'), order.get('$'))
                total_price += int(order.get('price'))

            print('Total consumption: {} pesos'.format(total_price))

            print('================== Thank You and Come Again! =====================')
            break
                app.run()
