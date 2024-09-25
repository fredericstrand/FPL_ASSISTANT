import React, { useState } from "react";
import "../styles/navbar.css";

function Navbar() {
  // State to handle the toggle of the nav and burger menu
  const [isNavActive, setNavActive] = useState(false);

  // Toggle the navigation links and burger animation
  const handleBurgerClick = () => {
    setNavActive(!isNavActive); // Toggle the state
  };

  return (
    <div class="navbar-container">
    <nav className="navbar">
      <div className="brand-title">
        <img src="images/fpl_logo.png" alt="FPL Logo" className="logo" />
      </div>
      
      {/* Divider Line */}
      <div className="divider"></div>

      <div className="burger" onClick={handleBurgerClick}>
        {/* Burger Menu (3 divs to create the burger icon) */}
        <div className={`line1 ${isNavActive ? "toggle" : ""}`}></div>
        <div className={`line2 ${isNavActive ? "toggle" : ""}`}></div>
        <div className={`line3 ${isNavActive ? "toggle" : ""}`}></div>
      </div>

      <ul className={`nav-links ${isNavActive ? "nav-active" : ""}`}>
        <li><a href="/">DASHBOARD</a></li>
        <li><a href="/your-team">YOUR TEAM</a></li>
        <li><a href="/ai-team">AI TEAM</a></li>
        <li><a href="/about">ABOUT</a></li>
        <li><a href="/login" id="login-button">LOG IN</a></li>
      </ul>
    </nav>
    </div>
  );
}

export default Navbar;
