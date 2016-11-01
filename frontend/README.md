# isserviceup frontend

## Build Setup

``` bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build
```

If you want to deploy it on a custom domain name change the `API_HOST` variable in the [config file](https://github.com/marcopaz/is-service-up/blob/master/frontend/src/config.js).
 
Once you have build it for production you need to place the content of the dist folder in the static folder of the backend, see [scripts/build_frontend.sh](https://github.com/marcopaz/is-service-up/blob/master/scripts/build_frontend.sh).
