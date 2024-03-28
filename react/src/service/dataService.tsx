import axios from 'axios';

const BASE_URL = 'http://localhost/';

export const register = (
  email: string,
  password: string,
  phone: string,
  lastName: string,
  firstName: string
) => {
  axios
    .post(
      BASE_URL + 'auth/register',
      {
        email: email,
        password: password,
        phone_number: phone,
        last_name: lastName,
        first_name: firstName
      },
      { withCredentials: true }
    )
    .then((r) => {
      console.log(r);
      return r.data;
    });
};

export const login = (email: string, password: string) => {
  axios
    .post(
      BASE_URL + 'auth/login',
      {
        email: email,
        password: password
      },
      { withCredentials: true }
    )
    .then((r) => {
      console.log(r);
      return r.data;
    });
};

export const logout = () => {
  axios
    .post(BASE_URL + 'auth/logout', {}, { withCredentials: true })
    .then((r) => console.log(r))
    .catch((e) => console.log(e));
};

export const getCategories = (categorySlug: string | undefined) => {
  return [
    { id: 1, name: 'first', isLast: true },
    { id: 2, name: 'second', isLast: false }
  ];
};

export const getCategoriesList = () => {
  return [
    {
      id: 1,
      name: 'clothes',
      children: [
        { id: 1, name: 'men', children: [] },
        {
          id: 2,
          name: 'women',
          children: [
            { id: 1, name: 'dresses', children: [] },
            { id: 2, name: 'skirts', children: [] }
          ]
        }
      ]
    },
    { id: 2, name: 'pets', children: [] }
  ];
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
  axios
    .post(
      BASE_URL + 'auth/register',
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
      },
      { withCredentials: true }
    )
    .then((r) => {
      console.log(r);
      return r.data;
    });
};

export const getCountries = async () => {
  return await axios
    .get(BASE_URL + 'countries')
    .then((response) => response.data)
    .catch((error) => console.error('Error fetching countries:', error));
};

export const getCities = async () => {
  return await axios
    .get(BASE_URL + 'cities')
    .then((response) => response.data)
    .catch((error) => console.error('Error fetching cities:', error));
};
