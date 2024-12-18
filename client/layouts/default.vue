<script setup lang="ts">

  import { onMounted, onUnmounted } from 'vue';
  
  const config = useRuntimeConfig()
  const mainStore = useMainStore()

  // const wsUrl = `${ config.public.socketURL }ws/api/`
  const wsUrl = `${ config.public.socketURL }ws/api/`

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

    let counter = 0
    // Событие: получение сообщения
    socket.onmessage = (event) => {
      counter++
      console.log('Получено сообщение:', counter);
      mainStore.updateDrawings(
        JSON.parse(event.data)
      )
      // console.log('Получено сообщение:', event.data);
      // messages.value = event.data
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
  <div class="selec t-none">
    <div class="">


      <slot />


    </div>
  </div>
</template>