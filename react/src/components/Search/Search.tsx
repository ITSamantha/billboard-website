import { Button, Input } from 'antd';

const Search = () => {
  const handleSearch = () => {
    return;
  };

  return (
    <div>
      <Input placeholder="Search for anything" />
      <Button onClick={handleSearch}>Search</Button>
    </div>
  );
};

export default Search;
