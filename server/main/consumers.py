import json
from channels.generic.websocket import AsyncWebsocketConsumer


import sys
import datetime
from time import sleep
from io import BytesIO
from pdf2image import convert_from_path, convert_from_bytes

from django.core.files.uploadedfile import InMemoryUploadedFile



import asyncio
import json
from channels.generic.websocket import AsyncWebsocketConsumer


from asgiref.sync import sync_to_async
from draw.models import DrawingModel
from draw.serializers import DrawingSocketSerializer

from datetime import datetime


def now_time():
    return datetime.now().strftime("%H:%M:%S")



class MyWebSocketConsumer(AsyncWebsocketConsumer):

    @sync_to_async
    def get_serialized_data(self, base_url):
        qs = DrawingModel.objects.all()
        serializer = DrawingSocketSerializer(qs, many=True, context={'base_url': base_url} )
        return serializer.data


    async def connect(self):
        # При подключении клиента
        await self.accept()
        self.keep_sending = True  # Флаг для контроля отправки данных
        asyncio.create_task(self.send_data_loop())  # Запуск фона для отправки данных

    async def disconnect(self, close_code):
        # При отключении клиента
        self.keep_sending = False  # Остановить отправку данных
        print(f"Клиент отключился: {close_code}")

    async def receive(self, text_data):
        # Обработка входящих сообщений от клиента
        data = json.loads(text_data)
        print(f"Получено сообщение: {data}")

        # Пример ответа клиенту
        await self.send(text_data=json.dumps({
            "message": f"Ваше сообщение: {data.get('message', '')}"
        }))

    async def send_data_loop(self):
        counter = 0
        while self.keep_sending:
            counter += 1

            base_url = f"http://deop.local:8080"

            # Получаем данные
            serialized_data = await self.get_serialized_data(base_url)

            # serialized_data = await self.get_serialized_data()
            # print(serialized_data)
            print(f'{now_time()} Отправка данных: {counter}')


            try:
                # Пример отправки данных
                await self.send(text_data=json.dumps(serialized_data, ensure_ascii=False))
                await asyncio.sleep(0.5)  # Задержка
            except Exception as e:
                print(f"Ошибка при отправке данных: {e}")
                break
