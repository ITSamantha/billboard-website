import { useEffect, useState } from 'react';
import '../scss/upload-form.scss';
import {
  createAd,
  getAdvertisementTypes,
  getCategories,
  getCategoriesList,
  getCities,
  getCountries, getMyAddresses
} from '../service/dataService';
import { Autocomplete, Button, Input, TextField } from '@mui/material';
import Loader from './Loader';
import { useNavigate } from 'react-router-dom';
import { HiOutlinePhoto } from 'react-icons/hi2';
import { useSelector } from 'react-redux';
import { selectMyUser } from '../redux/slices/MyUserSlice';
import MapInput from './Map/MapInput';

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
  const [city, setCity] = useState<number | undefined>(undefined);
  const [country, setCountry] = useState<number | undefined>(undefined);
  const [street, setStreet] = useState<string>('');
  const [house, setHouse] = useState<string>('');
  const [flat, setFlat] = useState<string>('');
  const [cities, setCities] = useState<Data[]>([]);
  const [countries, setCountries] = useState<Data[]>([]);
  const [adTypes, setAdTypes] = useState<Data[]>([]);
  const [error, setError] = useState<string>('');

  const [addressMode, setAddressMode] = useState<number>();

  const navigate = useNavigate();

  const [mainPhotoIndex, setMainPhotoIndex] = useState<number>(0);
  const [loading, setLoading] = useState<boolean>(false);
  const [base64Images, setBase64Images] = useState<string[]>([]);

  const user = useSelector(selectMyUser);
  const [myAddresses, setMyAddresses] = useState<AdAddress[]>([]);
  const [addressId, setAddressId] = useState<number>();

  useEffect(() => {
    setAddressId(undefined)
  }, [addressMode])

  useEffect(() => {
    if (user !== null) {
      getMyAddresses(user.id).then((addresses) => {
        setMyAddresses(addresses);
      });
    }
  }, [user]);

  function encodeImageFileAsURL(files: FileList | null) {
    setMainPhotoIndex(0);
    if (!files) {
      return;
    }
    const filesArray: File[] = Array.from(files);
    const images: string[] = [];
    setLoading(true);
    filesArray.forEach((file: File) => {
      let reader = new FileReader();
      reader.onloadend = function() {
        if (typeof reader.result === 'string') {
          images.push(reader.result);
        }
      };
      reader.readAsDataURL(file);
    });

    setLoading(true);
    let interval = setInterval(() => {
      if (images.length === filesArray.length) {
        setBase64Images(images);
        setLoading(false);
        clearInterval(interval);
      }
    }, 3000);

  }

  useEffect(() => {
    async function fetchData() {
      const [countriesData, citiesData, typesData, categoriesData] = await Promise.all([
        getCountries(),
        getCities(),
        getAdvertisementTypes(),
        getCategoriesList()
      ]);
      setCountries(countriesData);
      setCities(citiesData);
      setAdTypes(typesData);
      setCategories(categoriesData);
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
      !house ||
      !base64Images ||
      !base64Images.length
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
      flat,
      [base64Images[mainPhotoIndex], ...base64Images.slice(0, mainPhotoIndex), ...base64Images.slice(mainPhotoIndex + 1)]
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
    <div className="Upload">
      <div className="Upload__Container">
        <h1>Create advertisement</h1>
        <div className="Upload__Wrapper">
          <div className="Upload__Photos">
            <label htmlFor="photos">
              <div className="Upload__Button Upload__Button--Files">
                <div><HiOutlinePhoto /></div>
                <div>Upload files</div>
              </div>
            </label>
            <input
              accept="image/*"
              style={{ display: 'none' }}
              id="photos"
              multiple
              type="file"
              onChange={(e) => encodeImageFileAsURL(e.target.files)}
            />

            <div className="Upload__Photos__Selected">
              {loading ? <Loader /> : (
                base64Images.map((el, index) => (
                  <div className={'Upload__Photos__Selected__Item ' + (index === mainPhotoIndex ? '_active' : '')} onClick={() => setMainPhotoIndex(index)}>
                    <img src={el} alt="#" />
                  </div>
                ))
              )}
            </div>

          </div>
          <div className="Upload__Inputs">
            <div className="Upload__Item">
              <TextField
                label="Title "
                placeholder="Enter advertisement title"
                type="text"
                required
                onChange={(e) => {
                  setTitle(e.target.value);
                }}
              />
            </div>
            <div className="Upload__Item">
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
            </div>
            <div className="Upload__Item">
              <Autocomplete
                id=""
                options={adTypes}
                getOptionLabel={(option) => option?.title}
                onChange={(event, value) => setAdType((value as Data | null)?.id)}
                renderInput={(params) => (
                  <TextField
                    label="Advertisement type"
                    {...params}
                  />
                )}
              />
            </div>
            <div className="Upload__Item">
              <Autocomplete
                id=""
                options={categories}
                getOptionLabel={(option) => option?.title}
                onChange={(event, value) => setCategoryId((value as Data | null)?.id)}
                renderInput={(params) => (
                  <TextField
                    label="Category"
                    {...params}
                  />
                )}
              />
            </div>
            <div className="Upload__Item">
              <TextField
                prefix="₪"
                label="Price"
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
            </div>

            <div className="Upload__AddressMode">
              <div className="Upload__Item">

                <Autocomplete
                  id="address_mode"
                  options={[
                    {
                      id: 0,
                      title: `Previous address`
                    },
                    {
                      id: 1,
                      title: `New address with map`
                    },
                    {
                      id: 2,
                      title: `New address with text`
                    }
                  ]}
                  getOptionLabel={(option) => option?.title}
                  onChange={(event, value) => setAddressMode((value as Data | null)?.id)}
                  renderInput={(params) => (
                    <TextField
                      label="How to enter address?"
                      {...params}
                    />
                  )}
                />
              </div>
            </div>

            {addressMode === 1 && (
              <div className="Upload__Map">
                <div className="Upload__Item">
                  <MapInput onChange={(smhth) => {
                    console.log(smhth);
                  }} />
                </div>
              </div>
            )}

            {addressMode === 0 && (
              <div className="Upload__OldAddress">
                <div className="Upload__Item">

                  <Autocomplete
                    id="address_id"
                    options={myAddresses.map((el) => {
                      return {
                        id: el.id,
                        title: `${el.country.title}, ${el.city.title}, ${el.street}, ${el.house}`
                      };
                    })}
                    getOptionLabel={(option) => option?.title}
                    onChange={(event, value) => setAddressId((value as Data | null)?.id)}
                    renderInput={(params) => (
                      <TextField
                        label="Address"
                        {...params}
                      />
                    )}
                  />
                </div>
              </div>
            )}

            {addressMode === 2 && (
              <div className="Upload__NewAddress">
                <div className="Upload__Item">
                  <Autocomplete
                    id=""
                    options={countries}
                    getOptionLabel={(option) => option?.title}
                    onChange={(event, value) => setCountry((value as Data | null)?.id)}
                    renderInput={(params) => (
                      <TextField
                        label="Country"
                        {...params}
                      />
                    )}
                  />
                </div>
                <div className="Upload__Item">
                  <Autocomplete
                    id=""
                    options={cities}
                    getOptionLabel={(option) => option?.title}
                    onChange={(event, value) => setCity((value as Data | null)?.id)}
                    renderInput={(params) => (
                      <TextField {...params} label="City" />
                    )}
                  />
                </div>
                <div className="Upload__Item">
                  <TextField
                    label="Street"
                    type="text"
                    onChange={(e) => {
                      setStreet(e.target.value);
                    }}
                  />
                </div>
                <div className="Upload__Item">
                  <TextField
                    label="House"
                    type="text"
                    onChange={(e) => {
                      setHouse(e.target.value);
                    }}
                  />
                </div>
                <div className="Upload__Item">
                  <TextField
                    label="Flat"
                    type="text"
                    onChange={(e) => {
                      setFlat(e.target.value);
                    }}
                  />
                </div>
              </div>
            )}

            <div>{error}</div>
            {/* TODO: make text red */}
            <button className="Upload__Button" onClick={handleCreate}>Create</button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default UploadForm;
