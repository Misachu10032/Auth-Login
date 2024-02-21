import React from 'react';
import { Route, Routes, Navigate } from 'react-router-dom';
import { AuthProvider } from './component/authentication/authentication';
import Login from './pages/login';
import Home from './pages/home';

function App() {
  return (
    <AuthProvider>
   
        <Routes>
          <Route path="/login" element={<Login />} />
          <Route path="/home" element={<Home />} />
          <Route path="/" element={<Navigate to="/login" />} />
        </Routes>
      
    </AuthProvider>
  );
}

export default App;
