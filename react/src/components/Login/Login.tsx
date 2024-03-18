import React, { useEffect, useState } from 'react';
import { IoIosArrowRoundBack } from 'react-icons/io';
import InputField from '../InputField';
import axios from 'axios';
import { Link, useNavigate } from 'react-router-dom';
import { googleLogout, useGoogleLogin } from '@react-oauth/google';
import { Button } from 'antd';
import GoogleLogin from '../GoogleLogin/GoogleLogin';
import { login } from '../../service/dataService';

function Login() {
  const [email, setEmail] = useState<string>('');
  const [password, setPassword] = useState<string>('');
  const navigate = useNavigate();

  axios.defaults.withCredentials = true;

  // @ts-ignore
  axios.defaults.credentials = 'include';

  const handleLogin = () => {
    // TODO: check if login is successful
    login(email, password);
    navigate('/');
  };

  const handleLogout = () => {};

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
              <InputField label="אימייל" id="email" type="text" value={email} setValue={setEmail} />
              <InputField
                label="סיסמה"
                id="password"
                type="password"
                value={password}
                setValue={setPassword}
              />
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
