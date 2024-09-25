import React from 'react';
import ReactDOM from 'react-dom/client';
import './styles/navbar.css';
import './styles/landing-page.css';
import App from './components/App';
import Navbar from './components/navbar';
import Landing_page from './components/landing-page';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <Navbar />
    <Landing_page />
    <App />
  </React.StrictMode>
);


