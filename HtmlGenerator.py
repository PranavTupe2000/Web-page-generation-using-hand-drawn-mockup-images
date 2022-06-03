#  Import
# from black import out
from jinja2 import Environment, FileSystemLoader, Template
from matplotlib.pyplot import title
from Tokens import tokens
import os

# Load Environment
file_loader = FileSystemLoader(searchpath="./")
env = Environment(loader=file_loader)
template = env.get_template('template.html')

# output = template.render(title="Hello World", main="Jinja is Awesome")
# print(output)

# Main Class which contains all the layout information of HTML Page 
# and the main algorithm of HTML Page Generation
# Here elements = [{elementClass,associatedText,grid,X,Y,width,height}]

class HtmlPage:
    def __init__(self,title,isForm,elements,theme):
        self.title=title
        self.isForm=isForm
        self.elements=elements
        self.theme=theme
        self.grid = [[[] for j in range(4)] for i in range(9)]
        


        
    def gridInit(self):
        count = 0 
        for i in self.elements:
            xp = i['x']
            yp = i['y']
            x_list = [j1 - xp if j1 > xp else 999 for j1 in [300,600,900,1200]]
            y_list = [j2 - yp if j2 > yp else 1999 for j2 in [100,200,300,400,500,600,700,800,900]]
            # y_list = [j2 - yp if j2 > yp else 1999 for j2 in [150,300,450,600,750,900]]
            grid_x = x_list.index(min(x_list))
            grid_y = y_list.index(min(y_list))
            self.elements[count]['grid'] =  (grid_y,grid_x)
            self.grid[grid_y][grid_x].append(i) 
            count += 1
    
    def generate(self):
        main = ''
        output = template.render(title=self.title, main='{{ main }}')
        template1 = Template(output)
        for i in self.grid[0][0]:
            if 'header' == i['class']:
                # print('header')
                output = template1.render(main=tokens['header'].replace('{{ text }}', i['associated_text']).replace('{{ theme }}',self.theme))
                template1 = Template(output)
                self.grid[0][0].remove(i)
                break
        
        output = template1.render(title="Hello World", main=tokens['container'])
        template1 = Template(output)
        
        # sub-Algo1
        # for i in self.grid:
        #     main += tokens['row']
        #     for j in i:
        #         main = main.replace('{{ main }}',tokens['col'])
        #         # for k in [k1 for k1 in j if k1 !=[] ]:
        #         for k in j:
        #             main = main.replace('{{ main }}',tokens[k['class']].replace('{{ text }}', k['associated_text'],1))

        #         main = main.replace('{{ main }}','').replace('{{ next }}','{{ main }}',1)
            
        #     main = main.replace('{{ main }}','').replace('{{ next }}','{{ main }}',1)
        
        # sub-Algo2
        for i in self.grid:
            ch = len([ch1 for ch1 in i if ch1!=[]])
            # print(ch)
            if ch:
                main += '\t<div class="row">\n'
            for j in i:
                if j!=[]:
                    main +=  '\t\t<div class="col">\n'

                for k in j:
                    main += '\t\t\t'+tokens[k['class']].replace('{{ text }}', k['associated_text']).replace('{{ main }}','\n')
                    if k['class'] == 'Button':
                        main = main.replace('{{ theme }}',self.theme)
                if j!=[]:
                    main += '\t\t</div>\n'
            if ch:
                main += '\t</div>\n'
            
            # main = main.replace('{{ main }}','').replace('{{ next }}','{{ main }}',1)
        
        output = template1.render(main = main)
        # print(output)
        with open('output/'+self.title+'.html', 'w') as file:
            file.write(output)
        



if __name__ == '__main__':
    test_element = [
        {'class':'header','associated_text':'Shipping Info','x':104,'y':2,'width':1085,'height':21},
        
        {'class':'Textbox','associated_text':'First Name','x':117,'y':215,'width':449,'height':66},
        {'class':'Textbox','associated_text':'Last Name','x':602,'y':215,'width':574,'height':60},
        {'class':'Textbox','associated_text':'Phone','x':128,'y':377,'width':440,'height':66},
        {'class':'Textbox','associated_text':'E-mail','x':609,'y':381,'width':564,'height':74},
        {'class':'Button','associated_text':'Back','x':113,'y':791,'width':506,'height':94},
        {'class':'Button','associated_text':'Next Step','x':638,'y':789,'width':494,'height':94},
        
        # ['textbox','First Name',117,215,449,66],
        # ['textbox','Last Name',602,215,574,60],
        # ['textbox','Phone',128,377,440,66],
        # ['textbox','E-mail',609,381,564,74],
        # ['button','Back',113,791,506,94],
        # ['button','Next Step',638,789,494,94],
    ]
    test = HtmlPage("Shipping Info",True,test_element,'danger')
    test.gridInit()
    # print(test.elements)
    # print(test.grid)
    test.generate()
    
    
    
        