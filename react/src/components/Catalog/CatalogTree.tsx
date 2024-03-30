import React, { useEffect } from 'react';
import { Typography, Container, List, ListItem, ListItemText, Collapse } from '@mui/material';
import { RiArrowDropUpLine } from 'react-icons/ri';
import { RiArrowDropDownLine } from 'react-icons/ri';
import { Link } from 'react-router-dom';
import Loader from '../Loader';

export type Category = {
  id: string;
  title: string;
  url: string;
  children?: Category[];
}

const CategoryTree: React.FC<{ categories: Category[], categoryId?: string }> = ({ categories, categoryId }) => {
  const [openIds, setOpenIds] = React.useState<string[]>([]);

  const propagateCategory = (targetId: string, category: Category, categoryIdStack: string[]) => {
    console.log("C", targetId, category, categoryIdStack)
    category.children?.forEach(child => {
      if (child.id === targetId) {
        console.log(categoryIdStack)
        setOpenIds(categoryIdStack)
        return;
      }
      let currentStack = JSON.parse(JSON.stringify(categoryIdStack))
      currentStack.push(category.id)
      propagateCategory(targetId, child, currentStack)
    })
  }

  const openIdsWithCategory = (categoryId: string) => {
    console.log("B", categories, categoryId)
    categories.forEach(x => propagateCategory(categoryId, x, []))
  }

  useEffect(() => {
    if (categoryId) {
      // page like /category/:categoryID
      console.log("A", categoryId)
      openIdsWithCategory(categoryId)
    } else {
      // home page
      setOpenIds([])
    }
  }, [categoryId, categories]);

  const handleClick = (id: string) => {
    setOpenIds((prevOpenIds) => {
      if (prevOpenIds.includes(id)) {
        return prevOpenIds.filter((openId) => openId !== id);
      } else {
        return [...prevOpenIds, id];
      }
    });
  };

  const renderTree = (nodes: Category[], level: number, openIds: string[]) => (
    <List>
      {nodes.map((node, index) => (
        <React.Fragment key={index}>
          <ListItem style={{ padding: 0, marginLeft: 10 * level }} onClick={() => handleClick(node.id)} >
            {
              (node.children && node.children.length) ? (
                <>
                  <ListItemText primary={node.title} />
                  {node.children && (openIds.includes(node.id) ? <RiArrowDropUpLine /> : <RiArrowDropDownLine />)}
                </>
              ) : (
                <Link to={'/category/' + node.id }><ListItemText primary={node.title} /></Link>
              )
            }

          </ListItem>
          {(node.children && node.children.length) ? (
            <Collapse in={openIds.includes(node.id)} timeout="auto" unmountOnExit>
              {renderTree(node.children, level + 1, openIds)}
            </Collapse>
          ) : ''}
        </React.Fragment>
      ))}
    </List>
  );

  return (
    <Container maxWidth="md" style={{marginBottom: 15}}>
      <Typography variant="h6" gutterBottom>
        Выберите категорию
      </Typography>
      { !categories.length ? (<Loader />) : renderTree(categories, 0, openIds) }
    </Container>
  );
};

// Usage: <CategoryTree categories={categoriesData} />

export default CategoryTree;
