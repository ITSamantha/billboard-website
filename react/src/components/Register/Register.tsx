import { useState } from 'react';
import '../../scss/register.scss';
import GoogleLogin from '../GoogleLogin/GoogleLogin';
import { register } from '../../service/dataService';
import { useNavigate } from 'react-router-dom';
import { Button, IconButton, Input, InputAdornment, OutlinedInput } from '@mui/material';
import Visibility from '@mui/icons-material/Visibility';
import VisibilityOff from '@mui/icons-material/VisibilityOff';

const Register = () => {
  const [passwordVisible, setPasswordVisible] = useState<boolean>(false);
  const [firstName, setFirstName] = useState<string>('');
  const [lastName, setLastName] = useState<string>('');
  const [email, setEmail] = useState<string>('');
  const [password, setPassword] = useState<string>('');
  const [phone, setPhone] = useState<string>('');
  const navigate = useNavigate();

  const handleClickShowPassword = () => setPasswordVisible((show) => !show);

  const handleMouseDownPassword = (event: any) => {
    event.preventDefault();
  };

  const handleRegister = () => {
    console.log(firstName, lastName, email, password, phone);
    register(email, password, phone, lastName, firstName);
    // TODO: check if login is successful
    navigate('/home');
  };

  return (
    <div className="register-container">
      <div>
        <div>Register form</div>
        <div className="name-field">
          <Input
            placeholder="First name"
            type="text"
            onChange={(e) => {
              setFirstName(e.target.value);
            }}
          ></Input>
          <Input
            placeholder="Last name"
            type="text"
            onChange={(e) => {
              setLastName(e.target.value);
            }}
          ></Input>
        </div>

        <Input
          placeholder="email"
          type="email"
          onChange={(e) => {
            setEmail(e.target.value);
          }}
        ></Input>
        <OutlinedInput
          id="outlined-adornment-password"
          type={passwordVisible ? 'text' : 'password'}
          onChange={(event) => setPassword(event.target.value)}
          endAdornment={
            <InputAdornment position="end">
              <IconButton
                aria-label="toggle password visibility"
                onClick={handleClickShowPassword}
                onMouseDown={handleMouseDownPassword}
                edge="end"
              >
                {passwordVisible ? <VisibilityOff /> : <Visibility />}
              </IconButton>
            </InputAdornment>
          }
          label="Password"
        />
        {/* <Input
          placeholder="phone number"
          type="tel"
          pattern="[0-9]{3} [0-9]{3} [0-9]{4}"
          onChange={(e) => {
            setPhone(e.target.value);
          }}
        ></Input> */}
      </div>
      <Button onClick={handleRegister}>Register</Button>
      <div>or</div>
      <GoogleLogin />
    </div>
  );
};

export default Register;
