title: The pitfalls of using Sammy.js and Knockout.js
tease: >
        A lot of people coming to Knockout probably did the [excellent tutorial application](http://learn.knockoutjs.com/). The tutorial takes a user nicely through a gmail style application complete with html5 history routing via Sammy. This is all fine for a simple application. Sammy has a very nice simple api for dealing with routing. In the real world the Sammy is not just a routing library but much more, including the vital dom rendering that knockout specialises in.
published: 2013-09-23T03:18:05Z
updated: 2013-09-23T03:18:05Z


As knockout and Sammy both do dom rendering, they use the same event hooks. This can be seen in action of form submission [here](https://github.com/fredkingham/Sammy-knockout-conflict)


There are always work arounds. A colleague just used the click event rather than the submit event. In theory this 
is bad practice as there are other ways to submit a form. 


##### Method 1: pressing enter in a text box.

However the majority of browsers, at time of writing Chrome, firefox and safari (versions 29.0.1547.76, 24.0 and 6.0.5 respectively),  will fire the click event even if you're pressing enter. Also this is allowed for but not required by the [html5 specs](http://dev.w3.org/html5/spec-preview/constraints.html#implicit-submission"). So we could just use the click event and accept it may not work on some browsers. 


##### Method 2: submitting the event programmatically


As we're using knockout we would probably just call the knockout event independently, however any jquery plugins or other third party tools would not fire e.g. [jsfiddle](http://jsfiddle.net/MkrRu/8/)

In conclusion, Sammy and knockout can work together but not smoothly. My recommendation is either roll your own with the excellent history.js, or another routing framework such as pager.js which has been specifically designed for knockout
