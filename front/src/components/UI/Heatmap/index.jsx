import s from "./Heatmap.module.css";

import { useDispatch } from "react-redux";
import { setSelectModel } from "../../../slices/selectModelSlice";

function Heatmap() {
  const dispatch = useDispatch();
  return (
    <button
      className={s.heatmap}
      onClick={() => dispatch(setSelectModel(2))}
    ></button>
  );
}

export default Heatmap;
