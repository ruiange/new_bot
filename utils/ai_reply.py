
# Please install OpenAI SDK first: `pip3 install openai`

from openai import OpenAI




def ai_reply(content):
    client = OpenAI(api_key="sk-c69cac7288fb4547a7a7d6cc682434b5", base_url="https://api.deepseek.com")

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "user", "content": content},
        ],
        stream=False
    )
    return response.choices[0].message.content
