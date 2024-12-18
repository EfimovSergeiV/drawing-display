<script setup lang="ts">
  import { onMounted, onUnmounted } from 'vue';

  // const wsUrl = 'ws://websocket-echo.com';


  const wsUrl = 'ws://192.168.60.203:8080/ws/api/';
  const messages = ref<string[]>([]);
  const message = ref('');
  let socket: WebSocket | null = null;

  // Подключение к серверу WebSocket
  const connectWebSocket = () => {
    socket = new WebSocket(wsUrl);

    // Событие: открытие соединения
    socket.onopen = () => {
      console.log('WebSocket соединение установлено');
    };

    // Событие: получение сообщения
    socket.onmessage = (event) => {
      console.log('Получено сообщение:', event.data);
      messages.value = event.data
      // messages.value.push(`Сервер: ${event.data}`);
    };

    // Событие: ошибка соединения
    // socket.onerror = (error) => {
    //   console.error('WebSocket ошибка:', error);
    // };

    // Событие: закрытие соединения
    socket.onclose = () => {
      console.log('WebSocket соединение закрыто');
        

      connectWebSocket();

    };
  };

  // Отправка сообщения на сервер
  const sendMessage = () => {
    if (socket && socket.readyState === WebSocket.OPEN) {

      let jsonData = {
        "message": message.value
      }

      // socket.send(message.value);
      socket.send(JSON.stringify(jsonData));
      messages.value.push(`Вы: ${message.value}`);
      message.value = '';
    } else {
      console.error('WebSocket не подключен');
    }
  };

  // Управление жизненным циклом WebSocket
  onMounted(() => {
    connectWebSocket()
  });

  onUnmounted(() => {
    if (socket) {
      socket.close();
    }
  });
</script>

<template>
  <div class="px-8">
    <h1>Эхо-сервер WebSocket</h1>
    <div>
      <input v-model="message" placeholder="Введите сообщение" />
      <button @click="sendMessage">Отправить</button>
    </div>
    <div>
      <h2>История сообщений</h2>
      <ul>
        <li>{{ messages }}</li>
      </ul>
    </div>
  </div>
</template>


<style scoped>
h1 {
  font-size: 24px;
  margin-bottom: 16px;
}
input {
  padding: 8px;
  margin-right: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
}
button {
  padding: 8px 16px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
button:hover {
  background-color: #0056b3;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  margin: 8px 0;
  padding: 8px;
  background-color: #f8f9fa;
  border: 1px solid #ccc;
  border-radius: 4px;
}
</style>
