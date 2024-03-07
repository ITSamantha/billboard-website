import React from 'react';
import { Wrapper } from '@googlemaps/react-wrapper';
import MapComponent from '../map/MapComponent';
import AdvancedMarker from '../map/AdvancedMarker';

const Map = () => {
  return (
    <div className="Map">
      <div className="Map__Content">
        <Wrapper apiKey={''} libraries={['marker']}>
          <MapComponent center={{ lat: 46, lng: 43 }} zoom={13} />
        </Wrapper>
      </div>
      <div className="Map__Item"></div>
    </div>
  );
};

export default Map;
