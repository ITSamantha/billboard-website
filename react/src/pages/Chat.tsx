import { ThemeProvider, Typography } from '@mui/material';
import React, { useEffect, useRef, useState } from 'react';
import { useSelector } from 'react-redux';
import { selectToken } from '../redux/slices/MyUserSlice';
import WebSocketInstance from './WebSocketInstance';
import {useParams} from 'react-router-dom';
import { BASE_WS_URL, getAllChats, getChat, sendMessage } from '../service/dataService';
import Loader from '../components/Loader';
import ChatHeader from '../components/Chat/ChatHeader';
import { THEME } from './profile/Profile';
import ChatMessage from '../components/Chat/ChatMessage';
import ChatElement from '../components/Chat/ChatElement';

export type ChatType = {
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

type ChatInfo = {
  id: number;
  user: ProfileInfo;
  created_at: string;
  messages: Message[];
};

const Chat = () => {
  const [chatList, setChatList] = useState<ChatType[]>([]);
  const [loading, setLoading] = useState<boolean>(false);
  const { id } = useParams();
  const token = useSelector(selectToken);
  const [messages, setMessages] = useState<Message[]>([]);
  const [currentMessage, setCurrentMessage] = useState<string>('');
  const [chatHistory, setChatHistory] = useState<ChatInfo | undefined>();

  useEffect(() => {
    const fetchData = async () => {
      setLoading(true);


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
            const websocket = new WebSocketInstance(BASE_WS_URL + 'ws/notifications');

            websocket.onopen = () => {
                console.log('WebSocket connected');
                websocket.send(token);
            };

            websocket.onmessage = (event) => {
                console.log("Message received", event.data)
                try {
                    let newMessage = JSON.parse(event.data)
                    if (!messages.filter(msg => msg.id === newMessage.data.id).length) {
                        setMessages([...messages, newMessage.data])
                    }
                } catch (e) {
                    console.error("JSON PARSE ERROR!")
                }
            };
        }
    }, [token]);

    const sendCurrentMessage = () => {
        if (currentMessage) {
            setMessages((prevMessages) => [...prevMessages, {text: currentMessage}] as any);
            sendMessage(Number(id), currentMessage);
            setCurrentMessage('');
        }
    };

    fetchData();
  }, []);

    useEffect(() => {
        let chatMessageDiv = document.querySelector('.Chat__Messages')
        if (chatMessageDiv) {
            chatMessageDiv.scrollTop = chatMessageDiv.scrollHeight;
        }
    }, [messages])


    if (loading) {
        return (
            <div>
                <Loader/>
            </div>
        );
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

  const messageBlockRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    messageBlockRef.current?.scrollIntoView({ block: 'end' });
  }, []);

  if (loading) {
    return (
      <div>
        <Loader />
      </div>
    );
  }

  return (
    <ThemeProvider theme={THEME}>
      <div className="Chat__Wrapper">
        <div className="Chat__Left">
          <Typography variant="h4" fontWeight={500} style={{ marginBottom: 15 }}>
            My chats
          </Typography>
          <div className="Chat__Container">
            {chatList.length ? (
              chatList.map((chat) => <ChatElement chat={chat} />)
            ) : (
              <Typography>You have no chats</Typography>
            )}
          </div>
        </div>
        <div className="Chat__Right">
          {chatHistory ? (
            <>
              <div className="Chat__Header">
                <ChatHeader user={chatHistory.user} />
              </div>
              <div className="Chat__Messages" ref={messageBlockRef}>
                {messages.map((message) => (
                  <ChatMessage
                    message={message}
                    received={
                      message.chat_user && message.chat_user.user_id === chatHistory.user.id
                    }
                  />
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
            </>
          ) : (
            'No messages yet'
          )}
        </div>
      </div>
    </ThemeProvider>
  );
};

export default Chat;
