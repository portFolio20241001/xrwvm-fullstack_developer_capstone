// Reactと必要なフックをインポート
import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';

// スタイルシートのインポート
import "./Dealers.css";
import "../assets/style.css";

// 画像ファイルのインポート
import positive_icon from "../assets/positive.png";
import neutral_icon from "../assets/neutral.png";
import negative_icon from "../assets/negative.png";
import review_icon from "../assets/reviewbutton.png";

// ヘッダーコンポーネントのインポート
import Header from '../Header/Header';

// Dealerコンポーネントの定義
const Dealer = () => {
  // ディーラー情報の状態管理
  const [dealer, setDealer] = useState({});
  // レビュー情報の状態管理
  const [reviews, setReviews] = useState([]);
  // レビューがない場合のフラグ
  const [unreviewed, setUnreviewed] = useState(false);
  // レビュー投稿ボタンの状態管理
  const [postReview, setPostReview] = useState(<></>);

  // 現在のURLを取得
  let curr_url = window.location.href;
  // ルートURLを抽出
  let root_url = curr_url.substring(0, curr_url.indexOf("dealer"));
  // URLパラメータを取得
  let params = useParams();
  // ディーラーのIDを取得
  let id = params.id;

  // APIエンドポイントの作成
  let dealer_url = root_url + `djangoapp/dealer/${id}`;
  let reviews_url = root_url + `djangoapp/reviews/dealer/${id}`;
  let post_review = root_url + `postreview/${id}`;

  // ディーラー情報を取得する非同期関数
  const get_dealer = async () => {

    console.log("確認ポイント1")

    console.log("【Dealer.jsx】dealer_url:",dealer_url)

    const res = await fetch(dealer_url, { method: "GET" });
    const retobj = await res.json();

    // ステータスコードが200（成功）の場合
    if (retobj.status === 200) {

      console.log("確認ポイント2")
      console.log("retobj:",retobj)

      let dealerobjs = Array.from(retobj.dealer); // 配列に変換

      console.log("dealerobjs:",dealerobjs)

      setDealer(dealerobjs[0]); // 最初のディーラー情報をセット
    }
  };

  // レビュー情報を取得する非同期関数
  const get_reviews = async () => {
    try {
      const res = await fetch(reviews_url, { method: "GET" });
  
      if (!res.ok) {
        throw new Error("Network response was not ok");
      }
  
      const retobj = await res.json();

      console.log("retobj.reviews:", retobj.reviews);  // ここで reviews の型と内容を確認
      console.log("typeof retobj.reviews:", typeof retobj.reviews);
      console.log("Array.isArray(retobj.reviews):", Array.isArray(retobj.reviews));

      console.log("retobj:", retobj);
      
      // reviews が配列でない場合でも扱えるように修正
      const reviewsData = Array.isArray(retobj.reviews) ? retobj.reviews : [];
  
      if (reviewsData.length > 0) {
        setReviews(reviewsData); // レビューがあれば状態を更新
      } else {
        setUnreviewed(true); // レビューがない場合の処理
      }
    } catch (error) {
      console.error("Error fetching reviews:", error);
    }
  };
  

  // 感情分析アイコンを取得する関数
  const senti_icon = (sentiment) => {
    let icon =
      sentiment === "positive"
        ? positive_icon
        : sentiment === "negative"
        ? negative_icon
        : neutral_icon;
    return icon;
  };

  // 初回レンダリング時にデータを取得
  useEffect(() => {
    get_dealer(); // ディーラー情報を取得
    get_reviews(); // レビュー情報を取得

    // ユーザーがログインしている場合、レビュー投稿ボタンを表示
    if (sessionStorage.getItem("username")) {
      setPostReview(
        <a href={post_review}>
          <img
            src={review_icon}
            style={{ width: "10%", marginLeft: "10px", marginTop: "10px" }}
            alt="Post Review"
          />
        </a>
      );
    }

    console.log("reviews:", reviews);
    console.log("reviews type:", typeof reviews);
    console.log("Array.isArray(reviews):", Array.isArray(reviews));

  }, []); // 依存関係に関数を指定

  // JSXのレンダリング
  return (
    <div style={{ margin: "20px" }}>
      {/* ヘッダーコンポーネントを表示 */}
      <Header />
      <div style={{ marginTop: "10px" }}>
        {/* ディーラー名とレビュー投稿ボタンを表示 */}
        <h1 style={{ color: "grey" }}>
          {dealer.full_name}
          {postReview}
        </h1>
        {/* ディーラーの住所情報を表示 */}
        <h4 style={{ color: "grey" }}>
          {dealer["city"]}, {dealer["address"]}, Zip - {dealer["zip"]},{" "}
          {dealer["state"]}
        </h4>
      </div>

      {/* レビューパネルの表示 */}
      <div className="reviews_panel">
        {/* レビューが読み込み中の場合 */}
        {reviews.length === 0 && unreviewed === false ? (
          <text>Loading Reviews....</text>
        ) : unreviewed === true ? (
          <div>No reviews yet! </div> // レビューがない場合の表示
        ) : (
          reviews.map((review) => (
            // 個々のレビューを表示
            <div className="review_panel">
              <img
                src={senti_icon(review.sentiment)}
                className="emotion_icon"
                alt="Sentiment"
              />
              <div className="review">{review.review}</div>
              <div className="reviewer">
                {review.name} {review.car_make} {review.car_model}{" "}
                {review.car_year}
              </div>
            </div>
          ))
        )}
      </div>
    </div>
  );
};

export default Dealer;
