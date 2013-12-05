title: Static html vs Django
published: 2013-11-17T15:37:43Z
updated: 2013-11-17T15:37:43Z
tease: |
        How does static html served by apache perform against a simple Django memcached app?

##### Short answer, twice as fast.

I recently moved this site from Django to [frozen flask]("https://github.com/SimonSapin/Frozen-Flask"). Django is fantastic but for a little blog seemed a little over powered for what I needed.

##### Moving to a static site does limit functionality.

* It meant giving up on comments but they're rarely informative. Outsourcing them to HN news or the similar where voting functionality tries to promote the useful comments is much more useful. I could always bring in Disqus or another piece of commenting software if necessary.

* All new blog posts now require a migration. I can't add new posts through a web interface. However moving to flask flat pages mean I'm able to keep my posts versioned via git which more than makes up for it.

* On the other hand it should be significantly faster and scale absurdly easily via ELB. To be honest, I thought it would be even faster than it actually was.


##### Caveats

* Varnish would probably be even faster, this is a limited comparison

* Django is not stripped down, I kept admin and session middleware is enabled for example because if you're hosting on Django you want the advantage of being able to post blogs straight from the admin if necessary.

* Both tests were run against an apache server m1 medium amazon instances.

* The Django went from a virgin state, with no precaching.


### Results
Blitz.io made the basic load testing easy. The below averages are when the server was under a lot of strain. Under light traffic Django was returning at 0.9ms while static pages were being saved at 0.5ms.

<div class="row">
<div class="col-md-6">
<h5>Django and Memcache</h5>
<h1>235 MS</h1>
<p class="small">Average Response Time</a>
<a href="https://www.blitz.io/report/14700fa0c283368a02ee6b23dc636000">details</a>
</div>
<div class="col-md-6">
<h5>Flat Files</h5>
<h1>118 MS</h1>
<p class="small">Average Response Time</a>
<a href="https://www.blitz.io/report/14700fa0c283368a02ee6b23dca5e007">details</a>
</div>
</div>

<h3>Conclusion</h3>
Django stands up very well but static files are still twice as fast.