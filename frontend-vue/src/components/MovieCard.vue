<template>
  <div class="movie-card" @click="showDetails = true" title="Click here to view more details">
    <button title="Delete movie" class="delete-button" @click.stop="deleteMovie()">
      <i class="mdi mdi-trash-can-outline"></i>
    </button>
    <img
      :src="posterUrl"
      alt="Movie Poster"
      class="movie-poster"
    />
    <div class="movie-info">
      <h3 class="movie-title" :title="title">{{ title }}</h3>
      <p class="movie-date">Added on {{ formattedDate() }}</p>
    </div>
    <BaseModal v-model="showDetails">
    <MovieDetailsModal
        :title="title"
        :description="description"
        :poster-url="posterUrl"
        :video-file="videoFile"
        @update-movie="handleMovieUpdate($event)"
        @close="showDetails = false"
    />
    </BaseModal>
  </div>
</template>


<script>
import api from '@/api/axios.js'; 

import BaseModal from './BaseModal.vue';
import MovieDetailsModal from './MovieDetailsModal.vue';

export default {
    name: 'MovieCard',

    components: {
        BaseModal,
        MovieDetailsModal,
    },

    data() {
        return {
            showDetails: false
        }
    },

    props: {
        id: {
            type: Number,
            required: true
        },

        title: {
            type: String,
            required: true
        },
        dateAdded: {
            type: String,
            required: true
        },
        posterUrl: {
            type: String,
            default: 'https://s.studiobinder.com/wp-content/uploads/2019/06/Movie-Poster-Template-Movie-Credits-StudioBinder.jpg'
        },
        description: {
            type: String,
            required: false
        },
        videoFile: {
            type: String,
            required: false
        },
    },

    methods: {
        formattedDate() {
            const date = new Date(this.dateAdded)
            return date.toLocaleDateString(undefined, {
                year: 'numeric',
                month: 'short',
                day: 'numeric'
            })
        },

        handleDetails() {
            this.showDetails = true;
        },

        deleteMovie() {
            this.$emit('delete')
        },

        async handleMovieUpdate(formData) {
            try {
                console.trace();
                const res = await api.patch(`movies/${this.id}/`, formData);
                console.log('Edit success:', res.data);
                this.$emit('fetch-movie', this.id)
            } catch (error) {
                console.error('Edit failed:', error.response?.data || error.message);
                alert('Failed to edit movie. Check console.');
                console.log('inside handle movie submit');
            }
        },
    }
};
</script>

<style lang='scss' scoped>
    @use '@/stylesheets/styles.scss';
    
    .movie-card {
        position: relative;
        width: 200px;
        border-radius: 8px;
        overflow: hidden;
        background-color: var(--card-background);
        color: var(--white);
        transition: transform 0.3s ease;
        cursor: pointer;
        max-height: 400px;

        &:hover {
            transform: scale(1.05);
        }

        &::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 60px;
            background: linear-gradient(to bottom, rgba(0, 0, 0, 0.5), transparent);
            backdrop-filter: blur(0.6px);
            z-index: 1;
            pointer-events: none;
        }
    }

    .movie-poster {
        width: 100%;
        height: auto;
        height: 300px; 
        object-fit: cover;
        display: block;
    }

    .movie-info {
        padding: 12px;
        background-color: var(--card-info-background);
    }

    .movie-title {
        font-size: 16px;
        margin: 0;
        font-weight: bold;
    }

    .movie-date {
        font-size: 14px;
        color: var(--secondary);
        margin-top: 4px;
    }

    .delete-button {
        position: absolute;
        top: 8px;
        right: 8px;
        background: var(--black);
        border: none;
        color: var(--white);
        border-radius: 50%;
        padding: 6px;
        cursor: pointer;
        z-index: 2;
        display: flex;
        align-items: center;
        justify-content: center;

        i {
            font-size: 18px;
        }

        &:hover {
            background: var(--btn-primary);
        }
    }
</style>
