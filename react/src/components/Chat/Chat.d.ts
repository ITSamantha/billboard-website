type ChatType = {
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

type ChatInfo = {
  id: number;
  user: ProfileInfo;
  created_at: string;
  messages: Message[];
};
