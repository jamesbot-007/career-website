image
- <img> is closing tag
- we have "src" somthing called as attribute

## Downlaod an image and upload to replit
visit https://unsplash.com/ for images on unsplash we can find royalty free image means we don't need to buy the photo for using it 

Download an image upload to replit using three dots of file explorer so that it can be access by our flask appication.
  We will put the image some where from that we can access the image for our flask application. That's where is "static" folder  
  for that we create a folder called "static" this should be outside the templates 

## Static folder
Anything we put under the "static" folder will be directly shared by flask

flask will allow you(user) to access the static file using the url 
Ex: make sure your server is running and click on this url : https://\<url_by_replit\>/static/banner.jpg by which we can access the image 

## <ins>Static</ins> folder and <ins>templates</ins> folder
templates : templates folder contains that we want to serve when user visit some specific url / endpoint.
  - for that we use render_template()
Anything we put in templates is called template

static : It contains a static data that can access html file which is inside templates
  - fot that we use url_for()
Anything we put in static is called assets

## About section 
we can search for text generators
or "lorem ipsum text generator" it is standard text that is used 
https://loremipsum.io/


## Styling using CSS
The sote looks ugly,It doesn't really look that great. so far we have seen render templates and use static assets. So, anything we put inside a static folder called assets.
- CSS all about properties and selector.
- every color that you can see on the screen that is buit using red(r), greeen(g), bkue(b) colors
  - If we have same value for red,blue and green then it will be shades of gray in rgb()
  - The values of rgb has range 0-255 Total 266 values.

- Id is ideally something that should be unique on the page only one element on the web page should have an id. Otherwise browser make it confuse.

- if the image is streched from left and right. for that we have property "object-fit:cover" which will instead if streaching the picture we will use the portion of that picture that will fit as per we mention height and weidth

- if the paragraph is expanded takes full width then, it is hard to read so, we'll reduce weidth also text-align:center

We can use a Framework for faster devlopment. Instead of writting CSS manually for every website we build we can use pre existing set fo styles that have been created by good designers because we may not have good design skills and we can apply those css by specifing classes.

--> commit changes and remove all styles, class, id from the file make it simple pure HTML.

## Bootstrap
Search for getbootstrap.com
Right now we just include the CSS CDN

CDN is link within the \<link\> tag.It is way to add a link to some other resource on the internet inside the html page

If we just add the CSS CDN then all the default styles will apply to the html. That is little bit nice styles. It makes page pretty good.

let's use bootstrap by adding classes to the tags.
see layouts->container, and also we can search for anything we want margin, image, text center etc...

## Dynamic Data on Webpage.
It is not a good thing to list all the jobs in directly Html file, because every time we want to add a job we will have to go in html file and change something that thing we also need to do when we want to remove job, Making changes inside an Html file can be tricky.
Often we done like, Data is stored somewhere else in database where admin can directly create jobs and, information fetch from the database and entered into html and display to the screen.

we will not create database but, we'll do something similar to that.
we create a python list job who stores inforamtion related to jobs

after creating job some how we need to send that information in home.html. The way to do it is by providing arguments to render template.

come back to home2.html their we will use some special syntax that is not html,python it is the syntax of jinja2 template engine. It is the way to insert dynamic data into html.

That's we can add dynamically data to the html. that's why these are called template these are not shown always be in same way because if it is like that then we need to create a buch of file for every page that you want to showw. The templates were using certain information using this {{}} tags

the troble is we don't want to show the data in dictionary format we want a readble format as we see in 
https://excalidraw.com/#json=rGB215Ka1I0dbWhLxaJKn,xCinmKb3TucX4FQk9ht72w

solution :-
Template support some special syntax as well. we actually use a for loop inside {{}} template .

visit the home2.html then home3.html

We can add limited amount of content inside \<p\> tag if the content is coming by using template engine.
that's why we generally uses a \<div\> tag to  put content inside it.

if there is no salary for certain job then how can we handle it ? 
Just like "for" we have "if".
After adding if-statement in html(jinja template). if no-salary then it doesn't show salary.
In this type of case, we must handle the error using the if-statement otherwise the template engine will do some unexpected thing.



Another thing,
If we want to show the job details on ther page also then "cut" everything  inside the for create a new layout(html document) inside the 'templates' folder. 
- job_item.html
Put all the code of "for" block in job_item.html

Then comeback to the "home3.html" and instead of having all those code we use include the template using the template engine


```python
{% for job in jobs %}
  {% include "job_item.html"%}
{% endfor %}
```
By this code what we're telling flask is,
- inside the for-loop each time with the different value of "job" include the template job_item.html and pass the variable that are availaibale to the variable "job" so that they can be accessible inside the job_item.html template
- This how we can reuse a template, extract reuseable components out of the templates and render nice template.



Let's add border-bottom and Apply button
- for button we create "columns" using bootstrap. 1st column have job list and 2nd have Apply button
- We can make one big column and another will be small.  b.d. we have 12 columns in a row

```html
<div class="row">
  <div clas="col-9"></div>
  <div clas="col-3"></div>
</div>
```
12 column in each row. 9 col have by first div and 3 have by second one.
if set the column, beyond 12 then elements will be come in next line 



