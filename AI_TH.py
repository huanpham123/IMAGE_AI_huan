from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    image_url = None
    if request.method == "POST":
        prompt = request.form.get("prompt")
        api_url = f"https://api.hamanhhung.site/ai/text2image?prompt={prompt}"
        
        try:
            # Thêm timeout là 10 giây
            response = requests.get(api_url, timeout=10)
            if response.status_code == 200:
                data = response.json()
                image_url = data.get("url")
            else:
                image_url = None
        except Exception as e:
            print(f"Error: {e}")  # In ra lỗi để kiểm tra nếu có
            image_url = None
    
    return render_template("AI_TH.html", image_url=image_url)

if __name__ == "__main__":
    app.run(debug=True)
