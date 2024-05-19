import React, { useEffect, useState } from 'react';
import { makeStyles } from '@mui/styles';
import { THEME } from '../../pages/profile/Profile';
import { Button, Checkbox, Typography, Container, Box, ThemeProvider } from '@mui/material';
import { getCategoriesList, getFilterList } from '../../service/dataService';

const useStyles = makeStyles({
  container: {
    maxWidth: '500px',
    margin: '0 auto',
    padding: '1rem',
    backgroundColor: '#f5f5f5',
    borderRadius: '8px',
    boxShadow: '0 2px 4px rgba(0, 0, 0, 0.1)'
  },
  filterItem: {
    marginBottom: '1rem'
  },
  filterName: {
    fontWeight: 'bold',
    marginBottom: '0.5rem'
  }
});

type Value = {
  id: number;
  value: string;
};

type Filter = {
  id: number;
  title: string;
  type: string;
  filter_values: Value[];
};

type FilterProps = {
  categoryId: number;
};

const FilterItems = ({ categoryId }: FilterProps) => {
  const [filters, setFilters] = useState<Filter[]>([]);

  useEffect(() => {
    getFilterList(categoryId).then((r) => setFilters(r));
  }, [categoryId]);

  const handleChange = (filterId: number) => (event: any) => {
    console.log(`Filter ${filterId} changed: `, event.target.checked);
  };

  const handleFiltersSet = () => {
    console.log('SET');
  };

  return (
    <ThemeProvider theme={THEME}>
      <Container maxWidth="md">
        {filters.map((item) => (
          <Box key={item.id} mb={2} p={2} bgcolor="#f5f5f5" borderRadius="8px">
            <Typography variant="h6">{item.title}</Typography>
            {item.filter_values.map((value) => (
              <div key={value.id} style={{ display: 'flex', alignItems: 'center' }}>
                <label style={{ display: 'flex', alignItems: 'center', cursor: 'pointer' }}>
                  <Checkbox
                    size={'small'}
                    onChange={handleChange(value.id)}
                    color="primary"
                    inputProps={{ 'aria-label': 'Checkbox' }}
                  />
                  <Typography variant="body1">{value.value}</Typography>
                </label>
              </div>
            ))}
          </Box>
        ))}
        {filters.length ?  <Button variant="contained" color="primary" onClick={handleFiltersSet}>
          Apply
        </Button> : <></>}
       
      </Container>
    </ThemeProvider>
  );
};

export default FilterItems;
