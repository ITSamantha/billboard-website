import {memo, PropsWithChildren, useEffect, useState} from 'react';

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

    useEffect(() => {
        if (!map) return;

        if (!marker) {
            const container = document.createElement('div');
            container.innerHTML = "<span class='map-cluster'>" + count + "</span>";
            setMarker(
                new google.maps.marker.AdvancedMarkerElement({
                    ...options,
                    gmpClickable: true,
                    content: container,
                    map
                })
            );
        }
    }, [marker, map]);

    useEffect(() => {
    }, [marker]);

    useEffect(() => {
        if (!marker) return;
        if (onClick) {
            google.maps.event.addListener(marker, 'gmp-click', () => {
                onClick(marker)
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

export default memo(AdvancedMarkerCluster);
