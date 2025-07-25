<template>
  <div class="form-wrapper">
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
    </form>
  </div>
</template>

<script>
import BaseButton from './BaseButton.vue';

export default {
  name: 'MovieFormModal',
  
  components: {
    BaseButton
  },

  data() {
    return {
      title: '',
      description: '',
      posterUrl: '',
      videoFile: null
    };
  },
  methods: {
    handleFileUpload(event) {
      const file = event.target.files[0];
      if (file) {
        this.videoFile = file;
      }
    },
    submitForm() {
      const formData = new FormData();
      formData.append('title', this.title);
      formData.append('description', this.description);
      if (this.posterUrl) formData.append('poster_url', this.posterUrl);
      if (this.videoFile) formData.append('video_file', this.videoFile);

      this.$emit('submit', formData);
      this.$emit('close');
    }
  }
};
</script>

<style scoped lang="scss">
  @use '@/stylesheets/styles.scss' as *;

  .form-wrapper {
    @include flex-column;
    color: white;
    gap: 20px;
  }

  .form-header {
    display: flex;
    justify-content: space-between;
    align-items: center;

    h3 {
      margin: 0;
      font-size: 1.25rem;
      font-weight: bold;
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
  }

  .form {
    display: flex;
    flex-direction: column;
    gap: 16px;

    label {
      display: flex;
      flex-direction: column;
      font-size: 0.95rem;
      color: var(--white);

      input,
      textarea {
        margin-top: 6px;
        padding: 10px 12px;
        border-radius: 6px;
        border: 1px solid #333;
        background-color: #1c1c1c;
        color: var(--white);
        resize: vertical;

        &:focus {
          outline: none;
          border-color: var(--btn-primary);
          box-shadow: 0 0 0 2px rgba(229, 9, 20, 0.3);
        }
      }

      input[type='file'] {
        padding: 0;
        background-color: transparent;
        color: var(--white);
      }
    }

    button {
      margin-top: 12px;
      align-self: flex-end;
    }
  }
</style>
