
const { html, render } = window.libs.lit;

// setup events on document ready
document.addEventListener('DOMContentLoaded', () => {

  // setup event listeners
  document.querySelectorAll('.o-card').forEach((x) => {
    x.addEventListener('mousemove', (e) => {
    const rect = x.getBoundingClientRect();
    const centerX = rect.left + rect.width / 2;
    const centerY = rect.top + rect.height / 2;
    
    const deltaX = e.clientX - centerX;
    const deltaY = e.clientY - centerY;
    const angle = Math.atan2(deltaY, deltaX) * (180 / Math.PI);

    // Apply the rotation to the card
    x.style["border-image"] = `linear-gradient(${angle + 180}deg, #2176FF,#43E8ED,#6FFFBF,#32FF7A,#FF53A1,#A259F7,#23272A,#2176FF) 1`;
  })
  })
});