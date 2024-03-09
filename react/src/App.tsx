import React from 'react';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import RouterWrapper from './RouterWrapper';
import Login from './components/Login/Login';
import './scss/main.scss';
import Map from './pages/Map';
import Home from './pages/Home';
import Upload from './pages/Upload';
import { GoogleOAuthProvider } from '@react-oauth/google';
import Register from './components/Register/Register';
import MapWrapper from "./pages/Map";

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
      path: 'upload-form',
      element: (
        <RouterWrapper>
          <Upload />
        </RouterWrapper>
      )
    },
    {
      path: '/register',
      element: (
        <RouterWrapper>
          <Register />
        </RouterWrapper>
      )
    },
    {
      path: '/map',
      element: (
        <RouterWrapper>
          <MapWrapper />
        </RouterWrapper>
      )
    }
  ]);

  return (
    <>
      <GoogleOAuthProvider clientId={process.env.REACT_APP_CLIENT_ID || ''}>
        <React.StrictMode>
          <RouterProvider router={router} />
        </React.StrictMode>
      </GoogleOAuthProvider>
    </>
  );
}

export default App;
