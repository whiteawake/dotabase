//Identifies the browser and applies a relevant .css file to manage with browser variations in styling.

var isIE = /*@cc_on!@*/false || !!document.documentMode;
var isSafari = Object.prototype.toString.call(window.HTMLElement).indexOf('Constructor') > 0;
var isFirefox = typeof InstallTrigger !== 'undefined';
var isChrome = !!window.chrome && !isOpera;
var isOpera = !!window.opera || navigator.userAgent.indexOf(' OPR/') >= 0;

if (isChrome == true) {
	document.write('<link rel="stylesheet" type="text/css" href="resources/css/mainstyle.css" />');	
};

if (isIE == true) {
	document.write('<link rel="stylesheet" type="text/css" href="resources/css/ie.css" />');
};

if (isSafari == true) {
	document.write('<link rel="stylesheet" type="text/css" href="resources/css/safari.css" />');	
};

if (isFirefox == true) {
	document.write('<link rel="stylesheet" type="text/css" href="resources/css/firefox.css" />');
};

if (isOpera == true) {
	document.write('<link rel="stylesheet" type="text/css" href="resources/css/opera.css" />');
};
