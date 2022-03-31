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
      var obj = JSON.parse(stats[0]["result"])['evaluations'];
      for (let i = 0; i < obj.length; ++i) {
      	for (let j = 0; j < 5; ++j) {
      		if (obj[i][j] == 'present') textNode.textContent += 'Y';
      		else if (obj[i][j] == 'absent') textNode.textContent += 'B';
      		else textNode.textContent += 'G';
      	}
      	textNode.textContent += '\n';
      }
    }
  );
});

function getStats() {
  //console.log(localStorage.getItem("nyt-wordle-state"));
  return localStorage.getItem("nyt-wordle-state")
}
