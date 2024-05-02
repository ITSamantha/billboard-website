import { useEffect, useState } from 'react';
import '../scss/upload-form.scss';
import {
  createAd,
  getAdvertisementTypes,
  getCategories,
  getCategoriesList,
  getCities,
  getCountries
} from '../service/dataService';
import { Autocomplete, Button, Input, TextField } from '@mui/material';
import Loader from './Loader';
import { useNavigate } from 'react-router-dom';

type Data = {
  id: number;
  title: string;
};

const UploadForm = () => {
  const [title, setTitle] = useState<string>('');
  const [description, setDescription] = useState<string>('');
  const [adType, setAdType] = useState<number | undefined>(undefined);
  const [price, setPrice] = useState<number>(0);
  const [adTags, setAdTags] = useState<[]>([]);
  const [categoryId, setCategoryId] = useState<number | undefined>(undefined);
  const [categories, setCategories] = useState<Data[]>([]);
  const [adPhotos, setAdPhotos] = useState();
  const [city, setCity] = useState<number | undefined>(undefined);
  const [country, setCountry] = useState<number | undefined>(undefined);
  const [street, setStreet] = useState<string>('');
  const [house, setHouse] = useState<string>('');
  const [flat, setFlat] = useState<string>('');
  const [cities, setCities] = useState<Data[]>([]);
  const [countries, setCountries] = useState<Data[]>([]);
  const [adTypes, setAdTypes] = useState<Data[]>([]);
  const [error, setError] = useState<string>('');
  const navigate = useNavigate();

  useEffect(() => {
    async function fetchData() {
      let countries = await getCountries();
      let cities = await getCities();
      let types = await getAdvertisementTypes();
      let categories = await getCategoriesList();
      setCities(cities);
      setCountries(countries);
      setAdTypes(types);
      setCategories(categories);
    }
    fetchData();
  }, []);

  const handleCreate = async () => {
    if (
      !title ||
      !description ||
      !adType ||
      price === 0 ||
      !categoryId ||
      !city ||
      !country ||
      !street ||
      !house
    ) {
      console.log(price);
      console.log(adType);
      console.log(categoryId);
      console.log(city);
      console.log(country);
      setError('All marked fields should be not empty');
      return;
    }
    setError('');
    let ad = await createAd(
      title,
      description,
      price,
      adType,
      categoryId,
      adTags,
      city,
      country,
      street,
      house,
      flat
    ).then((r) => navigate(`/advertisement/${r.id}`));
  };

  if (!cities && !countries && !adTypes) {
    return (
      <div>
        <Loader />
      </div>
    );
  }

  return (
    <div className="upload-form">
      <div>Create post</div>
      <Input
        placeholder="Title *"
        type="text"
        required
        onChange={(e) => {
          setTitle(e.target.value);
        }}
      />
      <TextField
        id="outlined-multiline-static"
        label="Description"
        multiline
        rows={4}
        required
        value={description}
        onChange={(e) => {
          setDescription(e.target.value);
        }}
      />
      <Autocomplete
        id=""
        options={adTypes}
        getOptionLabel={(option) => option?.title}
        style={{ width: 500, color: 'white' }}
        onChange={(event, value) => setAdType((value as Data | null)?.id)}
        renderInput={(params) => (
          <TextField
            style={{ width: 500, background: 'white' }}
            {...params}
            placeholder="Advertisement type *"
          />
        )}
      />
      <Autocomplete
        id=""
        options={categories}
        getOptionLabel={(option) => option?.title}
        style={{ width: 500, color: 'white' }}
        onChange={(event, value) => setCategoryId((value as Data | null)?.id)}
        renderInput={(params) => (
          <TextField
            style={{ width: 500, background: 'white' }}
            {...params}
            placeholder="Category *"
          />
        )}
      />
      <TextField
        prefix="₪"
        // suffix="ILS"
        placeholder="Price *"
        inputProps={{ min: '0' }}
        type="number"
        value={price}
        onChange={(e) => {
          let numVal = parseFloat(e.target.value);
          numVal < 0 ? setPrice(-numVal) : setPrice(numVal);
        }}
      />
      <Autocomplete
        id=""
        options={countries}
        getOptionLabel={(option) => option?.title}
        style={{ width: 500, color: 'white' }}
        onChange={(event, value) => setCountry((value as Data | null)?.id)}
        renderInput={(params) => (
          <TextField
            style={{ width: 500, background: 'white' }}
            {...params}
            placeholder="Country *"
          />
        )}
      />
      <Autocomplete
        id=""
        options={cities}
        getOptionLabel={(option) => option?.title}
        style={{ width: 500, color: 'white' }}
        onChange={(event, value) => setCity((value as Data | null)?.id)}
        renderInput={(params) => (
          <TextField style={{ width: 500, background: 'white' }} {...params} placeholder="City *" />
        )}
      />
      <Input
        placeholder="Street *"
        type="text"
        onChange={(e) => {
          setStreet(e.target.value);
        }}
      />
      <Input
        placeholder="House *"
        type="text"
        onChange={(e) => {
          setHouse(e.target.value);
        }}
      />
      <Input
        placeholder="Flat"
        type="text"
        onChange={(e) => {
          setFlat(e.target.value);
        }}
      />
      <div>{error}</div>
      {/* TODO: make text red */}
      <Button onClick={handleCreate}>Create</Button>
    </div>
  );
};

export default UploadForm;
