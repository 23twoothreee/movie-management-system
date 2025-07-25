<template>
  <div class="details-modal">
    <header class="details-header">
      <h2>{{ title }}</h2>
      <button class="close" @click="$emit('close')">
        <i class="mdi mdi-close"></i>
      </button>
    </header>
    <p v-if="description" class="description">{{ description }}</p>
    <img :src="posterUrl" alt="Poster" class="poster-preview" />

    <video v-if="videoFile" controls class="video-preview">
      <source :src="videoFile" type="video/mp4" />
      Your browser does not support the video tag.
    </video>
    <BaseButton class="primary edit" @click="emitEdit">Edit movie</BaseButton>
  </div>
</template>

<script>
import BaseButton from './BaseButton.vue';

export default {
  name: 'MovieDetailsModal',

  props: {
    title: String,
    description: String,
    posterUrl: String,
    videoFile: {
      type: String,
    },
  },

  components: {
    BaseButton
  },
};
</script>

<style lang="scss" scoped>
  @use '@/stylesheets/styles.scss' as *;

  .details-modal {
    display: flex;
    flex-direction: column;
    gap: 16px;
    width: 100%;
    color: white;
    overflow: auto;
  }

  .poster-preview {
    width: 100%;
    max-height: 300px;
    object-fit: cover;
    border-radius: 8px;
  }

  .video-preview {
    width: 100%;
    border-radius: 8px;
  }

  .details-header {
    display: flex;
    justify-content: space-between;
  }

  .close {
      background: none;
      border: none;
      color: var(--white);
      font-size: 1.5rem;
      cursor: pointer;

      i {
        pointer-events: none;
      }

      &:hover {
        color: var(--btn-primary);
      }
    }

    .edit {
      align-self: flex-end;
      width: fit-content
    }
</style>
