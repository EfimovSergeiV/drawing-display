<script setup>
  import { onMounted } from 'vue';
  import { useNuxtApp } from '#app';

  const { $PhotoSwipeLightbox, $PhotoSwipeDeepZoom } = useNuxtApp()
  const config = useRuntimeConfig()
  const props = defineProps(['markready',]);
  const mainStore = useMainStore()
  

  const { data: draws } = await useFetch(`${ config.public.baseURL }draws/list/`)

  onMounted(() => {
    const lightbox = new $PhotoSwipeLightbox({
      gallery: '.gallery',
      children: 'a',

      // Recommended PhotoSwipe options for this plugin
      allowPanToNext: false, // prevent swiping to the next slide when image is zoomed
      allowMouseDrag: true, // display dragging cursor at max zoom level
      wheelToZoom: true, // enable wheel-based zoom
      zoom: false, // disable default zoom button

      pswpModule: () => import('photoswipe'),
    });

    // Инициализируем Deep Zoom плагин для PhotoSwipe
    new $PhotoSwipeDeepZoom(lightbox, {
      tileSize: 256
    });

    lightbox.init();
  });


  const backendFail = ref(false)
  // const updateDraw = async () => {
  //   await $fetch(`${ config.public.baseURL }draws/list/`, {
  //     method: 'GET',
  //     timeout: 300
  //   }).then((response) => {
  //     draws.value = response
  //     backendFail.value = false
  //   }).catch((error) => {
  //     backendFail.value = true
  //   })
  // }


  // let intervalId;

  // onMounted(() => {
  //   // Установить интервал каждые 5 минут
  //   intervalId = setInterval(() => {
  //     updateDraw()
  //     // console.log('updateDraw()');
  //   }, 5000); // 5 минут = 300000 мс
  // });

  // onUnmounted(() => {
  //   // Очистить интервал, чтобы избежать утечек памяти
  //   clearInterval(intervalId);
  // });











  const removeDraw = async (id) => {
    const formData = new FormData()
    formData.append('id', id)
    const response = await $fetch(`${config.public.baseURL}draws/list/`, {
      method: 'DELETE',
      body: formData
    })

    /// Получаем новый список чертежей
    const newDraws = await $fetch(`${ config.public.baseURL }draws/list/`)
    draws.value = newDraws

  }


  const completeDraw = async (uuid) => {
    const formData = new FormData()
    formData.append('uuid', uuid)
    const response = await $fetch(`${config.public.baseURL}draws/list/`, {
      method: 'PUT',
      body: formData
    })

    /// Получаем новый список чертежей
    const newDraws = await $fetch(`${ config.public.baseURL }draws/list/`)
    draws.value = newDraws

  }

</script>


<template>
  


  <div id="photoSwipeGallery relative selec t-none">



    <transition-group name="fade" tag="div" mode="out-in" class="gallery grid grid-cols-2 md:grid-cols-3 xl:grid-cols-5 gap-8" >
      <div v-for="(image, index) in mainStore.drawings" :key="index" class="relative">

        <transition name="fade" mode="out-in">
          <div v-if="markready" class="absolute z-40 w-full">
            <button @click="completeDraw(image.uuid)" class=" bg-green-500 opacity-90 px-4 py-2 w-full active:bg-green-600">
              <p class="text-center text-white font-bold text-xl md:text-xl uppercase">Отметить</p>
              <p class="text-center text-white font-bold text-xl md:text-xl uppercase">выполненным</p>
            </button>
          </div>          
        </transition>

        <a
          :key="index"
          :href="image.webp"
          :data-pswp-width="image.webp_size.width"
          :data-pswp-height="image.webp_size.height"
          :data-deep-zoom="JSON.stringify(image.webp)"
          class="gallery-item "
        >

          <div class="bg-white">
            
            <div class="">
              <div class="">
                <img :src="image.prw" :alt="`Image ${index + 1}`" class="w-full" />          
              </div>
            </div>

            <div class="flex items-center justify-center mt-2">
              <p class="text-center text-gray-800">{{ image.name }}</p>
            </div>

          </div>
        </a>

      </div>
    </transition-group>  

  </div>
</template>




<style scoped>
/* .gallery {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
} */

.gallery-item img {
  height: auto;
  cursor: pointer;
  object-fit: cover;
}
</style>