const TITLES = [
  'I Write About My Empty Thoughts',
  'I Cannot Save You Baby',
  'I Feel Useless',
  'Just kiss Me Baby',
  'Make Up Your Mind You Little Shit'
]

const app = () => {
  // get loader reference
  const loader = document.querySelector('#loader')

  // get main title reference
  const mainTitle = document.querySelector('#main-heading')

  // get logo references
  const logo = document.querySelector('#logo')

  // get random title
  const titleIndex = Math.floor(Math.random() * TITLES.length)
  const title = TITLES[titleIndex]

  // assign selected title
  if (mainTitle) {
    mainTitle.textContent = title
  }

  // take off loader
  if (loader && logo) {
    setTimeout(() => {
      loader.classList.add('loader--hide')
      logo.classList.add('stop-logo')
    }, 1500)
  }
}

window.addEventListener('DOMContentLoaded', () => app())
