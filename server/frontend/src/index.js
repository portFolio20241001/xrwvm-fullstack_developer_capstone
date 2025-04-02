import React from 'react'; // Reactライブラリをインポート（Reactコンポーネントを作成するために必要）
import ReactDOM from 'react-dom/client'; // ReactDOMをインポート（ReactコンポーネントをHTMLに描画するために使用）
import App from './App'; // メインコンポーネント（アプリ全体のルートコンポーネント）をインポート
import { BrowserRouter } from "react-router-dom"; // ルーティング機能を提供するBrowserRouterをインポート

// Reactアプリを描画するためのルート（HTMLのid='root'要素を取得）
const root = ReactDOM.createRoot(document.getElementById('root')); 

// ルートコンポーネント（App）をBrowserRouterでラップし、Reactアプリをレンダリング
root.render(
    <BrowserRouter>  {/* ルーティング機能を有効化 */}
      <App />         {/* アプリケーションのメインコンポーネント */}
    </BrowserRouter>
);