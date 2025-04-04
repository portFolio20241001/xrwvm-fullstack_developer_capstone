// 必要なモジュールをインポート
const express = require('express');  // Expressフレームワークをインポート
const mongoose = require('mongoose');  // Mongooseをインポート（MongoDBとの接続を管理）
const fs = require('fs');  // ファイルシステムを操作するモジュール
const cors = require('cors');  // CORS設定を行うためのモジュール
const app = express();  // Expressアプリケーションを作成
const port = 3030;  // サーバーがリスンするポート番号

// CORSを有効化（他のオリジンからのリクエストを許可）
app.use(cors());

// リクエストのbodyをURLエンコード形式で処理できるようにする
app.use(require('body-parser').urlencoded({ extended: false }));

// reviews.jsonとdealerships.jsonの内容を読み込む
const reviews_data = JSON.parse(fs.readFileSync("./data/reviews.json", 'utf8'));  // レビューのデータを読み込み
const dealerships_data = JSON.parse(fs.readFileSync("./data/dealerships.json", 'utf8'));  // ディーラーのデータを読み込み

// MongoDBに接続（MongoDBのホスト名は'mongo_db'、データベース名は'dealershipsDB'）
mongoose.connect("mongodb://mongo_db:27017/", {'dbName':'dealershipsDB'});

// モデルのインポート（レビューとディーラーのモデル）
const Reviews = require('./review');  // レビューのモデルをインポート
const Dealerships = require('./dealership');  // ディーラーのモデルをインポート

// 既存のデータを削除して、新しいデータを挿入
try {
  // レビューのデータを全削除し、再度データを挿入
  Reviews.deleteMany({}).then(() => {
    Reviews.insertMany(reviews_data.reviews);
  });
  
  // ディーラーのデータを全削除し、再度データを挿入
  Dealerships.deleteMany({}).then(() => {
    Dealerships.insertMany(dealerships_data.dealerships);
  });
} catch (error) {
  // エラーが発生した場合、エラーレスポンスを返す
  res.status(500).json({ error: 'Error fetching documents' });
}

// Expressルート：ホームページにアクセスすると「Welcome to the Mongoose API」と表示
app.get('/', async (req, res) => {
  res.send("Welcome to the Mongoose API");  // ホームページにメッセージを送信
});

// Expressルート：全てのレビューを取得するAPI
app.get('/fetchReviews', async (req, res) => {
  try {
    const documents = await Reviews.find();  // すべてのレビューを取得
    res.json(documents);  // 取得したレビューをJSON形式で返す
  } catch (error) {
    res.status(500).json({ error: 'Error fetching documents' });  // エラーハンドリング：500エラー
  }
});

// Expressルート：特定のディーラーに関連するレビューを取得するAPI
app.get('/fetchReviews/dealer/:id', async (req, res) => {
  try {
    // 指定されたディーラーIDに関連するレビューを取得
    const documents = await Reviews.find({ dealership: req.params.id });
    res.json(documents);  // 取得したレビューをJSON形式で返す
  } catch (error) {
    res.status(500).json({ error: 'Error fetching documents' });  // エラーハンドリング：500エラー
  }
});

// Expressルート：全てのディーラーを取得するAPI
app.get('/fetchDealers', async (req, res) => {
  try {
    const documents = await Dealerships.find();  // すべてのディーラーを取得
    res.json(documents);  // 取得したディーラーをJSON形式で返す
  } catch (error) {
    res.status(500).json({ error: 'Error fetching dealerships' });  // エラーハンドリング：500エラー
  }
});

// Expressルート：特定の州に関連するディーラーを取得するAPI
app.get('/fetchDealers/:state', async (req, res) => {
  try {
    // 指定された州に関連するディーラーを取得
    const documents = await Dealerships.find({ state: req.params.state });
    res.json(documents);  // 取得したディーラーをJSON形式で返す
  } catch (error) {
    res.status(500).json({ error: 'Error fetching dealerships by state' });  // エラーハンドリング：500エラー
  }
});

// Expressルート：特定のディーラーIDでディーラー情報を取得するAPI
app.get('/fetchDealer/:id', async (req, res) => {
  try {
    // 指定されたIDでディーラー情報を取得
    const dealership = await Dealerships.findOne({ id: req.params.id }); //findOneにすると辞書データが返される。findはArray
    if (dealership) {
      res.json(dealership);  // 取得したディーラー情報をJSON形式で返す
    } else {
      res.status(404).json({ error: 'Dealer not found' });  // ディーラーが見つからない場合は404エラー
    }
  } catch (error) {
    res.status(500).json({ error: 'Error fetching dealership by ID' });  // エラーハンドリング：500エラー
  }
});

// Expressルート：新しいレビューを追加するAPI
app.post('/insert_review', express.raw({ type: '*/*' }), async (req, res) => {
  data = JSON.parse(req.body);  // リクエストボディからJSONデータを取得
  const documents = await Reviews.find().sort({ id: -1 });  // 最新のレビューをID順で取得
  let new_id = documents[0].id + 1;  // 新しいレビューのIDを決定（最後のID + 1）

  // 新しいレビューを作成
  const review = new Reviews({
    "id": new_id,  // 新しいIDを設定
    "name": data.name,  // レビュー投稿者の名前
    "dealership": data.dealership,  // 関連するディーラーのID
    "review": data.review,  // レビューの内容
    "purchase": data.purchase,  // 購入有無
    "purchase_date": data.purchase_date,  // 購入日
    "car_make": data.car_make,  // 車のメーカー
    "car_model": data.car_model,  // 車のモデル
    "car_year": data.car_year,  // 車の年式
  });

  try {
    const savedReview = await review.save();  // 新しいレビューを保存
    res.json(savedReview);  // 保存したレビューをJSON形式で返す
  } catch (error) {
    console.log(error);  // エラーが発生した場合はコンソールに出力
    res.status(500).json({ error: 'Error inserting review' });  // エラーハンドリング：500エラー
  }
});

// Expressサーバーを起動
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);  // サーバーが起動したことをログに出力
});
