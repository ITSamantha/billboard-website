import { Link } from 'react-router-dom';
import '../../scss/products-list.scss';
type Product = {
  id: number;
  title: string;
  description: string;
};

type Props = {
  products: Product[];
};

const ProductsList = ({ products }: Props) => {
  if (!products) {
    return <></>;
  }

  return (
    <div className="products-container">
      {products.map((item) => (
        <Link key={item.id} to={`/products/${item.id}`}>
          <div className="products-item">
            <div>{item.id}</div>
            <div>{item.title}</div>
            <div>{item.description}</div>
          </div>
        </Link>
      ))}
    </div>
  );
};

export default ProductsList;
