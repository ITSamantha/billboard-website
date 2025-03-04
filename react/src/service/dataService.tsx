import axios from 'axios';

export const BASE_URL = 'https://api.otiva.space/';
export const BASE_WS_URL = 'wss://api.otiva.space/';

export const createApi = () => {
  let apiInstance = axios.create({
    baseURL: BASE_URL,
    withCredentials: false,
    headers: {
      'Content-type': 'application/json',
      'x-jwt-access-token': localStorage.getItem('access_token'),
      'x-jwt-refresh-token': localStorage.getItem('refresh_token')
    }
  });
  apiInstance.interceptors.response.use(
    function (response) {
      return response;
    },
    function (error) {
      let response = error.response;
      if (response.status !== 401) throw error;
      if (
        response.config.url.includes('login') ||
        response.config.url.includes('register') ||
        response.config.url.includes('refresh')
      ) {
        return Promise.reject(error);
      }
      apiInstance
        .post('auth/refresh')
        .then((response) => {
          localStorage.setItem('access_token', response.data.access_token);
          localStorage.setItem('refresh_token', response.data.refresh_token);
          window.location.reload();
        })
        .catch((e) => {
          localStorage.clear();
          window.location.replace('/login');
        });
    }
  );
  return apiInstance;
};

let api = createApi();

export const register = (
  email: string,
  password: string,
  phone: string,
  lastName: string,
  firstName: string
) => {
  return api
    .post('auth/register', {
      email: email,
      password: password,
      phone_number: phone,
      last_name: lastName,
      first_name: firstName
    })
    .then((response) => {
      localStorage.setItem('access_token', response.data.access_token);
      localStorage.setItem('refresh_token', response.data.refresh_token);
      api = createApi();
      return response.data;
    });
};

export const login = async (email: string, password: string) => {
  return await api
    .post('auth/login', {
      email: email,
      password: password
    })
    .then((response) => {
      localStorage.setItem('access_token', response.data.access_token);
      localStorage.setItem('refresh_token', response.data.refresh_token);
      api = createApi();
      return response.data;
    })
    .catch((error) => {
      throw new Error('Incorrect credentials. Please try again.');
    });
};

export const refreshToken = async (id: number) => {
  return await api
    .post(`auth/refresh`)
    .then((response) => response.data)
    .catch((error) => console.error('Error refresh token:', error));
};

export const logout = () => {
  api
    .post('auth/logout', {})
    .then((response) => {
      localStorage.clear();
    })
    .catch((error) => console.error('Error fetching logout:', error));
};

export const getCategory = async (categoryId: number) => {
  return await api
    .get(`categories/${categoryId}`)
    .then((response) => response.data)
    .catch((error) => console.error('Error fetching countries:', error));
};

export const getCategories = (categorySlug: string | undefined) => {
  return [
    { id: 1, name: 'first', isLast: true },
    { id: 2, name: 'second', isLast: false }
  ];
};

export const getCategoriesList = async () => {
  return await api
    .get('categories')
    .then((response) => {
      return response.data;
    })
    .catch((error) => {
      throw error;
    });
};

