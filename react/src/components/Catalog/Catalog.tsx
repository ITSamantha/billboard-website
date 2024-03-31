import CatalogTree, { Category } from './CatalogTree';
import CategoriesBlock from './CategoriesBlock';
import '../../scss/catalog.scss';
import FilterItems from './FilterItems';
import { Pagination } from 'antd';
import { getCategoriesList } from '../../service/dataService';
import { useEffect, useState } from 'react';

type CatalogProps = {
  categoryId?: string;
};

const Catalog = ({ categoryId }: CatalogProps) => {
  const [categories, setCategories] = useState<Category[]>([]);

  useEffect(() => {
    getCategoriesList().then((r) => setCategories(r));
  }, []);

  return (
    <div className="catalog-container">
      <div style={{ width: 300 }}>
        <CatalogTree categories={categories} categoryId={categoryId} />
        {categoryId && <FilterItems categoryId={categoryId} />}
      </div>
      <div>
        {/*<CategoriesBlock />*/}
        <Pagination defaultCurrent={6} total={500} />
      </div>
    </div>
  );
};

export default Catalog;
