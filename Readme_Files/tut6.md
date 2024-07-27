## Add some Functionals & Asthetic Improvements
## To make the site working
- First add navbar using Bootstrap
  - put it into a file called nav.html and include it in home2.html as jinja2 template
  - add shadow, make it sticky using "fixed-top"
  - problem : navbar hides the heading h1 of home3 page.
    - solution : put \<div style="height : 56px">\</div>
- add footer
- make the site responsive using bootstrap classes like md(medium devices)
- The "Apply" button don't quite work right now because we don't implement 2nd page
  - we can do a quick trick here, by click on Apply button we can chnage the button to anchor tag and add the "href" attribute. so, when we click on that it will open google.com That thing we need to do in job_item.html

--> The links like "http" and "https" that open in the browser 
but there is one special type of link called "mailto" links

[For reference](https://css-tricks.com/snippets/html/mailto-links/)


```html
<a href="mailto:hello@mymail.ai?subject=Application for {{job['title']}} " type="button" class="btn btn-outline-primary float-right align-middle">
```

make anchot tag like this
when we click on "Apply" it will open the mail application.


--> we can generate "mailto:<email addreess\>" for 'href' attribute of 'a' using [mailto](https://mailtolink.me/) 

same thing we do with contact us button
we update the links of footer also(if we want)

Our website is fully responsive, mobile friendly.