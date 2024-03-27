import React from 'react';
import { makeStyles } from '@mui/styles';
import {
  Container,
  Typography,
  Grid,
  Paper,
  Avatar,
  Button
} from '@mui/material';

const useStyles = makeStyles({
  root: {
    marginTop: '1.5rem',
  },
  section: {
    marginBottom: '1.5rem',
  },
  sectionTitle: {
    color: '#1a73e8',
    fontSize: '1.5rem',
    marginBottom: '1rem',
  },
  avatar: {
    width: '100px',
    height: '100px',
  },
  advertisement: {
    padding: '1rem',
    backgroundColor: '#f1f3f4',
    borderRadius: '8px',
    boxShadow: '0 2px 4px rgba(0, 0, 0, 0.1)',
    marginBottom: '1rem',
  },
  advertisementAddress: {
    fontStyle: 'italic',
    color: '#888',
  },
});

const UserProfile = () => {
  const classes = useStyles();

  return (
    <Container maxWidth="md" className={classes.root}>
      <Typography variant="h2" component="h1" gutterBottom>User Profile</Typography>

      <section className={classes.section}>
        <Typography variant="h3" component="h2" className={classes.sectionTitle}>Personal Information</Typography>
        <Grid container spacing={2} alignItems="center">
          <Grid item>
            <Avatar alt="User Avatar" src="[Avatar Image URL]" className={classes.avatar} />
          </Grid>
          <Grid item>
            <Typography variant="subtitle1" gutterBottom>Name: [First Name] [Last Name]</Typography>
            <Typography variant="subtitle1" gutterBottom>Email: [Email Address]</Typography>
            <Typography variant="subtitle1" gutterBottom>Phone Number: [Phone Number]</Typography>
          </Grid>
        </Grid>
      </section>

      <section className={classes.section}>
        <Typography variant="h3" component="h2" className={classes.sectionTitle}>Account Information</Typography>
        <Grid container spacing={2}>
          <Grid item xs={12} md={4}>
            <Paper className={classes.advertisement}>
              <Typography variant="h4" component="h3">Advertisement Title</Typography>
              <Typography variant="body1">Advertisement Description</Typography>
              <img src="[Advertisement Image URL]" alt="Advertisement" />
              <Typography variant="body2" className={classes.advertisementAddress}>Advertisement Address</Typography>
            </Paper>
          </Grid>
          {/* Add more advertisements here */}
        </Grid>
      </section>

      <section className={classes.section}>
        <Typography variant="h3" component="h2" className={classes.sectionTitle}>Edit Profile</Typography>
        <Button variant="contained" color="primary">Edit Personal Information</Button>
        <Button variant="contained" color="secondary">Change Password</Button>
      </section>
    </Container>
  );
};

export default UserProfile;
