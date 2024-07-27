Video Reference : https://www.youtube.com/watch?v=yBDHkveJUf4

🔗 Part 1: https://jovian.com/aakashns/web-development-with-python
🔗 Part 2: https://jovian.com/aakashns/database-driven-web-applications


# Web Devlopment in Python from scratch
## Create a career website and Deploy it using "free" online resources.

**What we learn ?**
  - Python, Flask
  - Git
  - Replit
  - HTML, CSS and Bootstrap framework
  - Deployment on cloud platform (specifically on the render.com)
  - set up own custom domain and configure it to point the website we created and deployed.

### **Git hub Repository** 
The name of github repository should be named as, It can have one or more lowercase world seprated with (-)
Ex : career-website  

- When It is starting of out project, If there is no files to push then adding a readme.md is good thing. It will initialize the repository so we we don't need to push to get started.

- And then we also going to add .gitignore file. so that we can ignore compile files, build files, intermediate files are created by Python.
which we may not put onto git beacause it is not actual source code they are simply used to run the source code.
select a .gitignore template for python. that will be added to the root of the repository.

As per we're working on different languages. For diff. prog. lang. we want to ignore diff. files. For that thing github provides a template for diff. prog. lang. and that way here we choose the template of Python

- When we make our project public It is definitely good idea to add license. And when it is free the why should we don't add it. It makes out respository looks like professional.

License lets other know how they can use it wheather they can use it commercially(વ્યાપારી રીતે) wheather they can build on top of it.
select : MIT License
which is the most liberal(दानशील,उदार) license

- create repo

- see the .gitignore it has list of files that should be exlded from git.

### Open the project on Replit.
Github is used to store and share project. But we can not devlop project here.
so that why we'll use a cloud platfrom that is Replit.com. It is online IDE.

Connect Replit with github and select repository.
change he language to python or flask(reccomended for webview)
 then import from github.

- We need to configure a run command and everytime we click on the  [▶ Run] button that run command will execute and output will shown to the console tab.

configure command : python app.py

- This will change the file called .replit which contains the information which file will run afte click on the Run button.
.replit file is hidden file

- we have a shell that works like terminal. we can run any command line utilities like ls, pwd, cd.
Basically it is like linux terminal and it has linux commands 

- create a file app.py
and text it by simple python program
```python
print("Hello World")
```

we can run the code using either 
(i)  **Run** button
(ii) using **shell** python app.py command

{
There is anoter way also
 - create new flask repl
 - fire a command : git clone <url>
  where, url = github repo. url 
}



### Create a flask Web Server
flask documentation : https://flask.palletsprojects.com/en/3.0.x/

flask is one of the most popular package in Python

check the installation and quick start section.
Every libaray have installation guide and quick start in it's docs. 

In shell fire :-
```
> pip install flask
```



#### flask quick start
https://flask.palletsprojects.com/en/3.0.x/quickstart/

module name flask is installed 

- modules always have name in lowercase. Ex : numpy, pandas, flask
- classes are in PascalCase
- method are in camelCase
- variable can be in camelCase or snake_case

```python
from flask import Flask
```
Import Flask class from flask module. Even though both have same name so it will be little bit confusing.


