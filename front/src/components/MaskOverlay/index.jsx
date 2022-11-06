import { Polygon } from "react-leaflet";

import { useSelector } from "react-redux";
const MaskOverlay = (props) => {
  const areaCoords = useSelector((state) => state.areaCoords.areaCoords);
  return (
    <>
      <Polygon pathOptions={{ color: "lime" }} positions={areaCoords} />
    </>
  );
};
export default MaskOverlay;
