import React from 'react';
import { makeStyles } from '@mui/styles';
import {
  Avatar,
  Button,
  Container,
  createTheme,
  Grid,
  Paper,
  Typography,
  ThemeProvider
} from '@mui/material';
import { Link } from 'react-router-dom';

const useStyles = makeStyles({
  typography: {
    fontFamily: ['Montserrat', '"Helvetica Neue"', '"Segoe UI"'].join(',')
  },
  root: {
    marginTop: '1.5rem'
  },
  section: {
    marginBottom: '24px'
  },
  sectionTitle: {
    color: '#1a73e8',
    fontSize: '24px',
    paddingBottom: '8px'
  },
  avatar: {
    width: '100px',
    height: '100px'
  },
  advertisement: {
    padding: '1rem',
    backgroundColor: '#f1f3f4',
    borderRadius: '8px',
    boxShadow: '0 2px 4px rgba(0, 0, 0, 0.1)',
    marginBottom: '1rem'
  },
  advertisementAddress: {
    fontStyle: 'italic',
    color: '#888'
  },
  advertisementImage: {
    width: 200,
    height: 200,
    objectFit: 'cover',
    borderRadius: 6,
    overflow: 'hidden'
  }
});

export const THEME = createTheme({
  typography: {
    fontFamily: `"Montserrat", "Helvetica", "Arial", sans-serif`,
    fontSize: 14,
    fontWeightLight: 300,
    fontWeightRegular: 400,
    fontWeightMedium: 500
  }
});

const Profile = () => {
  const classes = useStyles();

  return (
    <ThemeProvider theme={THEME}>
      <Container maxWidth="md" className={classes.root}>
        <Typography variant="h4" component="h4" gutterBottom fontWeight={600}>
          User Profile
        </Typography>
        <section className={classes.section}>
          <Typography variant="h5" component="h5" className={classes.sectionTitle}>
            Personal Information
          </Typography>
          <Grid container spacing={2} alignItems="center">
            <Grid item>
              <Avatar alt="User Avatar" src="https://http.cat/200" className={classes.avatar} />
            </Grid>
            <Grid item>
              <Typography variant="subtitle1">Name: [First Name] [Last Name]</Typography>
              <Typography variant="subtitle1">Email: [Email Address]</Typography>
              <Typography variant="subtitle1">Phone Number: [Phone Number]</Typography>
            </Grid>
          </Grid>
        </section>

        <section className={classes.section}>
          <Typography variant="h5" component="h5" className={classes.sectionTitle}>
            My advertisements
          </Typography>
          <Grid container spacing={2}>
            <Grid item xs={12} md={4}>
              <Paper className={classes.advertisement}>
                <img
                  className={classes.advertisementImage}
                  src="https://http.cat/300"
                  alt="Advertisement"
                />
                <Typography variant="h6" component="h6">
                  Advertisement Title
                </Typography>
                <Typography variant="body1">Advertisement Description</Typography>
                <Typography variant="body2" className={classes.advertisementAddress}>
                  Advertisement Address
                </Typography>
              </Paper>
            </Grid>
            <Grid item xs={12} md={4}>
              <Paper className={classes.advertisement}>
                <img
                  className={classes.advertisementImage}
                  src="https://http.cat/500"
                  alt="Advertisement"
                />
                <Typography variant="h6" component="h6">
                  Advertisement Title
                </Typography>
                <Typography variant="body1">Advertisement Description</Typography>
                <Typography variant="body2" className={classes.advertisementAddress}>
                  Advertisement Address
                </Typography>
              </Paper>
            </Grid>
            <Grid item xs={12} md={4}>
              <Paper className={classes.advertisement}>
                <img
                  className={classes.advertisementImage}
                  src="https://http.cat/400"
                  alt="Advertisement"
                />
                <Typography variant="h6" component="h6">
                  Advertisement Title
                </Typography>
                <Typography variant="body1">Advertisement Description</Typography>
                <Typography variant="body2" className={classes.advertisementAddress}>
                  Advertisement Address
                </Typography>
              </Paper>
            </Grid>
          </Grid>
        </section>

        <section className={classes.section}>
          <Link to="/profile/edit">
            <Button style={{ marginRight: '15px' }} variant="contained" color="primary">
              Edit Personal Information
            </Button>
          </Link>
        </section>
      </Container>
    </ThemeProvider>
  );
};

export default Profile;
