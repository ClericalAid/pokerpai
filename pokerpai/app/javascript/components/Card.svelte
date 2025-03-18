<script>
  let { rank, suit, size = "normal" } = $props();
</script>

<div class="{size === 'small' ? 'w-10 h-14' : 'w-12 h-16'} bg-gray-800 text-white border border-gray-700 rounded flex justify-center items-center font-bold shadow-md text-lg">
  {#if suit === '♥' || suit === '♦'}
    {rank}<span class="text-red-500">{suit}</span>
  {:else}
    {rank}{suit}
  {/if}
</div>
