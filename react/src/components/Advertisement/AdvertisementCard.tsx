import { Button, Spin } from 'antd';
import React, { useEffect, useState } from 'react';
import { Link, useParams } from 'react-router-dom';
import { getAdvertisementById } from '../../service/dataService';
import Loader from '../Loader';

type Status = {
  id: number;
  title: string;
  is_shown: boolean;
};
type AdType = {
  id: number;
  title: string;
};

type AdInfo = {
  id: number;
  title: string;
  user_description: string;
  auto_booking: boolean;
  bookable: boolean;
  created_at_str: string;
  reviews: string[];
  deleted_at: string | null;
  updated_at: string;
  created_at: string;
  ad_photos: string[];
  ad_tags: string[];
  creationDate: string;
  price: number;
  userId: number;
  ad_status: Status;
  ad_type: AdType;
  address: object;
  user: object;
};

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
