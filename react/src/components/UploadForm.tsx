import { Input, Select, Button } from 'antd';
import TextArea from 'antd/es/input/TextArea';
import { useState } from 'react';
import '../scss/upload-form.scss';

const UploadForm = () => {
  const [title, setTitle] = useState<string>('');
  const [description, setDescription] = useState<string>('');
  const [adType, setAdType] = useState<number>(0);
  const [price, setPrice] = useState<number>(0);
  const [tags, setTags] = useState<[]>([]);
  const [categories, setCategoris] = useState();
  const [adPhotos, setAdPhotos] = useState();
  const [city, setCity] = useState<string>('');
  const [street, setStreet] = useState<string>('');
  const [house, setHouse] = useState<string>('');
  const [flat, setFlat] = useState<string>('');

  const handleCreate = () => {
    return;
  };

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
      <TextArea
        autoSize={{ minRows: 2, maxRows: 6 }}
        placeholder="Description"
        value={description}
        onChange={(e) => {
          setDescription(e.target.value);
        }}
      />
      <Select
        placeholder="Advertisement type"
        style={{ width: '400px' }}
        onChange={(e) => {
          setAdType(e.target.value);
        }}
        options={[{ value: 'lucy', label: 'Lucy' }]}
      />
      <Input
        prefix="₪"
        suffix="ILS"
        placeholder="Price"
        type="number"
        min="0"
        onChange={(e) => {
          setTitle(e.target.value);
        }}
      />
      <Input
        placeholder="City"
        type="text"
        onChange={(e) => {
          setCity(e.target.value);
        }}
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
