### ✅ Agar `stateless_http=False` (Stateful)

Tum likhti ho:  
**“Hello, what’s your name?”**

Server is conversation ko **save kar lega** (yaad rakhega).

Jab tum next request bhejti ho:  
**“Tell me my name again.”**  
→ Server ko yaad hoga ke tumne apna naam pichle message me bataya tha.  
So wo reply karega: **“Your name is Laiba.”**

💾 *Matlab context saved hai.*

---

### ❌ Agar `stateless_http=True` (Stateless)

Tum likhti ho:  
**“Hello, my name is Laiba.”**

Server reply karega: **“Nice to meet you!”**

Ab tum likhti ho:  
**“Tell me my name again.”**

Server ko **yaad nahi hoga** ke tumne naam bataya tha,  
to wo confuse ho jayega 😅  
aur bolega: **“I don’t know your name.”**

🔄 *Matlab har request nayi hai — no memory, no connection between requests.*
