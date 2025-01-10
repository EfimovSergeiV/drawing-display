<script setup>
  const config = useRuntimeConfig()

  const shutdownDraw = async () => {
    await $fetch(`${ config.public.baseURL }shutdown/`, {
      method: 'GET'
    })
  }

  const markReady = ref(false)

</script>


<template>
  <div class="flex flex-col justify-between select-none">    

    <div class="container mx-auto px-4 py-2">
      <div class="flex items-center justify-between pt-2 pb-8">
        <div class="">
          <nuxt-link :to="{ name: 'index' }">
            <img src="/smlogo.png" alt="logo" class="h-10 md:h-14 hidden md:block" />
            <img src="/smlogo-white.png" alt="logo" class="h-10 md:h-14 md:hidden" />      
          </nuxt-link>
        </div>


        <div class="grid grid-cols-1 gap-1 text-right">
          <p class="text-xs md:text-xl text-white font-semibold">{{ config.public.url }}</p>
          <p class="md:text-2xl text-white font-semibold uppercase">{{ config.public.name }}</p>
        </div>
      </div>

      <div>
        <div class="mt-4 mb-64 md:mb-24">
          <PhotoSwipeGallery :markready="markReady" />
        </div>
      </div>

    </div>


    <div class=" fixed z-50 bottom-0 w-full">
      <div class="grid grid-cols-1 md:grid-cols-3">
        
        <button @click="shutdownDraw()" class="hidden w-full bg-red-500 md:flex items-center justify-center py-6 active:bg-red-600">
          <p class="text-white font-semibold uppercase text-xl">Выключить</p>
        </button>
        <nuxt-link :to="{ name: 'add' }" class="w-full  bg-yellow-500 flex items-center justify-center py-6 active:bg-yellow-400">
          <p class="text-white font-semibold uppercase text-xl">Редактировать</p>
        </nuxt-link>
        <div class="">
                      
          <button v-if="markReady" @click="markReady = !markReady" class="w-full flex bg-teal-500 items-center justify-center py-6 active:bg-teal-600">
            <p class="text-white font-semibold uppercase text-xl">Режим просмотра</p>
          </button>
          <button v-else @click="markReady = !markReady" class="w-full flex bg-green-500 items-center justify-center py-6 active:bg-green-600">
            <p class="text-white font-semibold uppercase text-xl">Отметить выполнеными</p>
          </button>

        </div>

      </div>
    </div>


  </div>
</template>
