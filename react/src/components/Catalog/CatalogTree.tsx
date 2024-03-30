import React, { useEffect } from 'react';
import { Typography, Container, List, ListItem, ListItemText, Collapse } from '@mui/material';
import { RiArrowDropUpLine } from 'react-icons/ri';
import { RiArrowDropDownLine } from 'react-icons/ri';
import { Link } from 'react-router-dom';

export type Category = {
  id: number;
  title: string;
  url: string;
  children?: Category[];
}

const CategoryTree: React.FC<{ categories: Category[], categoryId?: string }> = ({ categories, categoryId }) => {
  const [openIds, setOpenIds] = React.useState<number[]>([]);

  useEffect(() => {
    console.log(categoryId)
  }, [categoryId]);

  const handleClick = (id: number) => {
    setOpenIds((prevOpenIds) => {
      if (prevOpenIds.includes(id)) {
        return prevOpenIds.filter((openId) => openId !== id);
      } else {
        return [...prevOpenIds, id];
      }
    });
  };

  const renderTree = (nodes: Category[], level: number) => (
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
              {renderTree(node.children, level + 1)}
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
      {renderTree(categories, 0)}
    </Container>
  );
};

// Usage: <CategoryTree categories={categoriesData} />

export default CategoryTree;
