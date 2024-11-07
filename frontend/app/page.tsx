/* eslint-disable */
"use client"

import { Input } from "@/components/ui/input"
import { Button } from "@/components/ui/button"
import {
  Table,
  TableBody,
  TableCaption,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table"
import { useEffect, useState} from 'react';
import { Label } from "@/components/ui/label"
import { Switch } from "@/components/ui/switch"
import {getRequest} from "@/app/endpoints";


enum DataTypeToDisplay {
    ABOUT_GUTENBERG,
    BOOK_TEXT,
    RECENT_ACTIVITY,
}


interface SearchProps {
    setBookId:  (value: (((prevState: string) => string) | string)) => void,
    setDataTypeToDisplay:  (value: (((prevState: DataTypeToDisplay) => DataTypeToDisplay) | DataTypeToDisplay)) => void
}

interface BookDetailsProps {
    bookId: string
}

function AboutPage(){
    return (
        <>
            <h1 className="scroll-m-20 text-3xl font-extrabold tracking-tight lg:text-4xl">
                About Project Gutenberg
            </h1>
            <p className="leading-7 [&:not(:first-child)]:mt-6">
                Project Gutenberg is a pioneering digital library that provides free access to a vast collection of
                literary works, primarily those in the public domain. Founded in 1971 by Michael S. Hart, it was one
                of the first initiatives to digitize and distribute literary texts on a large scale. With over 60,000
                eBooks available in various formats, including plain text, ePub, and Kindle, Project Gutenberg aims to
                promote literacy and education by making classic literature accessible to everyone, regardless of
                location or economic status. The project thrives on community contributions, relying on volunteers for
                digitization and proofreading efforts, and has inspired similar initiatives globally. Through its
                user-friendly platform, Project Gutenberg continues to play a vital role in preserving cultural
                heritage and democratizing access to literature.
            </p>
        </>
    )
}

function LoadingSpinner(){
    return (
        <div className="flex justify-center items-center h-full">
            <div className="animate-spin h-12 w-12 rounded-full border-4 border-solid border-current border-r-transparent"></div>
        </div>
    )
}


function BookViewToggle({toggleText, setToggleText}: {toggleText: boolean, setToggleText:  (value: (((prevState: boolean) => boolean) | boolean)) => void}){
    return (
        <div className="flex justify-end">
            <div className="flex items-center space-x-3">
                <Switch checked={toggleText} onClick={() => setToggleText(!toggleText)}/>
                <Label className="w-32">{toggleText ? "Plot summary": "Book text"}</Label>
            </div>
        </div>
    )
}


function BookView({toggleText, bookText}: {toggleText: boolean, bookText: string}){
    return (
        <div className="max-h-full overflow-y-auto overflow-x-hidden break-words p-4 max-w-full">
            {
                toggleText ? <p className="whitespace-pre-wrap">{bookText}</p> :
                    <p className="whitespace-pre">{bookText}</p>
            }
        </div>
    )
}


function BookDetails({bookId}: BookDetailsProps){
    const [toggleText, setToggleText] = useState<boolean>(false)
    const [isLoading, setIsLoading] = useState<boolean>(true)
    const [bookText, setBookText] = useState<string>("")
    const [error, setError] = useState<string>("")
    useEffect(() => {
        (async () => {
            setError("")
            setIsLoading(true);
            try {
                const urlToRequest = toggleText ? `/text-analysis/book/${bookId}` : `/book/${bookId}`
                const response = await getRequest(urlToRequest)
                setBookText(response.text)
            } catch (error) {
                const customError = error as Error
                setError(customError.message)
            }
            setIsLoading(false);
        })();
    }, [toggleText, bookId])

    if(error){
        return <p>{error}</p>
    }

    return (
        <div className="flex flex-col gap-10 overflow-hidden">
            {bookText != "" && <BookViewToggle toggleText={toggleText} setToggleText={setToggleText}/>}
            {isLoading ? <LoadingSpinner/> : <BookView toggleText={toggleText} bookText={bookText}/>}
        </div>
    )
}


function RecentActivity() {
    const [recentActivity, setRecentActivity] = useState([])
    const [error, setError] = useState<string>("")
    const [isLoading, setIsLoading] = useState<boolean>(true)
    useEffect(() => {
        // fetch recent activity
        (async () => {
            setError("")
            setIsLoading(true);
            try {
                const response = await getRequest(`/recent-activity`)
                setRecentActivity(response);
            } catch (error) {
                const customError = error as Error
                setError(customError.message)
            }
            setIsLoading(false);
        })();
    }, [])

    if (error) {
        return <p>{error}</p>
    }

    return isLoading ? <LoadingSpinner/> : (
        <Table>
            <TableCaption>previously accessed books</TableCaption>
          <TableHeader>
            <TableRow>
              <TableHead>Book ID</TableHead>
              <TableHead>Title</TableHead>
              <TableHead>Author</TableHead>
              <TableHead>date published</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
        {
          recentActivity.map((activity: any, index) => (
            <TableRow key={index}>
              <TableCell>{activity.book_id}</TableCell>
              <TableCell>{activity.title}</TableCell>
              <TableCell>{activity.author}</TableCell>
              <TableCell>{activity.date_published}</TableCell>
            </TableRow>
          ))
        }
          </TableBody>
        </Table>
    )
}


function Search({ setBookId, setDataTypeToDisplay }: SearchProps){
    const [bookIdInput, setBookIdInput] = useState<string>("")
    return (
        <div className="flex flex-col justify-center gap-4 row-start-2 items-center sm:items-start px-20 w-full">
            <h3 className="scroll-m-20 text-2xl font-semibold tracking-tight text-center">
                Project Gutenberg
            </h3>
            <Input placeholder="Enter book ID" value={bookIdInput} onChange={(event) => setBookIdInput(event.target.value)}/>
            <Button className="w-full" onClick={() => {
                setDataTypeToDisplay(DataTypeToDisplay.BOOK_TEXT)
                setBookId(bookIdInput)
            }}>Search Book</Button>
            <Button className="w-full" variant="outline" onClick={() => {setDataTypeToDisplay(DataTypeToDisplay.RECENT_ACTIVITY)}}>Recent activity</Button>
        </div>
    );
}


export default function Home() {
    const [dataTypeToDisplay, setDataTypeToDisplay] = useState<DataTypeToDisplay>(DataTypeToDisplay.ABOUT_GUTENBERG)
    const [bookId, setBookId] = useState<string>("")

    return (
        <div className="flex min-h-screen">
            <div className="flex items-center justify-center h-screen w-2/5 bg-white p-6 shadow-lg">
                <Search setBookId={setBookId} setDataTypeToDisplay={setDataTypeToDisplay}/>
            </div>
            <div className="flex flex-col h-screen w-3/5 bg-white p-20 shadow-lg">
                {dataTypeToDisplay === DataTypeToDisplay.ABOUT_GUTENBERG && <AboutPage/>}
                {dataTypeToDisplay === DataTypeToDisplay.BOOK_TEXT && <BookDetails bookId={bookId}/>}
                {dataTypeToDisplay === DataTypeToDisplay.RECENT_ACTIVITY && <RecentActivity/>}
            </div>
        </div>
    );
}
