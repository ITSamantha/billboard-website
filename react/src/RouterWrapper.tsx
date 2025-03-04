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
  }, [dispatch]);

  return (
    <>
      <Menu />
      {props.children}
    </>
  );
}

export default RouterWrapper;
