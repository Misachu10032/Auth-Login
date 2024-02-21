// SignUpModal.js
import React, { useState } from 'react';
import Modal from 'react-modal';
import { signUpUser } from '../../api';
import { isStatusCode2xx } from '../../utils/checkStatusCode';

const SignUpModal = ({ isOpen, onClose }) => {
  const customModalStyle = {
    content: {
      width: '50%',
      height: '50%',
      margin: 'auto',
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      justifyContent: 'center',
    },
  };

  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [email, setEmail] = useState('');
  const [error, setError] = useState('');
  const handleSubmit = async() => {

    try {
      const signUpForm = new FormData();
      signUpForm.append('username', username);
      signUpForm.append('password', password);
      signUpForm.append('firstname', firstName);
      signUpForm.append('lastname', lastName);
      signUpForm.append('email', email);

      const response = await signUpUser(signUpForm);

      if (isStatusCode2xx(response.status)) {

        onClose();
      }
    } catch (error) {
      setError('incorrect forms');
    }


  };

  return (
    <Modal
      isOpen={isOpen}
      onRequestClose={onClose}
      style={customModalStyle}
    >
      <h2>Sign Up</h2>
      <form>
        <div className="mb-4">
          <label htmlFor="username">Username:</label>
          <input
            type="text"
            id="username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            className="w-full p-2 border rounded"
          />
        </div>
        <div className="mb-4">
          <label htmlFor="password">Password:</label>
          <input
            type="password"
            id="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            className="w-full p-2 border rounded"
          />
        </div>
        <div className="mb-4">
          <label htmlFor="firstName">First Name:</label>
          <input
            type="text"
            id="firstName"
            value={firstName}
            onChange={(e) => setFirstName(e.target.value)}
            className="w-full p-2 border rounded"
          />
        </div>
        <div className="mb-4">
          <label htmlFor="lastName">Last Name:</label>
          <input
            type="text"
            id="lastName"
            value={lastName}
            onChange={(e) => setLastName(e.target.value)}
            className="w-full p-2 border rounded"
          />
        </div>
        <div className="mb-4">
          <label htmlFor="email">Email:</label>
          <input
            type="email"
            id="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            className="w-full p-2 border rounded"
          />
        </div>
        {error && <p className="text-red-500 mb-4">{error}</p>}
        <button
          type="button"
          onClick={handleSubmit}
          className="bg-green-500 text-white p-2 rounded"
        >
          Submit
        </button>
        <button
          type="button"
          onClick={onClose}
          className="bg-red-500 text-white p-2 rounded mt-4"
        >
          Close
        </button>
      </form>
    </Modal>
  );
};

export default SignUpModal;
