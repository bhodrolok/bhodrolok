function getDate(){
    // (Loosely) replicate the default output of the Linux 'date' command, with the '-u' i.e. '--universal' flag 
    // https://www.gnu.org/software/coreutils/manual/html_node/date-invocation.html#date-invocation
    const elemToModify = document.getElementById('curr-date');
    var today = new Date();
    const dateOptions_LDS = {
        weekday: 'long',
        month: 'short',
        day: 'numeric',
        year: 'numeric',
    };
    const dateOptions_LTS = {
        timeZone: 'UTC',
        timeZoneName: 'short',
    }
    let todayDate = today.toLocaleDateString(navigator.language, dateOptions_LDS);
    let todayTime = today.toLocaleTimeString(navigator.language, dateOptions_LTS);
    var fmtDateRes2 = `${todayDate} ${todayTime}`;
    if (elemToModify) {
        elemToModify.innerHTML = fmtDateRes2;
    }
}

// Call it
window.onload = getDate;