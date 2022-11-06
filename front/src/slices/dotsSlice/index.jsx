import { createSlice } from "@reduxjs/toolkit";

export const dotsSlice = createSlice({
  name: "dots",
  initialState: { dots: [] },
  reducers: {
    setDots(state, action) {
      state.dots = action.payload;
    },
  },
});

// Action creators are generated for each case reducer function
export const { setDots } = dotsSlice.actions;

export default dotsSlice.reducer;
