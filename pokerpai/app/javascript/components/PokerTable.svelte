<script>
  import PlayerBox from './PlayerBox.svelte';
  import Pot from './Pot.svelte';
  import CommunityCards from './CommunityCards.svelte';
  import TerminalPrompt from './TerminalPrompt.svelte';
  import { getPlayerData, formatCurrency } from '../stores/gameState.svelte.js';

  let { gameState } = $props();

  // Map players to seats counter-clockwise from hero (bottom center)
  function mapPlayersToSeats() {
    const seats = Array(9).fill(null);

    for (let i = 0; i < gameState.player_count; i++) {
      const playerData = getPlayerData(i);
      if (playerData) {
        seats[i] = playerData;
      }
    }

    return seats;
  }

  // Counter-clockwise seat mapping:
  // 0 = hero (bottom center)
  // 1 = left bottom
  // 2 = left top
  // 3 = top left
  // 4 = top center-left
  // 5 = top center-right
  // 6 = top right
  // 7 = right top
  // 8 = right bottom

  let seats = $derived(mapPlayersToSeats());
</script>

<div class="w-fit h-full flex flex-col bg-gray-800 rounded-lg border-2 border-gray-700 shadow-xl items-center">
  <!-- Top row - seats 3,4,5,6 -->
  <div class="w-fit flex justify-center items-center gap-2 pt-2">
    {#if seats[3]}
      <div class="relative">
        <PlayerBox
          name={seats[3].name}
          stack={seats[3].stack}
          bet={seats[3].bet}
          betPosition="bottom-right"
          folded={seats[3].folded}
          cards={seats[3].cards}
          isActor={seats[3].isActor}
        />
      </div>
    {/if}
    {#if seats[4]}
      <div class="relative">
        <PlayerBox
          name={seats[4].name}
          stack={seats[4].stack}
          bet={seats[4].bet}
          betPosition="bottom"
          folded={seats[4].folded}
          cards={seats[4].cards}
          isActor={seats[4].isActor}
        />
      </div>
    {/if}
    {#if seats[5]}
      <div class="relative">
        <PlayerBox
          name={seats[5].name}
          stack={seats[5].stack}
          bet={seats[5].bet}
          betPosition="bottom"
          folded={seats[5].folded}
          cards={seats[5].cards}
          isActor={seats[5].isActor}
        />
      </div>
    {/if}
    {#if seats[6]}
      <div class="relative">
        <PlayerBox
          name={seats[6].name}
          stack={seats[6].stack}
          bet={seats[6].bet}
          betPosition="bottom-left"
          folded={seats[6].folded}
          cards={seats[6].cards}
          isActor={seats[6].isActor}
        />
      </div>
    {/if}
  </div>

  <!-- Middle section with side players and table -->
  <div class="flex w-fit justify-center items-center px-6 py-8">
    <!-- Left side - seats 2,1 -->
    <div class="flex flex-col gap-4 pr-24">
      {#if seats[2]}
        <div class="relative">
          <PlayerBox
            name={seats[2].name}
            stack={seats[2].stack}
            bet={seats[2].bet}
            betPosition="right"
            folded={seats[2].folded}
            cards={seats[2].cards}
            isActor={seats[2].isActor}
          />
        </div>
      {/if}
      {#if seats[1]}
        <div class="relative">
          <PlayerBox
            name={seats[1].name}
            stack={seats[1].stack}
            bet={seats[1].bet}
            betPosition="right"
            folded={seats[1].folded}
            cards={seats[1].cards}
            isActor={seats[1].isActor}
          />
        </div>
      {/if}
    </div>

    <!-- Table center with pot and community cards -->
    <div class="w-72 text-center">
      <Pot amount={formatCurrency(gameState.total_pot_amount)} />
      <CommunityCards board={gameState.board} />
    </div>

    <!-- Right side - seats 7,8 -->
    <div class="flex flex-col gap-4 pl-24">
      {#if seats[7]}
        <div class="relative">
          <PlayerBox
            name={seats[7].name}
            stack={seats[7].stack}
            bet={seats[7].bet}
            betPosition="left"
            folded={seats[7].folded}
            cards={seats[7].cards}
            isActor={seats[7].isActor}
          />
        </div>
      {/if}
      {#if seats[8]}
        <div class="relative">
          <PlayerBox
            name={seats[8].name}
            stack={seats[8].stack}
            bet={seats[8].bet}
            betPosition="left"
            folded={seats[8].folded}
            cards={seats[8].cards}
            isActor={seats[8].isActor}
          />
        </div>
      {/if}
    </div>
  </div>

  <!-- Bottom section with hero and terminal -->
  <div class="w-full flex justify-between items-center pb-2 px-6">
    <div class="flex-1">
      <!-- Spacer -->
    </div>

    <!-- Hero player - seat 0 -->
    {#if seats[0]}
      <div class="relative z-10">
        <PlayerBox
          name={seats[0].name}
          stack={seats[0].stack}
          bet={seats[0].bet}
          betPosition="top"
          isHero={true}
          cards={seats[0].cards}
          isActor={seats[0].isActor}
        />
      </div>
    {/if}

    <div class="flex-1 flex justify-end">
      <!-- Terminal Prompt -->
      <TerminalPrompt
        minBet={gameState.checking_or_calling_amount}
        maxBet={gameState.current_stacks[gameState.actor_index] || 0}
      />
    </div>
  </div>
</div>
