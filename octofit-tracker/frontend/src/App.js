
import './App.css';
import { Routes, Route, Link } from 'react-router-dom';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';
import logo from '../public/logo192.png';
function App() {
  return (
    <div className="App">
      <nav className="navbar navbar-expand navbar-light mb-4">
        <div className="container-fluid">
          <Link className="navbar-brand d-flex align-items-center" to="/">
            <img src={logo} alt="OctoFit Logo" className="App-logo me-2" />
            OctoFit Tracker
          </Link>
          <ul className="navbar-nav me-auto mb-2 mb-lg-0">
            <li className="nav-item">
              <Link className="nav-link" to="/activities">Activities</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/workouts">Workouts</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/teams">Teams</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/users">Users</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/leaderboard">Leaderboard</Link>
            </li>
          </ul>
        </div>
      </nav>
      <div className="container">
        <Routes>
          <Route path="/" element={<h1>Welcome to OctoFit Tracker!</h1>} />
          <Route path="/activities" element={<Activities />} />
          <Route path="/workouts" element={<Workouts />} />
          <Route path="/teams" element={<Teams />} />
          <Route path="/users" element={<Users />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
        </Routes>
      </div>
    </div>
	);
}

export default App;
