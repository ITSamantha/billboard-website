import { useEffect, useState } from 'react';
import '../scss/upload-form.scss';
import { createAd, getAdvertisementTypes, getCities, getCountries } from '../service/dataService';
import { Autocomplete, Button, Input, TextField } from '@mui/material';

type Data = {
  id: number;
  title: string;
};

const UploadForm = () => {
  const [title, setTitle] = useState<string>('');
  const [description, setDescription] = useState<string>('');
  const [adType, setAdType] = useState<number>(0);
  const [price, setPrice] = useState<number>(0);
  const [adTags, setAdTags] = useState<[]>([]);
  const [categoryId, setCategoryId] = useState<number>(0);
  const [adPhotos, setAdPhotos] = useState();
  const [city, setCity] = useState<number>(0);
  const [country, setCountry] = useState<number>(0);
  const [street, setStreet] = useState<string>('');
  const [house, setHouse] = useState<string>('');
  const [flat, setFlat] = useState<string>('');
  const [cities, setCities] = useState<Data[]>([]);
  const [countries, setCountries] = useState<Data[]>([]);
  const [adTypes, setAdTypes] = useState<Data[]>([]);

  useEffect(() => {
    async function fetchData() {
      let countries = await getCountries();
      let cities = await getCities();
      let types = await getAdvertisementTypes();
      setCities(cities);
      setCountries(countries);
      setAdTypes(types);
    }
    fetchData();
  }, []);

  const handleCreate = () => {
    createAd(
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
    );
  };

  if (!cities && !countries && !adTypes) {
    return <div>Loading...</div>;
  }

  return (
    <div className="upload-form">
      <div>Create post</div>
      <Input
        placeholder="Title"
        type="text"
        onChange={(e) => {
          setTitle(e.target.value);
        }}
      />
      <TextField
        id="outlined-multiline-static"
        label="Description"
        multiline
        rows={4}
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
        onChange={(event, value) => console.log(value)}
        renderInput={(params) => (
          <TextField
            style={{ width: 500, background: 'white' }}
            {...params}
            placeholder="Advertisement type"
          />
        )}
      />
      <Input
        prefix="₪"
        // suffix="ILS"
        placeholder="Price"
        type="number"
        // min="0"
        onChange={(e) => {
          setTitle(e.target.value);
        }}
      />
      <Autocomplete
        id=""
        options={countries}
        getOptionLabel={(option) => option?.title}
        style={{ width: 500, color: 'white' }}
        onChange={(event, value) => console.log(value)}
        renderInput={(params) => (
          <TextField
            style={{ width: 500, background: 'white' }}
            {...params}
            placeholder="Country"
          />
        )}
      />
      <Autocomplete
        id=""
        options={cities}
        getOptionLabel={(option) => option?.title}
        style={{ width: 500, color: 'white' }}
        onChange={(event, value) => console.log(value)}
        renderInput={(params) => (
          <TextField style={{ width: 500, background: 'white' }} {...params} placeholder="City" />
        )}
      />
      <Input
        placeholder="Street"
        type="text"
        onChange={(e) => {
          setStreet(e.target.value);
        }}
      />
      <Input
        placeholder="House"
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

      <Button onClick={handleCreate}>Create</Button>
    </div>
  );
};

export default UploadForm;
