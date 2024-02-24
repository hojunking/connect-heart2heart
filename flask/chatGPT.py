import openai
API_KEY = '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'

openai.api_key = API_KEY


def get_gpt_answer(user_input):
    # GPT 모델에 질문을 넣고 답변을 생성합니다.
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",    # GPT-3.5 Turbo 모델 엔진 선택
        messages=[
            {"role": "system", "content": "You are the machine of writing a letter"},  # 시스템 역할 설정
            {"role": "system", "content": "writing in 500 charaters"},  # 시스템 역할 설정
            {"role": "system", "content": "You are going to write a letter for grandmother or grandfather or parents"},  # 시스템 역할 설정
            {"role": "user", "content": user_input},  # 사용자 역할과 입력 설정
        ],
        max_tokens=500,             # 생성할 최대 토큰 수 (길이 조절)
        temperature=0.7,           # 생성의 확률 분포 조절 (높을수록 랜덤성 증가)
        top_p=1.0,                 # 생성 후보 중 확률적으로 선택할 상위 p 비율 (전체 후보 선택)
        frequency_penalty=0.2,     # 단어 빈도 조절 (중복이 적게 되도록 약간의 패널티 부여)
        presence_penalty=0.0,      # 단어 중복 빈도 조절 (중복에 대한 패널티 없음)
    )

    return response.choices[0].message["content"].strip()  # 생성된 답변 반환

    ## "할머니께 보내는 편지를 써주세요. 할머니의 이름은 김순자이시고, 60대이십니다. 편지에는 '사랑'과 '보고 싶다'는 말이 꼭 포함되어야 합니다. 진정성 있는 마음을 담아주세요."