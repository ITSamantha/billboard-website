import { PayloadAction, createAsyncThunk, createSlice } from '@reduxjs/toolkit';
import { getUserById } from '../../service/dataService';

interface UserState {
  user: object;
  isLoading: boolean;
  hasError: boolean;
}

export const fetchUser = createAsyncThunk('users/fetchUser', async (data: any) => {
  return await getUserById(data.id);
});

const initialState: UserState = {
  user: {},
  isLoading: false,
  hasError: false
};

const UserSlice = createSlice({
  name: 'user',
  initialState,
  reducers: {
    logout: (state) => {
      state.user = {};
      state.isLoading = false;
      state.hasError = false;
    }
  },
  extraReducers: (builder) => {
    builder
      .addCase(fetchUser.pending, (state, action) => {
        state.isLoading = true;
        state.hasError = false;
      })
      .addCase(fetchUser.fulfilled, (state, action: PayloadAction<any>) => {
        state.user = action.payload;
        state.isLoading = false;
        state.hasError = false;
      })
      .addCase(fetchUser.rejected, (state, action) => {
        state.hasError = true;
        state.isLoading = false;
      });
  }
});

export const selectUser = (state: { user: { user: any } }) => state.user.user;
export const selectLoading = (state: { user: { isLoading: any } }) => state.user.isLoading;
export const selectError = (state: { user: { hasError: any } }) => state.user.hasError;
export const { logout } = UserSlice.actions;

export default UserSlice.reducer;
