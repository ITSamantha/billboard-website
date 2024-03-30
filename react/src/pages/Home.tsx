import { Button } from 'antd';
import Catalog from '../components/Catalog/Catalog';
import Search from '../components/Search/Search';
import { Link } from 'react-router-dom';

const data = [
  { id: 1, name: 'first' },
  { id: 2, name: 'second' }
];

const Home = () => {
  return (
    <div>
      <Search />
      <Catalog />
      <Link to={'advertisement/3'}>
        <Button>Advertisement test</Button>
      </Link>
    </div>
  );
};

export default Home;
