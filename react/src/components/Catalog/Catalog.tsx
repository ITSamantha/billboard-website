import CatalogTree, { Category } from './CatalogTree';
import '../../scss/catalog.scss';
import FilterItems from './FilterItems';
import { getAdvertisementsByPage, getCategoriesList } from '../../service/dataService';
import { useEffect, useState } from 'react';
import { Pagination, Stack } from '@mui/material';

type CatalogProps = {
  categoryId?: string;
};

const Catalog = ({ categoryId }: CatalogProps) => {
  const [categories, setCategories] = useState<Category[]>([]);
  const [page, setPage] = useState<number>(1);
  useEffect(() => {
    getCategoriesList().then((r) => setCategories(r));
  }, []);

  const handlePageChange = (event: React.ChangeEvent<unknown>, value: number) => {
    setPage(value);

    // async function fetchData
    // getAdvertisementsByPage(page, 20, Number(categoryId));
  };

  return (
    <div className="catalog-container">
      <div style={{ width: 300 }}>
        <CatalogTree categories={categories} categoryId={categoryId} />
        {categoryId && <FilterItems categoryId={categoryId} />}
      </div>
      <Stack spacing={2}>
        <Pagination count={12} shape="rounded" onChange={handlePageChange} page={page} />
      </Stack>
    </div>
  );
};

export default Catalog;
