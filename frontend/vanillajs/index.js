
const { html, render } = window.libs.lit;

// Now you can use lit-html without direct imports
setInterval(()=>
    render(html`<p>Hello from lit-html</p>`, document.querySelector("footer"), 1000))
