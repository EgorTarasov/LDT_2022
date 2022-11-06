import { MapContainer, TileLayer, useMapEvents } from "react-leaflet";
import { useDispatch } from "react-redux";
import s from "./Map.module.css";

import Model from "../Model";
import { setDot } from "../../slices/dotSlice";

const Maps = () => {
  const dispatch = useDispatch();

  const MapEvents = () => {
    /**
     * https://stackoverflow.com/questions/70392715/how-to-get-coordinates-of-current-mouse-click-in-leaflet-react-js
     */
    useMapEvents({
      click(e) {
        dispatch(setDot([e.latlng.lat, e.latlng.lng]));
      },
    });
    return false;
  };
  return (
    <div className={s.container}>
      <MapContainer
        center={[55.677769, 37.764748]}
        zoom={11}
        scrollWheelZoom={false}
        className={s.leafletContainer}
      >
        <TileLayer
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />

        <Model />
        <MapEvents />
      </MapContainer>
    </div>
  );
};
/**
 * Model not redraws
 */
export default Maps;
