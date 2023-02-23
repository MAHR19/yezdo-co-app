import { createSlice } from "@reduxjs/toolkit";


export const authSlice = () => createSlice({
    name : 'auth',
    initialState : {
        status: 'checking',
        uid : null,
        email : null,
        displayname : null,
        photoURL : null,
        error : null,
    },
    reducers : {
        login : ( state, action ) => {

        },
        logout : ( state, payload ) => {

        },
        checkCredentials : ( state ) => {

        }
    }
});


export const{ login, logout, checkCredentials } = authSlice.actions;