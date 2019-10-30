import mistune
import requests

markdownurl = 'https://raw.githubusercontent.com/lowell-dev-club/python-text-game/master/workshop.md'
r = requests.get(markdownurl, allow_redirects=True)

markdownData = str(r.content)

markdownLines = markdownData.split('\\n')
lenToCheck = len(markdownLines) - 1

markdown = mistune.Markdown()
f = open("templates/workshop2_test.html","w+")
f.write('''
{% extends 'base.html' %}

{% block title %}
Lowell Dev Club Workshop 2
{% endblock %}

{% block head_css %}
  <link rel="stylesheet" href="../../static/css/navbar.min.css">
  <link rel="stylesheet" href="../../static/css/footer.min.css">
  <link rel="stylesheet" href="../../static/css/markdown.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
  <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css" integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
{% endblock %}

{% block content %}
  <div class="body-wrapper">
    <nav class="navbar">
    <a href="/" class="navbar-text" id="test"><img src="../../static/img/logo-transparent.png"></a>
      <div class="navbar-right">
        <a href="/workshop/old" class="navbar-text">Workshop</a>
        <a href="/about" class="navbar-text">About</a>
        <a href="/partners" class="navbar-text">Partners</a>
        <!--<a href="/sponsors" class="navbar-text">Sponsors</a>-->
      </div>
      <div style="clear:both"></div>
    </nav>
    <div class="container rounded">
        ''')
for count in range(len(markdownLines)):
    if count == 0:
        firstLine = markdownLines[count]
        editied = firstLine[2:]
        f.write(markdown(editied))
    elif count != lenToCheck:
        f.write(markdown(markdownLines[count]))
f.write('''
    </div>
  </div>
  </div>
  {% endblock %}

{% block trailing_js %}
  <script type="text/javascript" src="../../static/js/home.js"></script>
{% endblock %}
	    ''')