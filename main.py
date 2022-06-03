from flask import Flask, request, Response, send_file
from werkzeug.utils import secure_filename
from Preprocessor import ElementMaker
from HtmlGenerator import HtmlPage

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    pic = request.files['pic']
    if not pic:
        return 'No pic uploaded!', 400
    filename = secure_filename(pic.filename)

    pic.save('upload/'+filename)

    title = request.form.get("title-0")
    # isFormBool = request.form.get("form-0")
    theme = request.form.get("theme-0")
    # if str(isFormBool) == 'on':
    #     isForm =  True
    # else:
    #     isForm = False 
    
    # return str(isForm)
    
    elements = ElementMaker(img_path = 'upload/'+filename)
    htmlpage = HtmlPage(title,True,elements,theme)
    htmlpage.gridInit()
    htmlpage.generate()
    
    result_path = 'output/' + title +'.html'

    return send_file(result_path)

if __name__ == "__main__":
    app.run(debug = True)