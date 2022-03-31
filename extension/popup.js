let stats_button = document.getElementById("get-stats-button");

// When the button is clicked, getStats is run in the context of current tab
stats_button.addEventListener("click", async () => {
  let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
  chrome.scripting.executeScript(
    {
      target: { tabId: tab.id },
      function: getStats,
    },
    (stats) => {
      console.log(stats[0]["result"]);
      let textNode = document.getElementById("stats-text");
      textNode.textContent = "";
      var txt = ""
      var obj = JSON.parse(stats[0]["result"])['evaluations'];
      for (let i = 0; i < obj.length; ++i) {
      	for (let j = 0; j < 5; ++j) {
      		if (obj[i][j] == 'present') txt += '🟨';
      		else if (obj[i][j] == 'absent') txt += '⬛';
      		else txt += '🟩';
      	}
		//console.log(req.status, req.statusText);
		// → 200 OK
		//console.log(req.getResponseHeader("content-type"));
		// → text/plain
      }
  	textNode.textContent = txt;
  	var req = new XMLHttpRequest();
	req.open("GET", "http:/127.0.0.1:5000/notify?user=denisrtyhb&log=" + txt, false);
	req.send("tebya");
    }
  );
});

function getStats() {
  //console.log(localStorage.getItem("nyt-wordle-state"));
  return localStorage.getItem("nyt-wordle-state")
}
