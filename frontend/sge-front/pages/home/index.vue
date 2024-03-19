<script setup lang="ts">
const { signOut } = useAuth();
definePageMeta({
    middleware: 'auth'
})

const submitLogout = ()=> {
    signOut({redirect: false}).then(()=>{
        console.log("successfully performed the logout");
        navigateTo("/")
    }).catch((error)=>{
        console.log("error when trying logout ", error);
    })
}
</script>

<template>
    <div>
        <h1>Minha Tela Home!!!</h1>    
        <button @click="submitLogout" class="customButton">SAIR</button>
    </div>
</template>

<style lang="scss">

</style>