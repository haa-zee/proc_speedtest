/* Szerző: midnightcoder2 http://blog.hu/user/1157834 */
static void Main (string[] args)
{
    int n=0,e=0;
    for (int i = 0; i < 1; i++)
    {
        foreach (var s in Directory.GetDirectories (@"C:\proc").Where 
                            (w => char.IsDigit (Path.GetFileName (w) [0])))
        try
        {
            using (var f = new StreamReader (Path.Combine (s, "stat")))
            {
            string str = f.ReadLine (); 
            n++;
            }
        }
        catch
        {
            e++;
        }
    }
    Console.WriteLine ($"count: {n}, error:{e}");
}
