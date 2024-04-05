import { Button, TextField, ThemeProvider } from '@mui/material';
import { useEffect, useRef, useState } from 'react';
import { useSelector } from 'react-redux';
import { selectToken } from '../redux/slices/MyUserSlice';
import WebSocketInstance from './WebSocketInstance';
import { useParams } from 'react-router-dom';
import { getChat, sendMessage } from '../service/dataService';
import Loader from '../components/Loader';
import ChatHeader from '../components/Chat/ChatHeader';
import { THEME } from './profile/Profile';
import ChatMessage from '../components/Chat/ChatMessage';

type ChatInfo = {
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

  const messageBlockRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    messageBlockRef.current?.scrollIntoView({ block:"end" })
  }, [])


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
    <ThemeProvider theme={THEME}>
      <div>
        <div className="Chat__Header">
          <ChatHeader user={chatHistory.user} />
        </div>
        <div className="Chat__Messages" ref={messageBlockRef}>

          {messages.map((message) => (
            <ChatMessage message={message} received={message.chat_user && message.chat_user.user_id === chatHistory.user.id} />
          ))}
        </div>
        <div className="Chat__Send">
          <input
            placeholder="Enter a message"
            value={currentMessage}
            onChange={(e) => {
              setCurrentMessage(e.target.value);
            }}
          />
          <button onClick={sendCurrentMessage}>Send</button>
        </div>
      </div>
    </ThemeProvider>
  );
};

export default Chat;
