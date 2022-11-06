import { createSlice } from "@reduxjs/toolkit";

export const areaSlice = createSlice({
  name: "area",
  initialState: { area: "Филёвский Парк" },
  reducers: {
    setArea(state, action) {
      state.area = action.payload;
    },
  },
});

// Action creators are generated for each case reducer function
export const { setArea } = areaSlice.actions;

export default areaSlice.reducer;
