<script>
  import Card from './Card.svelte';

  let {
    name,
    stack,
    bet,
    isHero,
    betPosition,
    action,
    cards = [{rank: '?', suit: ''}, {rank: '?', suit: ''}],
  } = $props();
</script>

<div class="w-45 p-3 {isHero ? 'bg-gray-800 border-2 border-blue-500' : 'bg-gray-900 border border-gray-700'} rounded shadow-lg">
  <div class="flex justify-between items-center">
    <!-- Left side: Player info -->
    <div class="flex-1 mr-2">
      <div class="w-16 font-bold truncate {isHero ? 'text-blue-400' : 'text-purple-400'}">{name}</div>
      <div class="text-sm mt-1">{stack}</div>
    </div>

    <!-- Right side: Cards -->
    <div class="flex gap-1">
      {#each cards as card}
        <Card rank={card.rank} suit={card.suit} size="small" />
      {/each}
    </div>
  </div>

  {#if bet}
    <div class="absolute {betPosition === 'bottom' ? '-bottom-8 left-1/2 transform -translate-x-1/2' :
                           betPosition === 'top' ? '-top-8 left-1/2 transform -translate-x-1/2' :
                           betPosition === 'right' ? '-right-16 top-1/2 transform -translate-y-1/2' :
                           betPosition === 'bottom-left' ? '-bottom-8 -left-0' :
                           betPosition === 'bottom-right' ? '-bottom-8 -right-0' :
                           '-left-16 top-1/2 transform -translate-y-1/2'}
                 bg-gray-900 border border-gray-700 rounded px-2 py-1 text-sm font-bold text-blue-400">{bet}</div>
  {/if}

  {#if action}
    <div class="absolute {betPosition === 'bottom' ? '-bottom-8 left-1/2 transform -translate-x-1/2' :
                           betPosition === 'top' ? '-top-8 left-1/2 transform -translate-x-1/2' :
                           betPosition === 'right' ? '-right-16 top-1/2 transform -translate-y-1/2' :
                           '-left-16 top-1/2 transform -translate-y-1/2'}
                 bg-gray-900 border border-gray-700 rounded px-2 py-1 text-sm font-bold text-gray-400">{action}</div>
  {/if}
</div>
