import { useState, useEffect, memo, useRef, PropsWithChildren } from "react";
import { Root, createRoot } from "react-dom/client";

type AdvancedMarkerProps = {
    onClick?: Function;
    map?: google.maps.Map;
} & google.maps.marker.AdvancedMarkerElementOptions;

const AdvancedMarker: React.FC<PropsWithChildren<AdvancedMarkerProps>> = ({
                                                                              onClick,
                                                                              map,
                                                                              children,
                                                                              ...options
                                                                          }) => {
    const [marker, setMarker] =
        useState<google.maps.marker.AdvancedMarkerElement>();

    useEffect(() => {
        if (!map) return;

        if (!marker) {
            const container = document.createElement("div");
            container.innerHTML = "<span class='map-icon'></span>"
            setMarker(
                new google.maps.marker.AdvancedMarkerElement({
                    ...options,
                    gmpClickable: true,
                    gmpDraggable: true,
                    // content: container,
                    map,
                }),
            );
        }
    }, [marker, map]);

    useEffect(() => {
    }, [marker]);

    useEffect(() => {
        if (!marker) return;
        if (onClick) {
            google.maps.event.addListener(marker, "gmp-click", onClick);
            console.log("gmpclick", google.maps.event.hasListeners(marker, 'gmp-click'))
        }
        return () => {
            if (marker) {
                google.maps.event.clearListeners(marker, "gmp-click");
            }
        };
    }, [marker, children, onClick]);

    return null;
};

export default memo(AdvancedMarker);