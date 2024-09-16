import axios from 'axios';
import React,{useState} from 'react';
import './App.css';

function App() {
  const [message,setMessage]=useState('');
  const [image,setImage]=useState(null);
  const [chat,setChat]=useState([]);
  const sendMessage = async()=>{
    const formData=new FormData();
    formData.append('message',message);
    formData.append('image',image);
    try{
      const response = await axios.post('http://localhost:8000/send', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
        responseType: 'blob',
      });
    const imgUrl=URL.createObjectURL(response.data);
    setChat([...chat,{imgUrl}]);
    setMessage('');
    setImage(null);}
    catch(error){
      console.error("Error sending message",error);
    }
  };

  return (
    <div className="chat_container">
      <div id="chat-box">
        {chat.map((chatItem,index)=>(
          <div className="chat-message" key={index}>
            <img src={chatItem.imgUrl} alt="Encoded"/>
            </div>
        ))}
        </div>
        <input
        type="text"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Type a message"/>
        <input type="file" onChange={(e)=>setImage(e.target.files[0])} />
        <button onClick={sendMessage}>Send</button>
      </div>
      
  
  );
}

export default App;
