from jinja2 import Template

TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Jnanipith Award</title>
</head>
<body>
    <div id="Intro">
    <h1>Bharatiya Janta Party</h1>
    Bharatiya Jnanpith is a literary organization based in Delhi. It also presents highest literary awards in India.
    </div>
    <div id="main">
        <h1>Awardees</h1>
        <table>
            <thead>
                <tr>
                    <th>Yaer</th>
                    <th>Awardees</th>
                    <th>Language</th>
                </tr>
            </thead>
            <tbody>
            {% for janapith in janapith_data %}
                <tr>
                    <td>{{ janapith["year"] }}</td>
                    <td>{{ janapith["awardees"] }}</td>
                    <td>{{ janapith["language"] }}</td>
                </tr>
            {% endfor %}
            </tbody>
        </table>
    </div>
    
</body>
</html>'''

janapith_data = [{"year":2021,"awardees":"Krishna Gautam","language":"Hindi"},{"year":2022,"awardees":"Ritik Goyal","language":"Oria"},{"year":2015,"awardees":"Rajat Mishra","language":"English"}]
def main():
    template = Template(TEMPLATE)
    content = template.render(janapith_data=janapith_data)
    myfile = open("janapith.html",'w')
    myfile.write(content)
    myfile.close()

if __name__ == '__main__':
    main()