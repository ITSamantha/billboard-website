import {createAsyncThunk, createSlice, PayloadAction} from '@reduxjs/toolkit';
import {createApi, getMyUser, login as enter, register} from '../../service/dataService';
import axios from 'axios';

interface MyUserState {
  user: any;
  token: any;
  isLoading: boolean;
  hasError: boolean;
}

export const fetchLogin = createAsyncThunk('myUser/fetchLogin', async (data: any) => {
  return await enter(data.email, data.password);
});

export const fetchRegister = createAsyncThunk('myUser/fetchRegister', async (data: any) => {
  return await register(data.email, data.password, data.phone, data.lastName, data.firstName);
});

export const fetchMyUser = createAsyncThunk('myUser/fetchMyUser', async () => {
  return await getMyUser();
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
      createApi().post('auth/logout').then(() => {
        localStorage.removeItem("user")
        window.location.reload()
      })
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

export const selectMyUser = (state: any) => {
  if (state.myUser.user) return state.myUser.user
  let userJson = localStorage.getItem('user')
  if (userJson) {
    return JSON.parse(userJson)
  // } else {
  //   createApi().get('users/me').then(response => {
  //     localStorage.setItem("user", JSON.stringify(response.data))
  //
  //   })
  }
};

export const selectLoading = (state: any) => state.myUser.isLoading;
export const selectError = (state: any) => state.myUser.hasError;
export const selectToken = (state: any) => state.myUser.token;
export const { logout } = MyUserSlice.actions;

export default MyUserSlice.reducer;
