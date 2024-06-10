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