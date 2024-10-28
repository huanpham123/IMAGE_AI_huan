from flask import Flask, render_template, request, jsonify
import requests
import os  # Nhập thư viện os

app = Flask(__name__)

# Lấy URL API từ biến môi trường hoặc sử dụng giá trị mặc định
api_url = os.getenv("AI_API_URL", "https://api.hamanhhung.site/ai/text2image")

@app.route("/", methods=["GET", "POST"])
def index():
    image_url = None
    error_message = None  # Biến để lưu thông báo lỗi
    if request.method == "POST":
        prompt = request.form.get("prompt")
        # Sử dụng api_url đã lấy từ biến môi trường

        try:
            # Thay đổi timeout về 10 giây
            response = requests.get(f"{api_url}?prompt={prompt}", timeout=10)
            if response.status_code == 200:
                data = response.json()
                image_url = data.get("url")
            else:
                error_message = "Không thể tạo hình ảnh, vui lòng thử lại sau."
        except Exception as e:
            error_message = f"Đã xảy ra lỗi: {e}"  # Lưu thông báo lỗi
    
    return render_template("AI_TH.html", image_url=image_url, error_message=error_message)

if __name__ == "__main__":
    app.run(debug=True)
