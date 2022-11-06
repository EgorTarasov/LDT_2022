import { createSlice } from "@reduxjs/toolkit";

export const areaCoordsSlice = createSlice({
  name: "areaCoords",
  initialState: { areaCoords: [] },
  reducers: {
    setAreaCoords(state, action) {
      state.areaCoords = action.payload;
    },
  },
});

// Action creators are generated for each case reducer function
export const { setAreaCoords } = areaCoordsSlice.actions;

export default areaCoordsSlice.reducer;
