#! /Users/fredkingham/.virtualenvs/fredkingham_flask_blog/bin/python
from flask import Flask, render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer
import sys
from urlparse import urljoin
from werkzeug.contrib.atom import AtomFeed
from jinja2.filters import do_mark_safe

DEBUG = False
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
app = Flask(__name__)     
freezer = Freezer(app)
rss_route = '/recent.atom'
root_name = 'http://fredkingham.com'
 

def get_articles():
    articles = (p for p in pages if 'published' in p.meta)
    return sorted(articles, reverse=True, key=lambda p: p.meta['published'])

@app.route('/')
def post_list():
    posts = get_articles()
    generic_discussion = pages.get("generic_discussion").meta["generic_discussion"]
    return render_template('contents_page.html', posts=posts, generic_discussion=generic_discussion)
 
@app.route('/blog/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    return render_template('blog_post.html', page=page)
 
@app.route(rss_route)
def recent_feed():
    feed = AtomFeed('recent articles', feed_url="%s/%s" %(root_name, rss_route), url=root_name)
    articles = get_articles()
    for article in articles:
        post = unicode(do_mark_safe(article.meta["title"] + article.meta["tease"] + article.html))

        feed.add(article.meta["title"], post,
                 content_type='html',
                 author='fredkingham',
                 url= "%s/blog/%s" % (root_name, article.path),
                 updated=article.meta["published"],
                 published=article.meta["updated"])
    return feed.get_response()

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(port=8000, debug=True)





