import "../Styles/global.css";
import "../Styles/chat.css";

function ChatHeader({ name, status }) {
  return (
    <nav className="nav-container">
      <div className="first-component">
        <img src="profile.webp" alt="profile" width={50} height={50} />
        <div className="online-component">
          <div className="online-one">
            <h4 className="profile-name">{name}</h4>
            <span class="material-symbols-outlined">favorite</span>
          </div>
          <div className="online-two">
            <span class="material-symbols-outlined">
              radio_button_unchecked
            </span>
            <p>{status}</p>
          </div>
        </div>
      </div>
      <div className="second-component">
        <span class="material-symbols-outlined">phone</span>
        <span class="material-symbols-outlined">video_call</span>
        <span class="material-symbols-outlined">search</span>
        <span class="material-symbols-outlined">expand_more</span>
      </div>
    </nav>
  );
}

function ChatArea() {
  return (
    <>
      <div className="chat-container">
        <div className="encryption-container">
          <span class="material-symbols-outlined">lock</span>
          <p>
            Messages are end-to-end encrypted. Non one outside of this chat, not
            even WhatsApp can read or listen to them click to learn more
          </p>
        </div>
        <div className="chat-component">
          <div className="chatting-area">
            <p>message typed</p>
            <div className="meta-data">
              <h6>8:25 PM</h6>
              <span class="material-symbols-outlined">done</span>
            </div>
          </div>
          <div className="chatting-area-to">
            <p>message typed</p>
            <div className="meta-data">
              <h6>8:25 PM</h6>
              <span class="material-symbols-outlined">done</span>
            </div>
          </div>
          <ChatBubble
            type={"text"}
            message={"Hey girl, got your number from a friend"}
          />{" "}
          <ChatBubble type={"text"} message={"What is your name?"} />
          <ChatBubble
            type={"text"}
            message={"My name is Ama. How did you get my number? "}
            recieved
          />
          <ChatBubble type={"text"} message={"Kwabena gave it to me "} />
          <ChatBubble type={"text"} message={"Abeg, send me a pic of you"} />
          <ChatBubble type={"text"} message={"Kwabena gave it to me "} />
          <ChatBubble
            type={"image"}
            src={
              "https://c8.alamy.com/comp/PAE30X/kara-togo-mar-9-2013-unidentified-togolese-angry-toothless-woman-portrait-people-in-togo-suffer-of-poverty-due-to-the-unstable-econimic-situatio-PAE30X.jpg"
            }
            message={"This is me"}
            recieved
          />
          <ChatBubble
            type={"text"}
            message={"Bye, bye. I don't like again 😂😂"}
          />
        </div>
      </div>
      <div className="typing-container">
        <div className="image-field">
          <span class="material-symbols-outlined mood">mood</span>
          <span class="material-symbols-outlined">image</span>
        </div>
        <div className="type">
          <input placeholder="Say Something..." name="typing-input" />
          <span class="material-symbols-outlined">mic</span>
        </div>
      </div>
    </>
  );
}

function SideBarTop() {
  return (
    <>
      <div className="sidebar-nav">
        <div className="image-container">
          <img src="profile.webp" alt="to profile" width={40} height={40} />
          <span class="material-symbols-outlined">quick_phrases</span>
        </div>
        <span class="material-symbols-outlined">expand_more</span>
      </div>
      <div className="search-chat">
        <span class="material-symbols-outlined">search</span>
        <input placeholder="Search or start a new chat" name="search" />
      </div>

      <div className="select-page">
        <button className="first">Favourites</button>
        <button>Friends</button>
        <button>Groups</button>
      </div>

      <div className="person-area">
        {samplemessages.map((item, index) => {
          return <MessageCard {...item} />;
        })}
        <div className="chat-icon">
          <span class="material-symbols-outlined chat">chat_bubble</span>
        </div>
      </div>
    </>
  );
}

function SideBar() {
  return (
    <div className="sidebar-container">
      <SideBarTop />
    </div>
  );
}

function Chat() {
  return (
    <div className="App">
      <SideBar />
      <div className="chat-area">
        <ChatHeader name={"Dennis fofie"} status={"Online"} />
        <ChatArea />
      </div>
    </div>
  );
}

export default Chat;

const samplemessages = [
  {
    profile: "profile.webp",
    name: "Dennis",
    message: "This is a new message.",
    time: "Today",
    state: "new",
  },
  {
    profile: "profile.webp",
    name: "Yaw",
    message: "Have you bought food.",
    time: "Today",
    state: "new",
  },
  {
    profile: "profile.webp",
    name: "Yaa ",
    message: "I miss you, boo💘😍",
    time: "3: 43pm",
    state: "read",
  },
  {
    profile: "profile.webp",
    name: "Kwabena",
    message: "Boy, the bread finish!!",
    time: "3: 43pm",
    state: "read",
  },
];
const MessageCard = (props) => {
  const { profile, name, message, time, state } = props;
  return (
    <div className="chat-element-one">
      <img
        src={profile}
        alt="message"
        width={60}
        height={60}
        className="chat-image"
      />
      <div className="chat-display">
        <div className="name-message">
          <h5>{name}</h5>
          <p>{message}</p>
        </div>
        <div className="time-check">
          <h6>{time}</h6>
          {state === "new" ? (
            <p className="noti">1</p>
          ) : state === "read" ? (
            <span class="material-symbols-outlined">done</span>
          ) : null}
        </div>
      </div>
    </div>
  );
};

const ChatBubble = ({ message, type, src, time, state, recieved }) => {
  return (
    <div className={recieved ? "chatting-area" : "chatting-area-to"}>
      {type === "image" ? (
        <>
          <img src={src} height={200} width={200} alt="" />
        </>
      ) : type === "audio" ? (
        <audio controls src={src} style={{ width: "100%" }}></audio>
      ) : type === "text" ? (
        <p>{message}</p>
      ) : null}
      <div className="footer">
        {type === "image" && <p>{message}</p>}{" "}
        <div className="meta-data">
          <h6>8:25 PM</h6>
          <span class="material-symbols-outlined">done</span>
        </div>
      </div>
    </div>
  );
};
