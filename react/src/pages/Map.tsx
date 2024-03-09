import React, {useEffect, useState} from 'react';
import {Wrapper} from '@googlemaps/react-wrapper';
import MapComponent from '../map/MapComponent';
import AdvancedMarker from "../map/AdvancedMarker";
import AdvancedMarkerCluster from "../map/AdvancedMarkerCluster";
import useDeepCompareEffect from "use-deep-compare-effect";


type DisplayedPoint = {
    point: google.maps.LatLngLiteral,
    isCluster?: boolean,
    count?: number
};

const Map = () => {

    const [currentZoom, setCurrentZoom] = useState<number>()
    const [currentCenter, setCurrentCenter] = useState<google.maps.LatLng>()
    const [points, setPoints] = useState<google.maps.LatLngLiteral[]>([])

    const [displayedPoints, setDisplayedPoints] = useState<DisplayedPoint[]>([])

    useEffect(() => {
        setPoints([...new Array(10000)].map(() => {
                return {lat: Math.random() * 100, lng: Math.random() * 100}
            }
        ))
    }, []);

    const handleIdle = (map: google.maps.Map) => {
        setCurrentZoom(map.getZoom())
        setCurrentCenter(map.getCenter())
    }

    useEffect(() => {
        if (currentZoom) {
            let zoomInKm = (40000 / Math.pow(2, currentZoom)) * 2
            let zoomInDeg = zoomInKm / 80
            let currentCenterLat = currentCenter?.lat()
            let currentCenterLng = currentCenter?.lng()
            if (currentCenterLat && currentCenterLng) {
                let radius = zoomInDeg;
                let filteredPoints = points.filter((point) => {
                    if (currentCenterLat && currentCenterLng) {
                        return Math.abs(point.lat - currentCenterLat) <= radius && Math.abs(point.lng - currentCenterLng) <= radius
                    }
                    return false
                })
                let fromLat = currentCenterLat - radius
                let toLat = currentCenterLat + radius
                let fromLng = currentCenterLng + radius
                let toLng = currentCenterLng + radius
                for (let i = 0; i < 8; i++) {
                    let currentFromLng = fromLng + (toLng - fromLng) * i / 8
                    let currentFromLat = fromLat + (toLat - fromLat) * i / 8

                }
                setDisplayedPoints(filteredPoints.map((point) => {
                    return {
                        point: point
                    }
                }))
            }

        }
    }, [currentZoom, currentCenter]);

    return (
        <div className="Map">
            <div className="Map__Content">
                <Wrapper apiKey={'AIzaSyCllS8bOprdLh7eMPd0DcM2ZNYe2TrNS9I'} libraries={['marker']} version="beta">
                    <MapComponent center={{lat: 46, lng: 43}} zoom={13} onIdle={handleIdle}>
                        {
                            displayedPoints.map((displayedPoint) => {
                                if (displayedPoint.isCluster) {
                                    return (
                                        <AdvancedMarkerCluster onClick={(e: any) => {
                                            console.log(e)
                                        }} position={displayedPoint.point} count={displayedPoint.count} ></AdvancedMarkerCluster>
                                    )
                                } else {
                                    return (
                                        <AdvancedMarker onClick={(e: any) => {
                                            console.log(e)
                                        }} position={displayedPoint.point}></AdvancedMarker>
                                    )
                                }
                            })
                        }
                    </MapComponent>
                </Wrapper>
            </div>
            <div className="Map__Item"></div>
        </div>
    );
};

export default Map;
