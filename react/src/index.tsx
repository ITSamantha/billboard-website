import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import { store } from './redux/store';
import { Provider } from 'react-redux';
import axios from 'axios';

axios.defaults.withCredentials = true;

ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
  <Provider store={store}>
    <App />
  </Provider>
);
