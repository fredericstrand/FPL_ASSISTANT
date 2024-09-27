import React, { useState } from "react";
import "../styles/landing-page.css"

function Landing_page() {
    return (
        <>
        <div class="hero-container">
            <div class="hero-content">
                <h1>Welcome to a Community of Dedicated FPL Players.</h1>
                <p>Through our dashboard and machine learning applications we will help you along the way to victory in your FPL League</p>
                <a href="login"><span>SIGN UP NOW </span></a>
            </div>
            <div class="hero-content-image">
                <img src="/images/intro-image.png" alt="into image" id="intro-image"></img>
            </div>
        </div>

        <div class="intro-container">
            <div class="intro-content">
                <div class ="intro-content-text-1">
                    <h2>We offer industry leading services</h2>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
                </div>
                <div class="intro-content-text-2">
                    <h2>We offer industry leading services</h2>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
                </div>
                <div class="intro-content-text-3">
                    <h2>We offer industry leading services</h2>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
                </div>
            </div>
        </div>
        </>
    );
}

export default Landing_page;
