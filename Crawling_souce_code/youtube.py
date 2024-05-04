import requests

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
        
        # 각 댓글의 정보 추출하여 리스트에 추가
        for item in data['items']:
            comment_info = {
                'text': item['snippet']['topLevelComment']['snippet']['textOriginal'],
                'like_count': item['snippet']['topLevelComment']['snippet']['likeCount'],
                'reply_count': item['snippet']['totalReplyCount']
            }
            all_comments.append(comment_info)
        
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

# 좋아요가 가장 많은 댓글 출력
most_liked_comment = max(all_comments, key=lambda x: x['like_count'])
print("좋아요가 가장 많은 댓글:")
print(f"댓글 내용: {most_liked_comment['text']}")
print(f"좋아요 개수: {most_liked_comment['like_count']}")
print(f"답글 개수: {most_liked_comment['reply_count']}")

# 답글이 가장 많은 댓글 출력
most_replied_comment = max(all_comments, key=lambda x: x['reply_count'])
print("\n답글이 가장 많은 댓글:")
print(f"댓글 내용: {most_replied_comment['text']}")
print(f"좋아요 개수: {most_replied_comment['like_count']}")
print(f"답글 개수: {most_replied_comment['reply_count']}")
