<script lang='ts'>
export default {
  data() {
    return {
        email: this.email(),
        string: this.string()
    }
  },
  
  methods: {
    email(email: string): boolean {
      return /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/g.test(email);
    },

    string(arg: any, length: number): boolean {
      return String(arg).replace(/\s/g, "").length >= length;
    },
  },
};
</script>