---> That is one way to return the dynamic data, one other way some website allow you to access some dynamic data is using an API.

## Dynamic data with API
instead of retuning html we can return JSON. -- JavaScript Object Notation

first we need to register this at route. 
- create route "/jobs"
- convert the jobs(i.e. list of dictionaries) --> JSON. For that we have a function jsonify it takes an object and convert into JSON  But for that we need to "from flask import json"

after that add an "/jobs" route run the server visit the /jobs and it will give the JSON data. when people say REST API, JSON API or API endpoint this what they mean The webserver returning some information not just as html, but in form of JSON. You can do whatever you want with the data.
Here the home page(html) shows that same JSON data in different format. The benifit of it is in JSON format data is, we can programically extract information. Analyze the data or modufy the data do whatever we want which we can not do if the data is present is only in html.

We need to convert it html-->JSON and it takes lots of time and effort.

#### Difference
render_template()    : creating an html endpoint<br/>
jsonify()            : creating an JSON endpoint

Often, just to differenciate the html page and non-html pages. we often tend to put /api in front of it and it becomes "/api/jobs".
API stands for Application Programming Interface. But what it really means just a url which doesn't return html to be shown in browser but it return some structured data in form of JSON, Which can then be programmatically analyzed

now, We created our first API route. 

Right now the information stored in "Jobs" variable. But it could be ver well be coming from a database. 
Enough bulding 
Let's Deploy the website on cloud.


## Deploy
It is already deployed in some sense it is on replit.
When you want to put it on production, you'll have to figure some cloud platform where you oing to deploy this.
one cloud platform that makes very easy to deploy python applications is render.com there are other cloud platfrom like AWS, heroku, Google cloud, asure etc... but render is very easy to work.

- Commit and push all the changes all the information sended back to github.
so we don't need to depend on replit
take the repository and go to https://render.com
create a free account

After creating an account it shows an dashboard 
new -> web services which means we're not just sending html normally. we're may also connecting to a database and getting some dynamic data, may be we have some api route something like that. 

new -> static site. It is just and html page you want to deploy no flask.

we'll create a web service. 

then github connect account this way we allow render.com to to pull your code. connect to github. 

---
# MK : i fork the website from the main account to 007 account also on that account i started deploying
---

give access to only the  "career-website" repository, back to web services page. reposisotry is connected click on connect.

configure the code :-
take the code which is on github and deploy it on the cloud using render we need to configure it.

first give name. for internal reference  : (career-website)

buld commad .

At startin we install flask. render.com doesn't know it need to install flask for render.com what we need to do. 
create a special file called "requirements.txt". It is standard file in python ecosystem. it doesn't actully needed by render.com. This file says in python project which all libararies it requires. it's a convention by devlopers to put that infromation in requirements.txt file.

add 'Flask' and 'gunicorn' library in requirement.txt

gunicorn is production server for python. remember for flask when we ran, it say that it is a devlopment server don't use it for production. so, when we want to put a flask app in production we need to use gunicorn library. It is  easy to use and exact same command every time.

commit changes

---
# Mk : resync the 007 account with main account
--- 

so, when render.com pull the code it's going to recieve requirement.txt and then it's going to run the bulit command
```powershell
pip install -r requirements.txt
```

We're just telling the pip using this command. look into the requirements.txt. and each line the name of library and please install the library for me.


When render pulls the code from the github everytime somthing chnages in repository render pulls the code and it's going to run "pip install -r requirements.txt" command..

To start server we're now going to use gunicorn. When gunicorn library is installed it also add commands for gunicorn this command needs to give the name of file that needs to be executed i.e. app.py. 
so, instead of doing "python app.py" we are running "gunicorn app.py"

python : for devlopment 
gunicorn : for production

so, "gunicorn app" instead of app.py we just only put "app" then not that we also need to specify the variable name which contains the flask application that we want to run app=Flask(\_\_name\_\_) so the command will be like "gunicorn app:app"

## Q. How can we find waht is "bulid command" and what is the "start command" ? 
Ans. search on google for "render.com deploy flask application". This is something that never learn by someone from it's birth. we can look it just few hours before deploying. It literally tells a example hello_world project.
That's literally from where we can learn all the things.

we need to learn this type of things specifically. we just need learn it when we need to connect with a specific platfrom. we need to look how to do it. that is often in the documentation.

if we're deploying on platform like heroku then this wil be slightly different. for another platform it's slightly different. all that matters is figure out how to make it work.

put all that information and select the paln(free paln). click on create web service
It's bulding....
It takes time don't worry about it. just because it's free. if we have paid plan then it deploy faster


## After deploy
when it deployed it shows ✔️Live
It provides an url. Once it is setup on the server and that server is poinsted to that url we'll able to access it. 
How is going to be run the actual server it's gonna be run the actual server using "gunicon app2:app".

copy the url and open in new tab
and that's it that is our website deployed on render.com

But url still looks ugly. we'll talk about later 

Before that goto app2.py change the salary of backend engineer
commit changes and push 
# MK : sync 007 account to main account 

goto deployed site 