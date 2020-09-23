module.exports = {
    pwa: {
        name: "ActionSale",
        themeColor: '#c70902',
        msTileColor: '#000000',
        appleMobileWebAppStatusBarStyle: 'black',
        appleMobileWebAppCapable: 'yes',
        workboxPluginMode: "InjectManifest",
        workboxOptions: {
            swSrc: "src/service-worker.js"
        }
    }
}