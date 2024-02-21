// Home.js
import React, { useEffect, useState } from 'react';
import { useAuth } from '../component/authentication/authentication';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import { getCurrentUser, getAllUsers, deleteUserById, getAllProduct } from '../api';

const Home = () => {
  const { setIsLoggedIn, isLoggedIn, logout } = useAuth();
  const navigate = useNavigate();

  const [isAdminUser, setIsAdminUser] = useState(false)
  const [users, setUsers] = useState([]);
  const [product, setProduct] = useState([]);
  const [selectedMenu, setSelectedMenu] = useState(null);
  const [error, setError] = useState('');

  //use the userId in local storage to fetch the User info first. 
  //Return login please, if there is no userID in the local storage
  useEffect(() => {

    const checkCurrentUser = async () => {
      const storedUserId = localStorage.getItem('userId');

      if (storedUserId) {
        setIsLoggedIn(true);
        const response = await getCurrentUser(storedUserId);


        if (response.data.user.role === 'Admin') {
          setIsAdminUser(true);
        }
      } else {
        setIsLoggedIn(false);
      }
    };

    checkCurrentUser();
  }, []);


  const handleDeleteUser = async (userId, index) => {
    await deleteUserById(userId);
    const updatedUsers = [...users];
    // Remove the user at the specified index
    updatedUsers.splice(index, 1);
    setUsers(updatedUsers)
  };

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  const handleHomeMenuClick = async () => {
    setSelectedMenu("Home");
    const response = await getAllProduct();
    console.log(response.data)
    setProduct(response.data.product_list)
  };


  const handleAdminMenuClick = async () => {
    setSelectedMenu("Admin");
    if (isAdminUser) {
      const response = await getAllUsers();
      setUsers(response.data.user_list)
      console.log(users)

    } else {
      setError('You are not an Admin, please use Admin, 123456 to login as an admin');
    }
  };
  const handleUserMenuClick = () => {
    setSelectedMenu("User");
  };

  return (
    <div className="flex h-screen text-2xl">


      <div className="w-3/4 p-4">
        <div className="flex justify-between items-center mb-4">
     
          <h2 className="mb-0">Home Page</h2>
          <button onClick={handleLogout} className="bg-red-500 text-white p-2 rounded">Logout</button>
        </div>
        {(error && selectedMenu === "Admin") && <p className="text-red-500 mb-4">{error}</p>}
        {isLoggedIn ? (
          <>
            <p>Welcome, {isAdminUser ? 'You are an Admin' : 'You are a User'}!</p>
            <div className="w-full bg-gray-200 p-4">
              <ul className="flex">
                <li className={`mr-4 ${selectedMenu === 'Home' ? 'text-blue-500' : ''}`}>
                  <button onClick={() => handleHomeMenuClick()}>Home</button>
                </li>

                <li className={`mr-4 ${selectedMenu === 'Admin' ? 'text-blue-500' : ''}`}>
                  <button onClick={() => handleAdminMenuClick()}>Admin</button>
                </li>

                <li className={`mr-4 ${selectedMenu === 'User' ? 'text-blue-500' : ''}`}>
                  <button onClick={() => handleUserMenuClick()}>User</button>
                </li>
              </ul>
            </div>


            <div className="mb-4">
              {selectedMenu === 'User' && (
                <div className="flex flex-col w-1/4">
                  <button className="bg-blue-500 text-white p-2 rounded mb-2">Profile</button>
                  <button onClick={handleLogout} className="bg-red-500 text-white p-2 rounded">Logout</button>
                </div>
              )}

              {selectedMenu === 'Admin' && (
                <div className="grid grid-cols-1 gap-4">
                  {users.map((user, index) => (
                    <div key={index} className="border p-4 rounded shadow mb-4 flex justify-between items-center">
                      <div>
                        <p className="font-bold">Username: {user.username}</p>
                        <p>Email: {user.email}</p>
                        <p>Name: {`${user.firstname} ${user.lastname}`}</p>
                      </div>
                      <button
                        onClick={() => handleDeleteUser(user.ID, index)}
                        className=" p-2 rounded"
                      >
                        Delete
                      </button>
                    </div>
                  ))}


                </div>

              )}


              {selectedMenu === 'Home' && (
                <div className="grid grid-cols-1 gap-4">
                  {product.map((product, index) => (
                    <div key={index} className="border p-4 rounded shadow mb-4 flex justify-between items-center">
                      <div>
                        <p className="font-bold"> Name:  {product.Name}</p>
                        <p>Description: {product.description}</p>
                        <p>Price: CAD {`${product.price} `}</p>
                      </div>
                    
                    </div>
                  ))}


                </div>

              )}
            </div>
          </>
        ) : (
          <p>Please log in to access the home page.</p>
        )}
      </div>
    </div>
  );
};

export default Home;
