document.getElementById('apps').hidden = true
document.getElementById('help').hidden = true


/* Functions */
function home() {
    document.getElementById('apps').hidden = true
    document.getElementById('home').hidden = false
    document.getElementById('help').hidden = true
}

function showApps() {
    document.getElementById('home').hidden = true
    document.getElementById('apps').hidden = false
    document.getElementById('help').hidden = true
}

function help() {
    document.getElementById('apps').hidden = true
    document.getElementById('home').hidden = true
    document.getElementById('help').hidden = false
}