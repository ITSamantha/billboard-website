import React, { ReactNode } from 'react';
import Menu from './components/Menu/Menu';
import axios from 'axios';
import { useSelector } from 'react-redux';
import { selectToken } from './redux/slices/MyUserSlice';

interface RouterWrapperProps {
  children: ReactNode;
}

function RouterWrapper(props: RouterWrapperProps) {
  return (
    <div className="container">
      <Menu />
      {props.children}
    </div>
  );
}

export default RouterWrapper;
