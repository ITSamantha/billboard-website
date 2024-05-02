import { ReactNode } from 'react';
import Menu from './components/Menu/Menu';

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
