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
      textNode.textContent = stats[0]["result"];
    }
  );
});

function getStats() {
  //console.log(localStorage.getItem("nyt-wordle-state"));
  return localStorage.getItem("nyt-wordle-state")
}
