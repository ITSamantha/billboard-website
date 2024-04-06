import axios from 'axios';

const BASE_URL = 'https://api.uvuv643.ru/';

const createApi = () => {
  return axios.create({
    baseURL: BASE_URL,
    withCredentials: false,
    headers: {
      'Content-type': 'application/json',
      'x-jwt-access-token': localStorage.getItem('access_token')
    }
  });
};

let api = createApi();


export const register = (
  email: string,
  password: string,
  phone: string,
  lastName: string,
  firstName: string
) => {
  api.post(
    'auth/register',
    {
      email: email,
      password: password,
      phone_number: phone,
      last_name: lastName,
      first_name: firstName
    }
  )
    .then((response) => {
      localStorage.setItem('access_token', response.data.access_token);
      localStorage.setItem('refresh_token', response.data.refresh_token);
      api = createApi();
      return response.data;
    })
    .catch((error) => console.error('Error fetching register:', error));
};

export const login = async (email: string, password: string) => {
  return await api.post('auth/login', {
    email: email,
    password: password
  })
    .then((response) => {
      localStorage.setItem('access_token', response.data.access_token);
      localStorage.setItem('refresh_token', response.data.refresh_token);
      api = createApi();
      return response.data;
    })
    .catch((error) => console.error('Error fetching login:', error));
};

export const refreshToken = async (id: number) => {
  return await api.post(`auth/refresh`)
    .then((response) => response.data)
    .catch((error) => console.error('Error refresh token:', error));
};

export const logout = () => {
  api.post('auth/logout', {})
    .then((response) => response.data)
    .catch((error) => console.error('Error fetching logout:', error));
};

export const getCategories = (categorySlug: string | undefined) => {
  return [
    { id: 1, name: 'first', isLast: true },
    { id: 2, name: 'second', isLast: false }
  ];
};

export const getCategoriesList = async () => {
  return await api.get('categories')
    .then((response) => {
      return response.data;
    })
    .catch((error) => {
      throw error;
    });
};

export const getFilterList = async (categoryId: string) => {
  return await api.get('categories/' + categoryId + '/filters')
    .then((response) => {
      return response.data;
    })
    .catch((error) => {
      throw error;
    });
};

export const getProducts = (categorySlug: string | undefined) => {
  return [
    { id: 1, title: 'first', description: 'first description' },
    { id: 2, title: 'second', description: 'second description' },
    { id: 2, title: 'second', description: 'second description' },
    { id: 2, title: 'second', description: 'second description' }
  ];
};

export const getFilters = (categorySlug: string | undefined) => {
  return [
    {
      id: 1,
      name: 'color',
      type: 'checkbox',
      values: [
        { id: 1, value: 'red' },
        { id: 2, value: 'green' },
        { id: 3, value: 'yellow' }
      ]
    },
    {
      id: 2,
      name: 'size',
      type: 'checkbox',
      values: [
        { id: 1, value: 's' },
        { id: 2, value: 'm' },
        { id: 3, value: 'l' }
      ]
    }
  ];
};

export const createAd = (
  title: string,
  description: string,
  price: number,
  adTypeId: number,
  categoryId: number,
  adTags: string[],
  cityId: number,
  countryId: number,
  street: string,
  house: string,
  flat: string | undefined
) => {
  api.post(
    'advertisements',
    {
      title: title,
      user_description: description,
      ad_type_id: adTypeId,
      price: price,
      category_id: categoryId,
      ad_tags: adTags,
      city_id: cityId,
      country_id: countryId,
      street: street,
      house: house,
      flat: flat
    }
  )
    .then((r) => {
      console.log(r);
      return r.data;
    });
};

export const getCountries = async () => {
  return await api.get('countries')
    .then((response) => response.data)
    .catch((error) => console.error('Error fetching countries:', error));
};

export const getCities = async () => {
  return await api.get('cities')
    .then((response) => response.data)
    .catch((error) => console.error('Error fetching cities:', error));
};

export const getMyUser = async () => {
  return await api.get('users/me')
    .then((response) => response.data)
    .catch((error) => console.error('Error fetching my user:', error));
};

export const getUserById = async (id: number) => {
  return await api.get(`users/${id}`)
    .then((response) => response.data)
    .catch((error) => console.error('Error fetching user:', error));
};

export const getAdvertisementById = async (id: number) => {
  return await api.get(`advertisements/${id}`)
    .then((response) => response.data)
    .catch((error) => console.error('Error fetching advertisement:', error));
};

export const getAdvertisementTypes = async () => {
  return await api.get(`advertisements/ad_type`)
    .then((response) => response.data)
    .catch((error) => console.error('Error fetching advertisement types:', error));
};

export const addToFavorites = async (id: number) => {
  return await api.post(`advertisements/favourites`, { advertisement_id: id })
    .then((response) => response.data)
    .catch((error) => console.error('Error add to favorites:', error));
};

export const deleteFromFavorites = async (id: number) => {
  return await api.delete(`advertisements/favourites/${id}`)
    .then((response) => response.data)
    .catch((error) => console.error('Error delete from favorites:', error));
};

export const getAdvertisementsByPage = async (
  page: number,
  perPage: number,
  categoryId: number
) => {
  return await api.get(`advertisements`, {
    params: { page: page, per_page: perPage, category_id: categoryId }
  })
    .then((response) => response.data)
    .catch((error) => console.error('Error fetching advertisements:', error));
};

export const sendMessage = async (id: number, message: string) => {
  return await api.post(`chats/${id}/messages`, { text: message })
    .then((response) => response.data)
    .catch((error) => console.error('Error sending message:', error));
};

export const createChat = async (id: number) => {
  return await api.post(`chats`, { user_id: id })
    .then((response) => response.data)
    .catch((error) => console.error('Error creating chat:', error));
};

export const getChat = async (id: any) => {
  return await api.get(`chats/${id}`)
    .then((response) => response.data)
    .catch((error) => console.error('Error getting chat:', error));
};

export const getAllChats = async () => {
  return await api.get(`chats`)
    .then((response) => response.data)
    .catch((error) => console.error('Error getting all chats:', error));
};
