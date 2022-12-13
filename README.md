# homecentre
Django website

Requirements - Python 3

**Steps to run this project on Windows 11 -**

1 -Create a folder and open Command Prompt Window in that directory

2- Clone the code from GitHub - HomeCentre
git clone https://github.com/imsaurabh1/homecentre.git

3- Install Virtual Environment – if not installed already  
pip install virtualenv

4 – Create a virtual environment with a name – for example ‘saurabh_env’
virtualenv saurabh_env

5- Activate virtual environment by navigating to .bat file 
.\saurabh_env\Scripts\activate.bat

6- Install all libraries using in the project using requirements.txt file
pip install -r requirements.txt

7 – Migrate Django project
python manage.py migrate

8 – Run the application  
python manage.py runserver


This project involves following functionalities – 
**-Signup** 
New user can signup using email, password

**-Login**
Existing user can login with email and password

**-Logout**
Logs out already logged in user

**-Admin Management**
Admin is able to manage Categories, Products and Orders 
Add, Delete, Update is possible 

**-Home** 
Displays Home Page with product images and details

**-Product Page**
Displays individual product details

**-Cart Page**
Displays products added by the user

**-Checkout Page**
Asks for user info – address and phone for shipping and shows total price 

**-Payment**
Takes the user to STRIPE payment gateway – it accepts card payments

**-Success**
Once the payment is complete, it displays thanks for purchasing


Snapshots of the website are added below – 
**HOME**
![HOME](/media/snaps/home.jpg)

**LOGIN**
![LOGIN](/media/snaps/login.jpg)

**SHOP**
![SHOP](/media/snaps/shop.jpg)

**PRODUCT**
![PRODUCT](/media/snaps/product.jpg)

**CART**
![CART](/media/snaps/cart.jpg)

**CHECKOUT**
![CHECKOUT](/media/snaps/checkout.jpg)

**PAYMENT**
![PAYMENT](/media/snaps/payment.jpg)

**SUCCESS**
![SUCCESS](/media/snaps/success.jpg)

**ADMIN-HOME**
![ADMIN-HOME](/media/snaps/admin-home.jpg)

**ADMIN-PRODUCT**
![ADMIN-PRODUCT](/media/snaps/admin-product.jpg)

**ADMIN-ORDER**
![ADMIN-ORDER](/media/snaps/admin-order.jpg)

