import React, { useState } from "react";
import "../styles/landing-page.css"

function Landing_page() {
    return (
        <div class="hero-container">
            <div class="hero-content">
                <h1>Welcome to a community of dedicated FPL players.</h1>
                <p>Through our dashboard and machine learning applications we help you along the way to victory in your FPL League</p>
                <a href="login">Sign up now!</a>
            </div>
        </div>
    );
}

export default Landing_page;
