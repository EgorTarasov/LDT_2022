import { useDispatch } from "react-redux";
import { setSelectModel } from "../../../slices/selectModelSlice";

import s from "./DotBtn.module.css";

function DotBtn() {
  const dispatch = useDispatch();
  return (
    <button
      className={s.DotBtn}
      onClick={() => dispatch(setSelectModel(4))}
    ></button>
  );
}

export default DotBtn;
