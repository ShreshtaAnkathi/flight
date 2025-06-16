import './Navbar.css'

function Navbar({ sortBy, setSortBy }) {
  return (
    <nav className="navbar">
      <div className="navbar-left">
        <img src="/logo.png" alt="Flight Finder" className="logo" />
        <h1>Flight Finder</h1>
      </div>
      <div className="navbar-right">
        <select value={sortBy} onChange={e => setSortBy(e.target.value)}>
          <option value="">Sort By</option>
          <option value="rate">Ratings</option>
          <option value="class">Class</option>
          <option value="seats">Seats</option>
        </select>
      </div>
    </nav>
  )
}

export default Navbar
