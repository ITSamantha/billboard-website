import CatalogTree from './CatalogTree';
import CategoriesBlock from './CategoriesBlock';
import '../../scss/catalog.scss';
import Filter from './Filter';
import { Pagination } from 'antd';
import { getCategoriesList } from '../../service/dataService';

const Catalog = () => {
  return (
    <div className="catalog-container">
      <div>
        <CatalogTree categories={getCategoriesList()}/>
        <Filter />
      </div>
      <CategoriesBlock />
      <Pagination defaultCurrent={6} total={500} />
    </div>
  );
};

export default Catalog;
