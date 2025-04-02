import React from 'react'; // Reactライブラリをインポート
import "../assets/style.css"; // スタイルシートをインポート
import "../assets/bootstrap.min.css"; // Bootstrapのスタイルシートをインポート

const Header = () => { // Headerコンポーネントの定義
    const logout = async (e) => { // ログアウト処理を行う非同期関数
        e.preventDefault(); // デフォルトのフォーム送信を防止
        let logout_url = window.location.origin + "/djangoapp/logout"; // ログアウトAPIのURLを設定
        const res = await fetch(logout_url, { // ログアウトAPIを呼び出す
            method: "GET", // GETメソッドでリクエストを送信
        });
    
        const json = await res.json(); // レスポンスをJSON形式で取得
        if (json) { // レスポンスがある場合
            let username = sessionStorage.getItem('username'); // セッションストレージからユーザー名を取得
            sessionStorage.removeItem('username'); // セッションストレージからユーザー名を削除
            window.location.href = window.location.origin; // ホームページへリダイレクト
            window.location.reload(); // ページをリロード
            alert("Logging out " + username + "..."); // ログアウトメッセージを表示
        } else { // ログアウトに失敗した場合
            alert("The user could not be logged out."); // エラーメッセージを表示
        }
    };
    
    let home_page_items = <div></div>; // デフォルトのホームページアイテム（空）

    let curr_user = sessionStorage.getItem('username'); // 現在のユーザー名を取得

    if (curr_user !== null && curr_user !== "") { // ユーザーがログインしている場合
        home_page_items = ( // ユーザー名とログアウトリンクを表示
            <div className="input_panel">
                <text className='username'>{sessionStorage.getItem("username")}</text> {/* ユーザー名を表示 */}
                <a className="nav_item" href="/djangoapp/logout" onClick={logout}>Logout</a> {/* ログアウトリンク */}
            </div>
        );
    }

    return ( // コンポーネントのレンダリング
        <div>
            {/* ナビゲーションバーのスタイルを設定 */}
            <nav className="navbar navbar-expand-lg navbar-light" style={{backgroundColor: "darkturquoise", height: "1in"}}>
                <div className="container-fluid"> {/* フル幅のコンテナ */}
                    <h2 style={{paddingRight: "5%"}}>Dealerships</h2> {/* サイトのタイトル */}
                    {/* ハンバーガーメニュー */}
                    <button className="navbar-toggler" type="button" data-bs-toggle="collapse"
                     data-bs-target="#navbarText" aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
                        <span className="navbar-toggler-icon"></span> {/* ハンバーガーメニューのアイコン */}
                    </button>
                    <div className="collapse navbar-collapse" id="navbarText"> {/* ナビゲーションメニューの折りたたみ機能 */}
                        <ul className="navbar-nav me-auto mb-2 mb-lg-0"> {/* ナビゲーションメニューのリスト */}
                            <li className="nav-item"> {/* ホームリンク */}
                                <a className="nav-link active" style={{fontSize: "larger"}} aria-current="page" href="/">Home</a>
                            </li>
                            <li className="nav-item"> {/* About Usリンク */}
                                <a className="nav-link" style={{fontSize: "larger"}} href="/about">About Us</a>
                            </li>
                            <li className="nav-item"> {/* Contact Usリンク */}
                                <a className="nav-link" style={{fontSize: "larger"}} href="/contact">Contact Us</a>
                            </li>
                        </ul>
                        <span className="navbar-text"> {/* ナビゲーションバーの右側に配置される要素 */}
                            <div className="loginlink" id="loginlogout"> {/* ログインまたはログアウトのリンク */}
                                {home_page_items} {/* 現在のユーザーの状態に応じたコンテンツを表示 */}
                            </div>
                        </span>
                    </div>
                </div>
            </nav>
        </div>
    );
};

export default Header; // Headerコンポーネントをエクスポート