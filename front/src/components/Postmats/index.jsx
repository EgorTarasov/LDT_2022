import { Popup, Marker } from "react-leaflet";

const Postmats = (props) => {
  let data = props.data;
  return (
    <>
      {data.map((el) => (
        <Marker position={[el["long"], el["lat"]]} key={el["id"]}>
          <Popup>
            {
              <>
                <p>{el["name"]}</p>

                <p>{el["lat"] + " & " + el["long"]}</p>
              </>
            }
          </Popup>
        </Marker>
      ))}
    </>
  );
};
export default Postmats;
