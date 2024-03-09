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
