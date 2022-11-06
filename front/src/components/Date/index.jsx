import React from "react";
import { DatePicker, message } from "antd";
import "antd/dist/antd.css";
import { useDispatch } from "react-redux";
import { setDate } from "../../slices/dateSlice";

const Date = () => {
  const dispatch = useDispatch();
  const handleChange = (value) => {
    message.info(
      `Selected Date: ${value ? value.format("YYYY-MM-DD") : "None"}`
    );
    dispatch(setDate(value.format("YYYY-MM-DD")));
  };
  return (
    <div style={{}}>
      <DatePicker onChange={handleChange} />
    </div>
  );
};
export default Date;
