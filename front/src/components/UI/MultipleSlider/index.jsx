import { Slider } from "antd";

import React from "react";
import { useDispatch } from "react-redux";
const marks = {
  0: "0",
  1000: "1000",
};

const MultipleSlider = (props) => {
  const dispatch = useDispatch();
  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
      }}
    >
      <span>{props.name}</span>
      <Slider
        range={{ draggableTrack: true }}
        marks={marks}
        defaultValue={props.val}
        onAfterChange={(e) => dispatch(props.setVal(e))}
        style={{ width: "200px", zIndex: "4" }}
        max={1000}
      />
    </div>
  );
};

export default MultipleSlider;
