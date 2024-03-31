import React, { useEffect, useState } from 'react';
import { Link, useParams } from 'react-router-dom';
import { getAdvertisementById } from '../../service/dataService';
import Loader from '../Loader';
import { Button } from '@mui/material';

const AdvertisementCard = () => {
  const { id } = useParams();
  const [ad, setAd] = useState<AdInfo | null>(null);

  useEffect(() => {
    async function fetchData() {
      let data = await getAdvertisementById(Number(id));
      setAd(data);
    }
    fetchData();
  }, [id]);

  if (!ad) {
    return <Loader />;
  }

  return (
    <div className="AdvertisementCard">
      <div>{ad.title}</div>
      <div>{ad.user_description}</div>
      <div>Price: {ad.price}</div>
      <div>{ad.created_at_str}</div>
      <div>{ad.reviews}</div>

      <Link to={'/chat'}>
        <Button>Contact the seller</Button>
      </Link>
    </div>
  );
};

export default AdvertisementCard;
