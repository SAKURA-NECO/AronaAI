# AronaAI
 AI project for the Japanese version of BlueArchive's character “A.R.O.N.A”.

This code utilizes Google Gemini AI. To use it, you need to obtain an API key from the following URL:

https://aistudio.google.com/app/prompts/new_chat?pli=1

Once you have the API key, add it to your .env file as follows:

GEMINI_API_KEY=your_obtained_api_key

Run main.py, and the AI will be ready to receive messages from clients on port 5000 at the /ask endpoint.

#アロナAI
　これは日本語版ブルーアーカイブのアロナのキャラクターAIです

このコードはGiminiを利用したAIです
ご利用の際には以下のURLからGiminiの目的に合ったAPIKeyを取得してください
https://aistudio.google.com/app/prompts/new_chat?pli=1
取得したAPIkeyは.envファイルに書くことで利用できます
”GEMINI_API_KEY=取得したAPIKeyを入力”
main.pyを実行すると5000番のポートの/askでAIがクライアントからのメッセージを待機します