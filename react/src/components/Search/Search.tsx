import { Button, Input } from 'antd';
import '../../scss/search.scss';

const Search = () => {
  const handleSearch = () => {
    return;
  };

  return (
    <div className="Search">
      <Input placeholder="Search for anything" />
      <Button onClick={handleSearch}>Search</Button>
    </div>
  );
};

export default Search;
