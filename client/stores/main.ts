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
      // console.log('Updating drawings ', now)

      // ВНИМАНИЕ! ЭТО НЕ БУДЕТ РАБОТАТЬ, КОГДА ПОДКЛЮЧИМ БЭКЕНД
      // this.drawings = data
      if (this.drawings !== data) {
        this.drawings = data
      }

    }
  },
})