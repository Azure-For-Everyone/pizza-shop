import { useState } from 'react';
import { useLoaderData } from 'react-router-dom';
import { getMenu } from '../../services/apiRestaurant';
import MenuItem from './MenuItem';

function Menu() {
  const initialMenu = useLoaderData();
  const [menu, setMenu] = useState(initialMenu);
  const [query, setQuery] = useState('');

  async function handleSubmit(e) {
    const filter = { query };
    const newMenu = await loader(filter);
    setMenu(newMenu);
  }
  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input
          placeholder="Search pizza"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          className="bg-white-100 my-10 w-full rounded-full px-8 py-3 text-[11px] transition-all duration-300 placeholder:text-stone-400 focus:outline-none focus:ring focus:ring-yellow-500 focus:ring-opacity-50 sm:w-full sm:focus:w-full"
        ></input>
      </form>

      <ul className="divide-y divide-stone-200 px-2">
        {menu.map((pizza) => (
          <MenuItem pizza={pizza} key={pizza.id} />
        ))}
      </ul>
    </div>
  );
}

export async function loader(filter) {
  const menu = await getMenu(filter);
  return menu;
}
export default Menu;
