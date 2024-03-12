import { useState, useEffect } from 'react';

type User = {
  picture: string;
  name: string;
  email: string;
};

const Profile = () => {
  const [user, setUser] = useState<User | null>(null);

  useEffect(() => {
    const fetchUser = async () => {
      // const userData = await getUserData();
      // setUser(userData);
    };

    fetchUser();
  }, []);

  if (!user) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <img src={user.picture} alt="User Profile"></img>
      <div>{user.name}</div>
      <div>{user.email}</div>
    </div>
  );
};

export default Profile;
