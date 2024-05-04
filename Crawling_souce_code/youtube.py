import requests
from bs4 import BeautifulSoup

def get_all_comments(youtube_url):
    # 비디오 ID 추출
    video_id = youtube_url.split("v=")[1]
    # YouTube API 호출을 위한 URL 설정
    api_key = "AIzaSyChhfS6I2bxUGwPnHnurVMbIS9kQSwosmE"  # 사용자의 API 키로 대체해야 합니다.
    url = f"https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId={video_id}&key={api_key}"
    # 모든 댓글을 저장할 리스트 생성
    all_comments = []
    # 다음 페이지 토큰 설정
    next_page_token = None
    
    # 모든 댓글을 가져오기 위해 루프 실행
    while True:
        # API 호출
        response = requests.get(url)
        data = response.json()
        
        # 각 댓글의 텍스트 추출하여 리스트에 추가
        for item in data['items']:
            comment_text = item['snippet']['topLevelComment']['snippet']['textOriginal']
            all_comments.append(comment_text)
        
        # 다음 페이지 토큰이 있는 경우에만 다음 페이지 호출
        if 'nextPageToken' in data:
            next_page_token = data['nextPageToken']
            url = f"https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId={video_id}&key={api_key}&pageToken={next_page_token}"
        else:
            break
    
    return all_comments

# 유튜브 링크를 입력하세요
youtube_url = input("유튜브 링크를 입력하세요: ")
# 모든 댓글 가져오기
all_comments = get_all_comments(youtube_url)
# 모든 댓글 출력
for comment in all_comments:
    print(comment)
