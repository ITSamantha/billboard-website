import React, { useState } from 'react';
import { Input } from 'antd';

// {
//     "first_name": "Lol",
//     "last_name": "Kekov",
//     "email": "user@gmail.com",
//     "password": "admin",
//     "phone_number": "+712312312",
//     "user_role_id": 1,
//     "city_id": 1,
//     "avatar_id": null
// }

const ProfileEdit = () => {

  const [firstName, setFirstName] = useState<string>('');
  const [lastName, setLastName] = useState<string>('');

  return (
    <div className="Profile__Edit">
      <h1>Edit your profile</h1>
      <div className="Profile__Edit__Input">
        <label htmlFor="first-name">First name</label>
        <Input
          id="first-name"
          placeholder="First Name"
          type="text"
          onChange={(e) => {
            setFirstName(e.target.value);
          }} />
      </div>
      <div className="Profile__Edit__Input">
        <label htmlFor="last-name">Last name</label>
        <Input
          id="last-name"
          placeholder="Last Name"
          type="text"
          onChange={(e) => {
            setLastName(e.target.value);
          }} />
      </div>

    </div>
  );

};

export default ProfileEdit;