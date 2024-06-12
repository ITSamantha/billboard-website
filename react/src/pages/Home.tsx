import Catalog from '../components/Catalog/Catalog';
import Search from '../components/Search/Search';

const data = [
  { id: 1, name: 'first' },
  { id: 2, name: 'second' }
];

const Home = () => {
  return (
    <div className="Home">
      <div className="container">
        <Search />
        <Catalog />
      </div>
    </div>
  );
};

export default Home;
