import { PayloadAction, createAsyncThunk, createSlice } from '@reduxjs/toolkit';
import { getMyUser, register, login as enter } from '../../service/dataService';
import axios from 'axios';
import { useSelector } from 'react-redux';

interface MyUserState {
  user: any;
  token: any;
  isLoading: boolean;
  hasError: boolean;
}

export const fetchLogin = createAsyncThunk('myUser/fetchLogin', async (data: any) => {
  const res = await enter(data.email, data.password);
  return res;
});

export const fetchRegister = createAsyncThunk('myUser/fetchRegister', async (data: any) => {
  const res = await register(data.email, data.password, data.phone, data.lastName, data.firstName);
  return res;
});

export const fetchMyUser = createAsyncThunk('myUser/fetchMyUser', async () => {
  const res = await getMyUser();
  return res;
});

const initialState: MyUserState = {
  user: null,
  token: null,
  isLoading: false,
  hasError: false
};

// TODO: fix token
const MyUserSlice = createSlice({
  name: 'myUser',
  initialState,
  reducers: {
    logout: (state) => {
      state.user = null;
      state.token = null;
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
        state.token = action.payload;
        axios.interceptors.request.use(function (config) {
          config.headers.jwt_access_token =  state.token;
          return config;
      });
      
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
        state.token = action.payload;
        state.isLoading = false;
        state.hasError = false;
      })
      .addCase(fetchRegister.rejected, (state, action) => {
        state.hasError = true;
        state.isLoading = false;
      })
      .addCase(fetchMyUser.pending, (state, action) => {
        state.isLoading = true;
        state.hasError = false;
      })
      .addCase(fetchMyUser.fulfilled, (state, action: PayloadAction<any>) => {
        state.user = action.payload;
        state.isLoading = false;
        state.hasError = false;
      })
      .addCase(fetchMyUser.rejected, (state, action) => {
        state.hasError = true;
        state.isLoading = false;
      });
  }
});

export const selectMyUser = (state: any) => state.myUser.user;
export const selectLoading = (state: any) => state.myUser.isLoading;
export const selectError = (state: any) => state.myUser.hasError;
export const selectToken = (state: any) => state.myUser.token;
export const { logout } = MyUserSlice.actions;

export default MyUserSlice.reducer;
