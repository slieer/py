from markupsafe import Markup, escape

# escape replaces special characters and wraps in Markup
escape("<script>alert(document.cookie);</script>")
Markup('&lt;script&gt;alert(document.cookie);&lt;/script&gt;')

# wrap in Markup to mark text "safe" and prevent escaping
Markup("<strong>Hello</strong>")
Markup('<strong>hello</strong>')

escape(Markup("<strong>Hello</strong>"))
Markup('<strong>hello</strong>')

# Markup is a str subclass
# methods and operators escape their arguments
template = Markup("Hello <em>{name}</em>")
template.format(name='"World"')
Markup('Hello <em>&#34;World&#34;</em>')
