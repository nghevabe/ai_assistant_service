import os
from flask import Flask, request, jsonify, render_template
from openai import OpenAI

from handle_result import content_parsing_text, content_parsing_img
from prompt_util import prompt_with_img, prompt_with_text

app = Flask(__name__)

# Khuyến nghị đọc API key từ biến môi trường
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# MODEL_NAME = "gpt-4.1-mini"
# model_config = "gpt-5-mini"
MODEL_NAME = "gpt-4.1"

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

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

        user_text = (data.get("text") or "").strip()
        image_url = (data.get("image_url") or "").strip()
        user_gender = (data.get("user_gender") or "Nam").strip()
        partner_gender = (data.get("partner_gender") or "Nữ").strip()
        language = (data.get("language") or "English").strip()

        allowed_languages = {"en", "vi"}
        if language not in allowed_languages:
            language = "English"

        if not user_text and not image_url:
            return jsonify({
                "success": False,
                "error": "Bạn cần truyền ít nhất 'text' hoặc 'image_url'."
            }), 400

        is_image_mode = bool(image_url)

        if is_image_mode:
            prompt = prompt_with_img(
                text_input=user_text,
                my_gender=user_gender,
                partner_gender=partner_gender,
                language=language,
            )
            content = [
                {"type": "input_text", "text": prompt},
                {"type": "input_image", "image_url": image_url},
            ]
            parser_func = content_parsing_img
        else:
            prompt = prompt_with_text(
                my_gender=user_gender,
                partner_gender=partner_gender,
                text_input=user_text,
                language=language,
            )
            content = [
                {"type": "input_text", "text": prompt},
            ]
            parser_func = content_parsing_text

        response = client.responses.create(
            model=MODEL_NAME,
            input=[
                {
                    "role": "user",
                    "content": content,
                }
            ]
        )

        output_text = response.output_text or ""

        analyze_content, mes1_content, mes2_content, mes3_content = parser_func(output_text)

        return jsonify({
            "success": True,
            "model": MODEL_NAME,
            "input_type": "image" if is_image_mode else "text",
            "language": language,
            "result": output_text,
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
