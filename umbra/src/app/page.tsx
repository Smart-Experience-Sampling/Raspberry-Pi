export default function Home() {
  return (
    <div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
      <main className="flex flex-col row-start-2 items-center text-center lg:text-9xl sm:text-3xl">
        Click the button when you have a social interaction
        <small className="text-3xl">3 clickers available</small>
      </main>
      <footer className="row-start-3 flex gap-6 flex-wrap items-center justify-center">
        Powered by Smart Sampling Group at Fonty`s ICT
      </footer>
    </div>
  );
}
