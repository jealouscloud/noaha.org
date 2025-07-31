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

## Navigation
Simplest tour of the code base

```shell
backend/ # Python web application / API lives here
  data/ # Data interop like with databases lives here
    store.py # Core interface to data interop
  server.py # Sets up server interface

frontend/ # Everything that makes up our "client" with an empasis on "thin"
  assets/ # Static assets, images
  css/ # all of our css lives under here
    main.css # This file organizes all other css in the directory and imports
             # each file in order. It also includes any css from libraries.
  package.json # Contains our dependency list and build instructions

public/ # Assets are built (if necessary) and copied here respecting their paths

build.sh # Proper build script
live-reload.py # Wrapper script run by `rye run dev` automates browser/server reloads
```

## The flow of a request
```
Request -> 
    server.py (app) route -> 
        Grab data from data.store
        Send data to hypertext.pages
        return hypertext
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

### Run production server
Run `rye run prod` which will run the wsgi server.