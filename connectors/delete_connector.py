import requests
import json

# Kafka Connect REST API 엔드포인트 URL
url = 'http://localhost:8083/connectors'

# 소스 커넥터의 이름
connector_name = 'connector-test'

endpoint = f'{url}/{connector_name}'
# DELETE 요청 보내기
response = requests.delete(endpoint)

print(response.status_code)
# 응답 확인
if response.status_code == 204:
    print(f"소스 커넥터 : '{connector_name}' 가 성공적으로 삭제되었습니다.")
elif response.status_code == 404:
    print(f"소스 커넥터: '{connector_name}' 을 찾을 수 없습니다.")
else:
    print(f"소스 커넥터: '{connector_name}' 을 삭제 실패 했습니다. status code : {response.text}")
