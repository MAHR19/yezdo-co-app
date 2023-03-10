import React from 'react';
import SignIn from './signin/SignIn';
import Dashboard from './dashboard/Dashboard';
import { Routes, Route } from 'react-router-dom';
import { Provider } from 'react-redux';
//import { store } from './store/store';

function App() {
  return (
      <>
      
        <SignIn />
    
      </>
  );
}

export default App;
