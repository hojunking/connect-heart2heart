from flask import Flask, request, render_template, send_from_directory, url_for
# chatGPT 라이브러리가 실제로 존재하지 않으므로 대체되었습니다. 적절한 라이브러리를 사용해주세요.
import chatGPT
import os


app = Flask(__name__)

# 업로드된 파일을 저장할 디렉토리 설정
# 프로젝트의 루트 디렉토리를 찾아 절대 경로로 설정합니다.
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['UPLOAD_FOLDER'] = os.path.join(BASE_DIR, 'static', 'uploads')

# 이 부분에서 OpenAI API 키를 환경변수에서 가져오거나 직접 할당합니다.

@app.route('/', methods=['GET'])
def form():
    # 기본 폼 페이지를 렌더링합니다.
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    # 사용자로부터 받은 데이터를 저장합니다.
    recipient = request.form['recipient']
    age_group = request.form['age_group']
    keywords = request.form['keywords']
    letter_style = request.form.getlist('letter_style')
    image = request.files['image']
    recipient_name = request.form['recipient_name']
    sender_name = request.form['sender_name']

    # 이미지 처리 (임시로 서버에 저장하거나 직접 바이너리 데이터로 처리할 수 있습니다)
    
    # 예시로 파일 이름을 'uploaded_image.jpg'로 저장합니다.
    image_filename = 'uploaded_image.jpg'
    image.save(os.path.join(app.config['UPLOAD_FOLDER'], image_filename))

    # ChatGPT API를 호출하여 편지 내용을 생성합니다.
    # 이 부분은 실제 API 호출 코드로 대체해야 합니다.
    prompt = f"이 편지는 {recipient}, 연령대 {age_group} {recipient_name}에게 보내는 것이며 보내는 사람의 이름은 {sender_name}입니다. 반드시 들어가야 하는 키워드는 {keywords}입니다. 스타일은 {', '.join(letter_style)}로 편지를 작성해주세요."
    generated_text = chatGPT.get_gpt_answer(prompt)
    generated_text = response.choices[0].text.strip()
    # generated_text = prompt # 예시로 prompt를 사용합니다.
    
    # generated_text = " "


    total_sender = f"사랑하는 {sender_name[1:]} 올림"  
    # 사용자에게 결과를 보여줄 페이지를 렌더링합니다.
    return render_template('generated_letter.html', letter_content=generated_text, image_path=image_filename, sender_name=total_sender)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True, host='172.16.2.75', port=5000)
