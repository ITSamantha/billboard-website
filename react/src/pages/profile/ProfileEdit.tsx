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
import { Link, useNavigate } from 'react-router-dom';
import { useSelector } from 'react-redux';
import { selectMyUser } from '../../redux/slices/MyUserSlice';
import { getCities, sendCode } from '../../service/dataService';
import Loader from '../../components/Loader';

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

type City = {
  id: number;
  title: string;
};

const EditProfile = () => {
  const [firstName, setFirstName] = useState<string>('');
  const [lastName, setLastName] = useState<string>('');
  const [email, setEmail] = useState<string>('');
  const [city, setCity] = useState<string | null>('');
  const [password, setPassword] = useState<string>('');
  const [phone, setPhone] = useState<string>('');
  const [cities, setCities] = useState<City[]>([]);
  const classes = useStyles();
  const user = useSelector(selectMyUser);

  const navigate = useNavigate()

  useEffect(() => {
    console.log(user)
    async function fetchData() {
      let cities = await getCities();
      setCities(cities);
    }
    fetchData();
  }, [user]);

  const handleProfileInfoChange = () => {
    return;
  };

  if (!user) {
    return (
      <div>
        <Loader />
      </div>
    );
  }

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
                defaultValue={user.first_name}
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
                defaultValue={user.last_name}
                name="lastName"
                onChange={(event) => setLastName(event.target.value)}
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
                defaultValue={user.email}
                onChange={(event) => setEmail(event.target.value)}
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
                defaultValue={user.phone_number}
                name="phoneNumber"
                onChange={(event) => setPhone(event.target.value)}
                autoComplete="tel"
              />
              { user.phone_vertified_at ? (
                <Typography variant="body2" align="right" style={{ marginTop: '8px' }}>Your phone was already verified</Typography>
              ) : (
                <Link to="/profile/phone" onClick={(e) => {
                  e.preventDefault()
                  sendCode().then((response) => {
                    console.log("code sent", response)
                  })
                  navigate("/profile/phone")
                }}>
                  <Typography variant="body2" align="right" style={{ marginTop: '8px' }}>
                    Confirm Phone
                  </Typography>
                </Link>
              )}

            </Grid>
            <Grid item xs={12} sm={6}>
              <Autocomplete
                options={cities}
                getOptionLabel={(option) => option?.title}
                onChange={(event, value) => setCity(value!.title)}
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
                defaultValue={user.password}
                label="Password"
                name="password"
                onChange={(event) => setPassword(event.target.value)}
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
                onChange={handleProfileInfoChange}
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
