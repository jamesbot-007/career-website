```python
from flask import Flask
```
Import Flask class from flask module. Even though both have same name so it will be little bit confusing.

```python
app = Flask(__name__)
```
app is object of class Flask. All we're doing here importing functionalities from flask and putting it into a variable(i.e. app)



## Let's check wheather the imported thing is class or function
visit  : [check.py](https://replit.com/@MayankKapadane/career-website#check.py)



Everytime we create a Falsk object we need to pass "name". Typically in each python file the varible \_\_name\_\_ is alredy defined. 

The \_\_name\_\_ is refers to how a perticular script was invoked(called or run). 
- if it is invoke using "python app.py" then the name = main
- and if it is invoke from somewhere else then name varible have some other value.

```python
print(__name__)
```
and the output will be:-
```shell
__main__
```



So, Till now we created a flsk application.


Now, we need to create route

- When we visit a website suppose www.MKcoder.com that time url is https://MKcoder.com
After we go inside 'about' section the url will change and become https://MKcoder.com/about
we see something different on about page as compare to Home page(i.e.  https://MKcoder.com)
- we need to tell flask a certain url is requested what should be return.

**Route : route is the simply part of the url after the domain name**

and the way we do that is with an '@' character.
@ character is known as decorator in python. It is slightly advance concept that's often used in libraries to provide some advanced funtionalities. 

In app.route() we need to pass which wanted to match. we pass "/" which is the empty route which is 
basically the home page of MKcoder.com
then we define a function below the decorator. By adding this we're saying to the flask when the url "/" accessed then show "hello world"

- Once we run it we see nothing will happen. Because they(flask docs) expected to run a flask app in slightly different way
- https://flask.palletsprojects.com/en/3.0.x/quickstart/

we can run the app.py using flask run command 

```powershell
> flask --app file_name run
```
<br/>  <!-- Adding a <br/> tag for emopty line -->

In our case that is like,
```powershell
> flask --app app run
``` 
- This will start running a flask app on port 5000

so, what we need to do go inside the .replit file and change the "run" command because flask expects to be run in different way.
 
 This is one way to run it another way to run it is. Another way is using app.run() For that visit app.py 
 
<!-- Add an horizontal ruler line -->
***  
___

When we run our app.py then replit will create a fake browser within our browser. 
b.d. a flask app will run on port=5000. Although, we can mention the port.

---
recap of what we do
- imported flask
- created a flask app
- register a route
- run the app by using app.run() on 0.0.0.0 this is something that we always need to put,  and debug = True so like everytime we have made change in our code that will automatically refelect on currently running server
    - that means we do not to restart the server after making some changes

\[ Note : We can open that fake browser in new tab of chrome that time url shows on which our flask app is deployed on  
we can share to someone 
replit is not good for production workload so we can not send lot of traffic on that url, But is great for testing, creating prototype, showing something to your colleague or friends
By the replit is saying that thing as warning in console section when we run the app.py amd start the server\]

