import { delay, getUserData } from `@/utils/helpers`

export default defineNuxtRouteMiddleware(async () => {
  const userData: boolean = await getUserData() ? true : false
  const redirect = (path: string): Promise<void> => delay(0).then(() => useRouter().push(path))
  const pathToAuth = (route = useRoute()): boolean =>
    ["/auth/login", "/auth/register"].includes(route.path)
      ? true
      : false;

  if (userData && pathToAuth()) {
    redirect("/")
  } 
  
  if (!userData && !pathToAuth()) {
    redirect("/auth/login")
  }
});
 