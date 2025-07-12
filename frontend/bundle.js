var lit = require("lit");

var htmx = require("htmx.org");
window.htmx = htmx; // recommended by htmx docs

// libs exposed to the global scope
window.libs = {
    "lit": lit
};

// Using require
const hljs = require('highlight.js/lib/core');

// Load any languages you need
hljs.registerLanguage('python', require('highlight.js/lib/languages/python'));
hljs.highlightAll();