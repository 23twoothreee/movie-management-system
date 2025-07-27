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
    <BaseButton class="primary edit" @click="isEditing = true">Edit movie</BaseButton>
    </div>
    
    <div v-else class="form-wrapper">
      <header class="form-header">
        <h3 class="title">Editing Movie</h3>
        <button class="close" @click="$emit('close')">
          <i class="mdi mdi-close"></i>
        </button>
      </header>

      <form class="form" @submit.prevent="submitForm">
        <label>
          Title:
          <input type="text" v-model="form.title" required placeholder="Enter movie title" />
        </label>

        <label>
          Description:
          <textarea v-model="form.description" required placeholder="Enter movie description" rows="4"></textarea>
        </label>

        <label>
          Poster URL (Optional):
          <input
            type="text"
            v-model="form.posterUrl"
            placeholder="https://example.com/poster.jpg"
          />
        </label>

        <label>
          Upload Video:
          <input type="file" @change="handleFileUpload" accept="video/*" />
        </label>

        <BaseButton type="submit">Update movie</BaseButton>
      </form>
    </div>
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
      form: {
        title: this.title,
        description: this.description,
        posterUrl: this.posterUrl,
        videoFile: null,
      },
    }
  },

  methods: {
    handleFileUpload(event) {
      const file = event.target.files[0];
      if (file) {
        this.form.videoFile = file;
      }
    },

    async submitForm() {
      const formData = new FormData();
      formData.append('title', this.form.title);
      formData.append('description', this.form.description);
      if (this.form.posterUrl) formData.append('poster_url', this.form.posterUrl);
      if (this.form.videoFile) formData.append('video_file', this.form.videoFile);

      this.$emit('update-movie', formData);
      this.$emit('close');
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
