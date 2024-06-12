import { useSelector } from 'react-redux';
import AdvertisementBlock from '../../components/Advertisement/AdvertisementBlock';
import { selectMyUser } from '../../redux/slices/MyUserSlice';
import { useEffect } from 'react';
import Loader from '../../components/Loader';

const Favorites = () => {
  const user = useSelector(selectMyUser);

  useEffect(() => {}, [user]);

  if (!user) {
    return (
      <div>
        <Loader />
      </div>
    );
  }

  return (
    <div className="container">
      <div className="Advertisements__All">
        <h1 className="Advertisements__Title">Your favourite advertisements</h1>
        <AdvertisementBlock
          advertisements={user.ad_favourites}
          advertisementsInRow={4}
          maxAdvertisements={user?.ad_favourites?.length}
        />
      </div>
    </div>
  );
};

export default Favorites;
