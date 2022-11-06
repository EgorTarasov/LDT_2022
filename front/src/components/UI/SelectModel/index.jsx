import Select from "react-select";
import { useDispatch, useSelector } from "react-redux";
import { setSelectModel } from "../../../slices/selectModelSlice";
import { useEffect, useState } from "react";
import { useFetch } from "../../../hooks";

const selectModelOptions = [
  { value: 1, label: "точки на карте" },
  { value: 2, label: "тепловая карта" },
  { value: 3, label: "сектор" },
  { value: 4, label: "ваша точка" },
];

function SelectModel() {
  const dispatch = useDispatch();
  const selectModel = useSelector((state) => state.selectModel.selectModel);

  useFetch();

  function handleSelectModelChange(selectedOption) {
    dispatch(setSelectModel(selectedOption));
  }

  const [currentChoise, setCurrentChoise] = useState(selectModelOptions[0]);

  useEffect(() => {
    setCurrentChoise(selectModelOptions[selectModel - 1]);
  }, [setCurrentChoise, selectModel]);

  return (
    <div style={{ width: "auto" }}>
      <Select
        value={currentChoise}
        onChange={(e) => handleSelectModelChange(e.value)}
        options={selectModelOptions}
      />
    </div>
  );
}
/**
 * сделал стейт по автозаполнению селекта,но он не меняется
 */
export default SelectModel;
