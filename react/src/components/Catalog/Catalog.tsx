
import CatalogTree from './CatalogTree';
import FilterItems from './FilterItems';
import { getAdvertisementsByPage, getCategoriesList } from '../../service/dataService';
import { useEffect, useState } from 'react';
import { Pagination, Stack } from '@mui/material';
import AdvertisementBlock from '../Advertisement/AdvertisementBlock';
import CategoriesBlock from '../Category/CategoriesBlock';

type CatalogProps = {
  categoryId?: number;
};

const Catalog = ({ categoryId }: CatalogProps) => {
  const [categories, setCategories] = useState<Category[]>([]);
  const [page, setPage] = useState<number>(1);
  const [adsPerPage, setAdsPerPage] = useState<number>(1);
  const [advertisements, setAdvertisements] = useState<AdInfo[]>([]);

  useEffect(() => {
    getCategoriesList().then((r) => setCategories(r));
  }, []);

  useEffect(() => {
    async function fetchData() {
      let ads = await getAdvertisementsByPage(page, adsPerPage, Number(categoryId));
      setAdvertisements(ads.data);
    }
    fetchData();
  }, [adsPerPage, categoryId, page]);

  const handlePageChange = (event: React.ChangeEvent<unknown>, value: number) => {
    setPage(value);
    getAdvertisementsByPage(page, adsPerPage, Number(categoryId));
  };

  return (
    <div className="Catalog">
      <div style={{ width: 300 }}>
        <CatalogTree categories={categories} categoryId={categoryId} />
        {categoryId && <FilterItems categoryId={categoryId} />}
      </div>
      <CategoriesBlock categories={categories}/>
      <div style={{ display: 'grid' }}>
        <AdvertisementBlock
          advertisements={advertisements}
          advertisementsInRow={4}
          maxAdvertisements={6}
        />
        <Stack spacing={2}>
          <Pagination count={12} shape="rounded" onChange={handlePageChange} page={page} />
        </Stack>
      </div>
    </div>
  );
};

export default Catalog;
