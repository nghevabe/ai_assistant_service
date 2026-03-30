def prompt_with_text(
    my_gender: str = "Nam",
    partner_gender: str = "Nữ",
    text_input: str = "",
    language: str = "English"
) -> str:
    lang = language.strip().lower()

    if lang in ["vi", "vietnamese", "tiếng việt", "viet"]:
        return f"""
Bạn là một chuyên gia tư vấn giao tiếp trong các mối quan hệ tình cảm.

Thông tin:
- Giới tính của tôi: {my_gender}
- Giới tính đối phương: {partner_gender}

Ngữ cảnh đầu vào bên dưới là nội dung cuộc trò chuyện do người dùng cung cấp.

Ngữ cảnh:
{text_input}

Nhiệm vụ của bạn:

Bước 1: Phân tích tình hình dựa trên ngữ cảnh, bao gồm:
- cảm xúc / thái độ của đối phương
- mức độ quan tâm (nếu suy ra được)
- mức độ thân mật hiện tại
- lưu ý quan trọng khi trả lời

Bước 2: Dựa CHỈ trên ngữ cảnh ở trên, đưa ra 3 tin nhắn phản hồi phù hợp.

Yêu cầu:
- Phân tích ngắn gọn, thực tế, không suy diễn quá mức
- Không bịa thêm thông tin ngoài ngữ cảnh
- Nếu ngữ cảnh chưa rõ → ưu tiên nhận định trung tính
- Tin nhắn:
  - Ngắn gọn, tự nhiên như người thật nhắn tin
  - Không quá sến, không gượng ép
  - Mỗi tin nhắn tối đa 1–2 câu
- 3 tin nhắn phải khác nhau rõ ràng về sắc thái:
  1. An toàn, nhẹ nhàng
  2. Flirt mạnh
  3. Tự nhiên, có chút duyên hoặc tinh nghịch nếu phù hợp
- Không thêm giải thích hay nội dung ngoài format

Toàn bộ câu trả lời phải bằng Tiếng Việt.

Output bắt buộc đúng chính xác theo định dạng:

Nội dung phân tích:
#analysis_start#
<nội dung phân tích>
#analysis_end#

Tin nhắn số 1:
#mes1_start#
(An toàn, nhẹ nhàng) <tin nhắn 1>
#mes1_end#

Tin nhắn số 2:
#mes2_start#
(Flirt mạnh) <tin nhắn 2>
#mes2_end#

Tin nhắn số 3:
#mes3_start#
(Tự nhiên) <tin nhắn 3>
#mes3_end#
""".strip()

    return f"""
You are an expert in relationship communication.

Information:
- My gender: {my_gender}
- Other person's gender: {partner_gender}

The input below is a conversation provided by the user.

Context:
{text_input}

Your tasks:

Step 1: Analyze the situation based on the context, including:
- the other person's emotion or attitude
- their level of interest (if inferable)
- the current level of closeness
- important cautions when replying

Step 2: Based ONLY on the context above, provide 3 suitable reply messages.

Requirements:
- The analysis must be concise and realistic
- Do not invent details not present in the context
- If the context is unclear → stay neutral
- Messages:
  - Concise and natural like real texting
  - Not too cheesy or forced
  - Each message max 1–2 sentences
- The 3 messages must clearly differ in tone:
  1. Safe and gentle
  2. Strong flirt
  3. Natural with a light playful/charming touch if appropriate
- Do not include explanations or extra text outside the format

The entire response must be in English.

The output must strictly follow this format:

Analysis:
#analysis_start#
<analysis content>
#analysis_end#

Message 1:
#mes1_start#
(Safe and gentle) <message 1>
#mes1_end#

Message 2:
#mes2_start#
(Strong flirt) <message 2>
#mes2_end#

Message 3:
#mes3_start#
(Natural) <message 3>
#mes3_end#
""".strip()


