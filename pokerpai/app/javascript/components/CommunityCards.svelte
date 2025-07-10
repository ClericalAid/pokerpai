<script>
  import Card from './Card.svelte';
  import { parseCard } from '../stores/gameState.svelte.js';

  let { board = [] } = $props();

  // Always show 5 cards, with blanks for remaining slots
  let cards = $derived([
    board[0] ? parseCard(board[0]) : { rank: '', suit: '' },
    board[1] ? parseCard(board[1]) : { rank: '', suit: '' },
    board[2] ? parseCard(board[2]) : { rank: '', suit: '' },
    board[3] ? parseCard(board[3]) : { rank: '', suit: '' },
    board[4] ? parseCard(board[4]) : { rank: '', suit: '' }
  ]);
</script>

<div class="flex justify-center gap-2 mb-6">
  {#each cards as card}
    <Card rank={card.rank} suit={card.suit} />
  {/each}
</div>
