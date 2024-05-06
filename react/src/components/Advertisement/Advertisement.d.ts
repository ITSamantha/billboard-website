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
  category: Category;
  creationDate: string;
  price: number;
  userId: number;
  ad_status: Status;
  ad_type: AdType;
  address: object;
  user: ProfileInfo;
};

type Category = {
  id: number;
  title: string;
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
