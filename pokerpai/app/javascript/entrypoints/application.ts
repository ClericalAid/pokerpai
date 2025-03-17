import App from '../components/App.svelte'
import { mount } from 'svelte'

document.addEventListener('DOMContentLoaded', () => {
  mount(
    App, 
    {
      target: document.getElementById('app'),
    },
  )
})
