import React, { useState } from 'react';
import '../scss/register.scss';
import GoogleLogin from '../components/GoogleLogin/GoogleLogin';
import { getMyUser, register } from '../service/dataService';
import {Link, useNavigate} from 'react-router-dom';
import {Button, IconButton, Input, InputAdornment, OutlinedInput, TextField, ThemeProvider} from '@mui/material';
import Visibility from '@mui/icons-material/Visibility';
import VisibilityOff from '@mui/icons-material/VisibilityOff';
import {IoIosArrowRoundBack} from "react-icons/io";
import {THEME} from "./profile/Profile";
import { fetchMyUser } from '../redux/slices/MyUserSlice';
import { useDispatch } from 'react-redux';
import { AppDispatch } from '../redux/store';

const Register = () => {
  const [passwordVisible, setPasswordVisible] = useState<boolean>(false);
  const [firstName, setFirstName] = useState<string>('');
  const [lastName, setLastName] = useState<string>('');
  const [email, setEmail] = useState<string>('');
  const [password, setPassword] = useState<string>('');
  const [phone, setPhone] = useState<string>('');
  const navigate = useNavigate();
  const dispatch = useDispatch<AppDispatch>();

  const [error, setError] = useState<string>()

  const handleClickShowPassword = () => setPasswordVisible((show) => !show);

  const handleMouseDownPassword = (event: any) => {
    event.preventDefault();
  };

  const handleRegister = () => {
    console.log(firstName, lastName, email, password, phone);
    register(email, password, phone, lastName, firstName).then(async () => {
      let myUser = await dispatch(fetchMyUser());
      localStorage.setItem('user', JSON.stringify(myUser.payload))
      navigate('/');
    }).catch(error => {
      setError(error.response.data.detail)
    });
  };

  return (
      <><ThemeProvider theme={THEME}>
          <div className="Login">
              <nav className="Login__Navigate">
                  <div className="Login__Navigate__Back">
                      <Link to="/">
                          <IoIosArrowRoundBack /> Back
                      </Link>
                  </div>
              </nav>
              <div className="Login__Block">
                  <div>
                      <div>
                          <h1>
                              היכנס או צור חשבון
                          </h1>
                      </div>

                      <div className="Login__Social">
                          <div>
                              אם אין לך חשבון אתה יכול <a href="/login">ליצור חשבון חדש</a> או להתחבר עם שירותים
                              אחרים
                          </div>
                          <div className="Login__Social__Buttons">
                              <div className="Login__Social__Buttons__Item">
                                  <GoogleLogin />
                              </div>
                          </div>
                      </div>
                      <div className="Login__Or">or</div>
                      <div className="Login__Form">
                          <div className="Login__Input">
                              <TextField
                                  variant="outlined"
                                  margin="normal"
                                  fullWidth
                                  id="first-name"
                                  label="First name"
                                  defaultValue={firstName}
                                  name="first-name"
                                  type="text"
                                  onChange={(event) => setFirstName(event.target.value)}
                                  autoComplete="first-name"
                              />
                          </div>
                          <div className="Login__Input">
                              <TextField
                                  variant="outlined"
                                  margin="normal"
                                  fullWidth
                                  id="last-name"
                                  label="Last name"
                                  defaultValue={lastName}
                                  type="text"
                                  name="last-name"
                                  onChange={(event) => setLastName(event.target.value)}
                                  autoComplete="last-name"
                              />
                          </div>
                          <div className="Login__Input">
                              <TextField
                                  variant="outlined"
                                  margin="normal"
                                  fullWidth
                                  id="email"
                                  type="email"
                                  label="Email"
                                  defaultValue={email}
                                  name="email"
                                  onChange={(event) => setEmail(event.target.value)}
                                  autoComplete="email"
                              />
                          </div>
                          <div className="Login__Input">
                              <TextField
                                  variant="outlined"
                                  margin="normal"
                                  fullWidth
                                  id="password"
                                  type="password"
                                  label="Password"
                                  defaultValue={password}
                                  name="password"
                                  onChange={(event) => setPassword(event.target.value)}
                                  autoComplete="family-name"
                              />
                          </div>
                        { error && <div className="Login__Error">{ error }</div> }
                        <div className="Login__Button">
                              <button
                                  onClick={handleRegister}
                                  type="submit"
                              >
                                  Register
                              </button>
                          </div>
                          <Link to={'/login'} className="Login__Redirect">
                              If you already have an account you can login
                          </Link>
                      </div>
                  </div>
              </div>
          </div>
      </ThemeProvider>
      </>
  );
};

export default Register;
