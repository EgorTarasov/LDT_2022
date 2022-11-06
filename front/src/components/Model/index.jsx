import { useEffect, useState } from "react";
import MaskOverlay from "../MaskOverlay";
import Postmats from "../Postmats";

import useGetJson from "../../hooks/useGetJson";

import { useSelector, useDispatch } from "react-redux";
import { HeatmapLayer } from "react-leaflet-heatmap-layer-v3";
import { Dot } from "../UI";
import { setAreaCoords } from "../../slices/areaCoordsSlice";

const Model = () => {
  const selectModel = useSelector((state) => state.selectModel.selectModel);
  const area = useSelector((state) => state.area.area);
  const dispatch = useDispatch();
  const [currentChoise, setCurrentChoise] = useState(<></>);
  const data = useGetJson();

  const dots = useGetJson().map((el) => [
    el["long"],
    el["lat"],
    `${Math.random()}`,
  ]);
  dispatch(
    setAreaCoords(
      data.map((el) => {
        if (el["name"] === area) {
          return el["geometry"]["coordinates"];
        }
        return [];
      })
    )
  );

  console.log("data");
  console.log("dots");
  console.log(data);
  console.log(dots);
  useEffect(() => {
    switch (selectModel) {
      case 1:
        setCurrentChoise(<Postmats data={data} />);
        break;

      case 2:
        setCurrentChoise(
          <HeatmapLayer
            fitBoundsOnLoad
            fitBoundsOnUpdate
            points={dots}
            longitudeExtractor={(m) => m[1]}
            latitudeExtractor={(m) => m[0]}
            intensityExtractor={(m) => parseFloat(m[2])}
            radius={10}
            max={100}
            minOpacity={1}
            useLocalExtrema={true}
          />
        );
        break;

      case 3:
        setCurrentChoise(<MaskOverlay />);
        break;
      case 4:
        setCurrentChoise(
          <>
            <Dot />
            <Postmats data={data} />
          </>
        );
        break;

      default:
        setCurrentChoise(<></>);
        break;
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [selectModel, dispatch, data]);
  return currentChoise;
};
export default Model;
