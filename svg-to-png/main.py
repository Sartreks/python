from flask import Flask ,url_for ,redirect ,render_template ,request
app = Flask(__name__)
import pyrebase
from firebase import Firebase

@app.route("/upload", methods=["POST","GET"])
def upload_image():
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            print(image)
            return redirect(request.url) 
    return render_template("upload_image.html")
   

## get the url in post body and download the image 
## convert image to png 
## upload the image to storage 
## return ajson with new image url 
    
if __name__ == "__main__":
    app.run(debug=True)


