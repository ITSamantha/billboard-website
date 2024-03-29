import React, { useEffect, useState } from 'react';
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
import { Link, useParams } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import { fetchUser, selectUser } from '../../redux/slices/UserSlice';
import { fetchMyUser, selectMyUser } from '../../redux/slices/MyUserSlice';
import { AppDispatch } from '../../redux/store';

type ProfileInfo = {
  id: number;
  avatar: string;
  email: string;
  phone_number: string;
  last_name: string;
  first_name: string;
};
const Profile = () => {
  const classes = useStyles();
  const { id } = useParams();
  const dispatch = useDispatch<AppDispatch>();
  const user = useSelector(selectUser);
  const myUser = useSelector(selectMyUser);
  const [profile, setProfile] = useState<ProfileInfo | null>(null);
  const [isMyProfile, setIsMyProfile] = useState<boolean>(false);

  useEffect(() => {
    async function fetchData() {
      await dispatch(fetchMyUser());
      await dispatch(fetchUser({ id }));
    }
    fetchData();
  }, [dispatch, id]);

  useEffect(() => {
    setIsMyProfile(myUser?.id == id);
  }, [myUser, id]);

  useEffect(() => {
    setProfile(user);
  }, [user]);

  if (!profile) {
    return <div></div>;
  }

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
              <Typography variant="subtitle1">
                Name: {profile.first_name} {profile.last_name}
              </Typography>
              <Typography variant="subtitle1">Email: {profile.email}</Typography>
              <Typography variant="subtitle1">Phone Number: {profile.phone_number}</Typography>
            </Grid>
          </Grid>
        </section>

        <section className={classes.section}>
          <Typography variant="h5" component="h5" className={classes.sectionTitle}>
            Advertisements
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
        {isMyProfile && (
          <section className={classes.section}>
            <Link to="/profile/edit">
              <Button style={{ marginRight: '15px' }} variant="contained" color="primary">
                Edit Personal Information
              </Button>
            </Link>
          </section>
        )}
      </Container>
    </ThemeProvider>
  );
};

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

export default Profile;
