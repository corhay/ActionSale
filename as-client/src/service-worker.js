self.__precacheManifest = [].concat(self.__precacheManifest || []);

/* workbox.setConfig({
    debug: true,
}); */

workbox.precaching.precacheAndRoute(self.__precacheManifest, {});

//cache categories
workbox.routing.registerRoute('https://as-api.herokuapp.com/v1/products/categories', new workbox.strategies.StaleWhileRevalidate({
    cacheName: 'categories-cache',
    method: "GET",
    cacheableResponse: {statuses: [0, 200]},
}));

//cache current discounts
workbox.routing.registerRoute('https://as-api.herokuapp.com/v1/discounts/current', new workbox.strategies.StaleWhileRevalidate({
    cacheName: 'current-cache',
    method: "GET",
    cacheableResponse: {statuses: [0, 200]},
}));

//cache denner images
workbox.routing.registerRoute(new RegExp("https://denner.imgix.net/assets/.+"), new workbox.strategies.StaleWhileRevalidate({
    cacheName: 'denner-img-cache',
    method: "GET",
    cacheableResponse: {statuses: [0, 200]},
}));

//cache coop images
workbox.routing.registerRoute(new RegExp("https://contentimages.coop.ch/aktionenimages/images/.+"), new workbox.strategies.StaleWhileRevalidate({
    cacheName: 'coop-img-cache',
    method: "GET",
    cacheableResponse: {statuses: [0, 200]},
}));

//cache migros images
workbox.routing.registerRoute(new RegExp("https://image.migros.ch/2017-medium/.+"), new workbox.strategies.StaleWhileRevalidate({
    cacheName: 'migros-img-cache',
    method: "GET",
    cacheableResponse: {statuses: [0, 200]},
}));


