import React from 'react';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import RouterWrapper from './RouterWrapper';
import Menu from './components/Menu/Menu';
import Login from './components/Login/Login';
import './scss/main.scss';
import Map from './pages/Map';
import Home from './pages/Home';

export const APP_URL = 'http://localhost:3000/';

function App() {
  const router = createBrowserRouter([
    {
      path: '/',
      element: (
        <RouterWrapper>
          <Home />
        </RouterWrapper>
      )
    },
    {
      path: '/sign-in',
      element: (
        <RouterWrapper>
          <Login />
        </RouterWrapper>
      )
    },
    {
      path: '/map',
      element: (
        <RouterWrapper>
          <Map />
        </RouterWrapper>
      )
    }
  ]);

  return (
    <>
      <React.StrictMode>
        <RouterProvider router={router} />
      </React.StrictMode>
    </>
  );
}

export default App;
