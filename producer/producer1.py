from kafka import KafkaProducer
from json import dumps
import time
import os

bootstrap_servers = 'broker:29092'

producer = KafkaProducer(
    acks=0, # 메시지 전송 완료에 대한 체크
    compression_type='gzip', # 메시지 전달할 때 압축(None, gzip, snappy, lz4 등)
    bootstrap_servers= bootstrap_servers, # 전달하고자 하는 카프카 브로커의 주소 리스트
    value_serializer=lambda x:dumps(x).encode('utf-8') # 메시지의 값 직렬화
)

start = time.time()

for i in range(100):
    data = {'producer3' : 'test'+str(i)}
    producer.send('producer1', value=data)
    producer.flush() # 
    
print('[Done]:', time.time() - start)