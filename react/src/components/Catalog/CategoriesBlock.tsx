import { Link, useParams } from 'react-router-dom';
import '../../scss/catalog.scss';
import { useEffect, useState } from 'react';
import { getCategories, getProducts } from '../../service/dataService';
import ProductsList from './ProductsList';
import CatalogTree from './CatalogTree';

type ItemData = {
  id: number;
  name: string;
};

type Product = {
  id: number;
  title: string;
  description: string;
};

const Catalog = () => {
  const [categories, setCategories] = useState<ItemData[]>([]);
  const { categorySlug } = useParams<{ categorySlug: string }>();
  const [products, setProducts] = useState<Product[]>([]);

  useEffect(() => {
    const categoriesData: ItemData[] = getCategories(categorySlug);
    setCategories(categoriesData);
    const productsData: Product[] = getProducts(categorySlug);
    setProducts(productsData);
  }, []);

  if (!categories.length) {
    return null;
  }

  return (
    <div className="categories-container">
      <CatalogTree />
      <div>
        <div className="categories">
          {categories.map((item: any) => (
            <Link to={`/categories/${item.name}`}>
              <div key={item.id} className="category-item">
                <div>{item.id}</div>
                <div>{item.name}</div>
              </div>
            </Link>
          ))}
        </div>

        <ProductsList products={products} />
      </div>
    </div>
  );
};

export default Catalog;
