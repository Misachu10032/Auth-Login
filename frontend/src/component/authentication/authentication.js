import { createContext, useContext, useState } from 'react';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [isAdmintUser, setIsAdminUser] = useState(false);


  const login = (userId) => {
    setIsLoggedIn(true);
    localStorage.setItem('userId', JSON.stringify(userId));
  };

  const logout = () => {

    setIsLoggedIn(false);
    localStorage.removeItem('userId')
  };

  const userIsAdmin = () => {
    setIsAdminUser(true);
  };

  const value ={isLoggedIn, isAdmintUser,setIsLoggedIn, login, logout,userIsAdmin}

  return (
    <AuthContext.Provider value={value }>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);
