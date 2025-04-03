import React, { useState, useEffect, useCallback } from 'react';    // Reactと、useState, useEffectをインポート
import { useParams } from 'react-router-dom';                       // URLパラメータを取得するためにuseParamsをインポート
import "./Dealers.css";                                             // CSSスタイルシートをインポート
import "../assets/style.css";                                       // 追加のスタイルシートをインポート
import Header from '../Header/Header';                              // ヘッダーコンポーネントをインポート


const PostReview = () => {
  // ステートを定義
  const [dealer, setDealer] = useState({});         // ディーラー情報
  const [review, setReview] = useState("");         // レビュー内容
  const [model, setModel] = useState();             // 車のモデル
  const [year, setYear] = useState("");             // 車の年式
  const [date, setDate] = useState("");             // 購入日
  const [carmodels, setCarmodels] = useState([]);   // 車のモデルリスト

  let curr_url = window.location.href;                                  // 現在のURLを取得
  let root_url = curr_url.substring(0, curr_url.indexOf("postreview")); // ベースURLを取得
  let params = useParams();                                             // URLのパラメータを取得
  let id = params.id;                                                   // ディーラーIDを取得
  let dealer_url = root_url + `djangoapp/dealer/${id}`;                 // ディーラー情報を取得するURL
  let review_url = root_url + `djangoapp/add_review`;                   // レビュー投稿用のURL
  let carmodels_url = root_url + `djangoapp/get_cars`;                  // 車モデル情報を取得するURL

  // レビューを投稿する関数
  const postreview = async () => {
    // セッションからユーザー名を取得
    let name = sessionStorage.getItem("firstname") + " " + sessionStorage.getItem("lastname");
    // 名前がnullの場合はユーザー名を使用
    if (name.includes("null")) {
      name = sessionStorage.getItem("username");
    }

    // 必須項目が未入力の場合、アラートを表示
    if (!model || review === "" || date === "" || year === "" || model === "") {
      alert("All details are mandatory");
      return;
    }

    // 車のモデルを分割してメーカー名とモデル名を取得
    let model_split = model.split(" ");
    let make_chosen = model_split[0];
    let model_chosen = model_split[1];

    // レビュー投稿用のJSONオブジェクトを作成
    let jsoninput = JSON.stringify({
      "name": name,
      "dealership": id,
      "review": review,
      "purchase": true,
      "purchase_date": date,
      "car_make": make_chosen,
      "car_model": model_chosen,
      "car_year": year,
    });

    console.log("jsoninput:",jsoninput); // デバッグ用にJSONオブジェクトを表示

    // レビュー投稿リクエストを送信
    const res = await fetch(review_url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: jsoninput,
    });

    console.log("res:",res); 

    // レスポンスをJSON形式で受け取る
    const json = await res.json();

    console.log("json.status:",json.status); 

    if (json.status === 200) {
      // 投稿が成功した場合、ディーラーのページにリダイレクト
      window.location.href = window.location.origin + "/dealer/" + id;
    }
  }

  // ディーラー情報を取得する非同期関数
  const get_dealer = useCallback(async () => {
    const res = await fetch(dealer_url, {
      method: "GET"
    });
    const retobj = await res.json();
    
    // ステータスが200（成功）の場合、ディーラー情報をステートにセット
    if (retobj.status === 200) {
      let dealerobjs = retobj.dealer;

      console.log("【get_dealer】res:", res);
      console.log("【get_dealer】retobj:", retobj);
      console.log("【get_dealer】dealerobjs:", dealerobjs);

      if (dealerobjs.length > 0)
        setDealer(dealerobjs[0]);
    }
  }, [dealer_url, setDealer]);  //dealer_url, setDealerの参照値が変わると再実行

  // 車のモデル情報を取得する非同期関数
  const get_cars = useCallback(async () => {
    const res = await fetch(carmodels_url, {
      method: "GET"
    });
    const retobj = await res.json();
    
    // 車のモデル情報をステートにセット
    let carmodelsarr = Array.from(retobj.CarModels);

    console.log("【get_cars】res:", res);
    console.log("【get_cars】retobj:", retobj);
    console.log("【get_cars】carmodelsarr:", carmodelsarr);

    setCarmodels(carmodelsarr);
  }, [carmodels_url, setCarmodels]);  //carmodels_url, setCarmodelsの参照値が変わると再実行

  // コンポーネントのマウント時にディーラー情報と車のモデル情報を取得
  useEffect(() => {
    get_dealer();
    get_cars();
  }, [get_dealer, get_cars]);

  return (
    <div>
      <Header /> {/* ヘッダーコンポーネントを表示 */}
      <div style={{ margin: "5%" }}>
        {/* ディーラー名を表示 */}
        <h1 style={{ color: "darkblue" }}>{dealer.full_name}</h1>
        {/* レビュー内容を入力 */}
        <textarea id='review' cols='50' rows='7' onChange={(e) => setReview(e.target.value)}></textarea>
        {/* 購入日を入力 */}
        <div className='input_field'>
          Purchase Date <input type="date" onChange={(e) => setDate(e.target.value)} />
        </div>
        {/* 車メーカー・車種を入力 */}
        <div className='input_field'>
          Car Make
          <select name="cars" id="cars" onChange={(e) => setModel(e.target.value)}>
            <option value="" selected disabled hidden>Choose Car Make and Model</option>
            {carmodels.map(carmodel => (
              // 車のモデルを選択肢として表示
              <option value={carmodel.CarMake + " " + carmodel.CarModel}>{carmodel.CarMake} {carmodel.CarModel}</option>
            ))}
          </select>
        </div>
        {/* 車の年代を入力 */}
        <div className='input_field'>
          Car Year <input type="int" onChange={(e) => setYear(e.target.value)} max={2023} min={2015} />
        </div>

        <div>
          <button className='postreview' onClick={postreview}>Post Review</button> {/* レビュー投稿ボタン */}
        </div>
      </div>
    </div>
  );
}

export default PostReview; // PostReviewコンポーネントをエクスポート
