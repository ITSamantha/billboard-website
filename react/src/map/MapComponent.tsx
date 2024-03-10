import React, {useEffect, useState} from 'react';
import AdvancedMarker from './AdvancedMarker';

type MapProps = {
    center: google.maps.LatLngLiteral;
    zoom: number;
    children: React.ReactNode;
    onClick?: (e: google.maps.MapMouseEvent) => void;
    onIdle?: (map: google.maps.Map) => void;
    map?: google.maps.Map;
    setMap: (map: google.maps.Map) => void;
} & google.maps.marker.AdvancedMarkerElementOptions;

function MapComponent({center, zoom, children, onClick, onIdle, map, setMap}: MapProps) {
    const ref = React.useRef<HTMLDivElement>(null);

    React.useEffect(() => {
        if (map) {
            ['click', 'idle'].forEach((eventName) => google.maps.event.clearListeners(map, eventName));
            if (onClick) {
                map.addListener('click', onClick);
            }
            if (onIdle) {
                map.addListener('idle', () => onIdle(map));
            }
        }
    }, [map, onClick, onIdle]);

    React.useEffect(() => {
        if (ref.current && !map) {
            setMap(
                new window.google.maps.Map(ref.current, {
                    center,
                    zoom,
                    mapId: 'DEMO_MAP_ID' // d5f70aa737c73675
                })
            );
        }
    }, [ref, map]);

    return (
        <>
            <div ref={ref} id="map"/>

            {React.Children.map(children, (child) => {
                if (React.isValidElement(child)) {
                    return child
                }
            })}
        </>
    );
}

export default MapComponent;
