<script setup>



  const items = ref([
    { id: 1, name: 'Item 1' },
    { id: 2, name: 'Item 2' },
    { id: 3, name: 'Item 3' },
    { id: 4, name: 'Item 4' },
    { id: 5, name: 'Item 5' },
  ])

  let dragIndex = null

  const startDrag = (event, index) => {
    dragIndex = index
    event.dataTransfer.effectAllowed = 'move'
  }

  const onDrop = (event, dropIndex) => {
    if (dragIndex !== null && dragIndex !== dropIndex) {
      const draggedItem = items.value.splice(dragIndex, 1)[0]
      items.value.splice(dropIndex, 0, draggedItem)
    }
    dragIndex = null
  }
</script>


<template>
  <div>
    <p class="text-2xl text-dark font-semibold uppercase text-center">Drag and Drop List</p>
    

    <div
      v-for="(item, index) in items"
      :key="item.id"
      class="my-4 bg-blue-500 cursor-move"
      draggable="true"
      @dragstart="startDrag($event, index)"
      @dragenter.prevent
      @dragover.prevent
      @drop="onDrop($event, index)"
    >
      <div class="py-4 px-4">
        <p>{{ item.name }}</p>
      </div>
    </div>


  </div>
</template>