import { createSlice } from "@reduxjs/toolkit";

export const dotSlice = createSlice({
  name: "dot",
  initialState: { dot: [58.8648852835837, 37.32055664062501] },
  reducers: {
    setDot(state, action) {
      state.dot = action.payload;
    },
  },
});

// Action creators are generated for each case reducer function
export const { setDot } = dotSlice.actions;

export default dotSlice.reducer;
