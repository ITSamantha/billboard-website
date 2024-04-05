import React, { useEffect, useState } from 'react';
import { IoIosArrowRoundBack } from 'react-icons/io';
import axios from 'axios';
import { Link, useNavigate } from 'react-router-dom';
import GoogleLogin from '../GoogleLogin/GoogleLogin';
import { useDispatch, useSelector } from 'react-redux';
import {
  fetchLogin,
  fetchMyUser,
  selectError,
  selectLoading,
  selectMyUser
} from '../../redux/slices/MyUserSlice';
import { AppDispatch } from '../../redux/store';
import { Input } from '@mui/material';
import Loader from '../Loader';

function Login() {
  const [email, setEmail] = useState<string>('');
  const [password, setPassword] = useState<string>('');
  const dispatch = useDispatch<AppDispatch>();
  const user = useSelector(selectMyUser);
  const navigate = useNavigate();
  const error = useSelector(selectError);
  const loading = useSelector(selectLoading);

  const handleLogin = async () => {
    await dispatch(fetchLogin({ email, password }) as any);
    await dispatch(fetchMyUser());
  };

  useEffect(() => {
    if (user && user.id && !error) {
      const id = user.id;
      navigate(`/profile/${id}`);
    }
  }, [user, navigate]);

  const handleLogout = () => {};

  if (error) {
    return <div>Error. Reload page</div>;
  }
  if (loading) {
    return (
      <div>
        <Loader />
      </div>
    );
  }

  return (
    <>
      <div className="page-container">
        <nav id="headerContainer">
          <div className="uitk-layout-flex uitk-layout-flex-align-items-center uitk-toolbar">
            <Link to="/" className="back-btn-login">
              <IoIosArrowRoundBack />
            </Link>
          </div>
        </nav>
        <div className="uitk-layout-flex uitk-layout-flex-align-content-center uitk-layout-flex-align-items-center uitk-layout-flex-flex-direction-row uitk-layout-flex-justify-content-center">
          <div className="uitk-spacing uitk-spacing-padding-inline-six uitk-layout-flex-item-align-self-center uitk-layout-flex-item uitk-layout-flex-item-max-width-one_hundred_twelve uitk-layout-flex-item-flex-basis-one_hundred_twelve">
            <div className="uitk-layout-flex uitk-layout-flex-flex-direction-column uitk-spacing uitk-spacing-padding-block-six">
              <h1 className="uitk-heading uitk-heading-4 uitk-layout-flex-item">
                היכנס או צור חשבון
              </h1>
            </div>

            <div
              id="signin-with-google-container"
              className="uitk-layout-flex-item-align-self-center uitk-layout-flex-item"
            >
              <div className="uitk-text uitk-type-300 uitk-text-default-theme uitk-spacing uitk-spacing-margin-blockend-six">
                אם אין לך חשבון אתה יכול <a href="/sign-up">ליצור חשבון חדש</a> או להתחבר עם שירותים
                אחרים
              </div>
              <div className="uitk-layout-flex">
                <GoogleLogin />
              </div>
              <div className="uitk-text uitk-type-center uitk-type-300 uitk-text-default-theme uitk-spacing uitk-spacing-margin-block-six">
                אוֹ
              </div>
            </div>
            <div className="uitk-layout-flex uitk-layout-flex-flex-direction-column uitk-layout-flex-gap-six">
              <Input
                placeholder="Email"
                type="text"
                onChange={(e) => {
                  setEmail(e.target.value);
                }}
              ></Input>
              <Input
                placeholder="Last name"
                type="password"
                onChange={(e) => {
                  setPassword(e.target.value);
                }}
              ></Input>

              <button
                onClick={handleLogin}
                id="loginFormSubmitButton"
                type="submit"
                className="uitk-button uitk-button-large uitk-button-has-text uitk-button-primary"
              >
                לְהַמשִׁיך
              </button>
              <Link to={'/register'}>
                <button>Register</button>
              </Link>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}

export default Login;
