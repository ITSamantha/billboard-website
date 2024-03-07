import React, { useEffect, useState } from 'react';
import { IoIosArrowRoundBack } from 'react-icons/io';
import InputField from '../InputField';
import axios from 'axios';
import { Link } from 'react-router-dom';
import { googleLogout, useGoogleLogin } from '@react-oauth/google';
import { Button } from 'antd';

interface Profile {
  picture: string;
  name: string;
  email: string;
}

function Login() {
  const [email, setEmail] = useState<string>('');
  const [password, setPassword] = useState<string>('');
  const [user, setUser] = useState<any>(null);
  const [profile, setProfile] = useState<Profile | null>(null);

  const login = useGoogleLogin({
    onSuccess: (codeResponse: any) => setUser(codeResponse),
    onError: (error: any) => console.log('Login Failed:', error)
  });

  useEffect(() => {
    if (user) {
      axios
        .get(`https://www.googleapis.com/oauth2/v1/userinfo?access_token=${user.access_token}`, {
          headers: {
            Authorization: `Bearer ${user.access_token}`,
            Accept: 'application/json'
          }
        })
        .then((res) => {
          setProfile(res.data);
        })
        .catch((err) => console.log(err));
    }
  }, [user]);

  useEffect(() => {
    if (user) {
      axios
        .get(`https://www.googleapis.com/oauth2/v1/userinfo?access_token=${user.access_token}`, {
          headers: {
            Authorization: `Bearer ${user.access_token}`,
            Accept: 'application/json'
          }
        })
        .then((res) => {
          setProfile(res.data);
        })
        .catch((err) => console.log(err));
    }
  }, [user]);

  const logOut = () => {
    googleLogout();
    setProfile(null);
  };

  axios.defaults.withCredentials = true;

  // @ts-ignore
  axios.defaults.credentials = 'include';

  const handleLogin = () => {
    axios
      .post(
        'https://api.uvuv643.ru/auth/login',
        {
          email: email,
          password: password
        },
        { withCredentials: true }
      )
      .then((r) => console.log(r));
  };

  const handleLogout = () => {
    axios
      .post('https://api.uvuv643.ru/auth/logout', {}, { withCredentials: true })
      .then((r) => console.log(r));
  };

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
                <Button onClick={() => login()}>Sign in with Google </Button>
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
            </div>
          </div>
        </div>
      </div>
    </>
  );
}

export default Login;
