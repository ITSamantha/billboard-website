import { memo, PropsWithChildren, useEffect, useState } from 'react';
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

  useDeepCompareEffect(() => {
    if (!map) return;

    if (!marker) {
      const container = document.createElement('div');
      container.innerHTML = "<span class='cluster-icon'>" + count + '</span>';
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
    return () => {
      if (marker) {
        console.log('CLUSTER V');
        marker.map = null;
      }
    };
  }, [marker]);

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
