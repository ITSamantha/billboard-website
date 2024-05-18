import CatalogTree from './CatalogTree';
import FilterItems from './FilterItems';
import { getAdvertisementsByPage, getCategoriesList, getCategory } from '../../service/dataService';
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
  const [pagesCount, setPagesCount] = useState<number>(0);
  const [adsPerPage, setAdsPerPage] = useState<number>(15);
  const [advertisements, setAdvertisements] = useState<AdInfo[]>([]);
  const [categoryChildren, setCategoryChildren] = useState<Category[]>([]);

  useEffect(() => {
    getCategoriesList().then((r) => setCategories(r));
  }, []);

  useEffect(() => {
    if (categoryId) {
      getCategory(categoryId).then((category) => setCategoryChildren(category.children));
    }
  }, [categoryId]);

  useEffect(() => {
    async function fetchData() {
      let ads = await getAdvertisementsByPage(page, adsPerPage, Number(categoryId));
      setAdvertisements(ads.data);
      setPagesCount(ads.pages_count);
    }
    fetchData();
  }, [adsPerPage, categoryId, page]);

  const handlePageChange = (event: React.ChangeEvent<unknown>, value: number) => {
    setPage(value);
    getAdvertisementsByPage(page, adsPerPage, Number(categoryId));
  };

  return (
    <div className="Catalog">
      {categoryId && (
        <div style={{ width: 300 }}>
          <CatalogTree categories={categories} categoryId={categoryId} />
          {categoryId && <FilterItems categoryId={categoryId} />}
        </div>
      )}
      <div style={{ display: 'grid', width: categoryId ? 'calc(100% - 300px)' : '100%' }}>
        {categoryId ? (
          <CategoriesBlock categories={categoryChildren} />
        ) : (
          <CategoriesBlock categories={categories} />
        )}
        {categoryId && (
          <div>
            <h1 className="Advertisements__Title">Advertisements in category {advertisements.length ? advertisements[0].category?.title : ''}:</h1>
            <AdvertisementBlock
              advertisements={advertisements}
              advertisementsInRow={4}
              maxAdvertisements={Infinity}
            />
            <Stack spacing={2}>
              <Pagination
                count={pagesCount}
                shape="rounded"
                onChange={handlePageChange}
                page={page}
              />
            </Stack>
          </div>
        )}
      </div>
    </div>
  );
};

export default Catalog;
