import App from '../components/App.svelte'
import { mount } from 'svelte'
import "../stylesheets/app.css"

document.addEventListener('DOMContentLoaded', () => {
  mount(
    App,
    {
      target: document.getElementById('app'),
    },
  )
})
