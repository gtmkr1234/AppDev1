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
                <tr>
                    <td>{{ janapith_data["year"] }}</td>
                    <td>{{ janapith_data["awardees"] }}</td>
                    <td>{{ janapith_data["language"] }}</td>
                </tr>
            </tbody>
        </table>
    </div>
    
</body>
</html>'''

janapith_data = {"year":2021,"awardees":"Krishna Gautam","language":"Hindi"}

def main():
    template = Template(TEMPLATE)
    print(template.render(janapith_data=janapith_data))

if __name__ == '__main__':
    main()