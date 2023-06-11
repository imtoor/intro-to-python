names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# create usernames
for i in range(len(names)):
    usernames.append(names[i].replace(" ", "_"))

print(usernames)

# modify usernames with range
for i in range(len(usernames)):
    usernames[i] = usernames[i].lower().replace(" ", "_")

print(usernames)

# tag counter
tokens = ['<bookstore>', '<book category="children">', '<title>Harry Potter</title>', '<author>J K. Rowling</author>', '<year>2005</year>', '<price>29.99</price>', '</book>', '<book category="web">', '<title>Learning XML</title>', '<author>Erik T. Ray</author>', '<year>2003</year>', '<price>39.95</price>', '</book>', '</bookstore>']

count = 0

for token in tokens:
    for i in range(len(token)):
        if token[i] == "<" and token[-1] == ">":
            count += 1

print("XML Tags found are {}".format(count))

# create an HTML List
html_str = []
items = ["reynaldi", "rahmat"]

html_str.append("<ul>")
for item in items:
    # html_str.append("<li>" + item.title() + "</li>")
    html_str.append("<li>{}</li>".format(item.title()))
html_str.append("</ul>")

for li in html_str:
    print(li)