import { Popup, Marker, Circle } from "react-leaflet";
import { useSelector } from "react-redux";

function Dot() {
  const dot = useSelector((state) => state.dot.dot);
  const range = useSelector((state) => state.range.range);

  return (
    <>
      <Marker position={dot}>
        <Popup>
          {
            <>
              <span>Выбранная точка </span>
              <br />
              <span>{dot[0] + " & " + dot[1]}</span>
            </>
          }
        </Popup>
      </Marker>
      <Circle
        center={dot}
        pathOptions={{ color: "green", fillColor: "green" }}
        radius={range[1]}
      />
    </>
  );
}

export default Dot;
