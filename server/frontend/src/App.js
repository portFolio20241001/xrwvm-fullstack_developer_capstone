import LoginPanel from "./components/Login/Login";           // LoginPanelコンポーネントをインポート
import RegisterPanel from "./components/Register/Register";  // RegisterPanelコンポーネントをインポート
import Dealers from './components/Dealers/Dealers';          // Dealersコンポーネントをインポート
import Dealer from "./components/Dealers/Dealer";            // Dealerコンポーネントをインポート
import PostReview from "./components/Dealers/PostReview";    // PostReviewコンポーネントをインポート
import { Routes, Route } from "react-router-dom";            // React RouterのRoutesとRouteをインポート

function App() {
  return (
    <Routes> {/* ルート定義開始 */}
      {/* /login のパスにアクセスした場合に LoginPanel コンポーネントを表示 */}
      <Route path="/login" element={<LoginPanel />} /> 
      
      {/* /register のパスにアクセスした場合に RegisterPanel コンポーネントを表示 */}
      <Route path="/register" element={<RegisterPanel />} /> 

      {/* /dealers のパスにアクセスした場合に Dealers コンポーネントを表示 */}
      <Route path="/dealers" element={<Dealers />} />

      {/* /dealer のパスにアクセスした場合に Dealer コンポーネントを表示 */}
      <Route path="/dealer/:id" element={<Dealer/>} />

      {/* /postreview のパスにアクセスした場合に PostReview コンポーネントを表示 */}
      <Route path="/postreview/:id" element={<PostReview/>} />
    </Routes>
  );
}

export default App; // このコンポーネントをエクスポート
