import React, { useEffect, useState } from 'react';
import { getAllChats } from '../service/dataService';
import Loader from '../components/Loader';
import { Container, ThemeProvider, Typography } from '@mui/material';
import { THEME } from './profile/Profile';
import ChatElement from '../components/Chat/ChatElement';

export type Chat = {
  id: number;
  user: ProfileInfo;
  created_at: string;
  messages: Message[];
};

export type Message = {
  id: number;
  chat_id: number;
  text: string;
  created_at: string;
  seen_at: string | null;
  chat_user: ChatUser;
};

export type ChatUser = {
  id: number;
  chat_id: number;
  user_id: number;
};

const MyChats = () => {
  const [chatList, setChatList] = useState<Chat[]>([]);
  const [loading, setLoading] = useState<boolean>(false);

  useEffect(() => {
    const fetchData = async () => {
      setLoading(true);

      try {
        const chats = await getAllChats();
        setChatList(chats);
      } catch (error) {
        console.error('Error fetching data:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (loading) {
    return (
      <div>
        <Loader />
      </div>
    );
  }

  if (chatList.length === 0) {
    return <div> No chats yet! </div>;
  }

  return (
    <ThemeProvider theme={THEME}>
      <Container maxWidth="md">
        <div className="Chat__Left">
          <Typography variant="h4" fontWeight={500} style={{marginBottom: 15}}>My chats</Typography>
          <div className="Chat__Container">
            {chatList.length ? (
              chatList.map((chat) => (
                <ChatElement chat={chat} />
              ))
            ) : (
              <Typography>You have no chats</Typography>
            )}
          </div>
        </div>
      </Container>
    </ThemeProvider>
  );
};

export default MyChats;
