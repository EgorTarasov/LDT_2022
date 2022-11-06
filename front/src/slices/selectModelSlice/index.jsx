import { createSlice } from "@reduxjs/toolkit";

export const selectModelSlice = createSlice({
  name: "selectModel",
  initialState: { selectModel: 1 },
  reducers: {
    setSelectModel(state, action) {
      state.selectModel = action.payload;
    },
  },
});

// Action creators are generated for each case reducer function
export const { setSelectModel } = selectModelSlice.actions;

export default selectModelSlice.reducer;
