
About : My Project Name Is OFS. It is a Web Application . 
         I Build By using Java, Jdbc, Servlets, JSsP & MYSQL. 
        It Handles Features Like Food ordering, Restaurent Listings, USer Login,  & Cart.
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

Why Did You use this Technologies?
MYSQL: is a opensource, light weight, & Integrates easily with Java Through JDBC.
JSP: It allowed me to embed Java Directly into the web pages for Displaying Data From Backend (like menu items, user cart, etc)
Servlets : is used to Handle Business Logic & HTTP Req (like adding items to cart, placing orders etc)
Java : Java is robust, object-oriented, and perfect for Building Scalable Backend Logic.
-------------------------------------------------------------------------------------------------------------------------------------------

How did you Implemnet user Authentication?
I Built LoginServlet to process login from Data, Queried MySQl with "select * from users where username=?" & stored valid users in sesssion.
Faild logins redirected with an Error".
---------------------------------------------------------------------------------------------------------------------------------------------

