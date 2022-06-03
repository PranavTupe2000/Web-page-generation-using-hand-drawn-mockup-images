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
    
    elements = ElementMaker('upload/'+filename,'GUI test','success')
    htmlpage = HtmlPage("Hello",True,elements,'primary')
    htmlpage.gridInit()
    htmlpage.generate()
    
    result_path = 'output/' + 'Hello.html'

    return send_file(result_path)

if __name__ == "__main__":
    app.run(debug = True)