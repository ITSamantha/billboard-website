import { PropsWithChildren, useEffect, useRef, useState } from 'react';
import useDeepCompareEffect from 'use-deep-compare-effect';

type AdvancedMarkerClusterProps = {
  onClick?: Function;
  map?: google.maps.Map;
  count?: number;
} & google.maps.marker.AdvancedMarkerElementOptions;

const AdvancedMarkerCluster: React.FC<PropsWithChildren<AdvancedMarkerClusterProps>> = ({
                                                                                          onClick,
                                                                                          map,
                                                                                          count,
                                                                                          children,
                                                                                          ...options
                                                                                        }) => {
  const [marker, setMarker] = useState<google.maps.marker.AdvancedMarkerElement>();
  const markerRef = useRef<google.maps.marker.AdvancedMarkerElement>();

  useEffect(() => {
    if (!map) return;

    if (!marker) {
      const container = document.createElement('div');
      container.innerHTML = '<span class=\'cluster-icon\'>' + Math.round(Math.random() * 1000) + '</span>';
      let currentMarker = new google.maps.marker.AdvancedMarkerElement({
        ...options,
        gmpClickable: true,
        content: container,
        map
      });
      markerRef.current = currentMarker
      setMarker(currentMarker);
    }
  }, [marker, map, options]);

  useEffect(() => {
    return () => {
      if (markerRef.current) {
        markerRef.current.map = null;
      } else {
        alert("ALARM")
      }
    };
  }, []);

  useEffect(() => {
    if (!marker) return;
    if (onClick) {
      google.maps.event.addListener(marker, 'gmp-click', () => {
        onClick(marker);
      });
    }
    return () => {
      if (marker) {
        google.maps.event.clearListeners(marker, 'gmp-click');
      }
    };
  }, [marker, children, onClick]);

  return null;
};

export default AdvancedMarkerCluster;
