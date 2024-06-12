import { useDispatch, useSelector } from 'react-redux';
import AdvertisementBlock from '../../components/Advertisement/AdvertisementBlock';
import { fetchUser, selectUser } from '../../redux/slices/UserSlice';
import { useEffect } from 'react';
import { AppDispatch } from '../../redux/store';
import { useParams } from 'react-router-dom';
import Loader from '../../components/Loader';

const ProfileAllAdvertisements = () => {
  const dispatch = useDispatch<AppDispatch>();
  const user = useSelector(selectUser);
  const { id } = useParams();

  useEffect(() => {
    dispatch(fetchUser({ id }));
    console.log(user);
  }, [dispatch, id]);

  if (!user || !user.advertisements) {
    return (
      <div>
        <Loader />
      </div>
    );
  }
  return (
    <div className="container">
      <div className="Advertisements__All">
        <h1 className="Advertisements__Title">Your advertisements</h1>
        <AdvertisementBlock
          advertisements={user.advertisements}
          advertisementsInRow={4}
          maxAdvertisements={user.advertisements.length}
        />
      </div>
    </div>
  );
};

export default ProfileAllAdvertisements;
