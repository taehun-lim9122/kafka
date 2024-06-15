from kafka import KafkaConsumer
import json

def create_consumer(broker, group_id, topic):
    # 컨슈머 생성 및 설정
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=[broker],
        group_id=group_id,
        auto_offset_reset='earliest',  # 초기 오프셋 설정
        enable_auto_commit=True,       # 자동 커밋 설정
        value_deserializer=lambda x: x.decode('utf-8')  # 메시지 디코딩 설정
    )
    return consumer

def consume_messages(consumer):
    try:
        while True:
            # 폴링, 타임아웃은 1초로 설정
            message_batch = consumer.poll(timeout_ms=1000)
            
            if message_batch:
                for tp, messages in message_batch.items():
                    for message in messages:
                        # 메시지 처리
                        print(f"Received message: {message.value}")
            else:
                # 메시지가 없으면 계속 대기
                print("Waiting for messages...")
    except KeyboardInterrupt:
        print("Stopping consumer...")
    finally:
        # 컨슈머 종료
        consumer.close()

if __name__ == "__main__":
    broker = 'localhost:9092'
    group_id = 'classicmodels.employees.subscriber'
    topic = 'topic.classicmodels.employees'

    consumer = create_consumer(broker, group_id, topic)
    consume_messages(consumer)
