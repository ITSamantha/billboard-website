import React from 'react';
import { Typography, Container, List, ListItem, ListItemText, Collapse } from '@mui/material';
import { RiArrowDropUpLine } from "react-icons/ri";
import { RiArrowDropDownLine } from "react-icons/ri";

interface Category {
  id: number;
  name: string;
  children?: Category[];
}

const CategoryTree: React.FC<{ categories: Category[] }> = ({ categories }) => {
  const [openIds, setOpenIds] = React.useState<number[]>([]);

  const handleClick = (id: number) => {
    setOpenIds((prevOpenIds) => {
      if (prevOpenIds.includes(id)) {
        return prevOpenIds.filter((openId) => openId !== id);
      } else {
        return [...prevOpenIds, id];
      }
    });
  };

  const renderTree = (nodes: Category[]) => (
    <List>
      {nodes.map((node) => (
        <React.Fragment key={node.id}>
          <ListItem onClick={() => handleClick(node.id)}>
            <ListItemText primary={node.name} />
            {node.children && (openIds.includes(node.id) ? <RiArrowDropUpLine /> : <RiArrowDropDownLine /> )}
          </ListItem>
          {node.children && (
            <Collapse in={openIds.includes(node.id)} timeout="auto" unmountOnExit>
              {renderTree(node.children)}
            </Collapse>
          )}
        </React.Fragment>
      ))}
    </List>
  );

  return (
    <Container maxWidth="md">
      <Typography variant="h6" gutterBottom>
        Select Category
      </Typography>
      {renderTree(categories)}
    </Container>
  );
};

// Usage: <CategoryTree categories={categoriesData} />

export default CategoryTree;
