import { Link } from 'react-router-dom';
import Loader from '../Loader';

type Props = {
  categories: Category[];
};

const CategoriesBlock = ({ categories }: Props) => {

if(!categories){
    return (
        <div>
          <Loader />
        </div>
      );
}
  return (
    <div>
        Categories
      {categories.map((category) => (
        <div>
          <img src="https://http.cat/201" alt="category" style={{ height: '100px' }}></img>
          <Link to={`/category/${category.id}`}>
            <div>{category.title}</div>
          </Link>
        </div>
      ))}
    </div>
  );
};
export default CategoriesBlock;
