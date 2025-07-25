<template>
  <div class="container">
    <div class="header">
      <h2 class="title">Movie List</h2>
      <BaseButton @click="showModal = true">Add a movie</BaseButton>
    </div>
    <div class="movie-list">
      <template v-if="movies.length > 0">
        <MovieCard
          v-for="movie in movies"
          :key="movie.id"
          :title="movie.title"
          :description="movie.description"
          :date-added="movie.dateAdded"
          :poster-url="movie.posterUrl"
          :video-file="movie.sampleVideoUrl"
          @click="openDetails(movie)"
        />
      </template>
      <div v-else class="empty-state">
        <i class="mdi mdi-movie-open-off-outline"></i>
        <p>No movies found.</p>
        <BaseButton @click="showAddPanel = true">Add a movie</BaseButton>
      </div>
    </div>
    <BaseModal v-model="showModal">
      <MovieFormModal @close="showModal = false" />
    </BaseModal>
  </div>
</template>

<script>
import BaseButton from '../components/BaseButton.vue';
import BaseModal from '@/components/BaseModal.vue'
import MovieCard from '@/components/MovieCard.vue'
import MovieFormModal from '@/components/MovieFormModal.vue'

export default {
  name: 'MovieList',

  components: {
    BaseButton,
    BaseModal,
    MovieCard,
    MovieFormModal
  },

  data() {
    return {
      showModal: false,   
      movies: [
        {
          id: 3,
          title: 'Interstellar',
          dateAdded: '2014-11-07',
          posterUrl: 'https://m.media-amazon.com/images/I/91kFYg4fX3L._AC_SY679_.jpg',
          sampleVideoUrl: 'https://samplelib.com/lib/preview/mp4/sample-5s.mp4',
          description: 'A group of explorers travel through a wormhole in space in an attempt to ensure humanity’s survival.'
        },
        {
          id: 1,
          title: 'Inception',
          dateAdded: '2021-07-16',
          posterUrl: 'https://m.media-amazon.com/images/I/81p+xe8cbnL._AC_SY679_.jpg',
          sampleVideoUrl: 'https://samplelib.com/lib/preview/mp4/sample-10s.mp4',
          description: 'A skilled thief who steals corporate secrets through dream-sharing technology is offered a chance to erase his past.'
        },
        {
          id: 2,
          title: 'The Matrix',
          dateAdded: '1999-03-31',
          posterUrl: 'https://m.media-amazon.com/images/I/51EG732BV3L.jpg',
          sampleVideoUrl: 'https://samplelib.com/lib/preview/mp4/sample-3s.mp4',
          description: 'A computer hacker learns about the true nature of his reality and his role in the war against its controllers.'
        }
      ]
    }
  },

  methods: {
    openDetails(movie) {
      this.selectedMovie = movie;
      this.showDetails = true;
    },
  }
}
</script>

<style lang='scss' scoped>
  @use '@/stylesheets/styles.scss' as *;

  .container {
    padding: 0px 40px;
    background-color: var(--page-background);
    height: 100vh;
  }

  .header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    color: var(--white);
    height: 80px;
  }

  .movie-list {
    @include flex-wrap;
    background-color: var(--page-background);
    gap: 40px;
    justify-content: center;
  }

  .empty-state {
    @include flex-column;
    align-items: center;
    justify-content: center;
    height: 80vh;
    width: 100%;
    text-align: center;
    gap: 16px;
    color: var(--secondary);

    i {
      font-size: 80px;
      color: var(--secondary);
    }

    p {
      font-size: 18px;
      margin: 0;
    }
  }
</style>
