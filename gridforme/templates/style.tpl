body {
    position: relative;
    display: block;
}

body:after {
    position: absolute;
    width: auto;
    height: auto;
    z-index: 9999;
    content: '';
    pointer-events: none;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    background: url(http://gridfor.me{{ imagepath }}) repeat-y center top !important;
    transition: display 1.5s;
}

body:active:after {
    display: none;
}
