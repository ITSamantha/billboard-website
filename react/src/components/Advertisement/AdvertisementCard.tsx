import { Button } from 'antd';
import React from 'react';
import { Link } from 'react-router-dom';

type Props = {
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

const AdvertisementCard = ({ title, description, address }: Props) => {
  return (
    <div className="AdvertisementCard">
      <div>{title}</div>
      <Link to={'/chat'}>
        <Button>Contact the seller</Button>
      </Link>
    </div>
  );
};

export default AdvertisementCard;