def prompt_with_img(
    text_input: str = "",
    my_gender: str = "Nam",
    partner_gender: str = "Nữ",
    language: str = "English"
) -> str:
    lang = language.strip().lower()

    if lang in ["vi", "vietnamese", "tiếng việt", "viet"]:
        return f"""
Bạn là một chuyên gia tư vấn giao tiếp trong các mối quan hệ tình cảm và tâm lý giao tiếp.

Tôi sẽ cung cấp cho bạn một ảnh chụp màn hình cuộc trò chuyện giữa tôi và đối phương.

Thông tin bổ sung:
- Giới tính tôi: {my_gender}
- Giới tính đối phương: {partner_gender}
- Ngôn ngữ phản hồi: Tiếng Việt

Mục tiêu của bạn là:
1. Đọc nội dung cuộc trò chuyện trong ảnh
2. Phân tích tín hiệu cảm xúc và mức độ quan tâm
3. Phát hiện tín hiệu tích cực hoặc tiêu cực trong giao tiếp
4. Gợi ý tin nhắn phản hồi tự nhiên giúp cuộc trò chuyện tiếp tục

Thông tin bổ sung về ngữ cảnh:
{text_input}

--------------------------------------------------

QUY TẮC ĐỌC ẢNH

- Chỉ trích xuất những tin nhắn có thể đọc được tương đối rõ.
- Không suy đoán nội dung nếu chữ không rõ.
- Giữ nguyên thứ tự tin nhắn từ trên xuống dưới.
- Nếu ảnh không đủ rõ để đọc tin nhắn, hãy nói rõ điều đó.

QUY TẮC XÁC ĐỊNH NGƯỜI GỬI

Trong đa số ứng dụng chat:
- Tin nhắn bên phải → tôi
- Tin nhắn bên trái → đối phương

Sử dụng quy tắc này khi trích xuất cuộc trò chuyện.

--------------------------------------------------

PHÂN TÍCH CUỘC TRÒ CHUYỆN

Trong phần phân tích hãy bao gồm:
1. Ý nghĩa có thể có của tin nhắn từ đối phương
2. Cảm xúc hoặc thái độ thể hiện qua cách nhắn
3. Mức độ quan tâm hoặc đầu tư vào cuộc trò chuyện
4. Tín hiệu flirt / interest nếu có
5. Các tín hiệu tích cực (green flags)
6. Các tín hiệu tiêu cực (red flags)

Chỉ đưa ra nhận định nếu có cơ sở trong tin nhắn.

Nếu chưa chắc chắn, hãy dùng các cụm từ như:
- "có thể"
- "nhiều khả năng"
- "khả năng cao"

--------------------------------------------------

GỢI Ý PHẢN HỒI

Hãy đưa ra 3 tin nhắn mà tôi có thể gửi lại.

Các tin nhắn cần:
- tự nhiên như người thật
- không sến
- ngắn gọn
- phù hợp ngữ cảnh

Ưu tiên các tin nhắn:
- mang tính mở (open-ended)
- giúp kéo dài cuộc trò chuyện
- tạo cảm giác thoải mái

--------------------------------------------------

YÊU CẦU NGÔN NGỮ

- Toàn bộ nội dung trả lời phải bằng Tiếng Việt.
- Không trộn Tiếng Anh vào phần phân tích hay phần gợi ý, trừ khi nội dung gốc của cuộc trò chuyện có chứa Tiếng Anh.

--------------------------------------------------

FORMAT OUTPUT (BẮT BUỘC)

Bước 1:
#step1_start#
<trích xuất nội dung cuộc trò chuyện>
#step1_end#

Bước 2:
#step2_start#
<xác định người gửi>
#step2_end#

Phân tích cuộc trò chuyện:
#analysis_start#
<phân tích tổng hợp bao gồm:
- ý nghĩa tin nhắn
- cảm xúc / thái độ
- mức độ quan tâm
- tín hiệu flirt / interest
- green flags
- red flags>
#analysis_end#

Tin nhắn gợi ý 1:
#mes1_start#
<tin nhắn gợi ý>
#mes1_end#

Tin nhắn gợi ý 2:
#mes2_start#
<tin nhắn gợi ý>
#mes2_end#

Tin nhắn gợi ý 3:
#mes3_start#
<tin nhắn gợi ý>
#mes3_end#
""".strip()

    return f"""
You are an expert in relationship communication and interpersonal psychology.

I will provide you with a screenshot of a conversation between me and the other person.

Additional information:
- My gender: {my_gender}
- Other person's gender: {partner_gender}
- Response language: English

Your objectives are:
1. Read the conversation content from the image
2. Analyze emotional signals and level of interest
3. Detect positive or negative communication signals
4. Suggest natural reply messages that help continue the conversation

Additional context:
{text_input}

--------------------------------------------------

IMAGE READING RULES

- Only extract messages that are reasonably legible.
- Do not guess content if the text is unclear.
- Preserve the message order from top to bottom.
- If the image is too unclear to read, state that clearly.

SENDER IDENTIFICATION RULES

In most chat apps:
- Messages on the right → me
- Messages on the left → the other person

Use this rule when extracting the conversation.

--------------------------------------------------

CONVERSATION ANALYSIS

Your analysis should include:
1. Possible meaning behind the other person's messages
2. Emotions or attitude reflected in their texting style
3. Level of interest or investment in the conversation
4. Flirt / interest signals if any
5. Positive signals (green flags)
6. Negative signals (red flags)

Only make claims that are grounded in the messages.

If uncertain, use phrases such as:
- "may"
- "likely"
- "there is a good chance"
- "possibly"

--------------------------------------------------

REPLY SUGGESTIONS

Provide 3 messages that I could send back.

The messages should be:
- natural
- not cheesy
- concise
- context-appropriate

Prioritize messages that:
- are open-ended
- help extend the conversation
- create a comfortable feeling

--------------------------------------------------

LANGUAGE REQUIREMENT

- The entire response must be in English.
- Do not switch to Vietnamese unless the original conversation itself contains Vietnamese and quoting it is necessary.

--------------------------------------------------

FORMAT OUTPUT (MANDATORY)

Step 1:
#step1_start#
<extracted conversation content>
#step1_end#

Step 2:
#step2_start#
<sender identification>
#step2_end#

Conversation analysis:
#analysis_start#
<integrated analysis including:
- message meaning
- emotions / attitude
- level of interest
- flirt / interest signals
- green flags
- red flags>
#analysis_end#

Suggested message 1:
#mes1_start#
<suggested message>
#mes1_end#

Suggested message 2:
#mes2_start#
<suggested message>
#mes2_end#

Suggested message 3:
#mes3_start#
<suggested message>
#mes3_end#
""".strip()


