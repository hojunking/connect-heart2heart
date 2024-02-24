# GPT API의 기본기능을 확일할 수 있는 스크립트입니다.
# openai_config.py에서 설정한 정보를 활용하여 API 요청을 수행합니다.

# 필요한 패키지 및 설정 가져오기
import openai
from config.openai_config import API_KEY
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
# OpenAI API 키를 설정합니다.
openai.api_key = API_KEY

def get_gpt_answer(user_input):
    # GPT 모델에 질문을 넣고 답변을 생성합니다.
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",    # GPT-3.5 Turbo 모델 엔진 선택
        messages=[
            {"role": "system", "content": "너는 안내를 해주는 가이드 입니다."},  # 시스템 역할 설정
            {"role": "system", "content": "귀엽게 대답해줘."},  # 시스템 역할 설정
            {"role": "user", "content": user_input},  # 사용자 역할과 입력 설정
            {"role": "assistant", "content": "저는 AI-BOT 입니다."}  # 어시스턴트 역할 설정
        ],
        max_tokens=60,             # 생성할 최대 토큰 수 (길이 조절)
        temperature=0.7,           # 생성의 확률 분포 조절 (높을수록 랜덤성 증가)
        top_p=1.0,                 # 생성 후보 중 확률적으로 선택할 상위 p 비율 (전체 후보 선택)
        frequency_penalty=0.2,     # 단어 빈도 조절 (중복이 적게 되도록 약간의 패널티 부여)
        presence_penalty=0.0,      # 단어 중복 빈도 조절 (중복에 대한 패널티 없음)
        stop=["공룡", "옷장"]     # 중단 단어 설정 (답변에 공룡 또는 옷장이 포함되지 않도록)
    )

    return response.choices[0].message["content"].strip()  # 생성된 답변 반환

if __name__ == "__main__":
    user_input = "나이가 몇살이지?"  # 테스트용 사용자 입력

    # GPT 모델을 활용하여 답변 생성
    answer = get_gpt_answer(user_input)

    # 생성된 답변 출력
    print("사용자 입력:", user_input)
    print("답변:", answer)
