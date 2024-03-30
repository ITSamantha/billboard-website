import React from 'react';
import { Spin } from 'antd';

interface LoaderProps {
  fullscreen ?: boolean
}

const Loader = ({ fullscreen } : LoaderProps)  => {

  if (fullscreen) {
    return <Spin spinning size="large" fullscreen />
  }
  return (
    <div className="Loader" style={{ minWidth: 100, minHeight: 100, display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
      <Spin spinning size="large" />
    </div>
  );

};

export default Loader;