import createPersistedState from "vuex-persistedstate";

export default {
    state: {
        currentUser: null,
        isLoggedIn: false,
        userId: null,
    },
    mutations: {
        loginSuccess(state, payload){
            state.isLoggedIn = true;
            state.currentUser = payload.username;
            state.userId = payload.id;
        },
        logout(state){
            state.isLoggedIn = false;
            state.currentUser = "";
            state.userId = -1;
        },
    },
    getters: {
        currentUser(state){
            return state.currentUser; 
        },
        isLoggedIn(state){
            return state.isLoggedIn; 
        },
        userId(state){
            return state.userId; 
        },
    },
    setters: {},
    plugins: [createPersistedState()]
};