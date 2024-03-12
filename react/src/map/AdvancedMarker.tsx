import { PropsWithChildren, useEffect, useRef, useState } from 'react';
import useDeepCompareEffect from 'use-deep-compare-effect';
import { MarkerClusterer } from '@googlemaps/markerclusterer';

type AdvancedMarkerProps = {
  onClick?: Function;
  map?: google.maps.Map;
  markerCluster?: MarkerClusterer;
} & google.maps.marker.AdvancedMarkerElementOptions;

const AdvancedMarker: React.FC<PropsWithChildren<AdvancedMarkerProps>> = ({
                                                                            onClick,
                                                                            map,
                                                                            children,
                                                                            markerCluster,
                                                                            ...options
                                                                          }) => {


  const [marker, setMarker] = useState<google.maps.marker.AdvancedMarkerElement>();
  const markerRef = useRef<google.maps.marker.AdvancedMarkerElement>();

  useEffect(() => {
    if (!map) return;

    if (!marker) {
      const container = document.createElement('div');
      container.innerHTML = '<span class=\'map-icon\'></span>';
      let currentMarker = new google.maps.marker.AdvancedMarkerElement({
        ...options,
        gmpClickable: true,
        content: container,
        map
      });
      setMarker(currentMarker);
      markerRef.current = currentMarker;
    }
  }, [marker, map, options]);

  useEffect(() => {
    return () => {
      if (markerRef.current) {
        markerRef.current.map = null;
      } else {
        alert("ALARM POINT")
      }
    }
  }, []);

  useEffect(() => {
    if (!marker) return;
    if (onClick) {
      google.maps.event.addListener(marker, 'gmp-click', () => onClick(marker));
    }
    return () => {
      if (marker) {
        google.maps.event.clearListeners(marker, 'gmp-click');
      }
    };
  }, [marker, children, onClick]);

  return null;
};

export default AdvancedMarker;
