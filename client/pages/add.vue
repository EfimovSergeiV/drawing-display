<script setup>
  const config = useRuntimeConfig()
  const mainStore = useMainStore()
  const loading = ref(false)
  



  const uploadFiles = async (event) => {
    
    loading.value = true

    /// Отправляем файлы на сервер
    const formData = new FormData()
    for (let i = 0; i < event.target.files.length; i++) {
      formData.append('files', event.target.files[i])
    }
    const response = await fetch(`${config.public.baseURL}drawings/list/`, {
      method: 'POST',
      body: formData
    })

    loading.value = false
  }

  const removeDraw = async (uuid) => {
    const formData = new FormData()
    formData.append('uuid', uuid)
    const response = await $fetch(`${config.public.baseURL}drawings/list/`, {
      method: 'DELETE',
      body: formData
    })
  }

  const { x, y } = useMouse()  
  const { pressed } = useMousePressed()

  let dragIndex = null
  let dragUUID = null

  const startDrag = (event, index, uuid) => {
    dragIndex = index
    dragUUID = uuid
    event.dataTransfer.effectAllowed = 'move'
  }

  const onDrop = (event, dropIndex, uuid) => {
    if (dragIndex !== null && dragIndex !== dropIndex) {
      const draggedItem = mainStore.drawings.splice(dragIndex, 1)[0]
      mainStore.drawings.splice(dropIndex, 0, draggedItem)

      $fetch(`${config.public.baseURL}drawings/list/`, {
        method: 'PUT',
        body: {
          method: 'move',
          from: dragUUID,
          to: uuid
        }
      })

    }
    dragIndex = null
    dragUUID = null
  }


</script>


<template>
	<div class="">
		<div class="container mx-auto px-4">
      <div class="grid grid-cols-1 gap-4 md:flex items-center md:justify-between pb-2">
        <div class="py-6">
          <nuxt-link :to="{ name: 'index' }">
            <img src="/smlogo.png" alt="logo" class="h-10 md:h-14 hidden md:block select-none" />
            <img src="/smlogo-white.png" alt="logo" class="h-10 md:h-14 md:hidden select-none" />
          </nuxt-link>        
        </div>

        <div class="">
          <div class="flex items-center justify-end ">

            <div v-if="loading" class="">
              <div class="flex items-center gap-3">
                <img src="/download.png" alt="loading" class="h-6 animate-bounce" />
                <p class="md:text-2xl text-white font-semibold uppercase">Загрузка файлов</p>
              </div>

            </div>
            
            <div v-else>
              <div class="">
                <div class="py-4">
                  <p class="text-base text-white font-semibold uppercase text-right">Загрузить PDF файлы</p>
                </div>
                
                <div class=" cursor-pointer">
                  <input id="newfile" type="file" accept=".pdf,.PDF" multiple
                    class="block w-full text-sm text-white
                    file:mr-4 file:py-2 file:px-4
                    file:rounded-full file:border-0
                    file:text-sm file:font-semibold
                    file:bg-sky-700 file:text-white
                    hover:file:bg-sky-800 transition-all duration-700"
                    @change="uploadFiles"
                  />
                </div>

              </div>
            </div>
          
          </div>
        </div>
      </div>		
		</div>



		<div class="container mx-auto px-4 py-4 pb-40 md:mb-20">

      <div class="py-2">
        <p class="text-white md:text-gray-900">Всего файлов: {{ mainStore.drawings.length }}</p>
      </div>

      <div>
        <transition-group name="fade" tag="div" class="grid grid-cols-3 xl:grid-cols-5 gap-2 md:gap-8 ">
          <div 
            v-for="(draw, index) in mainStore.drawings" 
            :key="draw.uuid"
            draggable="true"
            @dragstart="startDrag($event, index, draw.uuid)"
            @dragenter.prevent
            @dragover.prevent
            @drop="onDrop($event, index, draw.uuid)"
            >

            <div class="bg-white cursor-move">
              
              <div class="py-2 w-full flex items-center justify-center relative">
                <img :src="draw.prw" alt="" class="w-full" />

                <div class="absolute top-0 left-0 w-full h-full z-40">
                  <p class=""></p>
                </div>

              </div>
              
              <div class="py-2 w-full flex items-center justify-center">
                <p class="text-xs md:text-sm text-center text-gray-800 select-none">{{ draw.name }}</p>
              </div>

              <button @click="removeDraw(draw.uuid)" class="py-2 flex items-center justify-center bg-red-500 w-full active:bg-red-600">
                <p class="text-white">Удалить</p>
              </button>            
            </div>
          </div>
        </transition-group>
      </div>
		</div>


    <div class=" fixed z-50 bottom-0 w-full">
      <div class="grid grid-cols-1 md:grid-cols-3">
        <button @click="removeDraw(0)" class="w-full bg-red-500 flex items-center justify-center py-6 active:bg-red-600">
          <p class="text-white font-semibold uppercase text-xl">УДАЛИТЬ ВСЕ</p>
        </button>
        <div class="hidden w-full bg-green-500 md:flex items-center justify-center py-6">
          <p class="text-white font-semibold uppercase text-xl"></p>
        </div>
        <nuxt-link :to="{ name: 'index' }" class="w-full flex bg-teal-500 items-center justify-center py-6 active:bg-teal-600">
          <p class="text-white font-semibold uppercase text-xl">Режим просмотра</p>
        </nuxt-link>
      </div>
    </div>

	</div>

</template>

<style scoped>
	.drop-zone {
		border: 2px dashed #ccc;
		padding: 20px;
		text-align: center;
		transition: background-color 0.3s ease;
	}
	.drop-zone.is-dragover {
		background-color: #f0f0f0;
	}
</style>