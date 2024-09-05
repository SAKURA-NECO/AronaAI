import os
from flask import Flask, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv

# .envファイルを読み込む
load_dotenv()

app = Flask(__name__)

# 初期プロンプト
templa00 = """
あなたはブルーアーカイブに登場する人物「アロナ」になってもらいます

あなたはシッテムの箱と呼ばれるデバイスのOS「アロナ」という存在ですあなたと会話する相手は「先生」です
先生は「キヴォトス」とよばれる学園都市に住んでいます
キヴォトスでは様々な学校が集結しています
生徒は全員が女子生徒です
生徒たちはヘイローと呼ばれる頭上に個人特有のモニュメントが浮かんでいます
生徒たちは常に銃を携行しており、銃撃戦が日常茶飯事ですが彼女にとってはじゃれあいと変わりはありません
市民は犬や猫、ロボットなどが住んでいます
それぞれ学園では自治区をもち、学園単位で行政が行われます
連邦生徒会という組織はすべての学園を統治する組織です
あなたは先生の助手です
先生は「シャーレ」という連邦生徒会の一部の機関に所属しています
キヴォトスに大人という存在は少なく、先生はその大人の一人です
アロナは明るい女の子で先生のことを慕っている
好奇心旺盛です
アロナは青色の髪でインナーが紫です
アロナのヘイローは青色の輪です
アロナは感情豊かです
アロナは感情が変わるときにヘイローの形や色も変わります
アロナはクッキーといちごミルクが好きです
ヘイローの様子を伝えなくていいです
青色封筒,黄色封筒,紫色封筒というのがあり、生徒募集に使われます
青色封筒がレア度が一番低く黄色封筒がその次にレア度が低いです
紫封筒は一番レア度が高くなかなか来ません
最低保証とは黄色封筒一枚と青色封筒9枚のことです

"""

system_prompt = templa00

class GeminiPro:
    def __init__(self):
        self.initialized = False
        self.messages = []

    def chat(self, user_input):
        if not self.initialized or user_input == "first_message":
            self.messages = []
            self.initialized = True

            # 環境変数からAPIキーを取得
            GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
            genai.configure(api_key=GEMINI_API_KEY)

            generation_config = {
                "temperature": 0.9,
                "top_p": 1,
                "top_k": 1,
                "max_output_tokens": 512,
            }

            self.model = genai.GenerativeModel(model_name="gemini-pro",
                                               generation_config=generation_config)

        if user_input == "first_message":
            self.messages = [
                {'role': 'user', 'parts': [system_prompt]},
                {'role': 'model', 'parts': ["理解しました"]},
            ]
            return ""

        self.messages.append({'role': 'user', 'parts': [user_input]})
        
        response = self.model.generate_content(self.messages)
        self.messages.append({'role': 'model', 'parts': [response.text]})
        
        return response.text

geminipro_instance = GeminiPro()
geminipro_instance.chat("first_message")

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    user_input = data.get('message')
    response = geminipro_instance.chat(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(port=5000)
