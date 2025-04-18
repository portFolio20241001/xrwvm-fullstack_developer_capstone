import React, { useState } from "react";            // ReactとuseStateフックをインポート
import "./Register.css";                            // スタイルシートをインポート
import user_icon from "../assets/person.png"        // ユーザーアイコンの画像をインポート
import email_icon from "../assets/email.png"        // メールアイコンの画像をインポート
import password_icon from "../assets/password.png"  // パスワードアイコンの画像をインポート
import close_icon from "../assets/close.png"        // 閉じるアイコンの画像をインポート
import Header from '../Header/Header';              // ヘッダーコンポーネントをインポート

const Register = () => {
  // ユーザー名、パスワード、メールアドレス、名前を管理するためのステートを定義
  const [userName, setUserName] = useState(""); 
  const [password, setPassword] = useState(""); 
  const [email, setEmail] = useState(""); 
  const [firstName, setFirstName] = useState(""); 
  const [lastName, setlastName] = useState(""); 

  // ホームに戻るための関数
  const gohome = ()=> {
    window.location.href = window.location.origin; // 現在のオリジン（ホスト）にリダイレクト
  }

  // 登録処理を非同期で行う関数
  const register = async (e) => {
    e.preventDefault(); // フォームのデフォルト送信をキャンセル

    console.log("register処理")

    let register_url = window.location.origin + "/djangoapp/register"; // 登録用URLを設定
    
    // fetchを使用してサーバーにデータを送信
    const res = await fetch(register_url, {
        method: "POST", // POSTメソッドを使用
        headers: {
            "Content-Type": "application/json", // JSONデータを送信することを指定
        },
        body: JSON.stringify({ // 入力データをJSON形式で送信
            "userName": userName,
            "password": password,
            "firstName": firstName,
            "lastName": lastName,
            "email": email
        }),
    });

    const json = await res.json(); // レスポンスをJSON形式で取得

    console.log("res:",res)
    console.log("json:",json)

    if (json.status) { // 登録が成功した場合
        sessionStorage.setItem('username', json.userName); // ユーザー名をセッションストレージに保存
        window.location.href = window.location.origin; // ホームページにリダイレクト
    }
    else if (json.error === "Already Registered") { // すでに登録されているユーザー名の場合
      alert("The user with same username is already registered"); // 警告メッセージを表示
      window.location.href = window.location.origin; // ホームページにリダイレクト
    }

  };

  // JSXでレンダリングするUIを定義
  return(
    <div>

        <Header/>  {/* ヘッダーコンポーネントを表示 */}

        {/* 登録コンテナ */}
        <div className="register_container" style={{width: "50%"}}>

            {/* ヘッダー */}
            <div className="header" style={{display: "flex", flexDirection: "row", justifyContent: "space-between"}}>
            {/* サインアップテキスト */}
            <span className="text" style={{flexGrow:"1"}}>SignUp</span>
            {/* 閉じるアイコン（✖）の表示 */}
            <div style={{display: "flex", flexDirection: "row", justifySelf: "end", alignSelf: "start" }}>
                <a href="/" onClick={()=>{gohome()}} style={{justifyContent: "space-between", alignItems:"flex-end"}}>
                <img style={{width:"1cm"}} src={close_icon} alt="X"/>
                </a>
            </div>
            <hr/> {/* ヘッダー下の区切り線 */}
            </div>

            {/* フォーム */}
            <form onSubmit={register}>
                <div className="inputs"> {/* 入力フィールドコンテナ */}
                {/* ユーザー名入力 */}
                <div className="input">
                    <img src={user_icon} className="img_icon" alt='Username'/> {/* ユーザーアイコン */}
                    <input type="text"  name="username" placeholder="Username" className="input_field"
                    onChange={(e) => setUserName(e.target.value)}/> {/* ユーザー名入力フィールド */}
                </div>
                {/* 名入力 */}
                <div>
                    <img src={user_icon} className="img_icon" alt='First Name'/>
                    <input type="text"  name="first_name" placeholder="First Name" className="input_field"
                    onChange={(e) => setFirstName(e.target.value)}/>
                </div>
                {/* 姓入力 */}
                <div>
                    <img src={user_icon} className="img_icon" alt='Last Name'/>
                    <input type="text"  name="last_name" placeholder="Last Name" className="input_field"
                    onChange={(e) => setlastName(e.target.value)}/>
                </div>
                {/* メールアドレス入力 */}
                <div>
                    <img src={email_icon} className="img_icon" alt='Email'/>
                    <input type="email"  name="email" placeholder="email" className="input_field"
                    onChange={(e) => setEmail(e.target.value)}/>
                </div>
                {/* パスワード入力 */}
                <div className="input">
                    <img src={password_icon} className="img_icon" alt='password'/>
                    <input name="psw" type="password"  placeholder="Password" className="input_field"
                    onChange={(e) => setPassword(e.target.value)}/>
                </div>

                </div>
                {/* 登録送信ボタンパネル */}
                <div className="submit_panel">
                <input className="submit" type="submit" value="Register"/>
                </div>
            </form>
        </div>
    </div>
  )
}

export default Register; // Registerコンポーネントをエクスポート
