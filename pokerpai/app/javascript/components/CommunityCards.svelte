<script>
  import Card from './Card.svelte';
  let cards = [
    { rank: 'A', suit: '♦' },
    { rank: 'K', suit: '♠' },
    { rank: '10', suit: '♥' },
    { rank: '7', suit: '♣' },
    { rank: '2', suit: '♠' },
  ];
</script>

<div class="flex justify-center gap-2 mb-6">
  {#each cards as card}
    <Card rank={card.rank} suit={card.suit} />
  {/each}
</div>
