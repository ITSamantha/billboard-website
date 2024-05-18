import { ThemeProvider, Typography } from '@mui/material';
import React, { useEffect, useRef, useState } from 'react';
import { useSelector } from 'react-redux';
import { selectToken } from '../redux/slices/MyUserSlice';
import WebSocketInstance from './WebSocketInstance';
import { useParams } from 'react-router-dom';
import { BASE_WS_URL, getAllChats, getChat, sendMessage } from '../service/dataService';
import Loader from '../components/Loader';
import ChatHeader from '../components/Chat/ChatHeader';
import { THEME } from './profile/Profile';
import ChatMessage from '../components/Chat/ChatMessage';
import ChatElement from '../components/Chat/ChatElement';

const Chat = () => {
  const [chatList, setChatList] = useState<ChatType[]>([]);
  const [loading, setLoading] = useState<boolean>(false);
  const { id } = useParams();
  const token = useSelector(selectToken);
  const [messages, setMessages] = useState<Message[]>([]);
  const [currentMessage, setCurrentMessage] = useState<string>('');
  const [chatHistory, setChatHistory] = useState<ChatInfo | undefined>();

  const websocket = useRef(new WebSocketInstance(BASE_WS_URL + 'ws/notifications'));

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

  const ref = useRef<number>(0);

  useEffect(() => {
    if (token) {
      websocket.current.onopen = () => {
        console.log('WebSocket connected');
        websocket.current.send(token);
      };
      websocket.current.onmessage = (event) => {
        try {
          let newMessage = JSON.parse(event.data);
          if (
            !messages.some((msg) => msg.id === newMessage.data.id) &&
            newMessage.data.chat_id === parseInt(id ? id : '-1')
          ) {
            setMessages((oldMessages) => [...oldMessages, newMessage.data]);
          }
        } catch (e) {
          console.error('Json parse error', e);
        }
      };
    }
  }, [token]);

  const sendCurrentMessage = () => {
    if (currentMessage) {
      setMessages((prevMessages) => [...prevMessages, { text: currentMessage }] as any);
      sendMessage(Number(id), currentMessage);
      setCurrentMessage('');
    }
  };

  const messageBlockRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    let chatMessageDiv = document.querySelector('.Chat__Messages');
    if (chatMessageDiv) {
      chatMessageDiv.scrollTop = chatMessageDiv.scrollHeight;
    }
  }, [messages]);

  if (loading) {
    return (
      <div>
        <Loader />
      </div>
    );
  }

  return (
    <ThemeProvider theme={THEME}>
      <div className="Chat">
        <div className="Chat__Wrapper">
          <div className="Chat__Left">
            <div className="Chat__Container">
              {chatList?.length ? (
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
                    onKeyDown={(e) => e.key === 'Enter' && sendCurrentMessage()}
                  />
                  <button onClick={sendCurrentMessage}>Send</button>
                </div>
              </>
            ) : (
              <div className="Chat__NotSelected">Select the person you want to chat with</div>
            )}
          </div>
        </div>
      </div>
    </ThemeProvider>
  );
};

export default Chat;
