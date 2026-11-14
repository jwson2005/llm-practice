from google import genai

client = genai.Client()
chat = client.chats.create(model="gemini-3.5-flash")

while True:
    question = input("질문 (종료: q): ")
    if question == "q":
        break
    response = chat.send_message(question)
    print(response.text)