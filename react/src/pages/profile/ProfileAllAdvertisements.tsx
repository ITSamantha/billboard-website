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
    <div>
      <AdvertisementBlock
        advertisements={user.advertisements}
        advertisementsInRow={4}
        maxAdvertisements={user.advertisements.length}
      />
    </div>
  );
};

export default ProfileAllAdvertisements;
