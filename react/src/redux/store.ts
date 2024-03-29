import { configureStore } from '@reduxjs/toolkit';
import myUserReducer from './slices/MyUserSlice';
import userReducer from './slices/UserSlice';

export const store = configureStore({
  reducer: {
    myUser: myUserReducer,
    user: userReducer
  }
});

// Infer the `RootState` and `AppDispatch` types from the store itself
export type RootState = ReturnType<typeof store.getState>;
// Inferred type: {posts: PostsState, comments: CommentsState, users: UsersState}
export type AppDispatch = typeof store.dispatch;
