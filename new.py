#!/usr/bin/python
print('Content-Type: text/html')

import sqlite3, sys, cgi, csv
import cgitb; cgitb.enable()
from db_functions import *

print("""
<!DOCTYPE html>
<html ng-app="heroViewer">
    <head>
        <meta charset="UTF-8">
        <title>New Hero - Dotabase</title>
        <meta name="Author" content="Asha" />
        <link rel="icon" href="resources/images/favicon.ico" type="image/x-icon">
        <link type="text/css" rel="stylesheet" href="resources/css/pace.css" />
        <script type="text/javascript" src="resources/javascript/browsercheck.js"></script>
        <link type="text/css" rel="stylesheet" href="resources/css/menu.css" />
        <script type="text/javascript" src="resources/javascript/pace.js"></script>
        <script type="text/javascript" src="resources/javascript/less.js"></script>
        <script type="text/javascript" src="resources/javascript/qtek.js"></script>
        <script type="text/javascript" src="resources/javascript/angular.js"></script>
        <script type="text/javascript" src="resources/javascript/jquery.js"></script>
        <script type="text/javascript" src="resources/javascript/semantic.min.js"></script>
        <style type="text/css">
            body {
                overflow: hidden;
            }
            .fs {
                position: fixed; 
                right: 0; 
                bottom: 0;
                min-width: 100%; 
                min-height: 100%;
                width: auto; 
                height: auto; 
                z-index: -100;
                background: url('resources/images/wallpaper.png') no-repeat;
                background-size: cover;
                filter: alpha(opacity = 80); 
                opacity: .95;
            }
            h1.message {
                margin-top: -800px;
                margin-left: 300px;
                margin-bottom: 200px;
                color: aquamarine;
                letter-spacing: .1em;
                text-shadow: -1px -1px 1px #111111, 2px 2px 1px #363636;
                font-size: 2em;
                box-shadow: 0 0 20px red;
                background-color: #111;
                width: 525px;
                height: 220px;
                padding-left: 7px;
            }
        </style>
    </head>
    <body style="margin: 0px">
        <nav>
            <ul>
                <li><a class="menu" href="index.py#/heroes">Home</a></li>
                <li><a class="menu" href="create.py#/heroes">Create New</a></li>
                <li><a class="menu" href="insert.py#/heroes">Insert Data</a></li>
                <li><a class="menu" href="all.py#/heroes">All Heroes <font color="red">&#9557;</font></a></li>
                <li><a class="menu" href="by_trait.py#/heroes">by Trait <font color="red">|</font></a></li>
                <li><a class="menu" href="by_speed.py#/heroes">by Speed <font color="red">|</font></a></li>
                <li><a class="menu" href="by_damage.py#/heroes">by Damage <font color="red">|</font></a></li>
                <li><a class="menu" href="by_range.py#/heroes">by Range <font color="red">|</font></a></li>
                <li><a class="menu" href="win_rate.py#/heroes">by Win Rate <font color="red">&#9563;</font></a></li>
                <li><a class="menu" href="first_10.py#/heroes">First 10</a></li>
                <li><a class="menu" href="query.py#/heroes">Letter Query</a></li>
                <li class="current"><a class="menu" href="new.py#/heroes">Create Hero</a></li>
                <li><a class="menu" href="items.py#/heroes">All Items <font color="green">&#9557;</font></a></li>
                <li><a class="menu" href="by_type.py#/heroes">by Type <font color="green">|</font></a></li>
                <li><a class="menu" href="by_price.py#/heroes">by Cost <font color="green">|</font></a></li>
                <li><a class="menu" href="by_damage_items.py#/heroes">by Damage <font color="green">|</font></a></li>
                <li><a class="menu" href="win_rate_items.py#/heroes">by Win Rate <font color="green">|</font></a></li>
                <li><a class="menu" href="usage.py#/heroes">by Usage <font color="green">&#9563;</font></a></li>
                <li><a class="menu" href="https://github.com/whiteawake/dotabase" target="_blank"><img src="resources/images/github.png" width="30px" height="30px" style="margin-top: 5px;" /></a></li>
            </ul>
        </nav>
        <div id="formContainer">
            <h1 class="banner" style="width: 160px; margin-bottom: -30px;">Create a new</h1>
            <h2 class="banner" style="margin-left: -65px; margin-top: 32px;">Hero</h1>
            <form method="post" action="engine.py">  
                <input type="text" placeholder="Hero name" name="name" required /> <br />
                <select name="allegiance" style="width: 153px;" required>
                    <option value="Radiant">The Radiant</option>
                    <option value="Dire">The Dire</option>
                </select> <br />
                <select name="trait" style="width: 153px;" required>
                    <option value="Strength">Strength</option>
                    <option value="Agility">Agility</option>
                    <option value="Intelligence">Intelligence</option>
                </select> <br />
                <input type="number" placeholder="Base Strength" name="strength" required /> <br />
                <input type="number" placeholder="Base Agility" name="agility" required /> <br />
                <input type="number" placeholder="Base Intelligence" name="intelligence" required /> <br />
                <input type="number" placeholder="Movement Speed" name="movement" required /> <br />
                <input type="number" placeholder="Starting Armour" name="armour" required /> <br />
                <input type="number" placeholder="Damage (min)" name="min_damage" required /> <br />
                <input type="number" placeholder="Damage (max)" name="max_damage" required /> <br />
                <input type="number" placeholder="Attack Range" name="range_" required /> <br />
                <input type="number" placeholder="Win Rate (%)" name="rate" required /> <br />
                <input type="submit" id="submit" value="Add" />
            </form>
        </div>
        <br/><br/><br/><br/><br/>
        <div id="App">
            <canvas id="ViewPort" class="fs"></canvas>
            <div ng-view></div>
        </div>
        <script type="text/javascript">
            angular.module("heroViewer", []);
        </script>
        <script type="text/javascript" src="resources/javascript/SMDParser.js"></script>
        <script type="text/javascript" src="resources/javascript/config.js"></script>
        <script type="text/javascript" src="resources/javascript/background.js"></script>
        <script type="text/javascript" src="resources/javascript/sparkle.js"></script>
        <script type="text/javascript" src="resources/javascript/heroCtrl.js"></script>
        <script type="text/javascript" src="resources/javascript/heroListCtrl.js"></script>
        <script type="text/javascript" src="resources/javascript/app.js"></script>
    </body>
</html>
""")