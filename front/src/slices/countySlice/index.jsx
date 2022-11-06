import { createSlice } from "@reduxjs/toolkit";

export const countySlice = createSlice({
  name: "county",
  initialState: { county: "all" },
  reducers: {
    setCounty(state, action) {
      state.county = action.payload;
      
    },
  },
});

// Action creators are generated for each case reducer function
export const { setCounty } = countySlice.actions;

export default countySlice.reducer;
