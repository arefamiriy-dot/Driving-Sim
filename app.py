from flask import Flask, request, jsonify
from flask_cors import CORS
from speed_model import get_speed  # حتماً این فایل در همان فولدر backend باشد

# ایجاد اپلیکیشن Flask
app = Flask(__name__)

# فعال کردن CORS برای اجازه به همه منابع
CORS(app, resources={r"/*": {"origins": "*"}})

# مسیر API برای محاسبه سرعت و سایر مقادیر
@app.route("/calculate", methods=["POST"])
def calculate():
    try:
        data = request.json
        dist = float(data.get("distance", 10))   # مقدار پیشفرض 10 km
        urg = int(data.get("urgency", 5))        # مقدار پیشفرض 5 از 10

        # فراخوانی تابع محاسبه سرعت از speed_model
        res = get_speed(dist, urg)
        res["success"] = True

        return jsonify(res)
    except Exception as e:
        # در صورت خطا، پیام خطا را بازگرداند
        return jsonify({"success": False, "error": str(e)}), 400

# اجرای سرور Flask
if __name__ == "__main__":
    app.run(debug=True)
