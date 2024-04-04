import { useEffect, useState } from 'react';
import { getAllChats } from '../service/dataService';
import Loader from '../components/Loader';
import { Avatar } from '@mui/material';
import { Link } from 'react-router-dom';

type Chat = {
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
    <div>
      {chatList.map((chat: Chat, index) => (
        <Link to={`/chat/${chat.id}`} key={chat.id}>
          <div>
            <Avatar alt="User Avatar" src="https://http.cat/200" />
            <div>
              {chat.user.first_name} {chat.user.last_name} {chat.user.email}
            </div>
            <div>
              {chat.user.id === chat.messages[chat.messages.length - 1].chat_user.user_id
                ? ''
                : 'You: '}
              {chat.messages[chat.messages.length - 1].text}
              <div>
                {' '}
                {new Date(chat.messages[chat.messages.length - 1].created_at).toLocaleString()}
              </div>
            </div>
          </div>
        </Link>
      ))}
    </div>
  );
};

export default MyChats;
