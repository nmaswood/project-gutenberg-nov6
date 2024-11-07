const API_URL = process.env.NEXT_PUBLIC_API_URL

export async function getRequest(url: string) {
    console.log(API_URL)
    const response = await fetch(`${API_URL}${url}`)
    if(response.status == 404){
        throw new Error("Book not found!")
    }
    if(response.status == 500){
        throw new Error("Oops! Something went wrong!")
    }
    return await response.json()
}