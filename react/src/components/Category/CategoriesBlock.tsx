import { Link } from 'react-router-dom';
import Loader from '../Loader';

type Props = {
  categories: Category[];
};

const CategoriesBlock = ({ categories }: Props) => {
  if (!categories) {
    return (
      <div>
        <Loader />
      </div>
    );
  }
  return (
    <div className="Categories">
      <h1>Categories</h1>
      <div className="Categories__Wrapper">
        {categories.map((category) => (
          <div className="Categories__Item__Wrapper">
            <Link to={`/category/${category.id}`}>
              <div className="Categories__Item">
                <img src="https://http.cat/201" alt="category" />
                <h3>{category.title}</h3>
              </div>
            </Link>
          </div>
        ))}
      </div>
    </div>
  );
};
export default CategoriesBlock;
