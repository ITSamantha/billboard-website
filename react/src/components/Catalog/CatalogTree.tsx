import React, { useEffect, useState } from 'react';
import { Typography, Container, List, ListItem, ListItemText, Collapse } from '@mui/material';
import { RiArrowDropUpLine } from 'react-icons/ri';
import { RiArrowDropDownLine } from 'react-icons/ri';
import { Link } from 'react-router-dom';
import Loader from '../Loader';

const CategoryTree: React.FC<{ categories: Category[]; categoryId?: number }> = ({
                                                                                   categories,
                                                                                   categoryId
                                                                                 }) => {
  const [openIds, setOpenIds] = React.useState<number[]>([]);

  const [openedDropdown, setOpenedDropdown] = useState<boolean>(false);

  const propagateCategory = (targetId: number, category: Category, categoryIdStack: number[]) => {
    if (category.id === targetId) {
      setOpenIds([...categoryIdStack, targetId]);
      return;
    }
    category.children?.forEach((child) => {
      let currentStack = JSON.parse(JSON.stringify(categoryIdStack));
      currentStack.push(category.id);
      propagateCategory(targetId, child, currentStack);
    });
  };

  const openIdsWithCategory = (categoryId: number) => {
    categories.forEach((x) => propagateCategory(categoryId, x, []));
  };

  useEffect(() => {
    if (categoryId) {
      openIdsWithCategory(categoryId);
    } else {
      // home page
      setOpenIds([]);
    }
  }, [categoryId, categories]);

  const handleClick = (id: number) => {
    setOpenIds((prevOpenIds) => {
      if (prevOpenIds.includes(id)) {
        return prevOpenIds.filter((openId) => openId !== id);
      } else {
        return [...prevOpenIds, id];
      }
    });
  };

  useEffect(() => {
    console.log('OpenIDS', openIds);
  }, [openIds]);

  const renderTree = (nodes: Category[], level: number, openIds: number[]) => (
    <List>
      {nodes.map((node, index) => (
        <React.Fragment key={index}>
          <ListItem style={{ padding: 0, marginLeft: 20 * level }}>
            {node.children && node.children.length ? (
              <Link to={'/category/' + node.id}>
                <span className="CatalogTree__Title">{node.title} {node.children &&
                  (openIds.includes(node.id) ? <RiArrowDropUpLine style={{ marginBottom: -3}}/> : <RiArrowDropDownLine style={{ marginBottom: -3}} />)}</span>

              </Link>
            ) : (
              <Link to={'/category/' + node.id} onClick={() => setOpenedDropdown(false)}>
                <span className="CatalogTree__Title">{node.title}</span>
              </Link>
            )}
          </ListItem>
          {node.children && node.children.length ? (
            <Collapse in={openIds.includes(node.id)} timeout="auto" unmountOnExit>
              <div className={'CatalogTree__Category'}>
                {renderTree(node.children, level + 1, openIds)}
              </div>
            </Collapse>
          ) : (
            ''
          )}
        </React.Fragment>
      ))}
    </List>
  );

  return (
    <div className="CatalogTree">
      <h5 onClick={() => { setOpenedDropdown((prev) => !prev )}}>Filters <span className={openedDropdown ? '_rotated': ''}><RiArrowDropDownLine /></span></h5>
      <div className={"CatalogTree__Items " + (openedDropdown ? '_active' : '')}>
        {!categories.length ? <Loader /> : renderTree(categories, 0, openIds)}
      </div>
    </div>
  );
};

// Usage: <CategoryTree categories={categoriesData} />

export default CategoryTree;
