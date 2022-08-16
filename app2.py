from jinja2 import Template


janapith_data = [{"year":2021,"awardees":"Krishna Gautam","language":"Hindi"},{"year":2022,"awardees":"Ritik Goyal","language":"Oria"},{"year":2015,"awardees":"Rajat Mishra","language":"English"}]
def main():
    #read the template file
    template_file = open("template.html.jinja2",'r')
    TEMPLATE = template_file.read()
    template_file.close() #closing the file

    template = Template(TEMPLATE)
    content = template.render(janapith_data=janapith_data)
    myfile = open("janapith.html",'w')
    myfile.write(content)
    myfile.close()

if __name__ == '__main__':
    main()