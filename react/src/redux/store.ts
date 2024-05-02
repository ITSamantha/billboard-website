import { combineReducers, configureStore } from '@reduxjs/toolkit';
import myUserReducer from './slices/MyUserSlice';
import userReducer from './slices/UserSlice';
import storage from 'redux-persist/lib/storage';
import { persistReducer } from 'redux-persist';

// Configure Redux Persist
const persistConfig = {
  key: 'root',
  storage
};

// Combine reducers
const rootReducer = combineReducers({
  myUser: myUserReducer,
  user: userReducer
});

const persistedReducer = persistReducer(persistConfig, rootReducer);

export const store = configureStore({
  reducer: persistedReducer,
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware({
      serializableCheck: false // to avoid serializable check on redux-persist
    })
});

// Infer the `RootState` and `AppDispatch` types from the store itself
export type RootState = ReturnType<typeof store.getState>;
// Inferred type: {posts: PostsState, comments: CommentsState, users: UsersState}
export type AppDispatch = typeof store.dispatch;
