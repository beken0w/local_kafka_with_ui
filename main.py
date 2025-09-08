from aiokafka import AIOKafkaProducer
import asyncio

async def send_one():
    producer = AIOKafkaProducer(
        bootstrap_servers="localhost:9094",
        security_protocol="SASL_PLAINTEXT",
        sasl_mechanism="PLAIN",
        sasl_plain_username="alice",
        sasl_plain_password="alice-pass",
    )
    await producer.start()
    try:
        await producer.send("my_topic", b"Hello from Python")
    finally:
        await producer.stop()

asyncio.run(send_one())
