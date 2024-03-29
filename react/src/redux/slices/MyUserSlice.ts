import { PayloadAction, createAsyncThunk, createNextState, createSlice } from '@reduxjs/toolkit';
import { getMyUser, register, login as enter } from '../../service/dataService';

interface MyUserState {
  user: any;
  token: any;
  isLoading: boolean;
  hasError: boolean;
}

export const fetchLogin = createAsyncThunk(
  'myUser/fetchLogin',
  async (data: { email: string; password: string }) => {
    return await enter(data.email, data.password);
  }
);

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

const MyUserSlice = createSlice({
  name: 'myUser',
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
        state.token = action.payload;
        console.log(action.payload);
        console.log(state.token);
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
        console.log(action.payload);
        console.log(state.token);
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
        console.log(state.user);
        console.log(action.payload);
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
