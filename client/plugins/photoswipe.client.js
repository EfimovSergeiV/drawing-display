import { defineNuxtPlugin } from '#app';
import PhotoSwipeLightbox from 'photoswipe/lightbox';
import 'photoswipe/style.css';
import PhotoSwipeDeepZoom from 'photoswipe-deep-zoom-plugin';

export default defineNuxtPlugin((nuxtApp) => {
  nuxtApp.provide('PhotoSwipeLightbox', PhotoSwipeLightbox);
  nuxtApp.provide('PhotoSwipeDeepZoom', PhotoSwipeDeepZoom);
});