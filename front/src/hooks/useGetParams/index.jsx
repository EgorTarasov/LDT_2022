import { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import axios from "axios";
import { setDots } from "../../slices/dotsSlice";
function useGetParams() {
  const date = useSelector((state) => state.date.date);
  const dots = useSelector((state) => state.dots.dots);
  const dot = useSelector((state) => state.dot.dot);
  const county = useSelector((state) => state.county.county);
  const area = useSelector((state) => state.area.area);
  const type = useSelector((state) => state.type.type);
  const range = useSelector((state) => state.range.range);
  const demand = useSelector((state) => state.demand.demand);
  const selectModel = useSelector((state) => state.selectModel.selectModel);
  const dispatch = useDispatch();
  const params = {
    selectModel: selectModel,
    date: date,
    demand: demand,
    area: area,
    range: range,
    type: type,
    county: county,
    dots: dots,
    dot: dot,
  };
  useEffect(() => {
    axios
      .get("/places/radius", {
        params: {
          lat: 37.62268066406251,
          long: 55.75068339731634,
          r: 1500,
        },
      })
      .catch((error) => {
        console.log("error " + error);
        console.log(error.request);
      })
      .then((response) => response && dispatch(setDots(response.data)));
    console.log(111);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);
  useEffect(() => {
    axios
      .get("/places/radius", {
        params: {
          lat: dot[1],
          long: dot[0],
          r: range[1],
        },
      })
      .catch((error) => {
        console.log("error " + error);
        console.log(error.request);
      })
      .then((response) => response && dispatch(setDots(response.data)));
    console.log(222);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [range[1]]);
  useEffect(() => {
    selectModel === 4 &&
      axios
        .get("/places/radius", {
          params: {
            lat: dot[1],
            long: dot[0],
            r: range[1],
          },
        })
        .catch((error) => {
          console.log("error " + error);
          console.log(error.request);
        })
        .then((response) => response && dispatch(setDots(response.data)));
    console.log(333);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [dot]);
  useEffect(() => {
    axios
      .get("/places/all", {
        params: {
          offset: 0,
          count: 1000,
        },
      })
      .catch((error) => {
        console.log("error " + error);
        console.log(error.request);
      })
      .then((response) => response && dispatch(setDots(response.data)));
    console.log(333);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [date]);
  useEffect(() => {
    axios
      .get("/places/all", {
        params: {
          offset: 0,
          count: 10000,
        },
      })
      .catch((error) => {
        console.log("error " + error);
        console.log(error.request);
      })
      .then((response) => response && dispatch(setDots(response.data)));
    console.log(333);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return params;
}

export default useGetParams;
