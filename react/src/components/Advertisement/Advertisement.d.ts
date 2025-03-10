type AdAddress = {
  id: number;
  street: string;
  house: string;
  flat: string;
  longitude: number;
  latitude: number;
  country: {
    id: number;
    title: string;
  };
  city: {
    id: number;
    title: string;
  };
};

type AdInfo = {
  id: number;
  title: string;
  user_description: string;
  auto_booking: boolean;
  bookable: boolean;
  created_at_str: string;
  reviews: Review[];
  deleted_at: string | null;
  updated_at: string;
  created_at: string;
  ad_photos: Photo[];
  ad_tags: string[];
  category: Category;
  creationDate: string;
  price: number;
  userId: number;
  ad_status: Status;
  ad_type: AdType;
  address: AdAddress;
  user: ProfileInfo;
};

type Photo = {
  id: number;
  link: string;
};

type Category = {
  id: number;
  title: string;
  url: string;
  children?: Category[];
};

type Review = {
  id: number;
  rating: number;
  text: string;
  advertisement_id: number;
  created_at: string;
  created_at_str: string;
  updated_at: string;
  updated_at_str: string;
  deleted_at: string | null;
};

type Status = {
  id: number;
  title: string;
  is_shown: boolean;
};
type AdType = {
  id: number;
  title: string;
};

type ProfileInfo = {
  id: number;
  avatar: string;
  email: string;
  phone_number: string;
  last_name: string;
  first_name: string;
  ad_favourites: AdInfo[];
  advertisements: AdInfo[];
};
