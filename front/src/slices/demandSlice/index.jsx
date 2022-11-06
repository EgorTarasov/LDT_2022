import { createSlice } from "@reduxjs/toolkit";

export const demandSlice = createSlice({
  name: "demand",
  initialState: { demand: [0, 100] },
  reducers: {
    setDemand(state, action) {
      state.demand = action.payload;
    },
  },
});

// Action creators are generated for each case reducer function
export const { setDemand } = demandSlice.actions;

export default demandSlice.reducer;
