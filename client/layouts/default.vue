<script setup lang="ts">

  import { onMounted, onUnmounted } from 'vue'
  
  const config = useRuntimeConfig()
  const mainStore = useMainStore()

  const wsUrl = `${ config.public.socketURL }ws/api/`


  const messages = ref<string[]>([])
  const message = ref('')
  let socket: WebSocket | null = null
  const statusSocket = ref(false)

  // Подключение к серверу WebSocket
  const connectWebSocket = () => {
    socket = new WebSocket(wsUrl)

    // Событие: открытие соединения
    socket.onopen = () => {
      console.log('WebSocket соединение установлено')
      statusSocket.value = false
    }

    let counter = 0
    // Событие: получение сообщения
    socket.onmessage = (event) => {
      counter++
      console.log('Получено сообщение:', counter)
      mainStore.updateDrawings(
        JSON.parse(event.data)
      )
      statusSocket.value = false
      // console.log('Получено сообщение:', event.data)
      // messages.value = event.data
      // messages.value.push(`Сервер: ${event.data}`)
    }

    // Событие: ошибка соединения
    socket.onerror = (error) => {
      console.error('WebSocket ошибка: сервер не отвечает')
      statusSocket.value = true
    }

    // Событие: закрытие соединения
    socket.onclose = () => {
      console.log('WebSocket соединение закрыто')
      statusSocket.value = true  

      connectWebSocket()

    }
  }

  // Отправка сообщения на сервер
  const sendMessage = () => {
    if (socket && socket.readyState === WebSocket.OPEN) {

      let jsonData = {
        "message": message.value
      }

      // socket.send(message.value)
      socket.send(JSON.stringify(jsonData))
      messages.value.push(`Вы: ${message.value}`)
      message.value = ''
    } else {
      console.error('WebSocket не подключен')
    }
  }

  // Управление жизненным циклом WebSocket
  onMounted(() => {
    connectWebSocket()
  })

  onUnmounted(() => {
    if (socket) {
      socket.close()
    }
  })


</script>


<template>
  <div class="selec t-none">
    <div class="">

      <transition name="fade" mode="out-in">
        <div v-if="statusSocket" class="fixed z-50 top-10 md:top-0 left-0 w-full">
          <div class="flex items-center justify-center py-8 ">
            <div class=" flex items-center justify-center gap-2 px-4 py-2 rounded-lg bg-red-500/80" >
              <img src="/warning.png" alt="logo" class="h-6 md:h-8" />
              <p class="text-center text-white font-bold text-xl md:text-2xl uppercase">НЕТ СВЯЗИ С СЕРВЕРОМ</p>
            </div>
            
          </div>
        </div>    
      </transition>

      <slot />

    </div>
  </div>
</template>