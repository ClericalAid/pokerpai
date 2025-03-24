<script>
  let { rank, suit, size = "normal" } = $props();
  let suit_map = {
    "h": "♥",
    "d": "♦",
    "c": "♣",
    "s": "♠",
    "?": "",
  }
  let colour_map = {
   "h": "text-rose-400",
   "d": "text-sky-400",
   "c": "text-green-300",
   "s": "text-orange-300",
   "?": "text-white",
  }

</script>

<div class="{size === "small" ? "w-10 h-14" : "w-12 h-16"} bg-slate-900 border border-gray-700 rounded flex-col font-bold shadow-md text-lg">
  {#if (rank === "?")}
    <div class="w-full h-full align-middle text-center {colour_map[suit]}">{rank}{suit_map[suit]}</div>
  {:else}
    <div class="w-full text-center {colour_map[suit]}">{rank}{suit_map[suit]}</div>
    <div class="w-full text-center {colour_map[suit]}">{suit_map[suit]}{rank}</div>
  {/if}
</div>
