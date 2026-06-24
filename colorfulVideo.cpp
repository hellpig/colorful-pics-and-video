/*
Fun video!

This code uses the SFML 2 API.
It works with SFML 2.5/2.6. SFML 3 would require small API changes.

On macOS via MacPorts, I did...
  sudo port install sfml
  g++ -std=c++11 -O3 colorfulVideo.cpp -I/opt/local/include -L/opt/local/lib -lsfml-graphics -lsfml-window -lsfml-system
  ./a.out

On Linux (Ubuntu), I did...
  sudo apt install libsfml-dev
  g++ -O3 colorfulVideo.cpp -lsfml-graphics -lsfml-window -lsfml-system
  ./a.out
If you care to know, the SFML files are probably installed in /usr/include and /usr/lib .

On Windows, you can easily get SFML to work via the MinGW version that the SFML people link to...
  https://www.sfml-dev.org/download/sfml/2.6.2/
I put everything (MinGW, SFML, and this code) in the same folder, then ran...
  mingw64/bin/g++ -O3 colorfulVideo.cpp -I SFML-2.6.2/include -L SFML-2.6.2/lib -lsfml-graphics -lsfml-window -lsfml-system
To run via Cygwin terminal...
  PATH="$PWD/SFML-2.6.2/bin:$PWD/mingw64/bin:$PATH" ./a.exe
To run via PowerShell...
  $oldPath = $env:Path; $env:Path = "$PWD\SFML-2.6.2\bin;$PWD\mingw64\bin;$oldPath"; .\a.exe; $env:Path = $oldPath
I also tried SFML 2.5.1, and it works the exact same (just change all 2.6.2 with 2.5.1).

On Windows, I could also get things to work via Visual Studio Community (I only needed to install "Desktop development with C++")
by making a new "Project from Existing Code" and eventually selecting "Visual C++" then "console application".
In project properties, after selecting "All Configurations" and "All Platforms", link to the ...\include and ...\lib folders
(I first had to manually download and extract SFML), link to "sfml-graphics.lib;sfml-window.lib;sfml-system.lib;",
and change "Stack Reserve Size" to 10000000 (optionally, you can also choose O2 optimization).
To run the executable, I then had to move three .dll files from my SFML download to the project directory
(or you can just add SFML's bin into Windows' Path variable).
After all this work and installation of bloated software, it runs a bit slower than on other operating systems
(even if using Release instead of Debug and when running the .exe file directly).


 (c) 2019 Bradley Knockel
*/



#include <SFML/Graphics.hpp>



#include <cmath>

// for my millisecond sleep
#include <chrono>  // std::chrono::milliseconds
#include <thread>  // std::this_thread::sleep_for




int main(int argc, char ** argv){


  //// define some parameters
  const int n = 501;          // for n by n grid; n = 11 has an interesting look
  const int extraDelay = 10;   // per frame (in milliseconds)


  //// create steps and myRange[] for time steps
  const int steps = 231;   // myRange has 2*steps values
  const float max = 2.3;
  float myRange[steps*2];  // will linearly increase from 0 to max, then decrease back to 0
  for (int i=0; i<steps; i++)
    myRange[i] = max * i/(steps-1);
  for (int i=steps; i<2*steps; i++)
    myRange[i] = max * (2*steps-1-i)/(steps-1);

  //// create X[] and R[][]
  const float pi = 3.141592653;
  const float max2 = 8*pi;
  float X[n];   // x values throughout the image
  for (int x=0; x<n; x++)
    X[x] = max2 * x/(n-1);
  float R[n][n];   // distance from the center at each pixel; put on the stack
  for (int x=0; x<n; x++)
    for (int y=0; y<n; y++)
      R[x][y] = sqrt(pow(X[x] - max2/2, 2) + pow(X[y] - max2/2, 2));  // X[y] gives Y


  int k = -1;     // frame counter
  const float scale = 127.999;   // for scaling trig functions to be 0 to 255


  //////   SFML stuff
  sf::RenderWindow renderWindow(sf::VideoMode(n, n), "Fun video!");
  sf::Event event;
  sf::Image image;
  image.create(n, n, sf::Color(127,127,127,255));  // start as grey
  sf::Texture texture;
  texture.loadFromImage(image);
  sf::Sprite sprite(texture);
  while (renderWindow.isOpen()){     // loop over frames
    texture.loadFromImage(image);
    renderWindow.draw(sprite);
    renderWindow.display();
    while (renderWindow.pollEvent(event)){
      if (event.type == sf::Event::EventType::Closed)
        renderWindow.close();
    }


    // sleep
    std::this_thread::sleep_for(std::chrono::milliseconds(extraDelay));


    // take care of progress
    k++;
    if (k >= 6*steps) k=0;             // linearly increases; resets every 6*steps
    int j = k / (2*steps);             // equals 0 then 1 then 2 then resets when k resets
    float i = myRange[k % (2*steps)];  // increases then decreases; resets every 2*steps



    // update image

    float p11 = pow(i, 1.1);
    float p12 = pow(i, 1.2);
    int r, g, b;


    if (j==0) {             // 1st part of animation
      for (int x=0; x<n; x++){
        /*
           I should pre-calculate r[x], g[x], and b[x] arrays,
           but this is already fast enough and clearer as-is.
        */
        r = scale * sin(X[x]*i) + scale;
        g = scale * sin(X[x]*p11) + scale;
        b = scale * sin(X[x]*p12) + scale;
        for (int y=0; y<n; y++){
          image.setPixel(x, y, sf::Color(r, g, b, 255));
        }
      }
    } else if (j==1) {        // 2nd part of animation
      for (int x=0; x<n; x++){
        r = scale * sin((X[x] - max2)*i) + scale;
        g = scale * sin((X[x] - max2)*p11) + scale;
        b = scale * sin((X[x] - max2)*p12) + scale;
        for (int y=0; y<n; y++){
          image.setPixel(x, y, sf::Color(r, g, b, 255));
        }
      }
    } else {                  // 3rd part of animation
      for (int x=0; x<n; x++){
        r = scale * sin(X[x]*i) + scale;
        g = scale * sin((X[x] - max2)*p11) + scale;
        for (int y=0; y<n; y++){
          b = scale * sin(R[x][y]*i) + scale;
          image.setPixel(x, y, sf::Color(r, g, b, 255));
        }
      }
    }







  }

}

