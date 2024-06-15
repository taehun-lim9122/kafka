# kafka

## 실행 방법
1. 가상환경 생성 및 삭제
```python
# 생성
python -m venv "가상환경 이름"

# 삭제
sudo rm -rf "가상환경 이름"
```
2. 가상환경 접속 및 종료
```
# 접속
source "가상환경 이름"/bin/activate

# 종료
deactivate
```
3. requirements.txt를 통해 가상환경에 필요한 패키지 설치
```python
pip install -r requirements.txt
```
4. docker-compose 파일 실행 및 종료
```
# 전체 한번에 실행 시
docker-compose up -d

# 단일 컨테이너 실행 시
docker-compose up -d "컨테이너 이름"

# 컨테이너 종료
docker-compose down
```
5. debezium mysql source connector 생성 및 제거
```
# 생성
python3 create_connector.py

# 제거
python3 delete_connector.py
```

## 명령어

1. 로그 확인
```
docker-compose logs "컨테이너 이름"
```
2. 브로커 토픽 리스트 확인
```
docker exec -it broker kafka-topics --list --bootstrap-server broker:9092
```
3. 브로커 토픽 데이터 확인
```
docker exec -it broker kafka-console-consumer --bootstrap-server localhost:9092 --topic "{토픽 이름}" --from-beginning
```
4. 커넥터 리스트 확인
```
curl -X GET http://localhost:8083/connectors/
```
5. 커넥터 상태 확인
```
curl -X GET http://localhost:8083/connectors/"{커넥터 이름}"/status
```
6. 컨슈머 리스트 확인
```
docker exec -it broker kafka-consumer-groups --bootstrap-server broker:9092 --list
```