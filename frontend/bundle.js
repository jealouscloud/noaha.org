var lit = require("lit");

var htmx = require("htmx.org");
window.htmx = htmx; // recommended by htmx docs

// libs exposed to the global scope
window.libs = {
    "lit": lit
};