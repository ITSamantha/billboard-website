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
import { useSelector } from 'react-redux';
import { selectMyUser } from '../../redux/slices/MyUserSlice';

const AdvertisementCard = () => {
  const { id } = useParams();
  const [ad, setAd] = useState<AdInfo | null>(null);
  const user = useSelector(selectMyUser);

  useEffect(() => {
    async function fetchData() {
      let data = await getAdvertisementById(Number(id));
      setAd(data);
    }
    fetchData();
  }, [id]);

  useEffect(() => {}, [user]);

  const handleFavorite = () => {
    addToFavorites(Number(id));
  };

  const handleUnfavorite = () => {
    deleteFromFavorites(Number(id));
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
      <Link to={`/profile/${ad.user.id}`}>
        <div>
          Seller: {ad.user.first_name} {ad.user.last_name}
        </div>
      </Link>
      {user &&
        !user.advertisements.some((ad: AdInfo) => ad.id === Number(id)) &&
        user.ad_favourites.some((ad: AdInfo) => ad.id === Number(id)) && (
          <Button onClick={handleFavorite}>
            <FavoriteIcon />
          </Button>
        )}
      {user &&
        !user.advertisements.some((ad: AdInfo) => ad.id === Number(id)) &&
        !user.ad_favourites.some((ad: AdInfo) => ad.id === Number(id)) && (
          <Button onClick={handleUnfavorite}>
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
