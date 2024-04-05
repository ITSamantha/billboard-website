import React from 'react';
import { Avatar } from '@mui/material';

type User = {
  first_name: string,
  last_name: string,
  email: string,
  avatar?: string,
}

type ChatHeaderProps = {
  user: User
}

const ChatHeader = ({ user }: ChatHeaderProps) => {

  return (
    <div className="ChatHeader">
      <div className="ChatHeader__Avatar">
        <Avatar alt="User Avatar" src={user.avatar} />
      </div>
      <div className="ChatHeader__Information">
        <div className="ChatHeader__Name">
          {user.first_name} {user.last_name}
        </div>
        <div className="ChatHeader__Online">Last online 5 hours ago</div>
      </div>
    </div>
  );

};

export default ChatHeader;