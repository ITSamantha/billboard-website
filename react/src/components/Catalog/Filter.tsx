import React, { useEffect, useState } from 'react';
import { makeStyles } from '@mui/styles';
import { THEME } from '../../pages/profile/Profile';
import { Button, Checkbox, Typography, Container, Box, ThemeProvider } from '@mui/material';

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
  name: string;
  type: string;
  values: Value[];
};

const Filter = () => {
  const [filters, setFilters] = useState<Filter[]>([]);

  useEffect(() => {
    // Mock data for testing
    const mockFilters = [
      {
        id: 1,
        name: 'Filter 1',
        type: 'type1',
        values: [
          { id: 1, value: 'Value 1' },
          { id: 2, value: 'Value 2' }
        ]
      },
      {
        id: 2,
        name: 'Filter 2',
        type: 'type2',
        values: [
          { id: 3, value: 'Value 3' },
          { id: 4, value: 'Value 4' }
        ]
      }
    ];
    setFilters(mockFilters);
  }, []);

  const handleChange = (filterId: number) => (event: any) => {
    console.log(`Filter ${filterId} changed: `, event.target.checked);
    // Handle filter changes here
  };

  const handleFiltersSet = () => {
    // sendFilters();
  };

  return (
    <ThemeProvider theme={THEME}>
      <Container maxWidth="md">
        {filters.map((item) => (
          <Box key={item.id} mb={2} p={2} bgcolor="#f5f5f5" borderRadius="8px">
            <Typography variant="h6">{item.name}</Typography>
            {item.values.map((value) => (
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
        <Button variant="contained" color="primary" onClick={handleFiltersSet}>
          Apply
        </Button>
      </Container>
    </ThemeProvider>
  );
};

export default Filter;
