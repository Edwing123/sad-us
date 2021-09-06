const TITLES = [
  'I Write About My Empty Thoughts',
  'I Cannot Save You Baby',
  'I Feel Useless',
  'Just kiss Me Baby'
]


const app = () => {
  // get loader reference
  const loader = document.querySelector('#loader')

  // get main title reference
  const mainTitle = document.querySelector('#main-heading')

  // get random title
  const titleIndex = Math.floor(Math.random() * (TITLES.length))
  const title = TITLES[titleIndex]

  // assign selected title
  if (mainTitle) {
    mainTitle.textContent = title
  }

  // take off loader
  if (loader) {
    loader.classList.add('hide')
  }
}


window.addEventListener('DOMContentLoaded', () => app())
