from google import genai

client = genai.Client()

while True:
    question = input("질문 (종료: q): ")
    if question == "q":
        break
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=question,
    )
    print(response.text)