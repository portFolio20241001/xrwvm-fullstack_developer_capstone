// LoginPanelコンポーネントをインポート
import LoginPanel from "./components/Login/Login";
// RegisterPanelコンポーネントをインポート
import RegisterPanel from "./components/Register/Register"; 
// Dealersコンポーネントをインポート
import Dealers from './components/Dealers/Dealers';
// Dealerコンポーネントをインポート
import Dealer from "./components/Dealers/Dealer"
// React RouterのRoutesとRouteをインポート
import { Routes, Route } from "react-router-dom";

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
    </Routes>
  );
}

export default App; // このコンポーネントをエクスポート
