import { defineStore } from 'pinia'


interface Drawing {
  uuid: string, 
  name: string, 
  status: string, 
  created_at: string, 
  link: string, 
  pdf: string, 
  webp: string, 
  webp_size: object, 
  prw: string,
}



export const useMainStore = defineStore('MainStore', {

  state: () => ({
    drawings: [] as Drawing[],
  }),
  
  getters: {

  },

  actions: {
    updateDrawings( data: Drawing[] ) {

      /// Получаем текущие дату и время
      let now = new Date()
      console.log('Updating drawings ', now)
      this.drawings = data

    }
  },
})