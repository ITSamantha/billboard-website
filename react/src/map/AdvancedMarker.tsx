import { useState, useEffect, memo, useRef, PropsWithChildren } from 'react';
import { Root, createRoot } from 'react-dom/client';
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

  const rootRef = useRef<Root | null>(null);
  useDeepCompareEffect(() => {
    if (!map) return;

    if (!marker) {
      const container = document.createElement('div');
      container.innerHTML = "<span class='map-icon'></span>";
      setMarker(
        new google.maps.marker.AdvancedMarkerElement({
          ...options,
          gmpClickable: true,
          content: container,
          map
        })
      );
    }
  }, [marker, map, options]);

  useEffect(() => {
    if (marker && markerCluster) {
      markerCluster.addMarker(marker);
    }
  }, [marker]);

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
