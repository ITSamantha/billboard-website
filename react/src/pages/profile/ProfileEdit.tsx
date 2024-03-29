import React, { useEffect, useState } from 'react';
import { makeStyles } from '@mui/styles';
import {
  Autocomplete,
  Button,
  Container,
  Grid,
  TextField,
  ThemeProvider,
  Typography
} from '@mui/material';
import { THEME } from './Profile';
import { Link } from 'react-router-dom';
import { useSelector } from 'react-redux';
import { selectMyUser } from '../../redux/slices/MyUserSlice';

const cities = [
  { id: 1, label: 'New York' },
  { id: 2, label: 'Los Angeles' },
  { id: 3, label: 'Chicago' },
  { id: 4, label: 'Houston' },
  { id: 5, label: 'Phoenix' }
  // Add more cities as needed
];

const useStyles = makeStyles({
  root: {
    marginTop: '1.5rem'
  },
  form: {
    width: '100%',
    marginTop: '1rem'
  },
  submit: {
    margin: '1rem 0'
  },
  avatar: {
    width: '100px',
    height: '100px',
    marginBottom: '1rem'
  }
});

const EditProfile = () => {
  const [firstName, setFirstName] = useState<string>('');
  const [lastName, setLastName] = useState<string>('');
  const [email, setEmail] = useState<string>('');
  const [city, setCity] = useState<string>('');
  const [password, setPassword] = useState<string>('');
  const [phone, setPhone] = useState<string>('');
  const classes = useStyles();
  const user = useSelector(selectMyUser);

  useEffect(() => {}, [user]);

  return (
    <ThemeProvider theme={THEME}>
      <Container maxWidth="lg" className={classes.root} style={{ paddingBottom: 50 }}>
        <Typography fontWeight={600} variant="h4" component="h1" gutterBottom>
          Edit Profile
        </Typography>

        <form className={classes.form}>
          <Grid container spacing={2}>
            <Grid item xs={12} sm={6}>
              <TextField
                variant="outlined"
                margin="normal"
                fullWidth
                id="firstName"
                label="First Name"
                name="firstName"
                autoComplete="given-name"
                autoFocus
                onChange={(event) => setFirstName(event.target.value)}
              />
            </Grid>
            <Grid item xs={12} sm={6}>
              <TextField
                variant="outlined"
                margin="normal"
                fullWidth
                id="lastName"
                label="Last Name"
                name="lastName"
                autoComplete="family-name"
              />
            </Grid>

            <Grid item xs={12} sm={6}>
              <TextField
                variant="outlined"
                margin="normal"
                fullWidth
                id="email"
                label="Email Address"
                name="email"
                autoComplete="email"
              />
            </Grid>
            <Grid item xs={12} sm={6}>
              <TextField
                variant="outlined"
                margin="normal"
                fullWidth
                id="phoneNumber"
                label="Phone Number"
                name="phoneNumber"
                autoComplete="tel"
              />
              <Link to="/profile/phone">
                <Typography variant="body2" align="right" style={{ marginTop: '8px' }}>
                  Confirm Phone
                </Typography>
              </Link>
            </Grid>
            <Grid item xs={12} sm={6}>
              <Autocomplete
                options={cities}
                getOptionLabel={(option) => option.label}
                renderInput={(params) => (
                  <TextField
                    {...params}
                    label="City"
                    variant="outlined"
                    margin="normal"
                    fullWidth
                  />
                )}
                style={{ marginBottom: '1rem' }}
              />
            </Grid>
            <Grid item xs={12} sm={6}>
              <TextField
                variant="outlined"
                margin="normal"
                fullWidth
                id="password"
                label="Password"
                name="password"
                type="password"
                autoComplete="current-password"
              />
            </Grid>
            <Grid item xs={12} sm={12}>
              <Button
                type="submit"
                fullWidth
                style={{ marginTop: 15 }}
                variant="contained"
                color="primary"
                className={classes.submit}
              >
                Save Changes
              </Button>
            </Grid>
          </Grid>
        </form>
      </Container>
    </ThemeProvider>
  );
};

export default EditProfile;