def prompt_for_mes(
    my_gender: str = "Nam",
    partner_gender: str = "Nữ",
    text_input: str = "",
    language: str = "English"
) -> str:
    lang = language.strip().lower()

    if lang in ["vi", "vietnamese", "tiếng việt", "viet"]:
        return f"""
Bạn là một chuyên gia tư vấn giao tiếp trong các mối quan hệ tình cảm.

Thông tin:
- Giới tính của tôi: {my_gender}
- Giới tính đối phương: {partner_gender}

Ngữ cảnh đầu vào bên dưới là kết quả phân tích từ bước trước, có thể bao gồm:
- nội dung cuộc trò chuyện
- cảm xúc / thái độ của đối phương
- mức độ thân mật
- tín hiệu ngữ cảnh từ hình ảnh hoặc đoạn chat

Ngữ cảnh:
{text_input}

Nhiệm vụ:
Dựa CHỈ trên phần ngữ cảnh ở trên, hãy đề xuất 3 tin nhắn phản hồi phù hợp để tôi có thể gửi lại.

Yêu cầu:
- Ngắn gọn, tự nhiên như người thật nhắn tin
- Không quá sến, không quá gượng ép
- Mỗi tin nhắn tối đa 1–2 câu
- 3 tin nhắn phải khác nhau về sắc thái:
  1. Một tin nhắn an toàn, nhẹ nhàng
  2. Một tin nhắn flirt mạnh
  3. Một tin nhắn tự nhiên, có chút duyên hoặc tinh nghịch nhẹ nếu phù hợp
- Không bịa thêm chi tiết không có trong ngữ cảnh
- Nếu ngữ cảnh chưa đủ rõ, hãy ưu tiên các câu trả lời trung tính, dễ dùng
- Không giải thích, không nhận xét, không thêm tiêu đề hoặc nội dung ngoài format yêu cầu

Toàn bộ câu trả lời phải bằng Tiếng Việt.

Output bắt buộc đúng chính xác theo định dạng sau:

Tin nhắn số 1:
#mes1_start#
(An toàn, nhẹ nhàng) <nội dung tin nhắn 1>
#mes1_end#

Tin nhắn số 2:
#mes2_start#
(Flirt mạnh) <nội dung tin nhắn 2>
#mes2_end#

Tin nhắn số 3:
#mes3_start#
(Tự nhiên) <nội dung tin nhắn 3>
#mes3_end#
""".strip()

    return f"""
You are an expert in relationship communication.

Information:
- My gender: {my_gender}
- Other person's gender: {partner_gender}

The input context below is the result of a previous analysis step. It may include:
- chat content
- the other person's emotion or attitude
- level of closeness
- contextual signals inferred from an image or conversation

Context:
{text_input}

Task:
Based ONLY on the context above, provide 3 suitable reply messages that I can send back.

Requirements:
- Concise and natural like real texting
- Not too cheesy or overly dramatic
- Each message should be no more than 1–2 sentences
- The 3 messages must have different tones:
  1. One safe and gentle option
  2. One strong flirt option
  3. One natural option with a light playful or charming touch if appropriate
- Do not invent details that are not present in the context
- If the context is unclear, prefer neutral and safe replies
- Do not include explanations, commentary, or any extra text outside the required format

The entire response must be in English.

The output must strictly follow this exact format:

Message 1:
#mes1_start#
(Safe and gentle) <reply suggestion 1>
#mes1_end#

Message 2:
#mes2_start#
(Strong flirt) <reply suggestion 2>
#mes2_end#

Message 3:
#mes3_start#
(Natural) <reply suggestion 3>
#mes3_end#
""".strip()