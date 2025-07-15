#!/usr/bin/env python
print("Content-Type: text/html")

import sqlite3, sys, cgi, csv
import cgitb; cgitb.enable()
from db_functions import *

print("""
<!DOCTYPE html>
<html ng-app="heroViewer">
<head>
    <title>Hero View - Dotabase</title>
    <meta name="Authors" content="Asha" />
    <meta charset="UTF-8">
    <link type="text/css" rel="stylesheet" href="resources/origin/css/pace.css" />
    <link type="text/less" rel="stylesheet" href="resources/origin/css/app.less" />
    <link type="text/css" rel="stylesheet" href="resources/origin/css/semantic.min.css" />
    <script type="text/javascript" src="resources/origin/javascript/pace.js"></script>
    <script type="text/javascript" src="resources/origin/javascript/less.js"></script>
    <script type="text/javascript" src="resources/origin/javascript/qtek.js"></script>
    <script type="text/javascript" src="resources/origin/javascript/angular.js"></script>
    <script type="text/javascript" src="resources/origin/javascript/jquery.js"></script>
    <script type="text/javascript" src="resources/origin/javascript/semantic.min.js"></script>
</head>
<body style="margin:0px">
    <div id="App">
        <div id="HeroViewer">
            <canvas id="ViewPort"></canvas>
        </div>
        <div ng-view></div>
    </div>
    <div id="SoundControl">
        <div class="ui circular icon button blue" id="PlayPause">
            <i class="icon pause"></i>
        </div>
        <div class="ui circular icon button blue" id="Shuffle">
            <i class="icon shuffle"></i>
        </div>
    </div>
    <div id="Settings" class="ui right sidebar">
        <div class="ui label">Shadow Quality</div>
        <div id="ShadowQuality" dropdown class="ui labeled icon top right pointing dropdown purple mini button">
            <i class="dropdown icon"></i>
            <span class="text">High</span>
            <div class="menu">
                <div class="item">None</div>
                <div class="item">Low</div>
                <div class="item">High</div>
            </div>
        </div>
        <div class="ui label">Soft Shadow</div>
        <div id="SoftShadow" class="ui labeled icon top right pointing dropdown purple mini button">
            <i class="dropdown icon"></i>
            <span class="text">VSM</span>
            <div class="menu">
                <div class="item">PCF</div>
                <div class="item active">VSM</div>
            </div>
        </div>
    </div>
    <script type="text/javascript">
        angular.module("heroViewer", []);
    </script>
    <script type="text/javascript" src="resources/origin/javascript/SMDParser.js"></script>
    <script type="text/javascript" src="resources/origin/javascript/config.js"></script>
    <script type="text/javascript" src="resources/origin/javascript/background.js"></script>
    <script type="text/javascript" src="resources/origin/javascript/sparkle.js"></script>
    <script type="text/javascript" src="resources/origin/javascript/heroCtrl.js"></script>
    <script type="text/javascript" src="resources/origin/javascript/heroListCtrl.js"></script>
    <script type="text/javascript" src="resources/origin/javascript/app.js"></script>
</body>
</html>
    """)