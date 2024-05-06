import { ReactNode, useEffect } from 'react';
import Menu from './components/Menu/Menu';
import { useDispatch } from 'react-redux';
import { initialUpdate } from './redux/slices/MyUserSlice';

interface RouterWrapperProps {
  children: ReactNode;
}

function RouterWrapper(props: RouterWrapperProps) {
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(initialUpdate());
  }, []);

  return (
    // <div className="container">
    <>
      <Menu />
      {props.children}
    </>
    // </div>
  );
}

export default RouterWrapper;
