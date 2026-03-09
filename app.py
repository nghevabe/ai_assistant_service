import os
from flask import Flask, request, jsonify
from openai import OpenAI

from handle_result import content_parsing
from prompt_util import prompt_with_img

app = Flask(__name__)

# Khuyến nghị đọc API key từ biến môi trường
client = OpenAI(api_key="key")

# MODEL_NAME = "gpt-4.1-mini"
MODEL_NAME = "gpt-4.1"


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok",
        "message": "Flask API is running"
    }), 200


@app.route("/analyze-message", methods=["POST"])
def analyze_message():
    try:
        data = request.get_json(silent=True) or {}

        # Input từ client
        user_text = data.get("text", "")
        image_url = data.get("image_url", "")

        # Ví dụ thêm metadata nếu bạn muốn custom prompt
        user_gender = data.get("user_gender", "Nam")
        partner_gender = data.get("partner_gender", "Nữ")

        if not user_text and not image_url:
            return jsonify({
                "error": "Bạn cần truyền ít nhất 'text' hoặc 'image_url'."
            }), 400

        prompt = prompt_with_img(
            my_gender=user_gender,
            partner_gender=partner_gender,
        )

        content = [{"type": "input_text", "text": prompt}]

        if image_url:
            content.append({
                "type": "input_image",
                "image_url": image_url
            })

        response = client.responses.create(
            model=MODEL_NAME,
            input=[
                {
                    "role": "user",
                    "content": content
                }
            ]
        )

        analyze_content, mes1_content, mes2_content, mes3_content = content_parsing(response.output_text)

        return jsonify({
            "success": True,
            "model": MODEL_NAME,
            "result": response.output_text,
            "analyze_content": analyze_content,
            "message_content_1": mes1_content,
            "message_content_2": mes2_content,
            "message_content_3": mes3_content,
        }), 200

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)