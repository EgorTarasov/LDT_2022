import { configureStore } from "@reduxjs/toolkit";
import {
  areaCoordsReducer,
  areaReducer,
  countyReducer,
  dateReducer,
  demandReducer,
  dotReducer,
  dotsReducer,
  rangeReducer,
  selectModelReducer,
  typeReducer,
} from "../slices";
export const store = configureStore({
  reducer: {
    county: countyReducer,
    area: areaReducer,
    type: typeReducer,
    range: rangeReducer,
    demand: demandReducer,
    dot: dotReducer,
    date: dateReducer,
    selectModel: selectModelReducer,
    dots: dotsReducer,
    areaCoords: areaCoordsReducer,
  },
});
