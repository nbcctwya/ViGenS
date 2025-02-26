# Please install OpenAI SDK first: `pip3 install openai`
from openai import OpenAI

DeepSeekAPI = 'Your DeepSeek API Key'
client = OpenAI(api_key=f"{DeepSeekAPI}", base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    # model='deepseek-reasoner',  # 调用R1
    model="deepseek-chat",     # 调用V3
    # messages=[
    #     {"role": "system", "content": "You are a helpful assistant"},
    #     {"role": "user", "content": "Hello"},
    # ],
    messages=[
        {"role": "system", "content": "假如你是一位经济学与金融领域的专家，擅长经济学教学和金融工具分享"},
        {"role": "user", "content": "请帮我制作一个视频脚本，内容是关于如何选股"},
    ],
    stream=False
)

print(response.choices[0].message.content)


# # 流式输出
# response = client.chat.completions.create(
#     # model='deepseek-reasoner',  # 调用R1
#     model="deepseek-chat",     # 调用V3
#     # messages=[
#     #     {"role": "system", "content": "You are a helpful assistant"},
#     #     {"role": "user", "content": "Hello"},
#     # ],
#     messages=[
#         {"role": "system", "content": "假如你是一位经济学与金融领域的专家，擅长经济学教学和金融工具分享"},
#         {"role": "user", "content": "请帮我制作一个视频脚本，内容是关于如何选股"},
#     ],
#     stream=True
# )
#
# for chunk in response:
#     print(chunk.choices[0].delta.content)