import React, { useState, useEffect } from 'react';     // Reactと必要なフック（useState, useEffect）をインポート
import "./Dealers.css";                                 // DealersコンポーネントのCSSスタイルをインポート
import "../assets/style.css";                           // 共通のスタイルシートをインポート
import Header from '../Header/Header';                  // ヘッダーコンポーネントをインポート
import review_icon from "../assets/reviewicon.png"      // レビューアイコン画像をインポート

// Dealersコンポーネントの定義
const Dealers = () => {
  const [dealersList, setDealersList] = useState([]);  // ディーラーリストを格納する状態変数
  // let [state, setState] = useState("")  // 状態（未使用）
  let [states, setStates] = useState([]);  // 州リストを格納する状態変数

  // let root_url = window.location.origin  // サーバーのルートURL（未使用）

  let dealer_url ="/djangoapp/get_dealers";              // ディーラー情報を取得するためのAPIのURL
  let dealer_url_by_state = "/djangoapp/get_dealers/";   // 特定の州のディーラー情報を取得するAPIのURL
 
  // 特定の州のディーラー情報を取得してフィルタリングする非同期関数
  const filterDealers = async (state) => {

    dealer_url_by_state = dealer_url_by_state + state;  // APIのURLに州名を追加

    console.log("dealer_url_by_state:",dealer_url_by_state)

    const res = await fetch(dealer_url_by_state, {  // APIにGETリクエストを送信
      method: "GET"
    });
    const retobj = await res.json();  // レスポンスをJSON形式で取得

    console.log("retobj:",retobj)

    if(retobj.status === 200) {  // レスポンスのステータスが200（成功）なら
      let state_dealers = Array.from(retobj.dealers);  // ディーラーリストを配列に変換
      setDealersList(state_dealers);  // フィルタリングされたディーラーリストを状態にセット

      console.log("ポイント2")
    }
  }

  // コンポーネントがマウントされたときにディーラー情報を取得する
  useEffect(() => {

    // すべてのディーラー情報を取得する非同期関数
    const get_dealers = async () => {

        console.log("ポイント1")

        const res = await fetch(dealer_url, {  // APIにGETリクエストを送信
            method: "GET"
        });

        console.log("res:",res)

        const retobj = await res.json();  // レスポンスをJSON形式で取得

        console.log("retobj:",retobj)
        
        // レスポンスのステータスが200（成功）なら
        if(retobj.status === 200) {  
            let all_dealers = Array.from(retobj.dealers);  // ディーラーリストを配列に変換
            let states = [];                               // 州リストを初期化

            all_dealers.forEach((dealer) => {  // 各ディーラーについて
                states.push(dealer.state);  // 各ディーラーの州をstates配列に追加
            });

            console.log("all_dealers:",all_dealers)
            console.log("states:",states)

            setStates(Array.from(new Set(states)));  // 重複を除いた州リストを状態にセット
            setDealersList(all_dealers);  // すべてのディーラーリストを状態にセット
        }
    };

    get_dealers();  // ディーラー情報を取得する関数を実行
  },[dealer_url]);  // 初回レンダリング後にのみ実行

  // ログインしているかどうかをチェック
  let isLoggedIn = sessionStorage.getItem("username") != null ? true : false;

return(
  <div>
      <Header/>  {/* ヘッダーコンポーネントを表示 */}

     <table className='table'>  {/* ディーラー情報を表示するためのテーブル */}
      <tr>  {/* テーブルのヘッダー行 */}
        <th>ID</th>  {/* ディーラーのID */}
        <th>Dealer Name</th>  {/* ディーラー名 */}
        <th>City</th>  {/* 市 */}
        <th>Address</th>  {/* 住所 */}
        <th>Zip</th>  {/* 郵便番号 */}
        <th>
          {/* 州を選択するためのドロップダウンメニュー */}
          <select name="state" id="state" onChange={(e) => filterDealers(e.target.value)}>
            <option value="" selected disabled hidden>State</option>  {/* 初期状態（州を選択してください） */}
            <option value="All">All States</option>  {/* すべての州を表示 */}
            {/* states配列に格納されている各州を選択肢として表示 */}
            {states.map(state => (
                <option value={state}>{state}</option>  
            ))}
          </select>
        </th>
        {/* ログインしている場合に「Review Dealer」列を表示 */}
        {/* レビュー投稿用のカラム */}
        {isLoggedIn ? (
          <th>Review Dealer</th>  
        ) : <></>}  {/* ログインしていない場合は表示しない */}
      </tr>
      {/* dealersList配列に格納された各ディーラー情報を表示 */}
      {dealersList.map(dealer => (
        <tr key={dealer.id}>  {/* 各ディーラーのデータ行 */}
          <td>{dealer['id']}</td>  {/* ディーラーのID */}
          <td><a href={'/dealer/'+dealer['id']}>{dealer['full_name']}</a></td>  {/* ディーラー名（リンク） */}
          <td>{dealer['city']}</td>  {/* 市 */}
          <td>{dealer['address']}</td>  {/* 住所 */}
          <td>{dealer['zip']}</td>  {/* 郵便番号 */}
          <td>{dealer['state']}</td>  {/* 州 */}
          {/* ログインしている場合にのみレビュー投稿リンクを表示 */}
          {isLoggedIn ? (
            <td>
              <a href={`/postreview/${dealer['id']}`}>
                <img src={review_icon} className="review_icon" alt="Post Review"/>
              </a>
            </td>
          ) : <></>}  {/* ログインしていない場合はレビューリンクを表示しない */}
        </tr>
      ))}
     </table>;
  </div>
)
}

export default Dealers
