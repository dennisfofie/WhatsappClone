import '../Styles/global.css';
import '../Styles/chat.css'

function ChatHeader({name, status}) {
  return (
    <nav className='nav-container'>
      <div className='first-component'>
        <img src='profile.webp' alt='profile' width={50} height={50} />
        <div className='online-component'>
          <div className='online-one'>
            <h4 className='profile-name'>{name}</h4>
            <span class="material-symbols-outlined">favorite</span> 
          </div>
          <div className='online-two'>
            <span class="material-symbols-outlined">radio_button_unchecked</span>
            <p>{status}</p>
          </div>
        </div>
      </div>
      <div className='second-component'>
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
    <div className='chat-container'>
      <div className='encryption-container'>
        <span class="material-symbols-outlined">lock</span>
        <p>Messages are end-to-end encrypted. Non one outside of this chat, not even WhatsApp can read or listen to them click to learn more</p> 
      </div>
      <div className='chat-component'>
        <div className='chatting-area'>
            <p>message typed</p>
            <div className='meta-data'>
              <h6>8:25 PM</h6>
              <span class="material-symbols-outlined">done</span>
            </div>
        </div>
        <div className='chatting-area-to'>
            <p>message typed</p>
            <div className='meta-data'>
              <h6>8:25 PM</h6>
              <span class="material-symbols-outlined">done</span>
            </div>
        </div>
      </div>
    </div>
    <div className='typing-container'>
      <div className='image-field'>
        <span class="material-symbols-outlined mood">mood</span>
        <span class="material-symbols-outlined">image</span>
      </div>
      <div className='type'>
        <input placeholder='Say Something...' name='typing-input' />
        <span class="material-symbols-outlined">mic</span>
      </div>
    </div>
  </>
  );
}

function SideBarTop() {
  return (
    <>
    <div className='sidebar-nav'>
      <div className='image-container'>
        <img src='profile.webp' alt='to profile' width={40} height={40} />
        <span class="material-symbols-outlined">quick_phrases</span>
      </div>
        <span class="material-symbols-outlined">expand_more</span>    
    </div>
    <div className='search-chat'>
      <span class="material-symbols-outlined">search</span>
      <input placeholder='Search or start a new chat' name='search' />
    </div>

    <div className='select-page'>
      <button className='first'>Favourites</button>
      <button>Friends</button>
      <button>Groups</button>
    </div>

    <div className='person-area'>
      <div className='chat-element-one'>
          <img src='profile.webp' alt='message' width={40} height={40} />
          <div className='chat-display'>
            <div className='name-message'>
              <h5>Dennis</h5>
              <p>Hello this is dennis</p>
            </div>
            <div className='time-check'>
              <h6>05:14pm</h6>
              <span class="material-symbols-outlined">done</span>
            </div>
          </div>
      </div>
      <div className='chat-element'>
          <img src='profile.webp' alt='message' width={40} height={40} />
          <div className='chat-display'>
            <div className='name-message'>
              <h5>Dennis</h5>
              <p>Hello this is dennis</p>
            </div>
            <div className='time-check'>
              <h6>05:14pm</h6>
              <p className='noti'>1</p>
            </div>
          </div>
      </div>
      <span class="material-symbols-outlined chat">chat_bubble</span>
    </div>
    </>
  );
}

function SideBar() {
  return (
    <div className='sidebar-container'>
      <SideBarTop />
    </div>
  );
}

function Chat() {
  return (
    <div className="App">
      <SideBar />
      <div className='chat-area'>
        <ChatHeader  name={"Dennis fofie"} status={"Online"}/>
        <ChatArea />
      </div>
    </div>
  );
}

export default Chat;
