import openai

OPENAI_API_KEY = "sk-MyaTQEc2JPfqar6PmYh2Wo26eiHbt9PS8pOgm7m48gLEASwK"
openai.api_key = OPENAI_API_KEY
openai.api_base = "https://api.chatanywhere.cn/v1/"
text = """在进行openai api调用的时候，openai.ChatCompletion.create，加`stream=True`这个参数与不加有什么区别，优缺点在哪里，主要回答token和审查方面"""


def gpt_35_api_stream(messages: list):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            stream=True,
        )
        completion = {"role": "", "content": ""}
        for event in response:
            if event["choices"][0]["finish_reason"] == "stop":
                print(f"\n收到的完成数据: {completion}")
                break
            for delta_k, delta_v in event["choices"][0]["delta"].items():
                print(f"{delta_v}", end="")
                completion[delta_k] += delta_v
        messages.append(completion)
        return (True, "")
    except Exception as err:
        return (False, f"OpenAI API 异常: {err}")


if __name__ == "__main__":
    messages = [
        {
            "role": "user",
            "content": text,
        },
    ]
    print(gpt_35_api_stream(messages))
    # print(messages)
