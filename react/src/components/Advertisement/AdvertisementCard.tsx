import React, { useEffect, useState } from 'react';
import { Link, useParams } from 'react-router-dom';
import {
  addToFavorites,
  deleteFromFavorites,
  getAdvertisementById
} from '../../service/dataService';
import Loader from '../Loader';
import { Button } from '@mui/material';
import FavoriteBorderIcon from '@mui/icons-material/FavoriteBorder';
import FavoriteIcon from '@mui/icons-material/Favorite';
import { useDispatch, useSelector } from 'react-redux';
import { fetchMyUser, selectMyUser } from '../../redux/slices/MyUserSlice';

const AdvertisementCard = () => {
  const { id } = useParams();
  const [ad, setAd] = useState<AdInfo | null>(null);
  const user = useSelector(selectMyUser);
  const dispatch = useDispatch();

  useEffect(() => {}, [user]);

  useEffect(() => {
    async function fetchData() {
      let data = await getAdvertisementById(Number(id));
      await dispatch(fetchMyUser() as any);
      setAd(data);
    }
    fetchData();
  }, [dispatch, id]);

  const handleFavorite = async () => {
    await addToFavorites(Number(id));
  };

  const handleUnfavorite = async () => {
    await deleteFromFavorites(Number(id));
  };

  if (!ad) {
    return <Loader />;
  }

  return (
    <div className="AdvertisementCard">
      <img src="https://http.cat/300" alt="Advertisement" height={'300px'} />
      <div>{ad.title}</div>
      <div>{ad.user_description}</div>
      <div>Price: {ad.price}</div>
      <div>{ad.created_at_str}</div>
      <div>{ad.reviews}</div>
      <div>Type: {ad.ad_type.title}</div>
      <div>Category: {ad.category.title}</div>
      <Link to={`/profile/${ad.user.id}`}>
        <div>
          Seller: {ad.user.first_name} {ad.user.last_name}
        </div>
      </Link>
      {user &&
        user.ad_favourites.some((ad: AdInfo) => {
          return ad.id === Number(id);
        }) && (
          <Button onClick={handleUnfavorite}>
            <FavoriteIcon />
          </Button>
        )}
      {user &&
        user.ad_favourites.find((ad: AdInfo) => {
          return ad.id === Number(id);
        }) === undefined && (
          <Button onClick={handleFavorite}>
            <FavoriteBorderIcon />
          </Button>
        )}

      <Link to={'/chat'}>
        <Button>Contact the seller</Button>
      </Link>
    </div>
  );
};

export default AdvertisementCard;
