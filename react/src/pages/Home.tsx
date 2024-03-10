import Catalog from '../components/Catalog/CategoriesBlock';
import Search from '../components/Search/Search';

const data = [
  { id: 1, name: 'first' },
  { id: 2, name: 'second' }
];

const Home = () => {
  return (
    <div>
      <Search />
      <Catalog />
    </div>
  );
};

export default Home;
