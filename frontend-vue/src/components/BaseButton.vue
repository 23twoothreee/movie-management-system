<template>
  <button
    :class="['base-button', variant]"
    :type="type"
    @click="$emit('click')"
  >
    <slot />
  </button>
</template>

<script>
export default {
  name: 'BaseButton',
  props: {
    type: {
      type: String,
      default: 'button'
    },
    variant: {
      type: String,
      default: 'primary' // supports: primary, secondary, etc.
    }
  }
}
</script>

<style lang="scss" scoped>
  @use '@/stylesheets/styles.scss';

  .base-button {
    max-height: 40px;
    padding: 10px 20px;
    border-radius: 4px;
    font-weight: bold;
    cursor: pointer;
    transition: background-color 0.2s ease;

    &.primary {
      background-color: var(--btn-primary);
      color: var(--white);
      border: none;

      &:hover {
        background-color: var(--btn-primary-hover);
      }
    }

    &.secondary {
      background-color: var(--btn-secondary);
      color: var(--black);
      border: none;

      &:hover {
        background-color: var(--btn-secondary-hover);
      }
    }
  }
</style>