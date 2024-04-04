import { Avatar, Button, TextField } from '@mui/material';
import { useEffect, useState } from 'react';
import { useSelector } from 'react-redux';
import { selectToken } from '../redux/slices/MyUserSlice';
import WebSocketInstance from './WebSocketInstance';
import { useParams } from 'react-router-dom';
import { getChat, sendMessage } from '../service/dataService';
import Loader from '../components/Loader';

type ChatInfo = {
  id: number;
  user: ProfileInfo;
  created_at: string;
  messages: Message[];
};

type Message = {
  id: number;
  chat_id: number;
  text: string;
  created_at: string;
  seen_at: string | null;
  chat_user: ChatUser;
};

type ChatUser = {
  id: number;
  chat_id: number;
  user_id: number;
};

const Chat = () => {
  const { id } = useParams();
  const token = useSelector(selectToken);
  const [messages, setMessages] = useState<Message[]>([]);
  const [currentMessage, setCurrentMessage] = useState<string>('');
  const [chatHistory, setChatHistory] = useState<ChatInfo | undefined>();
  const [loading, setLoading] = useState<boolean>(false);

  useEffect(() => {
    async function fetchData() {
      setLoading(true);
      try {
        let chat = await getChat(Number(id));
        setChatHistory(chat);
        setMessages(chat.messages);
      } catch (error) {
        console.error('Error fetching data:', error);
      } finally {
        setLoading(false);
      }
    }
    fetchData();
  }, [id, token]);

  useEffect(() => {
    if (token) {
      const websocket = new WebSocketInstance('ws://localhost/ws/notifications');

      websocket.onopen = () => {
        console.log('WebSocket connected');
        websocket.send(token.access_token);
      };

      websocket.onmessage = (event) => {
        console.log(event.data);
        const message = JSON.parse(event.data);
        console.log(message);
        setMessages((prevMessages) => [...prevMessages, message]);
      };
    }
  }, [token]);

  const sendCurrentMessage = () => {
    if (currentMessage) {
      setMessages((prevMessages) => [...prevMessages, currentMessage] as any);
      sendMessage(Number(id), currentMessage);
      setCurrentMessage('');
    }
  };

  if (loading) {
    return (
      <div>
        <Loader />
      </div>
    );
  }

  if (!chatHistory) {
    return <div> No messages yet! </div>;
  }

  return (
    <div>
      <Avatar alt="User Avatar" src="https://http.cat/200" />
      <div>
        {chatHistory.user.first_name} {chatHistory.user.last_name} {chatHistory.user.email}
      </div>
      {messages.map((message) => {
        return message.chat_user && message.chat_user.user_id === chatHistory.user.id ? (
          <div key={message.id}>{message.text}</div>
        ) : (
          <div style={{ textAlign: 'center' }} key={message.id}>
            {message.text}
          </div>
        );
      })}
      <TextField
        rows={2}
        maxRows={6}
        value={currentMessage}
        onChange={(e) => {
          setCurrentMessage(e.target.value);
        }}
      />
      <Button onClick={sendCurrentMessage}>Send</Button>
    </div>
  );
};

export default Chat;
