import React from 'react';
import SignIn from './signin/SignIn';
import Dashboard from './dashboard/Dashboard';
import { Routes, Route } from 'react-router-dom';
import { Provider } from 'react-redux';
import { store } from './store/auth/store';

function App() {
  return (
      <>
      <Provider store={ store }>
       <Routes>
          <Route path='/' element = {<SignIn />} />
          <Route path='/main' element = {<Dashboard />} />
       </Routes>
       </Provider>
      </>
  );
}

export default App;
