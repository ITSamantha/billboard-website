import React from 'react'
import { useNavigate, useParams } from 'react-router-dom';
import Search from '../components/Search/Search';
import Catalog from '../components/Catalog/Catalog';

const Category = () => {

  const params = useParams()

  const navigate = useNavigate()
  if (params.id === undefined) {
    navigate('/404')
    return <></>
  }

  return (
    <div>
      <Search />
      <Catalog categoryId={params.id} />
    </div>
  );

}

export default Category