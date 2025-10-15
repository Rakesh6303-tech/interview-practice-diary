About :

My project is an Online Food Delivery System developed using Java, J2EE, Servlets, JSP, and MySQL.
It allows users to browse restaurants, view menus, add items to a cart, and place orders online.
The backend manages the orders and updates their status in real-time.
I used JDBC for database connectivity and Tomcat Server for deployment.
-----------------------------------------------------------------------------------------------------------
          
Technologies : 
Front End : HTML, Css
DB: MySQl
Backend : Java,  JDBC, Servlets, JSP
-------------------------------------------------------------------------------------------------------------

---->JDBC : Java DataBase Connectivity. Basically It is a API which is used to connect Java Program to DB.
General Steps to Connect DB:
1) Load Driver
2) Establish Connection
3) Create Sql Statement
4) Execute Stmt
5) Process Result
------------------------------------------------------------------------------------------------------------------------------------------

---->JSP : Java Server Pages which is used to create Dynamic Web Applications. It is combination of HTML code & Java Code.

How Did You Used Jsp in ur Project?
   In my project i used jsp to show restarnt listings & cart contents by pulling data from servlets.
------------------------------------------------------------------------------------------------------------------------------------------

---->Servlets : is used to Handle  the server side logic. They Process HTTP Request & Manage Response and connect Frontend<--->Backend
      In my roject Restarnt Servlet Fetched Data from Mysql & sent it to JSP for Display.
Servlets Which I created  in my Project
LoginServlet ,  HomeServlet, Restarnt Servlet, Menu Servlet, Cart Servlet, Order servlet

Session : Parameters  like get Attribute , Set Attribute
------------------------------------------------------------------------------------------------------------------------------------------
Which Arichiture Did you use in ur Project ? 
MVC : MODEL, VIEW, CONTROLLER
Model : In the Model Layer I've Placed POJO(user, Restarnt) classes.
View : In Viewer Layer I 've Placed JSP, HTML Css Files
Controller : In controller Layer  I've Placed Servlets
------------------------------------------------------------------------------------------------------------------------------------------

Challenges (or) Issues in ur Project & Overcome
I faced  some JDBC Issues, and fixed with Exception Handling
------------------------------------------------------------------------------------------------------------------------------------------
2️⃣ What technologies did you use and why?

------> Java & J2EE: Core logic and web handling.

------> Servlets: Handle client requests and responses.

-------> JSP: Display dynamic web content.

-------> JDBC: Connect Java code to MySQL database.

-------> MySQL: Store restaurant, user, and order details.

--------> HTML/CSS: Frontend design and layout.





# Why Did You use this Technologies?
# MYSQL: is a opensource, light weight, & Integrates easily with Java Through JDBC.
# Servlets : is used to Handle Business Logic & HTTP Req (like adding items to cart, placing orders etc)
# Java : Java is object-oriented, and perfect for Building Scalable Backend Logic.
# JSP → A part of J2EE.
# J2EE → A collection of technologies (including JSP, Servlets,  JDBC, etc.) to build enterprise apps.
# JDBC : Java DataBase Connectivity. Basically It is a API which is used to connect Java Program to DB.
-------------------------------------------------------------------------------------------------------------------------------------------

How did you Implemnet user Authentication?
I Built LoginServlet to process login from Data, Queried MySQl with "select * from users where username=?" & stored valid users in sesssion.
Faild logins redirected with an Error".
---------------------------------------------------------------------------------------------------------------------------------------------

