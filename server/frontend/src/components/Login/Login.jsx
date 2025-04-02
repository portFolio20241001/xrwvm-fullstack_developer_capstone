import React, { useState } from 'react';    // ReactとuseStateフックをインポート
import "./Login.css";                       // ログインページ用のCSSをインポート
import Header from '../Header/Header';      // ヘッダーコンポーネントをインポート

const Login = ({ onClose }) => {  // Loginコンポーネントを定義し、onCloseプロパティを受け取る

  const [userName, setUserName] = useState("");  // ユーザー名の状態を管理
  const [password, setPassword] = useState("");  // パスワードの状態を管理
  const [open, setOpen] = useState(true);        // モーダルの開閉状態を管理

  let login_url = window.location.origin + "/djangoapp/login";  // ログインAPIのエンドポイントを設定

  const login = async (e) => {  // ログイン処理を行う非同期関数
    e.preventDefault();  // フォームのデフォルトの送信動作を防止

    const res = await fetch(login_url, {  // APIへリクエストを送信
        method: "POST",  // HTTPメソッドをPOSTに設定
        headers: {
            "Content-Type": "application/json",  // リクエストのコンテンツタイプをJSONに設定
        },
        body: JSON.stringify({  // ユーザー情報をJSON形式で送信
            "userName": userName,
            "password": password
        }),
    });

    console.log("res:",res)
    
    const json = await res.json();  // レスポンスをJSON形式で取得

    console.log("json:",json)

    if (json.status != null && json.status === "Authenticated") {  // 認証成功の場合
        sessionStorage.setItem('username', json.userName);  // セッションストレージにユーザー名を保存
        setOpen(false);  // モーダルを閉じる
    }
    else {
      alert("The user could not be authenticated.")  // 認証失敗時にアラートを表示
    }
  };

  if (!open) {  // モーダルが閉じられた場合
    window.location.href = "/";  // ホームページへリダイレクト
  };
  
  return (
    <div>
      <Header/>  {/* ヘッダーコンポーネントを表示 */}
      <div onClick={onClose}>  {/* モーダル背景をクリックした際に閉じる */}
        {/* クリックイベントの伝播を防ぐ（モーダル内クリックで閉じないように） */}
        <div onClick={(e) => {e.stopPropagation()}} className='modalContainer'>
          {/* ログインフォーム */}
          <form className="login_panel" onSubmit={login}>  
              <div>
                {/* Username */}
                <span className="input_field">Username </span>
                <input type="text" name="username" placeholder="Username" className="input_field" onChange={(e) => setUserName(e.target.value)}/>
              </div>
              <div>
                {/* Password */}
                <span className="input_field">Password </span>
                <input name="psw" type="password" placeholder="Password" className="input_field" onChange={(e) => setPassword(e.target.value)}/>            
              </div>
              <div>
                {/* ログインボタン */}
                <input className="action_button" type="submit" value="Login"/>  
                {/* キャンセルボタン（モーダルを閉じる） */}
                <input className="action_button" type="button" value="Cancel" onClick={()=>setOpen(false)}/>
              </div>
              <a className="loginlink" href="/register">Register Now</a>  {/* 新規登録ページへのリンク */}
          </form>
        </div>
      </div>
    </div>
  );
};

export default Login;  // Loginコンポーネントをエクスポート
