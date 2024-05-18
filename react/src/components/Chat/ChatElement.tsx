import React from 'react';
import { Avatar, Typography } from '@mui/material';
import { Link } from 'react-router-dom';

type ChatElementProps = {
  chat: ChatType;
};

const ChatElement = ({ chat }: ChatElementProps) => {
  return (
    <Link to={`/chat/${chat.id}`} key={chat.id} className="chat-link">
      <div className="chat-item">
        <Avatar alt="User Avatar" src="https://http.cat/200" className="avatar" />
        <div className="content">
          <Typography variant="subtitle1" className="user-info">
            {chat.user.first_name} {chat.user.last_name} {chat.user.email}
          </Typography>
          <Typography variant="body2" className="last-message">
            {chat.user.id === chat.messages[chat.messages.length - 1].chat_user.user_id
              ? ''
              : 'You: '}
            {chat.messages[chat.messages.length - 1].text}
          </Typography>
          <Typography variant="caption" className="message-time">
            {new Date(chat.messages[chat.messages.length - 1].created_at).toLocaleString()}
          </Typography>
        </div>
      </div>
    </Link>
  );
};

export default ChatElement;
