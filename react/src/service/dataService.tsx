import axios from 'axios';

export const register = (
  email: string,
  password: string,
  phone: string,
  lastName: string,
  firstName: string
) => {
  axios
    .post(
      'http://localhost/auth/register',
      {
        email: email,
        user_name: 'userNa',
        password: password,
        phone_number: phone,
        last_name: lastName,
        first_name: firstName
      },
      { withCredentials: true }
    )
    .then((r) => console.log(r));
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
