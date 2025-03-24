<script>
  import Card from './Card.svelte';
  let cards = [
    { rank: 'A', suit: 'd' },
    { rank: 'K', suit: 's' },
    { rank: '10', suit: 'h' },
    { rank: '7', suit: 'c' },
    { rank: '2', suit: 's' },
  ];
</script>

<div class="flex justify-center gap-2 mb-6">
  {#each cards as card}
    <Card rank={card.rank} suit={card.suit} />
  {/each}
</div>
