import React, {useEffect, useState} from 'react'
import AdvancedMarker from "./AdvancedMarker";

type MapProps = {
    center: google.maps.LatLngLiteral,
    zoom: number,
} & google.maps.marker.AdvancedMarkerElementOptions

function MapComponent({center, zoom}: MapProps) {

    const ref = React.useRef<HTMLDivElement>(null);
    const [map, setMap] = React.useState<google.maps.Map>();

    const [options, setOptions] = useState<any>()

    useEffect(() => {
        if (map) {
            map.setOptions(options);
        }
    }, [map, options]);

    React.useEffect(() => {
        if (ref.current && !map) {
            setMap(new window.google.maps.Map(ref.current, {
                center, zoom, mapId: "DEMO_MAP_ID"
            }));
        }
    }, [ref, map]);

    return (
        <>

            <div ref={ref} id="map"/>
            <AdvancedMarker onClick={(e:any) => {console.log(e)}} map={map} position={center} zIndex={66}></AdvancedMarker>
            <AdvancedMarker map={map} position={{"lat": 34, "lng": 15}} zIndex={1}></AdvancedMarker>
            <AdvancedMarker map={map} position={{"lat": 36, "lng": 18}} zIndex={1}></AdvancedMarker>
            <AdvancedMarker map={map} position={{"lat": 37, "lng": 16}} zIndex={1}></AdvancedMarker>
        </>)

}

export default MapComponent