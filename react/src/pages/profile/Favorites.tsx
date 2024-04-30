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
    <div>
      <AdvertisementBlock
        advertisements={user.ad_favourites}
        advertisementsInRow={4}
        maxAdvertisements={user.ad_favourites.length}
      />
    </div>
  );
};

export default Favorites;
