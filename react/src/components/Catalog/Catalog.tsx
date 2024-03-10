import CatalogTree from './CatalogTree';
import CategoriesBlock from './CategoriesBlock';
import '../../scss/catalog.scss';
import Filter from './Filter';

const Catalog = () => {
  return (
    <div className="catalog-container">
      <div>
        <CatalogTree />
        <Filter />
      </div>

      <CategoriesBlock />
    </div>
  );
};

export default Catalog;
