<template>
  <div class="details-modal">
    <div v-if="!isEditing" class="details-modal">
    <header class="details-header">
      <h2>{{ title }}</h2>
      <button class="close" @click="$emit('close')">
        <i class="mdi mdi-close"></i>
      </button>
    </header>
    <p v-if="description" class="description">{{ description }}</p>
    <img :src="posterUrl" alt="Poster" class="poster-preview" />

    <video controls class="video-preview">
      <source :src="`http://127.0.0.1:8000${videoFile}`" type="video/mp4" />
      Your browser does not support the video tag.
    </video>
    <BaseButton class="primary edit">Edit movie</BaseButton>
    </div>
    <!-- <>
    <div v-else class="form-wrapper">
    <header class="form-header">
      <h3 class="title">Add a Movie</h3>
      <button class="close" @click="$emit('close')">
        <i class="mdi mdi-close"></i>
      </button>
    </header>

    <form class="form" @submit.prevent="submitForm">
      <label>
        Title:
        <input type="text" v-model="title" required placeholder="Enter movie title" />
      </label>

      <label>
        Description:
        <textarea v-model="description" required placeholder="Enter movie description" rows="4"></textarea>
      </label>

      <label>
        Poster URL:
        <input
          type="text"
          v-model="posterUrl"
          placeholder="https://example.com/poster.jpg"
        />
      </label>

      <label>
        Upload Video:
        <input type="file" @change="handleFileUpload" accept="video/*" required />
      </label>

      <BaseButton type="submit">Add movie</BaseButton>
    </form> -->
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
    videoFile: String,
  },

  components: {
    BaseButton
  },

  data() {
    return {
      isEditing: false,
    }
  }
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
