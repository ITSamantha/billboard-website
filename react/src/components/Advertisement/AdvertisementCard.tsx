import React, { useEffect, useState } from 'react';
import { Link, useNavigate, useParams } from 'react-router-dom';
import {
  addToFavorites,
  deleteFromFavorites,
  getAdvertisementById,
  getChatId
} from '../../service/dataService';
import Loader from '../Loader';
import { Button } from '@mui/material';
import FavoriteBorderIcon from '@mui/icons-material/FavoriteBorder';
import FavoriteIcon from '@mui/icons-material/Favorite';
import { useDispatch, useSelector } from 'react-redux';
import { fetchMyUser, selectMyUser } from '../../redux/slices/MyUserSlice';
import ReviewBlock from '../Review/ReviewBlock';

const AdvertisementCard = () => {
  const { id } = useParams();
  const [ad, setAd] = useState<AdInfo | null>(null);
  const user = useSelector(selectMyUser);
  const dispatch = useDispatch();
  const [isFavourite, setIsFavourite] = useState<boolean>();
  const navigate = useNavigate();

  useEffect(() => {
    async function fetchData() {
      let data = await getAdvertisementById(Number(id));
      await dispatch(fetchMyUser() as any);
      setAd(data);
      if (user) {
        const isFav = user.ad_favourites.some((ad: AdInfo) => ad.id === Number(id));
        setIsFavourite(isFav);
      }
    }
    fetchData();
  }, [dispatch, id]);

  const handleFavorite = async () => {
    setIsFavourite(true);
    await addToFavorites(Number(id));
    await dispatch(fetchMyUser() as any);
  };

  const handleUnfavorite = async () => {
    setIsFavourite(false);
    await deleteFromFavorites(Number(id));
    await dispatch(fetchMyUser() as any);
  };

  const handleGetChatId = async () => {
    const chatId = await getChatId(ad!.user.id);
    navigate(`/chat/${chatId.id}`);
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
      <div>Type: {ad.ad_type.title}</div>
      <div>Category: {ad.category.title}</div>
      <Link to={`/profile/${ad.user.id}`}>
        <div>
          Seller: {ad.user.first_name} {ad.user.last_name}
        </div>
      </Link>
      {isFavourite ? (
        <Button onClick={handleUnfavorite}>
          <FavoriteIcon />
        </Button>
      ) : (
        <Button onClick={handleFavorite}>
          <FavoriteBorderIcon />
        </Button>
      )}
      {user && user.id !== ad.user.id ? (
        <Button onClick={handleGetChatId}>Contact the seller</Button>
      ) : (
        <></>
      )}

      <ReviewBlock reviews={ad.reviews} />
    </div>
  );
};

export default AdvertisementCard;
