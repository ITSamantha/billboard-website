import React from 'react';
import { Avatar, Typography } from '@mui/material';
import { Link } from 'react-router-dom';

type ChatElementProps = {
  chat: ChatType;
};

const ChatElement = ({ chat }: ChatElementProps) => {
  if (!chat) {
    return <></>;
  }

  const lastMessage = chat.messages[chat.messages.length - 1];

  return (
    <Link to={`/chat/${chat.id}`} key={chat.id} className="chat-link">
      <div className="chat-item">
        <Avatar alt="User Avatar" src="https://http.cat/200" className="avatar" />
        <div className="content">
          <Typography variant="subtitle1" className="user-info">
            {chat.user.first_name} {chat.user.last_name} {chat.user.email}
          </Typography>
          <Typography variant="body2" className="last-message">
            {lastMessage && lastMessage.chat_user && chat.user.id === lastMessage.chat_user.user_id
              ? ''
              : 'You: '}
            {lastMessage ? lastMessage.text : 'No messages'}
          </Typography>
          <Typography variant="caption" className="message-time">
            {lastMessage ? new Date(lastMessage.created_at).toLocaleString() : ''}
          </Typography>
        </div>
      </div>
    </Link>
  );
};

export default ChatElement;
