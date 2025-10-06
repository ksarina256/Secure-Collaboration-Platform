import React, { useState } from "react";
import { api, setToken } from "./api";
import { encryptFor, generateKeypair } from "./crypto";

export default function App(){
  const [email, setEmail] = useState(""); 
  const [password, setPassword] = useState("");
  const [token, setTok] = useState<string>();

  async function register(){
    const r = await api.post("/users/register", {email, password});
    setTok(r.data.token); setToken(r.data.token);
  }
  async function login(){
    const r = await api.post("/users/login", {email, password});
    setTok(r.data.access_token); setToken(r.data.access_token);
  }

  async function demoEncrypt(){
    const kp = await generateKeypair();
    const ct = await encryptFor("hello secure world", kp.publicKey);
    alert("ciphertext sample:\n" + ct.substring(0, 60) + "...");
  }

  return (
    <div style={{padding:20, fontFamily:'system-ui'}}>
      <h2>Secure Collab (MVP)</h2>
      <div style={{display:'grid', gap:8, maxWidth:360}}>
        <input placeholder="email" value={email} onChange={e=>setEmail(e.target.value)} />
        <input placeholder="password" type="password" value={password} onChange={e=>setPassword(e.target.value)} />
        <div style={{display:'flex', gap:8}}>
          <button onClick={register}>Register</button>
          <button onClick={login}>Login</button>
          <button onClick={demoEncrypt}>Demo Encrypt</button>
        </div>
        <div>Token: {token ? token.slice(0,24) + "..." : "(none)"}</div>
      </div>
    </div>
  );
}
