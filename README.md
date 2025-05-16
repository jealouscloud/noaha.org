# web demo

This is an example project using the following stack:
* Python
* [html-compose](https://github.com/jealouscloud/html-compose)
* Flask
* gunicorn
* a node dependency "bundler" using Parcel
* vanillajs modules that can import from the bundle i.e. 
```js
const { html, render } = window.libs.lit
```

## Setup
### Dependencies
* [rye](https://rye.astral.sh/guide/installation/)
* pnpm

### Getting started
* git clone this project
* `rye sync`
* `cd frontend/`
* `pnpm install`
* `cd ..`
* `./build.sh`

### Run debug server
Run `rye run dev` which will run the `live-reload.py` module with browser and server hot-reloading.