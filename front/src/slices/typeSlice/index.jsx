import { createSlice } from "@reduxjs/toolkit";

export const typeSlice = createSlice({
  name: "type",
  initialState: { type: "all" },
  reducers: {
    setType(state, action) {
      state.type = action.payload;
    },
  },
});

// Action creators are generated for each case reducer function
export const { setType } = typeSlice.actions;

export default typeSlice.reducer;
