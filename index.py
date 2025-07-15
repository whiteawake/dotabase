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
        <title>Home - Dotabase</title>
        <meta name="Author" content="Asha" />
        <link rel="icon" href="resources/images/favicon.ico" type="image/x-icon">
        <link type="text/css" rel="stylesheet" href="resources/css/pace.css" />
        <link type="text/css" rel="stylesheet" href="resources/css/menu.css" />
        <script type="text/javascript" src="resources/javascript/browsercheck.js"></script>
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
        </style>
    </head>
    <body style="margin: 0px">
        <nav>
            <ul>
                <li class="current"><a class="menu" href="#">Home</a></li>
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
                <li><a class="menu" href="new.py#/heroes">Create Hero</a></li>
                <li><a class="menu" href="items.py#/heroes">All Items <font color="green">&#9557;</font></a></li>
                <li><a class="menu" href="by_type.py#/heroes">by Type <font color="green">|</font></a></li>
                <li><a class="menu" href="by_price.py#/heroes">by Cost <font color="green">|</font></a></li>
                <li><a class="menu" href="by_damage_items.py#/heroes">by Damage <font color="green">|</font></a></li>
                <li><a class="menu" href="win_rate_items.py#/heroes">by Win Rate <font color="green">|</font></a></li>
                <li><a class="menu" href="usage.py#/heroes">by Usage <font color="green">&#9563;</font></a></li>
                <li><a class="menu" href="https://github.com/whiteawake/dotabase" target="_blank"><img src="resources/images/github.png" width="30px" height="30px" style="margin-top: 5px;" /></a></li>
            </ul>
        </nav>
        <h1 class="title">Home</h1>
        <h2 class="subtitle">Click the links to get started.</h2>
        <div id="App">
            <canvas id="ViewPort" class="fs">
            </canvas>
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