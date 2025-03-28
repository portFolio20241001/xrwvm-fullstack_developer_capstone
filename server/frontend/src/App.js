// LoginPanelコンポーネントをインポート
import LoginPanel from "./components/Login/Login";
// RegisterPanelコンポーネントをインポート
import RegisterPanel from "./components/Register/Register"; 
// React RouterのRoutesとRouteをインポート
import { Routes, Route } from "react-router-dom";

function App() {
  return (
    <Routes> {/* ルート定義開始 */}
      {/* /login のパスにアクセスした場合に LoginPanel コンポーネントを表示 */}
      <Route path="/login" element={<LoginPanel />} /> 
      
      {/* /register のパスにアクセスした場合に RegisterPanel コンポーネントを表示 */}
      <Route path="/register" element={<RegisterPanel />} /> 
    </Routes>
  );
}

export default App; // このコンポーネントをエクスポート
