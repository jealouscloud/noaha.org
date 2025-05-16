const globals = require("globals");
const js = require("@eslint/js");

module.exports = [
    js.configs.recommended, 
    {
        languageOptions: {
            globals: {
                ...globals.browser,
                ...globals.node,
                ...globals.mocha
            },
            ecmaVersion: "latest",
            sourceType: "module",
        }
    },
    {
        ignores: [
            "dist/*",
        ],
    }
];