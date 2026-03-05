document.getElementById('sendBtn').addEventListener('click', sendMessage);
document.getElementById('userInput').addEventListener('keydown', function(e){ if(e.key === 'Enter') sendMessage(); });

async function sendMessage(){
  const inputEl = document.getElementById('userInput');
  const input = inputEl.value.trim();
  if(!input) return;

  const chat = document.getElementById('chat-window');
  chat.innerHTML += "<div class='user'>" + escapeHtml(input) + "</div>";
  chat.scrollTop = chat.scrollHeight;

  try{
    const res = await fetch('http://localhost:8000/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: input })
    });

    const data = await res.json();
    chat.innerHTML += "<div class='ai'>" + escapeHtml(data.reply) + "</div>";
    chat.scrollTop = chat.scrollHeight;
  }catch(err){
    chat.innerHTML += "<div class='ai'>Błąd połączenia z serwerem.</div>";
  }

  inputEl.value = '';
}

function escapeHtml(text){
  return text.replace(/[&<>"']/g, function(ch){
    return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":"&#39;"}[ch];
  });
}
