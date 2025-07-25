<template>
  <teleport to="body">
    <div v-if="modelValue" class="modal-overlay" @click.self="close">
      <div class="modal-content">
        <slot />
      </div>
    </div>
  </teleport>
</template>

<script>
export default {
  name: 'BaseModal',
  props: {
    modelValue: {
      type: Boolean,
      required: true
    }
  },
  methods: {
    close() {
      this.$emit('update:modelValue', false);
    }
  }
};
</script>

<style lang="scss" scoped>
  @use '@/stylesheets/styles.scss';

  .modal-overlay {
    position: fixed;
    inset: 0;
    background-color: rgba(0, 0, 0, 0.7);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 9999;
  }

  .modal-content {
    background-color: #1e1e1e;
    padding: 24px;
    border-radius: 12px;
    max-width: 700px;
    width: 100%;
    max-height: 80vh;
    overflow: auto;
  }
</style>
