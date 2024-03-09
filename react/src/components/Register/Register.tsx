import { Button, Input } from 'antd';
import { EyeInvisibleOutlined, EyeTwoTone } from '@ant-design/icons';
import { useState } from 'react';
import '../../scss/register.scss';
import GoogleLogin from '../GoogleLogin/GoogleLogin';
import axios from 'axios';

const Register = () => {
  const [passwordVisible, setPasswordVisible] = useState<boolean>(false);
  const [firstName, setFirstName] = useState<string>('');
  const [lastName, setLastName] = useState<string>('');
  const [email, setEmail] = useState<string>('');
  const [password, setPassword] = useState<string>('');
  const [phone, setPhone] = useState<string>('');

  const handleRegister = () => {
    console.log(firstName, lastName, email, password, phone);
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
        <Input.Password
          placeholder="input password"
          onChange={(e) => {
            setPassword(e.target.value);
          }}
          iconRender={(visible) => (visible ? <EyeTwoTone /> : <EyeInvisibleOutlined />)}
        />
        <Input
          placeholder="phone number"
          type="tel"
          pattern="[0-9]{3} [0-9]{3} [0-9]{4}"
          onChange={(e) => {
            setPhone(e.target.value);
          }}
        ></Input>
      </div>
      <Button onClick={handleRegister}>Register</Button>
      <div>or</div>
      <GoogleLogin />
    </div>
  );
};

export default Register;
