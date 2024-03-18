import React, { useEffect, useRef, useState } from 'react';
import { Wrapper } from '@googlemaps/react-wrapper';
import MapComponent from './MapComponent';

export interface MapPoint {
  lat: number,
  lng: number,
  address: string,
}

type MapInputProps = {
  onChange: (point: MapPoint) => void
}

const MapInput = ({ onChange } : MapInputProps) => {

  const [map, setMap] = React.useState<google.maps.Map>();
  const [currentPoint, setCurrentPoint] = useState<google.maps.LatLng>()
  const markerRef = useRef<google.maps.marker.AdvancedMarkerElement>()

  const [address, setAddress] = useState<string>('')
  const geocoderRef = useRef<google.maps.Geocoder>()


  const handleClick = (event: google.maps.MapMouseEvent) => {
    if (event.latLng) {
      setCurrentPoint(event.latLng)
    }
  };

  useEffect(() => {
    if (currentPoint && currentPoint?.lat() && currentPoint?.lng()) {
      if (markerRef.current) {
        markerRef.current.map = null
        delete markerRef.current
      }
      const targetPointPosition : google.maps.LatLngLiteral = {
        lat: currentPoint?.lat(),
        lng: currentPoint?.lng()
      }
      const container = document.createElement('div');
      container.innerHTML = '<span class=\'map-icon\'></span>';
      markerRef.current = new google.maps.marker.AdvancedMarkerElement({
        position: targetPointPosition,
        content: container,
        map
      })

      geocoderRef.current = new google.maps.Geocoder()
      geocoderRef.current.geocode({ location: currentPoint })
        .then(r => {
          if (r.results.length > 1) {
            onChange({
              ...targetPointPosition,
              address: r.results[1].formatted_address
            })
          } else if (r.results.length === 1) {
            onChange({
              ...targetPointPosition,
              address: r.results[0].formatted_address
            })
          }
        })
    }
  }, [currentPoint]);

  // useEffect(() => {
  //   if (point) {
  //     setCurrentPoint(new google.maps.LatLng(point))
  //   }
  // }, [point]);

  return (
    <div className="MapInput">
      <Wrapper
        apiKey={'AIzaSyCllS8bOprdLh7eMPd0DcM2ZNYe2TrNS9I'} //
        libraries={['marker', 'maps', 'geocoding']}
        version="beta"
      >
        <MapComponent
          map={map}
          setMap={setMap}
          center={{ lat: 46, lng: 43 }}
          zoom={13}
          onClick={handleClick}
        >
        </MapComponent>
      </Wrapper>
    </div>
  );

};

export default MapInput;