export const getFilterList = async (categoryId: number) => {
  return await api
    .get('categories/' + categoryId + '/filters')
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

export const createAd = async (
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
  flat: string | undefined,
  photos: string[]
) => {
  return await api
    .post('advertisements', {
      title: title,
      user_description: description,
      ad_type_id: adTypeId,
      price: price,
      category_id: categoryId,
      ad_tags: adTags,
      ad_photos: photos,
      city_id: cityId,
      address_id: null,
      country_id: countryId,
      street: street,
      house: house,
      flat: flat
    })
    .then((r) => r.data);
};

export const getCountries = async () => {
  return await api
    .get('countries')
    .then((response) => response.data)
    .catch((error) => console.error('Error fetching countries:', error));
};

export const getCities = async () => {
  return await api
    .get('cities')
    .then((response) => response.data)
    .catch((error) => console.error('Error fetching cities:', error));
};

export const getMyUser = async () => {
  return await api
    .get('users/me')
    .then((response) => response.data)
    .catch((error) => console.error('Error fetching my user:', error));
};

export const getUserById = async (id: number) => {
  return await api
    .get(`users/${id}`)
    .then((response) => response.data)
    .catch((error) => console.error('Error fetching user:', error));
};

export const getAdvertisementById = async (id: number) => {
  return await api
    .get(`advertisements/${id}`)
    .then((response) => response.data)
    .catch((error) => console.error('Error fetching advertisement:', error));
};

export const getAdvertisementTypes = async () => {
  return await api
    .get(`advertisements/ad_type`)
    .then((response) => response.data)
    .catch((error) => console.error('Error fetching advertisement types:', error));
};

export const addToFavorites = async (id: number) => {
  return await api
    .post(`advertisements/favourites`, { advertisement_id: id })
    .then((response) => response.data)
    .catch((error) => console.error('Error add to favorites:', error));
};

export const deleteFromFavorites = async (id: number) => {
  console.log(id);
  return await api
    .delete(`advertisements/favourites/${id}`)
    .then((response) => response.data)
    .catch((error) => console.error('Error delete from favorites:', error));
};

export const getAdvertisementsByPage = async (
  page: number,
  perPage: number,
  categoryId?: number
) => {
  if (Number.isNaN(categoryId)) {
    return await api
      .get(`advertisements`, {
        params: { page: page, per_page: perPage }
      })
      .then((response) => response.data)
      .catch((error) => console.error('Error fetching advertisements:', error));
  }
  return await api
    .get(`advertisements`, {
      params: { page: page, per_page: perPage, category_id: categoryId }
    })
    .then((response) => response.data)
    .catch((error) => console.error('Error fetching advertisements:', error));
};

export const sendMessage = async (id: number, message: string) => {
  return await api
    .post(`chats/${id}/messages`, { text: message })
    .then((response) => response.data)
    .catch((error) => console.error('Error sending message:', error));
};

export const createChat = async (id: number) => {
  return await api
    .post(`chats`, { user_id: id })
    .then((response) => response.data)
    .catch((error) => console.error('Error creating chat:', error));
};

export const getChat = async (id: number) => {
  return await api
    .get(`chats/${id}`)
    .then((response) => response.data)
    .catch((error) => console.error('Error getting chat:', error));
};

export const getAllChats = async () => {
  return await api
    .get(`chats`)
    .then((response) => response.data)
    .catch((error) => console.error('Error getting all chats:', error));
};

export const sendCode = async () => {
  return await api
    .post(`phone/send_code`)
    .then((response) => response.data)
    .catch((error) => console.error('Error sending code:', error));
};

export const tryCode = async (code: string) => {
  return await api
    .post(`phone/verify`, {
      code: code
    })
    .then((response) => {
      console.log('???', response);
      return response.data;
    })
    .catch((error) => {
      console.error('Error verifying code:', error);
      throw error;
    });
};

export const getSubscriptions = async () => {
  return await api
    .get('tariffs')
    .then((response) => response.data)
    .catch((error) => console.error('Error getting subscriptions:', error));
};

export const createPayment = async (tariff: number) => {
  return await api
    .post('payments/create', { tariff_id: tariff })
    .then((response) => response.data)
    .catch((error) => console.error('Error creating payment:', error));
};

export const getChatId = async (userId: number) => {
  return await api
    .post('chats', { user_id: userId })
    .then((response) => response.data)
    .catch((error) => console.error('Error getting chat id:', error));
};

export const getMyAddresses = async (userId: number) => {
  return await api
    .get('addresses?user_id=' + userId)
    .then((response) => response.data)
    .catch((error) => console.error('Error getting my addresses', error));
};

export const deleteAdvertisement = async (id: number) => {
  return await api
    .delete(`/advertisements/${id}`)
    .then((response) => response.data)
    .catch((error) => console.error('Error deleting advertisement', error));
};
