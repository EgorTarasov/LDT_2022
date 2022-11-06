import Select from "react-select";

import { useSelector, useDispatch } from "react-redux";

import { DotBtn, MultipleSlider } from "../UI";
import SelectModel from "../UI/SelectModel";

import s from "./Mods.module.css";

import { setCounty } from "../../slices/countySlice";
import { setArea } from "../../slices/areaSlice";
import { setType } from "../../slices/typeSlice";
import { setRange } from "../../slices/rangeSlice";
import { setDemand } from "../../slices/demandSlice";
import Heatmap from "../UI/Heatmap";
import DownloadBtn from "../UI/DownloadBtn";
import data from "./reg.json";

const Mods = () => {
  const county = useSelector((state) => state.county.county);
  const area = useSelector((state) => state.area.area);
  const type = useSelector((state) => state.type.type);
  const range = useSelector((state) => state.range.range);
  const demand = useSelector((state) => state.demand.demand);
  const dispatch = useDispatch();

  const areaOptions = data.map((el) => {
    return {
      value: el["name"],
      label: el["name"],
    };
  });

  const countyOptions = data.map((el) => {
    return {
      value: el["name_ao"],
      label: el["name_ao"],
    };
  });

  const typeOptions = [
    {
      value: "jack",
      label: "Jack",
    },
    {
      value: "lucy",
      label: "Lucy",
    },
    {
      value: "disabled",
      disabled: true,
      label: "Disabled",
    },
    {
      value: "Yiminghe",
      label: "yiminghe",
    },
  ];
  return (
    <div className={s.header}>
      <Select
        defaultValue={{ value: county, label: "область" }}
        style={{ width: "330px", zIndex: "4" }}
        onChange={(e) => dispatch(setCounty(e.value))}
        options={countyOptions}
      />
      <Select
        defaultValue={{ value: area, label: "район" }}
        style={{ width: "330px", zIndex: "4" }}
        onChange={(e) => dispatch(setArea(e.value))}
        options={areaOptions}
      />
      <Select
        defaultValue={{ value: type, label: "тип объекта" }}
        style={{ width: "330px", zIndex: "4" }}
        onChange={(e) => dispatch(setType(e.value))}
        options={typeOptions}
      />
      <SelectModel />
      <MultipleSlider val={range} setVal={setRange} name="радиус" />
      <MultipleSlider val={demand} setVal={setDemand} name="востребованность" />
      <Heatmap />
      <DotBtn />
      <DownloadBtn />
    </div>
  );
};
export default Mods;
