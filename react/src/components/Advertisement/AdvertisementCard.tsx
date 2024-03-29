import { Button } from 'antd';
import React, { useEffect, useState } from 'react';
import { Link, useParams } from 'react-router-dom';
import { getAdvertisementById } from '../../service/dataService';

type AdInfo = {
  title: string;
  description: string;
  address: string;
  tags: string[];
  isBooking: boolean;
  reviews: string[];
  creationDate: string;
  price: number;
  userId: number;
  status: string;
  photosPaths: string[];
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
    return <div>Loading...</div>;
  }

  return (
    <div className="AdvertisementCard">
      <div>{}</div>
      <Link to={'/chat'}>
        <Button>Contact the seller</Button>
      </Link>
    </div>
  );
};

export default AdvertisementCard;
