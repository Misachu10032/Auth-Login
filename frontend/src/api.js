// api.js
import axios from 'axios';

const BASE_URL = 'http://localhost:5000/api';
const config = {
  headers: {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET,PUT,POST,DELETE,PATCH,OPTIONS"
  }
};

 const loginUser = async (loginForm) => {
  try {
    const response = await axios.post(`${BASE_URL}/login`, loginForm, config);

    return response;
  } catch (error) {

    throw error;
  }
};

const signUpUser = async (signUpForm) => {
  try {
    const response = await axios.post(`${BASE_URL}/sign_up`, signUpForm, config);

    return response;
  } catch (error) {

    throw error;
  }
};
const getCurrentUser = async (userId) => {
  try {
    const response = await axios.get(`${BASE_URL}/get_user_by_id/${userId}`, config);

    return response;
  } catch (error) {

    throw error;
  }
};
const getAllUsers = async () => {
  try {
    const response = await axios.get(`${BASE_URL}/get_all_users`, config);

    return response;
  } catch (error) {

    throw error;
  }
};

const deleteUserById = async (userId) => {
  try {
    const response = await axios.delete(`${BASE_URL}/delete_user_by_id/${userId}`, config);

    return response;
  } catch (error) {

    throw error;
  }
};

const getAllProduct = async () => {
  try {
    const response = await axios.get(`${BASE_URL}/get_all_products`, config);

    return response;
  } catch (error) {

    throw error;
  }
};
export  {loginUser,signUpUser,getCurrentUser,getAllUsers,deleteUserById,getAllProduct}