/* 
  See Smashing Magazine Tutorial:
  https://www.smashingmagazine.com/2021/11/dyslexia-friendly-mode-website/
*/
const dyslexiaToggle = ev => {
  const content = document.querySelector('.content');
  content.classList.toggle('dyslexia-mode');

};
document.querySelector('#dyslexia-toggle').addEventListener('click',dyslexiaToggle)