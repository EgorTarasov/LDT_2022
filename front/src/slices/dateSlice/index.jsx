import { createSlice } from "@reduxjs/toolkit";

export const dateSlice = createSlice({
  name: "date",
  initialState: { date: "all" },
  reducers: {
    setDate(state, action) {
      state.date = action.payload;
    },
  },
});

// Action creators are generated for each case reducer function
export const { setDate } = dateSlice.actions;

export default dateSlice.reducer;
