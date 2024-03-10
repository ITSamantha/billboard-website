import { useEffect, useState } from 'react';
import { getCategoriesList } from '../../service/dataService';
import { Link } from 'react-router-dom';
import '../../scss/catalog-tree.scss';

type Item = {
  id: number;
  name: string;
  children: Item[];
};

const CatalogTree = () => {
  const [tree, setTree] = useState<Item[]>([]);

  useEffect(() => {
    const data = getCategoriesList();
    setTree(data);
  }, []);

  const renderChild = (obj: Item[], depth: number) => {
    return obj.map((item) => (
      <div style={{ paddingRight: `${depth * 15}px` }}>
        <Link to={`/categories/${item.name}`} key={item.id}>
          <div>{item.name}</div>
        </Link>

        {item.children.length > 0 && <div>{renderChild(item.children, depth + 1)}</div>}
      </div>
    ));
  };

  return (
    <div className="catalog-tree-container">
      <h3> Categories</h3>
      {tree.map((item) => (
        <div>
          <Link to={`/categories/${item.name}`} key={item.id}>
            <div>{item.name}</div>
          </Link>
          <div>{renderChild(item.children, 1)}</div>
        </div>
      ))}
    </div>
  );
};

export default CatalogTree;
