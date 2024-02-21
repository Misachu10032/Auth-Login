
import React, { useState } from 'react';
import { useAuth } from '../component/authentication/authentication';
import { isStatusCode2xx } from '../utils/checkStatusCode';
import { useNavigate } from 'react-router-dom';
import { loginUser } from '../api';
import SignUpModal from '../component/modal/signUpModal';

const Login = () => {
  const { isLoggedIn, isAdmintUser, login, userIsAdmin } = useAuth();
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [modalIsOpen, setModalIsOpen] = useState(false);
  const navigate = useNavigate();

  const openModal = () => setModalIsOpen(true);
  const closeModal = () => setModalIsOpen(false);

  const handleLogin = async () => {
    try {
      const loginForm = new FormData();
      loginForm.append('username', username);
      loginForm.append('password', password);
      const response = await loginUser(loginForm);

      if (isStatusCode2xx(response.status)) {
        const user = response.data.user


        login(user.ID);
        navigate('/home');
      } else {
        setError('Unexpected response from the server');
      }
    } catch (error) {
      setError('Invalid username or password');
    }
  };



  return (
    <div className="flex justify-center items-center h-screen text-2xl">
      <form className="w-1/3 flex flex-col">
        <h2 className="mb-4">Login</h2>
        <div className="mb-4">
          <label htmlFor="username" className="block text-gray-700">Username:</label>
          <input
            type="text"
            id="username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            className="w-full p-2 border rounded"
          />
        </div>
        <div className="mb-4">
          <label htmlFor="password" className="block text-gray-700">Password:</label>
          <input
            type="password"
            id="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            className="w-full p-2 border rounded"
          />
        </div>
        {error && <p className="text-red-500 mb-4">{error}</p>}
        <button
          type="button"
          onClick={handleLogin}
          className="bg-blue-500 text-white p-2 rounded mb-2 w-1/3"
        >
          Login
        </button>

        <button
          type="button"
          onClick={openModal}
          className="bg-green-500 text-white p-2 rounded w-1/3"
        >
          Sign Up
        </button>

        <SignUpModal isOpen={modalIsOpen} onClose={closeModal} />
      </form>
    </div>
  );
};

export default Login;
