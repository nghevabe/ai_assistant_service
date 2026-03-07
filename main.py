from openai import OpenAI

model_config = "gpt-4o-mini"
user_config = "user"
open_api_key = "key"

client = OpenAI(api_key=open_api_key)

promt = """
Hãy đóng vai trò là 1 nhà tư vấn tình cảm và giúp tôi phân tích tin nhắn của đối phương cho tôi.
-	Giới tính của tôi: Nam
-	Giới tính đối phương: Nữ
-	Nội dung tin nhắn: “Em chúc anh có 1 chuyến đi chơi vui vẻ”
Hãy phân tích nội dung và ý nghĩa của tin nhắn trên và đưa ra cho tôi 3 tin nhắn phản hồi phù hợp. Cấu trúc đầu ra tôi cần đúng theo định dạng như sau:
-	Nội dung phân tích: #analys_start#content analys here#analys_end#
-	Tin nhắn số 1:  #mes1_start#content mes1 here# mes1_end #
-	Tin nhắn số 2:  #mes2_start#content mes2 here# mes2_end #
-	Tin nhắn số 3:  #mes3_start#content mes3 here# mes3_end #
"""

response = client.responses.create(
    model="gpt-4.1-mini",
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": promt},
                # {
                #     "type": "input_image",
                #     "image_url": "https://your-firebase-storage-url"
                # }
            ]
        }
    ]
)

print(response.output_text)
