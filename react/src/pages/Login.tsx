import React, { useEffect, useState } from 'react';
import { IoIosArrowRoundBack } from 'react-icons/io';
import { Link, useNavigate } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import {
  fetchLogin,
  fetchMyUser,
  selectError,
  selectLoading,
  selectMyUser
} from '../redux/slices/MyUserSlice';
import { AppDispatch } from '../redux/store';
import { TextField, ThemeProvider } from '@mui/material';
import Loader from '../components/Loader';
import { THEME } from './profile/Profile';
import GoogleLogin from '../components/GoogleLogin/GoogleLogin';

function Login() {
  const [email, setEmail] = useState<string>('');
  const [password, setPassword] = useState<string>('');
  const dispatch = useDispatch<AppDispatch>();
  const user = useSelector(selectMyUser);
  const navigate = useNavigate();
  const error = useSelector(selectError);
  const loading = useSelector(selectLoading);

  const handleLogin = async () => {
    try {
      await dispatch(fetchLogin({ email, password }));
      if (localStorage.getItem('access_token')) {
        let myUser = await dispatch(fetchMyUser());
        localStorage.setItem('user', JSON.stringify(myUser.payload));
        navigate('/');
      }
    } catch (error) {}
  };

  useEffect(() => {
    if (user && user.id && !error) {
      const id = user.id;
      navigate(`/profile/${id}`);
    }
  }, [user, navigate]);

  return (
    <>
      <ThemeProvider theme={THEME}>
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
                <h1>היכנס או צור חשבון</h1>
              </div>

              <div className="Login__Social">
                <div>
                  אם אין לך חשבון אתה יכול <a href="/register">ליצור חשבון חדש</a> או להתחבר עם
                  שירותים אחרים
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
                    id="email"
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
                    autoComplete="password"
                  />
                </div>
                <div className="Login__Button">
                  <button onClick={handleLogin} type="submit">
                    <div> login</div>
                  </button>
                  {loading ? <Loader /> : <></>}
                </div>
                <div>{error ? <div>Incorrect credentials. Please try again.</div> : <></>}</div>
                <Link to={'/register'} className="Login__Redirect">
                  If you have no account you can register
                </Link>
              </div>
            </div>
          </div>
        </div>
      </ThemeProvider>
    </>
  );
}

export default Login;
