<script>
  import {} from "../stores/cableStore.svelte.js";
  let {
    minBet,
    maxBet,
  } = $props()

  let currentBet = $state(minBet);
  let inputValue = $state(minBet.toString());

  $effect(() => {
    inputValue = currentBet.toString();
  });
</script>

<div class="bg-slate-950 border border-gray-700 rounded p-2 font-mono w-full max-w-xs">
  <!-- Main action buttons (larger) -->
  <div class="flex gap-2 justify-between mb-2">
    <button class="px-3 py-2 bg-gray-700 text-gray-200 rounded font-bold hover:bg-gray-600 transition-colors flex-1 text-center">Fold</button>
    <button class="px-3 py-2 bg-sky-500 text-white rounded font-bold hover:bg-blue-500 transition-colors flex-1 text-center">Call ${minBet}</button>
    <button class="px-3 py-2 bg-rose-500 text-white rounded font-bold hover:bg-red-500 transition-colors flex-1 text-center">Raise</button>
  </div>

  <!-- Slider and bet amount -->
  <div class="flex items-center gap-2 mb-2">
    <input type="range" min={minBet} max={maxBet} step="0.01" bind:value={currentBet} class="flex-grow h-1 bg-gray-700 rounded-lg appearance-none">
    <div class="bg-gray-900 px-2 py-1 rounded text-blue-400 border border-gray-700 text-center text-sm min-w-16 relative">
      <span class="absolute left-1 top-1/2 transform -translate-y-1/2 text-xs">$</span>
      <input
        type="text"
        bind:value={inputValue}
        oninput={(e) => {
          inputValue = e.target.value.replace(/[^0-9.]/g, '');
        }}
        onkeydown={(e) => {
          if (e.key === 'Enter') {
            const value = parseFloat(inputValue);
            if (!isNaN(value)) {
              currentBet = Math.max(minBet, Math.min(maxBet, value));
            }
            inputValue = currentBet.toString();
          }
        }}
        class="bg-transparent text-blue-400 text-center text-sm w-full pl-3 pr-1 focus:outline-none focus:ring-1 focus:ring-blue-500 rounded"
      >
    </div>
  </div>

  <!-- Bet size shortcuts -->
  <div class="flex gap-1 justify-between">
    <button class="px-2 py-1 bg-gray-800 text-gray-300 rounded text-xs hover:bg-gray-700 transition-colors">33%</button>
    <button class="px-2 py-1 bg-gray-800 text-gray-300 rounded text-xs hover:bg-gray-700 transition-colors">50%</button>
    <button class="px-2 py-1 bg-gray-800 text-gray-300 rounded text-xs hover:bg-gray-700 transition-colors">75%</button>
    <button class="px-2 py-1 bg-gray-800 text-gray-300 rounded text-xs hover:bg-gray-700 transition-colors">100%</button>
    <button class="px-2 py-1 bg-gray-800 text-gray-300 rounded text-xs hover:bg-gray-700 transition-colors">150%</button>
    <button class="px-2 py-1 bg-gray-800 text-gray-300 rounded text-xs hover:bg-gray-700 transition-colors">All-in</button>
  </div>
</div>
