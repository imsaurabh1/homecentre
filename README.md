# homecentre
Django website  

Requirements - Python 3   

## **Steps to run this project on Windows 11 -** ##   

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
cd homecentre  
pip install -r requirements.txt  

7 – Migrate Django project   
python manage.py migrate  

8 – Run the application  
python manage.py runserver  


## This project involves following functionalities –##   

**1. Signup** 
(profile icon on top right)  
New user can signup using email, password  

**2. Login**  
(profile icon on top right)   
Existing user can login with email and password  

**3. My Account**  
(profile icon on top right)    
User can see profile details and my orders  
User can modify Name, Username and Email  

**4. Logout**  
(Logout button on top)  
Logs out already logged in user   

**5. Admin Management**  
(http://127.0.0.1:8000/admin/)  
Admin is able to manage Categories, Products and Orders   
Add, Delete, Update functionality for Categories, Products and Orders  
Filters and Sorting of Orders  

**6. Home**  
Displays Home Page with product images and details  
Add product to cart using cart icon   

**7. Product Page**  
(Shop Button on top left)  
Displays individual product details  
Ability to search by product name  
Filter by categories    

**8. Cart Page**  
(Cart Icon on top right)  
Displays products added by the user and total cost    
Ability to increase or decrease product count  

**9. Checkout Page**  
(Confirm Checkout Button)  
Asks for shipping information - all fields are mandatory  
Displays total amount  

**10. Payment**  
Takes the user to STRIPE payment gateway – accepts card payments  

**11. Success**  
(Pay Button on payment page)    
Once the payment is complete, it displays thanks for purchasing 

**12. Review**  
(Product page - scroll down)  
Rating from 1 to 6  
Review Comment  

## **Snapshots of the website are added below –** ##  


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

