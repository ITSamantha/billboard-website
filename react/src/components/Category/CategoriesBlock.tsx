import { Link } from 'react-router-dom';

type Props = {
  categories: Category[];
};

const CategoriesBlock = ({ categories }: Props) => {
  return (
    <div>
        Categories
      {categories.map((category) => (
        <div>
          <img src="https://http.cat/201" alt="category" style={{ height: '100px' }}></img>
          <Link to={`/category/${category.id}`}>
            {' '}
            <div>{category.title}</div>
          </Link>
        </div>
      ))}
    </div>
  );
};
export default CategoriesBlock;
