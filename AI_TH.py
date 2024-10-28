from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Dictionnary để lưu cache
image_cache = {}

@app.route("/", methods=["GET", "POST"])
def index():
    image_url = None
    if request.method == "POST":
        prompt = request.form.get("prompt")

        # Kiểm tra cache
        if prompt in image_cache:
            image_url = image_cache[prompt]
        else:
            api_url = f"https://api.hamanhhung.site/ai/text2image?prompt={prompt}"
            try:
                response = requests.get(api_url, timeout=30)
                if response.status_code == 200:
                    data = response.json()
                    image_url = data.get("url")
                    # Lưu vào cache
                    image_cache[prompt] = image_url
                else:
                    image_url = None
            except Exception as e:
                print(f"Error: {e}")
                image_url = None
    
    return render_template("AI_TH.html", image_url=image_url)

if __name__ == "__main__":
    app.run(debug=True)
