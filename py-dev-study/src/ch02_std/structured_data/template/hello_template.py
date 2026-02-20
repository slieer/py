'''
Created on Jul 20, 2015

@author: dev
'''
from jinja2 import Template
from jinja2 import Environment, PackageLoader 

def test():
    template = Template('Hello {{ name }}!') 
    print(template.render(name='World')) 
    
def test1():
    
    template = """
<html>
<head>
    <title>My Webpage</title>
</head>
<body>
    <ul id="navigation">
    {% for item in navigation %}
        <li><a href="{{ item.href }}">{{ item.caption }}</a></li>
    {% endfor %}
    </ul>

    <h1>My Webpage</h1>
    {{ a_variable }}
</body>
</html>
"""    
    print(template.render(a_variable='World', navigation=[{'t' : 'test'}, {'b' : 'bee'}]))
    
    
test1()     
