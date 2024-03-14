import React from 'react';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import RouterWrapper from './RouterWrapper';
import Login from './components/Login/Login';
import './scss/main.scss';
import Home from './pages/Home';
import Upload from './pages/Upload';
import { GoogleOAuthProvider } from '@react-oauth/google';
import Register from './components/Register/Register';
import Catalog from './components/Catalog/CategoriesBlock';
import MapWrapper from './pages/Map';
import Profile from './pages/Profile';

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
      path: 'category/:categorySlug',
      element: (
        <RouterWrapper>
          <Catalog />
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
      path: '/profile',
      element: (
        <RouterWrapper>
          <Profile />
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
