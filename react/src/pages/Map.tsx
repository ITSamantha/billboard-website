import React, { useEffect, useState } from 'react';
import { Wrapper } from '@googlemaps/react-wrapper';
import MapComponent from '../map/MapComponent';
import AdvancedMarker from '../map/AdvancedMarker';
import AdvancedMarkerCluster from '../map/AdvancedMarkerCluster';

type DisplayedPoint = {
  point: google.maps.LatLngLiteral;
  isCluster?: boolean;
  count?: number;
};

const Map = () => {
  const [currentZoom, setCurrentZoom] = useState<number>();
  const [currentCenter, setCurrentCenter] = useState<google.maps.LatLng>();
  const [points, setPoints] = useState<google.maps.LatLngLiteral[]>([]);

  const [displayedPoints, setDisplayedPoints] = useState<DisplayedPoint[]>([]);

  useEffect(() => {
    setPoints(
      [...new Array(10000)].map(() => {
        return { lng: Math.random() * 100 - 50, lat: Math.random() * 360 - 180 };
      })
    );
  }, []);

  const handleIdle = (map: google.maps.Map) => {
    setCurrentZoom(map.getZoom());
    setCurrentCenter(map.getCenter());
  };

  useEffect(() => {
    if (currentZoom) {
      let zoomInKm = (40000 / Math.pow(2, currentZoom)) * 2;
      let zoomInDeg = zoomInKm / 80;
      let currentCenterLat = currentCenter?.lat();
      let currentCenterLng = currentCenter?.lng();
      if (currentCenterLat && currentCenterLng) {
        let radius = zoomInDeg;
        let filteredPoints = points.filter((point) => {
          if (currentCenterLat && currentCenterLng) {
            return (
              Math.abs(point.lat - currentCenterLat) <= radius &&
              Math.abs(point.lng - currentCenterLng) <= radius
            );
          }
          return false;
        });
        let fromLat = currentCenterLat - radius;
        let toLat = currentCenterLat + radius;
        let fromLng = currentCenterLng - radius;
        let toLng = currentCenterLng + radius;

        const NUMBER_OF_SECTORS = 8;
        const CLUSTER_THRESHOLD = 6;

        let buckets: google.maps.LatLngLiteral[][][] = [...new Array(NUMBER_OF_SECTORS)].map(() =>
          [...new Array(NUMBER_OF_SECTORS)].map(() => [])
        );

        if (toLat - fromLat != 0 && filteredPoints.length > 0) {
          filteredPoints.forEach((point) => {
            let nearestLat = Math.floor(
              ((point.lat - fromLat) * NUMBER_OF_SECTORS) / (toLat - fromLat)
            );
            let nearestLng = Math.floor(
              ((point.lng - fromLng) * NUMBER_OF_SECTORS) / (toLng - fromLng)
            );
            buckets[nearestLat][nearestLng].push(point);
          });
        }

        let visiblePoints: DisplayedPoint[] = [];
        for (let i = 0; i < NUMBER_OF_SECTORS; i++) {
          for (let j = 0; j < NUMBER_OF_SECTORS; j++) {
            if (buckets[i][j].length > CLUSTER_THRESHOLD) {
              let centerPoint = buckets[i][j].reduce(
                (acc, current) => {
                  return {
                    lat: acc.lat + current.lat,
                    lng: acc.lng + current.lng
                  };
                },
                { lat: 0, lng: 0 }
              );
              centerPoint.lat /= buckets[i][j].length;
              centerPoint.lng /= buckets[i][j].length;
              visiblePoints.push({
                isCluster: true,
                count: buckets[i][j].length,
                point: centerPoint
              });
            } else {
              buckets[i][j].forEach((point) => visiblePoints.push({ point: point }));
            }
          }
        }
        console.log(visiblePoints);
        setDisplayedPoints(visiblePoints);
      }
    }
  }, [currentZoom, currentCenter]);

  const [map, setMap] = React.useState<google.maps.Map>();

  return (
    <div className="Map">
      <div className="Map__Content">
        <Wrapper
          apiKey={''} // AIzaSyCllS8bOprdLh7eMPd0DcM2ZNYe2TrNS9I
          libraries={['marker']}
          version="beta"
        >
          <MapComponent
            map={map}
            setMap={setMap}
            center={{ lat: 46, lng: 43 }}
            zoom={13}
            onIdle={handleIdle}
          >
            {displayedPoints.map((displayedPoint) => {
              if (displayedPoint.isCluster) {
                return (
                  <AdvancedMarkerCluster
                    onClick={(e: any) => {
                      console.log(e);
                    }}
                    position={displayedPoint.point}
                    count={displayedPoint.count}
                    map={map}
                  ></AdvancedMarkerCluster>
                );
              } else {
                return (
                  <AdvancedMarker
                    onClick={(e: any) => {
                      // e.element = null
                      e.map = null;
                      console.log(e.map);
                    }}
                    position={displayedPoint.point}
                    map={map}
                  ></AdvancedMarker>
                );
              }
            })}
          </MapComponent>
        </Wrapper>
      </div>
      <div className="Map__Item"></div>
    </div>
  );
};

export default Map;
