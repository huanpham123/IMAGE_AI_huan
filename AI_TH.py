from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

# Lấy URL API từ biến môi trường hoặc sử dụng giá trị mặc định
api_url = os.getenv("AI_API_URL", "https://api.hamanhhung.site/ai/text2image")

@app.route("/", methods=["GET", "POST"])
def index():
    image_url = None
    error_message = None  # Biến để lưu thông báo lỗi
    if request.method == "POST":
        prompt = request.form.get("prompt")
        
        try:
            # Giảm thời gian chờ xuống dưới 10 giây
            response = requests.get(f"{api_url}?prompt={prompt}", timeout=100)  # Thay đổi timeout xuống 5 giây
            if response.status_code == 200:
                data = response.json()
                image_url = data.get("url")
            else:
                error_message = "Không thể tạo hình ảnh, vui lòng thử lại sau."
        except requests.Timeout:
            error_message = "Yêu cầu đã hết thời gian chờ. Vui lòng thử lại."
        except Exception as e:
            error_message = f"Đã xảy ra lỗi: {e}"  # Lưu thông báo lỗi
    
    return render_template("AI_TH.html", image_url=image_url, error_message=error_message)

if __name__ == "__main__":
    app.run(debug=True)
