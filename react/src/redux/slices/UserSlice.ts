import { PayloadAction, createAsyncThunk, createSlice } from '@reduxjs/toolkit';
import { login as enter, register } from '../../service/dataService';

interface UserState {
  user: object;
  isLoading: boolean;
  hasError: boolean;
}

export const fetchLogin = createAsyncThunk('user/fetchLogin', async (data: any) => {
  return await enter(data.email, data.password);
});

export const fetchRegister = createAsyncThunk('user/fetchRegister', async (data: any) => {
  const res = await register(data.email, data.password, data.phone, data.lastName, data.firstName);
  return res;
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
      .addCase(fetchLogin.pending, (state, action) => {
        state.isLoading = true;
        state.hasError = false;
      })
      .addCase(fetchLogin.fulfilled, (state, action: PayloadAction<any>) => {
        state.user = action.payload;
        console.log(action.payload);
        state.isLoading = false;
        state.hasError = false;
      })
      .addCase(fetchLogin.rejected, (state, action) => {
        state.hasError = true;
        state.isLoading = false;
      })
      .addCase(fetchRegister.pending, (state, action) => {
        state.isLoading = true;
        state.hasError = false;
      })
      .addCase(fetchRegister.fulfilled, (state, action: PayloadAction<any>) => {
        state.user = action.payload;
        state.isLoading = false;
        state.hasError = false;
      })
      .addCase(fetchRegister.rejected, (state, action) => {
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
