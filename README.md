
================================================================================
FILE: .gitignore
================================================================================
# See https://help.github.com/articles/ignoring-files/ for more about ignoring files.

# dependencies
/node_modules

# next.js
/.next/
/out/

# production
/build

# debug
npm-debug.log*
yarn-debug.log*
yarn-error.log*
.pnpm-debug.log*

# env files
.env*

# vercel
.vercel

# typescript
*.tsbuildinfo
next-env.d.ts

================================================================================
FILE: components.json
================================================================================
{
  "$schema": "https://ui.shadcn.com/schema.json",
  "style": "default",
  "rsc": true,
  "tsx": true,
  "tailwind": {
    "config": "tailwind.config.ts",
    "css": "app/globals.css",
    "baseColor": "neutral",
    "cssVariables": true,
    "prefix": ""
  },
  "aliases": {
    "components": "@/components",
    "utils": "@/lib/utils",
    "ui": "@/components/ui",
    "lib": "@/lib",
    "hooks": "@/hooks"
  },
  "iconLibrary": "lucide"
}


================================================================================
FILE: next.config.mjs
================================================================================
/** @type {import('next').NextConfig} */
const nextConfig = {
  eslint: {
    ignoreDuringBuilds: true,
  },
  typescript: {
    ignoreBuildErrors: true,
  },
  images: {
    unoptimized: true,
    domains: ['localhost'],
  },
  // Suppress browser extension errors
  webpack: (config, { dev, isServer }) => {
    if (dev && !isServer) {
      // Add error handling for browser extensions
      config.resolve.fallback = {
        ...config.resolve.fallback,
        fs: false,
        net: false,
        tls: false,
      }
    }
    return config
  },
  
  // Experimental features
  experimental: {
    // Disable strict mode in development to prevent double rendering
    reactStrictMode: false,
  },

  // Headers for security
  async headers() {
    return [
      {
        source: '/(.*)',
        headers: [
          {
            key: 'X-Frame-Options',
            value: 'DENY',
          },
          {
            key: 'X-Content-Type-Options',
            value: 'nosniff',
          },
        ],
      },
    ]
  },
}

export default nextConfig


================================================================================
FILE: package.json
================================================================================
{
  "name": "my-v0-project",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint"
  },
  "dependencies": {
    "@hookform/resolvers": "^3.9.1",
    "@radix-ui/react-accordion": "latest",
    "@radix-ui/react-alert-dialog": "latest",
    "@radix-ui/react-aspect-ratio": "latest",
    "@radix-ui/react-avatar": "latest",
    "@radix-ui/react-checkbox": "latest",
    "@radix-ui/react-collapsible": "latest",
    "@radix-ui/react-context-menu": "latest",
    "@radix-ui/react-dialog": "latest",
    "@radix-ui/react-dropdown-menu": "latest",
    "@radix-ui/react-hover-card": "latest",
    "@radix-ui/react-label": "latest",
    "@radix-ui/react-menubar": "latest",
    "@radix-ui/react-navigation-menu": "latest",
    "@radix-ui/react-popover": "latest",
    "@radix-ui/react-progress": "latest",
    "@radix-ui/react-radio-group": "latest",
    "@radix-ui/react-scroll-area": "latest",
    "@radix-ui/react-select": "latest",
    "@radix-ui/react-separator": "latest",
    "@radix-ui/react-slider": "latest",
    "@radix-ui/react-slot": "latest",
    "@radix-ui/react-switch": "latest",
    "@radix-ui/react-tabs": "latest",
    "@radix-ui/react-toast": "latest",
    "@radix-ui/react-toggle": "latest",
    "@radix-ui/react-toggle-group": "latest",
    "@radix-ui/react-tooltip": "latest",
    "@stripe/stripe-js": "latest",
    "autoprefixer": "^10.4.20",
    "class-variance-authority": "^0.7.1",
    "clsx": "^2.1.1",
    "cmdk": "latest",
    "date-fns": "4.1.0",
    "embla-carousel-react": "latest",
    "input-otp": "latest",
    "jsonwebtoken": "latest",
    "lucide-react": "^0.454.0",
    "next": "14.2.16",
    "next-themes": "latest",
    "react": "^18",
    "react-day-picker": "latest",
    "react-dom": "^18",
    "react-hook-form": "latest",
    "react-resizable-panels": "latest",
    "recharts": "latest",
    "resend": "latest",
    "sonner": "latest",
    "stripe": "latest",
    "tailwind-merge": "^2.5.5",
    "tailwindcss-animate": "^1.0.7",
    "vaul": "latest",
    "zod": "^3.24.1"
  },
  "devDependencies": {
    "@types/node": "^22",
    "@types/react": "^18",
    "@types/react-dom": "^18",
    "postcss": "^8.5",
    "tailwindcss": "^3.4.17",
    "typescript": "^5"
  }
}

================================================================================
FILE: pnpm-lock.yaml
================================================================================
lockfileVersion: '9.0'

settings:
  autoInstallPeers: true
  excludeLinksFromLockfile: false

================================================================================
FILE: postcss.config.mjs
================================================================================
/** @type {import('postcss-load-config').Config} */
const config = {
  plugins: {
    tailwindcss: {},
  },
};

export default config;


================================================================================
FILE: tailwind.config.ts
================================================================================
import type { Config } from "tailwindcss"

const config: Config = {
  darkMode: ["class"],
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
    "*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        background: "hsl(var(--background))",
        foreground: "hsl(var(--foreground))",
        card: {
          DEFAULT: "hsl(var(--card))",
          foreground: "hsl(var(--card-foreground))",
        },
        popover: {
          DEFAULT: "hsl(var(--popover))",
          foreground: "hsl(var(--popover-foreground))",
        },
        primary: {
          DEFAULT: "hsl(var(--primary))",
          foreground: "hsl(var(--primary-foreground))",
        },
        secondary: {
          DEFAULT: "hsl(var(--secondary))",
          foreground: "hsl(var(--secondary-foreground))",
        },
        muted: {
          DEFAULT: "hsl(var(--muted))",
          foreground: "hsl(var(--muted-foreground))",
        },
        accent: {
          DEFAULT: "hsl(var(--accent))",
          foreground: "hsl(var(--accent-foreground))",
        },
        destructive: {
          DEFAULT: "hsl(var(--destructive))",
          foreground: "hsl(var(--destructive-foreground))",
        },
        border: "hsl(var(--border))",
        input: "hsl(var(--input))",
        ring: "hsl(var(--ring))",
        chart: {
          "1": "hsl(var(--chart-1))",
          "2": "hsl(var(--chart-2))",
          "3": "hsl(var(--chart-3))",
          "4": "hsl(var(--chart-4))",
          "5": "hsl(var(--chart-5))",
        },
        sidebar: {
          DEFAULT: "hsl(var(--sidebar-background))",
          foreground: "hsl(var(--sidebar-foreground))",
          primary: "hsl(var(--sidebar-primary))",
          "primary-foreground": "hsl(var(--sidebar-primary-foreground))",
          accent: "hsl(var(--sidebar-accent))",
          "accent-foreground": "hsl(var(--sidebar-accent-foreground))",
          border: "hsl(var(--sidebar-border))",
          ring: "hsl(var(--sidebar-ring))",
        },
      },
      borderRadius: {
        lg: "var(--radius)",
        md: "calc(var(--radius) - 2px)",
        sm: "calc(var(--radius) - 4px)",
        "4xl": "2rem",
        "5xl": "2.5rem",
      },
      keyframes: {
        "accordion-down": {
          from: {
            height: "0",
          },
          to: {
            height: "var(--radix-accordion-content-height)",
          },
        },
        "accordion-up": {
          from: {
            height: "var(--radix-accordion-content-height)",
          },
          to: {
            height: "0",
          },
        },
      },
      animation: {
        "accordion-down": "accordion-down 0.2s ease-out",
        "accordion-up": "accordion-up 0.2s ease-out",
      },
      fontFamily: {
        sans: ["var(--font-inter)"],
        body: ["var(--font-inter)"],
        display: ["var(--font-poppins)"],
      },
      transitionDuration: {
        "400": "400ms",
        "600": "600ms",
        "800": "800ms",
      },
      transitionTimingFunction: {
        "bounce-in": "cubic-bezier(0.25, 0.46, 0.45, 0.94)",
      },
    },
  },
  plugins: [require("tailwindcss-animate")],
}
export default config


================================================================================
FILE: tsconfig.json
================================================================================
{
  "compilerOptions": {
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "target": "ES6",
    "skipLibCheck": true,
    "strict": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "preserve",
    "incremental": true,
    "plugins": [
      {
        "name": "next"
      }
    ],
    "paths": {
      "@/*": ["./*"]
    }
  },
  "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx", ".next/types/**/*.ts"],
  "exclude": ["node_modules"]
}


################################################################################
DIRECTORY: app
################################################################################

--------------------------------------------------------------------------------
FILE: app/about/page.tsx
--------------------------------------------------------------------------------
"use client"

import { SiteHeader } from "@/components/site-header"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import Link from "next/link"
import { Heart, Users, Lightbulb, Target, ArrowRight, Zap } from "lucide-react"

export default function AboutPage() {
  const values = [
    {
      icon: <Heart className="h-8 w-8 text-red-500" />,
      title: "Simple & Friendly",
      description:
        "We believe energy planning shouldn't be complicated. Our tools are designed to be intuitive and accessible for everyone, from beginners to experts.",
    },
    {
      icon: <Users className="h-8 w-8 text-blue-500" />,
      title: "For Everyone",
      description:
        "Whether you're a homeowner planning solar installation or an energy professional designing microgrids, our platform scales to meet your specific needs.",
    },
    {
      icon: <Lightbulb className="h-8 w-8 text-yellow-500" />,
      title: "Innovation First",
      description:
        "We're constantly improving our simulation engine with the latest AI and machine learning technologies to give you the most accurate and reliable results.",
    },
    {
      icon: <Target className="h-8 w-8 text-green-500" />,
      title: "Results Focused",
      description:
        "Every feature we build is designed to help you make better energy decisions, reduce costs, and optimize performance for maximum efficiency.",
    },
  ]

  return (
    <div className="min-h-screen bg-gradient-primary">
      <SiteHeader />

      {/* Hero Section */}
      <section className="section-spacing">
        <div className="container-clean">
          <div className="text-center max-w-5xl mx-auto content-spacing animate-fade-in">
            <div className="inline-flex items-center px-8 py-4 bg-gradient-to-r from-blue-100 to-purple-100 border border-blue-200 rounded-2xl mb-12">
              <span className="text-blue-800 font-bold text-xl">About VoltSphere</span>
            </div>

            <h1 className="text-5xl lg:text-7xl font-bold mb-12 text-gray-900 leading-tight">
              Making Energy Planning
              <span className="text-gradient block mt-4">Simple & Powerful</span>
            </h1>

            <p className="text-2xl lg:text-3xl text-gray-700 leading-relaxed max-w-4xl mx-auto">
              We started VoltSphere because energy planning was too complicated. Our mission is to make clean energy
              accessible to everyone through simple, powerful, and intelligent simulation tools.
            </p>
          </div>
        </div>
      </section>

      {/* Story Section */}
      <section className="section-spacing bg-gradient-secondary">
        <div className="container-clean">
          <div className="grid lg:grid-cols-2 gap-16 lg:gap-24 items-center">
            <div className="content-spacing animate-slide-up">
              <h2 className="text-4xl lg:text-5xl font-bold mb-12 text-gray-900">Our Story</h2>
              <div className="space-y-8 text-gray-700 leading-relaxed">
                <p className="text-xl lg:text-2xl">
                  Energy simulation used to require expensive software and weeks of training. We thought there had to be
                  a better way to democratize access to these powerful tools.
                </p>
                <p className="text-xl lg:text-2xl">
                  So we built VoltSphere - a platform that makes energy modeling as easy as using a calculator. No
                  complex setup, no confusing interfaces, just results you can understand and act upon immediately.
                </p>
                <p className="text-xl lg:text-2xl">
                  Today, thousands of people use VoltSphere to plan everything from home solar systems to large
                  commercial microgrids. And we're just getting started on our journey to transform the energy industry!
                </p>
              </div>
            </div>

            <div className="animate-scale-in">
              <Card className="border-0 shadow-2xl bg-gradient-to-br from-blue-600 to-purple-600 text-white rounded-3xl">
                <CardContent className="p-12 text-center">
                  <div className="space-y-12">
                    <div>
                      <div className="text-5xl lg:text-6xl font-bold mb-4">10,000+</div>
                      <div className="text-xl opacity-90">Happy Users Worldwide</div>
                    </div>
                    <div>
                      <div className="text-5xl lg:text-6xl font-bold mb-4">50,000+</div>
                      <div className="text-xl opacity-90">Simulations Completed</div>
                    </div>
                    <div>
                      <div className="text-5xl lg:text-6xl font-bold mb-4">99%</div>
                      <div className="text-xl opacity-90">Customer Satisfaction</div>
                    </div>
                  </div>
                </CardContent>
              </Card>
            </div>
          </div>
        </div>
      </section>

      {/* Values Section */}
      <section className="section-spacing bg-gradient-accent">
        <div className="container-clean">
          <div className="text-center mb-20 animate-fade-in">
            <h2 className="text-4xl lg:text-5xl font-bold mb-8 text-gray-900">What We Believe</h2>
            <p className="text-2xl text-gray-700 max-w-4xl mx-auto leading-relaxed">
              Our core values guide everything we do, from product design to customer support, ensuring we deliver the
              best possible experience.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-12 lg:gap-16 stagger-children">
            {values.map((value, index) => (
              <Card key={index} className="card-enhanced hover-lift">
                <CardHeader className="p-10">
                  <div className="flex items-center gap-6 mb-6">
                    <div className="w-16 h-16 rounded-2xl bg-gray-50 flex items-center justify-center shadow-lg">
                      {value.icon}
                    </div>
                    <CardTitle className="text-2xl lg:text-3xl font-bold text-gray-900">{value.title}</CardTitle>
                  </div>
                </CardHeader>
                <CardContent className="px-10 pb-10">
                  <p className="text-gray-700 leading-relaxed text-lg lg:text-xl">{value.description}</p>
                </CardContent>
              </Card>
            ))}
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="section-spacing bg-gradient-to-r from-blue-600 via-purple-600 to-indigo-600">
        <div className="container-clean">
          <div className="text-center text-white max-w-5xl mx-auto content-spacing animate-fade-in">
            <h2 className="text-4xl lg:text-5xl font-bold mb-8">Ready to Try VoltSphere?</h2>
            <p className="text-2xl lg:text-3xl mb-16 opacity-90 leading-relaxed">
              Join thousands of people who've simplified their energy planning with our powerful and intuitive platform.
            </p>
            <div className="flex flex-col sm:flex-row gap-8 justify-center">
              <Button
                asChild
                size="lg"
                className="bg-white text-blue-600 hover:bg-gray-100 font-bold px-12 py-6 rounded-2xl text-xl shadow-xl hover:shadow-2xl transition-smooth"
              >
                <Link href="/simulations">
                  Start Free Trial
                  <ArrowRight className="ml-3 h-6 w-6" />
                </Link>
              </Button>
              <Button
                asChild
                variant="outline"
                size="lg"
                className="border-2 border-white text-white hover:bg-white hover:text-blue-600 font-bold px-12 py-6 rounded-2xl text-xl transition-smooth"
              >
                <Link href="/contact">Contact Us</Link>
              </Button>
            </div>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-gray-900 text-white section-spacing-sm">
        <div className="container-clean">
          <div className="grid md:grid-cols-4 gap-12 mb-12">
            <div className="space-y-6">
              <div className="flex items-center space-x-3">
                <div className="flex h-12 w-12 items-center justify-center rounded-2xl bg-gradient-to-r from-blue-600 to-purple-600">
                  <Zap className="h-6 w-6 text-white" />
                </div>
                <span className="text-2xl font-bold">VoltSphere</span>
              </div>
              <p className="text-gray-400 text-lg leading-relaxed">
                Advanced energy simulation and optimization platform for professionals worldwide.
              </p>
            </div>

            <div>
              <h3 className="font-bold mb-6 text-xl">Product</h3>
              <ul className="space-y-3 text-gray-400">
                <li>
                  <Link href="/simulations" className="hover:text-white transition-smooth text-lg">
                    Simulations
                  </Link>
                </li>
                <li>
                  <Link href="/pricing" className="hover:text-white transition-smooth text-lg">
                    Pricing
                  </Link>
                </li>
              </ul>
            </div>

            <div>
              <h3 className="font-bold mb-6 text-xl">Company</h3>
              <ul className="space-y-3 text-gray-400">
                <li>
                  <Link href="/about" className="hover:text-white transition-smooth text-lg">
                    About
                  </Link>
                </li>
                <li>
                  <Link href="/contact" className="hover:text-white transition-smooth text-lg">
                    Contact
                  </Link>
                </li>
              </ul>
            </div>

            <div>
              <h3 className="font-bold mb-6 text-xl">Support</h3>
              <ul className="space-y-3 text-gray-400">
                <li>
                  <Link href="/help" className="hover:text-white transition-smooth text-lg">
                    Help Center
                  </Link>
                </li>
                <li>
                  <Link href="/docs" className="hover:text-white transition-smooth text-lg">
                    Documentation
                  </Link>
                </li>
              </ul>
            </div>
          </div>

          <div className="border-t border-gray-800 pt-8 text-center text-gray-400">
            <p className="text-lg">&copy; 2024 VoltSphere. All rights reserved.</p>
          </div>
        </div>
      </footer>
    </div>
  )
}


--------------------------------------------------------------------------------
FILE: app/api/auth/login/route.ts
--------------------------------------------------------------------------------
import { NextResponse } from "next/server"
import { authenticateUser } from "@/lib/auth-server"
import jwt from "jsonwebtoken"

const JWT_SECRET = process.env.JWT_SECRET || "your-secret-key-change-in-production"

export async function POST(request: Request) {
  try {
    const { email, password } = await request.json()

    if (!email || !password) {
      return NextResponse.json({ success: false, message: "Email and password are required" }, { status: 400 })
    }

    const user = await authenticateUser(email, password)

    if (!user) {
      return NextResponse.json({ success: false, message: "Invalid email or password" }, { status: 401 })
    }

    // Create JWT token
    const token = jwt.sign({ userId: user.id, email: user.email }, JWT_SECRET, { expiresIn: "7d" })

    // Send confirmation email
    try {
      const emailResponse = await fetch(
        `${process.env.NEXT_PUBLIC_URL || "http://localhost:3000"}/api/auth/send-confirmation`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            email: user.email,
            type: "login",
            name: user.name,
          }),
        },
      )

      if (!emailResponse.ok) {
        console.error("Failed to send login confirmation email")
      } else {
        console.log("Login confirmation email sent successfully")
      }
    } catch (emailError) {
      console.error("Error sending login confirmation email:", emailError)
    }

    const response = NextResponse.json({
      success: true,
      message: "Login successful",
      user: {
        id: user.id,
        name: user.name,
        email: user.email,
        role: user.role,
        subscriptionTier: user.subscriptionTier,
      },
    })

    // Set HTTP-only cookie
    response.cookies.set("auth-token", token, {
      httpOnly: true,
      secure: process.env.NODE_ENV === "production",
      sameSite: "lax",
      maxAge: 60 * 60 * 24 * 7, // 7 days
    })

    return response
  } catch (error) {
    console.error("Login error:", error)
    return NextResponse.json({ success: false, message: "Internal server error" }, { status: 500 })
  }
}


--------------------------------------------------------------------------------
FILE: app/api/auth/logout/route.ts
--------------------------------------------------------------------------------
import { type NextRequest, NextResponse } from "next/server"
import { deleteSession } from "@/lib/auth-server"

export async function POST(request: NextRequest) {
  try {
    // FIXED: Always delete session on logout
    await deleteSession()

    return NextResponse.json({
      success: true,
      message: "Logged out successfully",
    })
  } catch (error) {
    console.error("Logout error:", error)
    // FIXED: Still return success even if error (user should be logged out)
    return NextResponse.json({
      success: true,
      message: "Logged out",
    })
  }
}


--------------------------------------------------------------------------------
FILE: app/api/auth/me/route.ts
--------------------------------------------------------------------------------
import { type NextRequest, NextResponse } from "next/server"
import { getCurrentUser } from "@/lib/auth-server"

export async function GET(request: NextRequest) {
  try {
    // FIXED: Only return user if there's a valid session cookie
    const user = await getCurrentUser()

    if (!user) {
      // FIXED: Return explicit failure when no user found
      return NextResponse.json(
        {
          success: false,
          user: null,
          message: "No active session",
        },
        { status: 401 },
      )
    }

    // FIXED: Only return user data if user exists
    return NextResponse.json({
      success: true,
      user: {
        id: user.id,
        email: user.email,
        name: user.name,
        role: user.role,
        subscriptionTier: user.subscriptionTier,
      },
    })
  } catch (error) {
    console.error("Auth check error:", error)
    // FIXED: Return explicit failure on error
    return NextResponse.json(
      {
        success: false,
        user: null,
        message: "Authentication check failed",
      },
      { status: 500 },
    )
  }
}


--------------------------------------------------------------------------------
FILE: app/api/auth/register/route.ts
--------------------------------------------------------------------------------
import { NextResponse } from "next/server"
import { createUser } from "@/lib/auth-server"
import jwt from "jsonwebtoken"

const JWT_SECRET = process.env.JWT_SECRET || "your-secret-key-change-in-production"

export async function POST(request: Request) {
  try {
    const { name, email, password } = await request.json()

    if (!name || !email || !password) {
      return NextResponse.json({ success: false, message: "Name, email, and password are required" }, { status: 400 })
    }

    // Validate email format
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
    if (!emailRegex.test(email)) {
      return NextResponse.json({ success: false, message: "Invalid email format" }, { status: 400 })
    }

    // Validate password strength
    if (password.length < 6) {
      return NextResponse.json(
        { success: false, message: "Password must be at least 6 characters long" },
        { status: 400 },
      )
    }

    const user = await createUser(name, email, password)

    if (!user) {
      return NextResponse.json({ success: false, message: "User with this email already exists" }, { status: 409 })
    }

    // Create JWT token
    const token = jwt.sign({ userId: user.id, email: user.email }, JWT_SECRET, { expiresIn: "7d" })

    // Send welcome email
    try {
      const emailResponse = await fetch(
        `${process.env.NEXT_PUBLIC_URL || "http://localhost:3000"}/api/auth/send-confirmation`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            email: user.email,
            type: "register",
            name: user.name,
          }),
        },
      )

      if (!emailResponse.ok) {
        console.error("Failed to send welcome email")
      } else {
        console.log("Welcome email sent successfully")
      }
    } catch (emailError) {
      console.error("Error sending welcome email:", emailError)
    }

    const response = NextResponse.json({
      success: true,
      message: "Registration successful",
      user: {
        id: user.id,
        name: user.name,
        email: user.email,
        role: user.role,
        subscriptionTier: user.subscriptionTier,
      },
    })

    // Set HTTP-only cookie
    response.cookies.set("auth-token", token, {
      httpOnly: true,
      secure: process.env.NODE_ENV === "production",
      sameSite: "lax",
      maxAge: 60 * 60 * 24 * 7, // 7 days
    })

    return response
  } catch (error) {
    console.error("Registration error:", error)
    return NextResponse.json({ success: false, message: "Internal server error" }, { status: 500 })
  }
}


--------------------------------------------------------------------------------
FILE: app/api/auth/send-confirmation/route.ts
--------------------------------------------------------------------------------
import { NextResponse } from "next/server"
import { Resend } from "resend"

const resend = new Resend("re_K1BrrnLC_EQYezUg6HguC8RJe9uxyug5m")

export async function POST(request: Request) {
  try {
    const { email, type, name } = await request.json()

    if (!email) {
      return NextResponse.json({ success: false, message: "Email is required" }, { status: 400 })
    }

    let subject = ""
    let htmlContent = ""

    if (type === "login") {
      subject = "VoltSphere - Login Confirmation"
      htmlContent = `
        <!DOCTYPE html>
        <html>
        <head>
          <meta charset="utf-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <title>Login Confirmation</title>
        </head>
        <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 600px; margin: 0 auto; padding: 20px;">
          <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 30px; border-radius: 15px; text-align: center; margin-bottom: 30px;">
            <h1 style="color: white; margin: 0; font-size: 28px;">VoltSphere</h1>
            <p style="color: white; margin: 10px 0 0 0; font-size: 16px;">Energy Simulation Platform</p>
          </div>
          
          <div style="background: #f8f9fa; padding: 30px; border-radius: 15px; border-left: 5px solid #667eea;">
            <h2 style="color: #333; margin-top: 0;">Login Confirmation</h2>
            <p style="font-size: 16px; margin-bottom: 20px;">Hello,</p>
            <p style="font-size: 16px; margin-bottom: 20px;">This email confirms that you have successfully logged in to your VoltSphere account.</p>
            <p style="font-size: 16px; margin-bottom: 20px;">If you did not initiate this login, please contact our support team immediately.</p>
            
            <div style="background: white; padding: 20px; border-radius: 10px; margin: 20px 0;">
              <p style="margin: 0; font-weight: bold; color: #667eea;">Login Time: ${new Date().toLocaleString()}</p>
            </div>
            
            <div style="text-align: center; margin-top: 20px;">
              <a href="https://voltsphere.com/simulation" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 12px 25px; text-decoration: none; border-radius: 8px; font-weight: bold; display: inline-block;">Access Your Account</a>
            </div>
          </div>
          
          <div style="text-align: center; margin-top: 30px; padding: 20px; color: #666;">
            <p>Thank you for using VoltSphere</p>
            <p style="font-size: 14px;">© 2024 VoltSphere. All rights reserved.</p>
          </div>
        </body>
        </html>
      `
    } else if (type === "register") {
      subject = `Welcome to VoltSphere, ${name || "User"}!`
      htmlContent = `
        <!DOCTYPE html>
        <html>
        <head>
          <meta charset="utf-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <title>Welcome to VoltSphere</title>
        </head>
        <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 600px; margin: 0 auto; padding: 20px;">
          <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 30px; border-radius: 15px; text-align: center; margin-bottom: 30px;">
            <h1 style="color: white; margin: 0; font-size: 28px;">VoltSphere</h1>
            <p style="color: white; margin: 10px 0 0 0; font-size: 16px;">Energy Simulation Platform</p>
          </div>
          
          <div style="background: #f8f9fa; padding: 30px; border-radius: 15px; border-left: 5px solid #667eea;">
            <h2 style="color: #333; margin-top: 0;">Welcome to VoltSphere!</h2>
            <p style="font-size: 16px; margin-bottom: 20px;">Hello ${name || "User"},</p>
            <p style="font-size: 16px; margin-bottom: 20px;">Thank you for creating an account with VoltSphere. We're excited to have you on board!</p>
            <p style="font-size: 16px; margin-bottom: 20px;">You can now access our energy simulation tools and start exploring renewable energy solutions.</p>
            
            <div style="background: white; padding: 20px; border-radius: 10px; margin: 20px 0; text-align: center;">
              <a href="https://voltsphere.com/simulation" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 15px 30px; text-decoration: none; border-radius: 8px; font-weight: bold; display: inline-block; margin-bottom: 10px;">Start Your First Simulation</a>
            </div>
            
            <p style="font-size: 16px; margin-bottom: 15px;">What you can do with VoltSphere:</p>
            <ul style="font-size: 16px; padding-left: 20px; margin-bottom: 20px;">
              <li style="margin-bottom: 8px;">Run free energy simulations</li>
              <li style="margin-bottom: 8px;">Analyze renewable energy potential</li>
              <li style="margin-bottom: 8px;">Access professional simulation tools</li>
              <li style="margin-bottom: 8px;">Export detailed reports</li>
            </ul>
            
            <div style="background: #e3f2fd; padding: 15px; border-radius: 8px; margin-top: 20px;">
              <p style="margin: 0; font-size: 14px; color: #1976d2;">
                <strong>Pro Tip:</strong> Start with our free simulation to explore the platform, then upgrade to access advanced features and detailed analytics.
              </p>
            </div>
          </div>
          
          <div style="text-align: center; margin-top: 30px; padding: 20px; color: #666;">
            <p>Thank you for choosing VoltSphere</p>
            <p style="font-size: 14px;">Need help? Contact us at support@voltsphere.com</p>
            <p style="font-size: 14px;">© 2024 VoltSphere. All rights reserved.</p>
          </div>
        </body>
        </html>
      `
    }

    // Send email using Resend
    const { data, error } = await resend.emails.send({
      from: "VoltSphere <onboarding@resend.dev>", // Using Resend's default domain
      to: [email],
      subject: subject,
      html: htmlContent,
    })

    if (error) {
      console.error("Resend error:", error)
      return NextResponse.json(
        {
          success: false,
          message: "Failed to send email",
          error: error,
        },
        { status: 500 },
      )
    }

    console.log("Email sent successfully:", data)

    return NextResponse.json({
      success: true,
      message: "Confirmation email sent successfully",
      emailId: data?.id,
    })
  } catch (error) {
    console.error("Error sending email:", error)
    return NextResponse.json(
      {
        success: false,
        message: "Failed to send email",
      },
      { status: 500 },
    )
  }
}


--------------------------------------------------------------------------------
FILE: app/api/auth/session/route.ts
--------------------------------------------------------------------------------
import { NextResponse } from "next/server"
import { getCurrentUser } from "@/lib/auth-server"

export async function GET() {
  try {
    const user = await getCurrentUser()

    return NextResponse.json(
      {
        user: user || null,
        authenticated: !!user,
      },
      { status: 200 },
    )
  } catch (error) {
    console.error("Session error:", error)
    return NextResponse.json(
      {
        user: null,
        authenticated: false,
        error: "Session check failed",
      },
      { status: 500 },
    )
  }
}


--------------------------------------------------------------------------------
FILE: app/api/checkout/session/route.ts
--------------------------------------------------------------------------------
import { NextResponse } from "next/server"
import { stripe, isStripeConfigured } from "@/lib/stripe"
import { getCurrentUser } from "@/lib/auth-server"

export async function GET(request: Request) {
  try {
    // Check if Stripe is configured
    if (!isStripeConfigured()) {
      return NextResponse.json(
        { error: "Payment processing is not configured. Please contact support." },
        { status: 503 },
      )
    }

    // Ensure user is authenticated
    const user = await getCurrentUser()
    if (!user) {
      return NextResponse.json({ error: "Unauthorized" }, { status: 401 })
    }

    // Get session ID from URL
    const url = new URL(request.url)
    const sessionId = url.searchParams.get("session_id")

    if (!sessionId) {
      return NextResponse.json({ error: "Session ID is required" }, { status: 400 })
    }

    // Retrieve session from Stripe
    const session = await stripe!.checkout.sessions.retrieve(sessionId, {
      expand: ["subscription", "customer"],
    })

    // Extract relevant information
    const subscription = session.subscription as any
    const plan = session.metadata?.tier || "pro"
    const billing = session.metadata?.billing || "monthly"

    return NextResponse.json({
      id: session.id,
      plan: plan.charAt(0).toUpperCase() + plan.slice(1),
      billing: billing.charAt(0).toUpperCase() + billing.slice(1),
      status: subscription?.status || "active",
      currentPeriodEnd: subscription?.current_period_end
        ? new Date(subscription.current_period_end * 1000).toISOString()
        : null,
    })
  } catch (error) {
    console.error("Error retrieving checkout session:", error)
    return NextResponse.json({ error: "Failed to retrieve session details" }, { status: 500 })
  }
}


--------------------------------------------------------------------------------
FILE: app/api/create-checkout-session/route.ts
--------------------------------------------------------------------------------
import { NextResponse } from "next/server"
import { stripe, getPriceId, isStripeConfigured } from "@/lib/stripe"
import { config } from "@/lib/config"
import { getCurrentUser } from "@/lib/auth-server"

export async function POST(request: Request) {
  try {
    // Check if Stripe is configured
    if (!isStripeConfigured()) {
      return NextResponse.json(
        { error: "Payment processing is not configured. Please contact support." },
        { status: 503 },
      )
    }

    // Get the current user
    const user = await getCurrentUser()
    if (!user) {
      return NextResponse.json({ error: "Unauthorized" }, { status: 401 })
    }

    // Parse the request body
    const body = await request.json()
    const { tier = "pro", billing = "monthly" } = body

    // Get the price ID for the selected tier and billing interval
    const priceId = getPriceId(tier, billing)
    if (!priceId) {
      return NextResponse.json({ error: "Invalid tier or billing interval" }, { status: 400 })
    }

    // Create a checkout session
    const session = await stripe!.checkout.sessions.create({
      payment_method_types: ["card"],
      billing_address_collection: "auto",
      customer_email: user.email,
      line_items: [
        {
          price: priceId,
          quantity: 1,
        },
      ],
      mode: "subscription",
      allow_promotion_codes: true,
      success_url: `${config.url}/billing/success?session_id={CHECKOUT_SESSION_ID}`,
      cancel_url: `${config.url}/pricing`,
      metadata: {
        userId: user.id,
        tier,
        billing,
      },
    })

    return NextResponse.json({ url: session.url })
  } catch (error) {
    console.error("Error creating checkout session:", error)
    return NextResponse.json({ error: "Failed to create checkout session" }, { status: 500 })
  }
}


--------------------------------------------------------------------------------
FILE: app/api/create-portal-session/route.ts
--------------------------------------------------------------------------------
import { NextResponse } from "next/server"
import { stripe, isStripeConfigured } from "@/lib/stripe"
import { config } from "@/lib/config"
import { getCurrentUser } from "@/lib/auth-server"

export async function POST(request: Request) {
  try {
    // Check if Stripe is configured
    if (!isStripeConfigured()) {
      return NextResponse.json(
        { error: "Payment processing is not configured. Please contact support." },
        { status: 503 },
      )
    }

    // Get the current user
    const user = await getCurrentUser()
    if (!user) {
      return NextResponse.json({ error: "Unauthorized" }, { status: 401 })
    }

    // Parse the request body
    const body = await request.json()
    const { customerId } = body

    if (!customerId) {
      return NextResponse.json({ error: "Customer ID is required" }, { status: 400 })
    }

    // Create a billing portal session
    const session = await stripe!.billingPortal.sessions.create({
      customer: customerId,
      return_url: `${config.url}/billing`,
    })

    return NextResponse.json({ url: session.url })
  } catch (error) {
    console.error("Error creating portal session:", error)
    return NextResponse.json({ error: "Failed to create portal session" }, { status: 500 })
  }
}


--------------------------------------------------------------------------------
FILE: app/api/locations/route.ts
--------------------------------------------------------------------------------
import { type NextRequest, NextResponse } from "next/server"

export async function GET(request: NextRequest) {
  try {
    // Check API key
    const authHeader = request.headers.get("authorization")
    if (!authHeader || !authHeader.startsWith("Bearer ")) {
      return NextResponse.json({ error: "Missing or invalid API key" }, { status: 401 })
    }

    const locations = [
      {
        id: "san-francisco",
        name: "San Francisco, CA",
        coordinates: { lat: 37.7749, lng: -122.4194 },
        timezone: "America/Los_Angeles",
        weatherSupport: true,
      },
      {
        id: "new-york",
        name: "New York, NY",
        coordinates: { lat: 40.7128, lng: -74.006 },
        timezone: "America/New_York",
        weatherSupport: true,
      },
      {
        id: "austin",
        name: "Austin, TX",
        coordinates: { lat: 30.2672, lng: -97.7431 },
        timezone: "America/Chicago",
        weatherSupport: true,
      },
      {
        id: "denver",
        name: "Denver, CO",
        coordinates: { lat: 39.7392, lng: -104.9903 },
        timezone: "America/Denver",
        weatherSupport: true,
      },
      {
        id: "phoenix",
        name: "Phoenix, AZ",
        coordinates: { lat: 33.4484, lng: -112.074 },
        timezone: "America/Phoenix",
        weatherSupport: true,
      },
      {
        id: "seattle",
        name: "Seattle, WA",
        coordinates: { lat: 47.6062, lng: -122.3321 },
        timezone: "America/Los_Angeles",
        weatherSupport: true,
      },
    ]

    return NextResponse.json({
      locations,
      total: locations.length,
      weatherEnabled: true,
    })
  } catch (error) {
    console.error("API locations error:", error)
    return NextResponse.json({ error: "Internal server error" }, { status: 500 })
  }
}


--------------------------------------------------------------------------------
FILE: app/api/simulate/route.ts
--------------------------------------------------------------------------------
import { type NextRequest, NextResponse } from "next/server"
import { SimulationEngine, type SimulationConfig } from "@/lib/simulation/engine"

export async function POST(request: NextRequest) {
  try {
    // Check API key
    const authHeader = request.headers.get("authorization")
    if (!authHeader || !authHeader.startsWith("Bearer ")) {
      return NextResponse.json({ error: "Missing or invalid API key" }, { status: 401 })
    }

    const apiKey = authHeader.substring(7)

    // In production, validate API key against database
    if (!apiKey.startsWith("vs_")) {
      return NextResponse.json({ error: "Invalid API key format" }, { status: 401 })
    }

    // Parse request body
    const body = await request.json()

    // Validate required fields
    const requiredFields = ["batteryCapacity", "batteryEfficiency", "solarEnabled"]
    for (const field of requiredFields) {
      if (!(field in body)) {
        return NextResponse.json({ error: `Missing required field: ${field}` }, { status: 400 })
      }
    }

    // Create simulation config
    const config: SimulationConfig = {
      batteryCapacity: body.batteryCapacity,
      batteryEfficiency: body.batteryEfficiency,
      solarEnabled: body.solarEnabled,
      batteryType: body.batteryType || "lithium",
      loadProfileType: body.loadProfile || "default",
      useRealWeather: body.weatherEnabled || false,
      weatherLocation: body.location ? `${body.location.lat},${body.location.lng}` : undefined,
      timeOfUseRates: body.timeOfUseRates || false,
      location: body.location,
      equipmentSpecs: body.equipmentSpecs,
      economicParams: body.economicParams,
    }

    // Run simulation
    const results = await SimulationEngine.runSimulation(config)

    // Format response
    const response = {
      simulationId: `sim_${Date.now()}`,
      timestamp: new Date().toISOString(),
      input: config,
      results: {
        energyFlow: {
          solar: results.solarProfile,
          load: results.loadProfile,
          battery: results.batteryStorage,
          grid: results.gridUsage,
        },
        economics: {
          dailyCost: results.costAnalysis.netCost,
          monthlyCost: results.costAnalysis.netCost * 30,
          annualCost: results.costAnalysis.netCost * 365,
          savings: results.costAnalysis.solarSavings + results.costAnalysis.batterySavings,
          paybackPeriod: results.costAnalysis.paybackPeriod,
          roi: results.costAnalysis.irr * 100,
        },
        environmental: {
          co2Saved: results.solarProfile.reduce((sum, solar) => sum + solar, 0) * 0.5, // kg CO2
          treesEquivalent: results.solarProfile.reduce((sum, solar) => sum + solar, 0) * 0.02,
        },
        weather: results.weatherData,
      },
      metadata: {
        processingTime: "1.2s",
        version: "v2.1.0",
      },
    }

    return NextResponse.json(response)
  } catch (error) {
    console.error("API simulation error:", error)
    return NextResponse.json({ error: "Internal server error" }, { status: 500 })
  }
}

export async function GET() {
  return NextResponse.json({
    message: "VoltSphere Microgrid Simulation API",
    version: "v2.1.0",
    endpoints: {
      "POST /api/simulate": "Run microgrid simulation",
      "GET /api/usage": "Get API usage statistics",
      "GET /api/locations": "Get supported locations",
    },
  })
}


--------------------------------------------------------------------------------
FILE: app/api/usage/route.ts
--------------------------------------------------------------------------------
import { type NextRequest, NextResponse } from "next/server"

export async function GET(request: NextRequest) {
  try {
    // Check API key
    const authHeader = request.headers.get("authorization")
    if (!authHeader || !authHeader.startsWith("Bearer ")) {
      return NextResponse.json({ error: "Missing or invalid API key" }, { status: 401 })
    }

    const apiKey = authHeader.substring(7)

    // In production, get actual usage from database
    // For demo, return mock data
    const usage = {
      apiKey: apiKey.substring(0, 8) + "...",
      tier: apiKey.includes("starter") ? "starter" : "growth",
      currentPeriod: {
        start: "2024-01-01T00:00:00Z",
        end: "2024-01-31T23:59:59Z",
        callsUsed: Math.floor(Math.random() * 1000),
        callsRemaining: 5000 - Math.floor(Math.random() * 1000),
        limit: 5000,
      },
      lastCall: new Date().toISOString(),
      endpoints: {
        "/api/simulate": Math.floor(Math.random() * 800),
        "/api/usage": Math.floor(Math.random() * 50),
        "/api/locations": Math.floor(Math.random() * 20),
      },
    }

    return NextResponse.json(usage)
  } catch (error) {
    console.error("API usage error:", error)
    return NextResponse.json({ error: "Internal server error" }, { status: 500 })
  }
}


--------------------------------------------------------------------------------
FILE: app/api/webhooks/stripe/route.ts
--------------------------------------------------------------------------------
import { NextResponse } from "next/server"
import { stripe, webhookSecret, isStripeConfigured } from "@/lib/stripe"
import { headers } from "next/headers"

export async function POST(request: Request) {
  try {
    // Check if Stripe is configured
    if (!isStripeConfigured() || !webhookSecret) {
      console.log("Stripe not configured or webhook secret missing")
      return NextResponse.json({ received: false }, { status: 503 })
    }

    const body = await request.text()
    const signature = headers().get("stripe-signature") as string

    let event

    try {
      event = stripe!.webhooks.constructEvent(body, signature, webhookSecret)
    } catch (err: any) {
      console.error(`Webhook signature verification failed: ${err.message}`)
      return NextResponse.json({ error: err.message }, { status: 400 })
    }

    // Handle the event
    switch (event.type) {
      case "checkout.session.completed":
        const session = event.data.object as any
        console.log(`Checkout session completed: ${session.id}`)

        // Here you would typically update your database with the subscription info
        // For example, update the user's subscription status, tier, etc.

        break
      case "customer.subscription.updated":
      case "customer.subscription.deleted":
        const subscription = event.data.object as any
        console.log(`Subscription ${event.type}: ${subscription.id}`)

        // Update the subscription status in your database

        break
      default:
        console.log(`Unhandled event type: ${event.type}`)
    }

    return NextResponse.json({ received: true })
  } catch (error) {
    console.error("Error handling webhook:", error)
    return NextResponse.json({ error: "Webhook handler failed" }, { status: 500 })
  }
}


--------------------------------------------------------------------------------
FILE: app/billing/page.tsx
--------------------------------------------------------------------------------
"use client"

import { useState } from "react"
import Link from "next/link"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Progress } from "@/components/ui/progress"
import { CreditCard, Download, Zap, TrendingUp, Settings, ExternalLink } from "lucide-react"

// Mock user data - replace with actual user context
const mockUser = {
  email: "user@example.com",
  subscription: {
    tier: "pro" as const,
    status: "active" as const,
    currentPeriodStart: new Date("2024-01-01"),
    currentPeriodEnd: new Date("2024-02-01"),
    cancelAtPeriodEnd: false,
    stripeCustomerId: "cus_example123",
  },
  usage: {
    simulationsToday: 15,
    simulationsThisMonth: 245,
    apiCallsThisMonth: 0,
  },
}

export default function BillingPage() {
  const [isLoading, setIsLoading] = useState(false)
  const [user] = useState(mockUser) // Replace with actual user context

  const handleManageSubscription = async () => {
    setIsLoading(true)

    try {
      const response = await fetch("/api/create-portal-session", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          customerId: user.subscription.stripeCustomerId,
        }),
      })

      const { url, error } = await response.json()

      if (error) {
        throw new Error(error)
      }

      if (url) {
        window.location.href = url
      }
    } catch (error) {
      console.error("Error creating portal session:", error)
      alert("Failed to open billing portal. Please try again.")
    } finally {
      setIsLoading(false)
    }
  }

  const getStatusColor = (status: string) => {
    switch (status) {
      case "active":
        return "bg-green-100 text-green-800"
      case "past_due":
        return "bg-yellow-100 text-yellow-800"
      case "canceled":
        return "bg-red-100 text-red-800"
      default:
        return "bg-gray-100 text-gray-800"
    }
  }

  const getTierName = (tier: string) => {
    switch (tier) {
      case "pro":
        return "Pro Tier"
      case "starter":
        return "Starter API"
      case "growth":
        return "Growth API"
      case "enterprise":
        return "Enterprise"
      default:
        return "Free Tier"
    }
  }

  const simulationLimit = user.subscription.tier === "free" ? 3 : -1
  const simulationProgress = simulationLimit > 0 ? (user.usage.simulationsToday / simulationLimit) * 100 : 0

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-50 to-blue-50 animate-fade-in">
      {/* Header */}
      <header className="glass-effect border-b sticky top-0 z-40 backdrop-enhanced">
        <nav className="container mx-auto mobile-padding py-3 sm:py-4 flex justify-between items-center">
          <Link
            href="/"
            className="text-xl sm:text-2xl font-bold gradient-text hover:scale-105 transition-transform duration-300 font-display"
          >
            VoltSphere
          </Link>
          <div className="hidden md:flex gap-6 lg:gap-8">
            <Link href="/" className="text-gray-700 hover:text-blue-600 transition-colors font-medium">
              Home
            </Link>
            <Link href="/simulation" className="text-gray-700 hover:text-blue-600 transition-colors font-medium">
              Simulation
            </Link>
            <span className="text-blue-600 font-semibold">Billing</span>
          </div>
        </nav>
      </header>

      <div className="container mx-auto mobile-padding py-12 sm:py-16">
        {/* Page Header */}
        <div className="mb-8 sm:mb-12">
          <h1 className="mobile-heading-xl mb-4 text-gray-800 font-display">Billing & Usage</h1>
          <p className="mobile-body-lg text-gray-600">Manage your subscription and monitor your usage</p>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 lg:gap-8">
          {/* Current Plan */}
          <div className="lg:col-span-2 space-y-6">
            <Card className="card-enhanced">
              <CardHeader>
                <CardTitle className="flex items-center gap-3 mobile-heading-md font-display">
                  <CreditCard className="h-6 w-6 text-blue-600" />
                  Current Plan
                </CardTitle>
              </CardHeader>
              <CardContent className="space-y-6">
                <div className="flex items-center justify-between">
                  <div>
                    <h3 className="text-2xl font-bold text-gray-800 font-display">
                      {getTierName(user.subscription.tier)}
                    </h3>
                    <p className="text-gray-600 mobile-body-md">
                      {user.subscription.tier === "free" ? "Free forever" : "$5.99/month"}
                    </p>
                  </div>
                  <Badge className={getStatusColor(user.subscription.status)}>
                    {user.subscription.status.charAt(0).toUpperCase() + user.subscription.status.slice(1)}
                  </Badge>
                </div>

                {user.subscription.tier !== "free" && (
                  <div className="space-y-2">
                    <div className="flex justify-between text-sm">
                      <span className="text-gray-600">Current billing period</span>
                      <span className="font-medium">
                        {user.subscription.currentPeriodStart.toLocaleDateString()} -{" "}
                        {user.subscription.currentPeriodEnd.toLocaleDateString()}
                      </span>
                    </div>
                    {user.subscription.cancelAtPeriodEnd && (
                      <p className="text-yellow-600 text-sm font-medium">
                        Your subscription will cancel on {user.subscription.currentPeriodEnd.toLocaleDateString()}
                      </p>
                    )}
                  </div>
                )}

                <div className="flex gap-4">
                  {user.subscription.tier === "free" ? (
                    <Link href="/pricing">
                      <Button className="bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700 mobile-btn mobile-rounded font-semibold touch-target">
                        Upgrade Plan
                      </Button>
                    </Link>
                  ) : (
                    <>
                      <Button
                        onClick={handleManageSubscription}
                        disabled={isLoading}
                        className="mobile-btn mobile-rounded font-semibold touch-target"
                      >
                        <Settings className="h-4 w-4 mr-2" />
                        {isLoading ? "Loading..." : "Manage Subscription"}
                      </Button>
                      <Link href="/pricing">
                        <Button variant="outline" className="mobile-btn mobile-rounded font-semibold touch-target">
                          Change Plan
                        </Button>
                      </Link>
                    </>
                  )}
                </div>
              </CardContent>
            </Card>

            {/* Usage Statistics */}
            <Card className="card-enhanced">
              <CardHeader>
                <CardTitle className="flex items-center gap-3 mobile-heading-md font-display">
                  <TrendingUp className="h-6 w-6 text-green-600" />
                  Usage This Month
                </CardTitle>
              </CardHeader>
              <CardContent className="space-y-6">
                {/* Simulations */}
                <div>
                  <div className="flex justify-between items-center mb-2">
                    <span className="font-medium text-gray-700">Daily Simulations</span>
                    <span className="text-sm text-gray-600">
                      {user.usage.simulationsToday}
                      {simulationLimit > 0 ? ` / ${simulationLimit}` : ""}
                    </span>
                  </div>
                  {simulationLimit > 0 && <Progress value={simulationProgress} className="h-2" />}
                  <p className="text-xs text-gray-500 mt-1">
                    {simulationLimit > 0
                      ? `${simulationLimit - user.usage.simulationsToday} simulations remaining today`
                      : "Unlimited simulations"}
                  </p>
                </div>

                <div>
                  <div className="flex justify-between items-center mb-2">
                    <span className="font-medium text-gray-700">Monthly Simulations</span>
                    <span className="text-sm text-gray-600">{user.usage.simulationsThisMonth}</span>
                  </div>
                </div>

                {user.subscription.tier !== "free" && user.subscription.tier !== "pro" && (
                  <div>
                    <div className="flex justify-between items-center mb-2">
                      <span className="font-medium text-gray-700">API Calls</span>
                      <span className="text-sm text-gray-600">
                        {user.usage.apiCallsThisMonth} / {user.subscription.tier === "starter" ? "5,000" : "50,000"}
                      </span>
                    </div>
                    <Progress
                      value={
                        (user.usage.apiCallsThisMonth / (user.subscription.tier === "starter" ? 5000 : 50000)) * 100
                      }
                      className="h-2"
                    />
                  </div>
                )}
              </CardContent>
            </Card>
          </div>

          {/* Quick Actions */}
          <div className="space-y-6">
            <Card className="card-enhanced">
              <CardHeader>
                <CardTitle className="mobile-heading-md font-display">Quick Actions</CardTitle>
              </CardHeader>
              <CardContent className="space-y-4">
                <Link href="/simulation">
                  <Button variant="outline" className="w-full justify-start mobile-btn mobile-rounded touch-target">
                    <Zap className="h-4 w-4 mr-2" />
                    Run Simulation
                  </Button>
                </Link>

                {user.subscription.tier !== "free" && (
                  <Button variant="outline" className="w-full justify-start mobile-btn mobile-rounded touch-target">
                    <Download className="h-4 w-4 mr-2" />
                    Download Reports
                  </Button>
                )}

                <Link href="/pricing">
                  <Button variant="outline" className="w-full justify-start mobile-btn mobile-rounded touch-target">
                    <ExternalLink className="h-4 w-4 mr-2" />
                    View All Plans
                  </Button>
                </Link>
              </CardContent>
            </Card>

            {/* Plan Features */}
            <Card className="card-enhanced">
              <CardHeader>
                <CardTitle className="mobile-heading-md font-display">Your Plan Includes</CardTitle>
              </CardHeader>
              <CardContent className="space-y-3">
                {user.subscription.tier === "free" ? (
                  <>
                    <div className="flex items-center gap-2">
                      <div className="w-2 h-2 bg-green-500 rounded-full"></div>
                      <span className="text-sm">3 simulations per day</span>
                    </div>
                    <div className="flex items-center gap-2">
                      <div className="w-2 h-2 bg-green-500 rounded-full"></div>
                      <span className="text-sm">Basic solar/load profiles</span>
                    </div>
                    <div className="flex items-center gap-2">
                      <div className="w-2 h-2 bg-gray-300 rounded-full"></div>
                      <span className="text-sm text-gray-500">No data export</span>
                    </div>
                  </>
                ) : (
                  <>
                    <div className="flex items-center gap-2">
                      <div className="w-2 h-2 bg-green-500 rounded-full"></div>
                      <span className="text-sm">Unlimited simulations</span>
                    </div>
                    <div className="flex items-center gap-2">
                      <div className="w-2 h-2 bg-green-500 rounded-full"></div>
                      <span className="text-sm">Data export (CSV/PNG)</span>
                    </div>
                    <div className="flex items-center gap-2">
                      <div className="w-2 h-2 bg-green-500 rounded-full"></div>
                      <span className="text-sm">Save projects</span>
                    </div>
                    <div className="flex items-center gap-2">
                      <div className="w-2 h-2 bg-green-500 rounded-full"></div>
                      <span className="text-sm">Priority support</span>
                    </div>
                  </>
                )}
              </CardContent>
            </Card>
          </div>
        </div>
      </div>
    </div>
  )
}


--------------------------------------------------------------------------------
FILE: app/billing/success/loading.tsx
--------------------------------------------------------------------------------
export default function Loading() {
  return null
}


--------------------------------------------------------------------------------
FILE: app/billing/success/page.tsx
--------------------------------------------------------------------------------
"use client"

import { useEffect, useState } from "react"
import { useSearchParams } from "next/navigation"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { CheckCircle, ArrowRight } from "lucide-react"
import Link from "next/link"

export default function SuccessPage() {
  const searchParams = useSearchParams()
  const sessionId = searchParams.get("session_id")
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState("")
  const [subscription, setSubscription] = useState<any>(null)

  useEffect(() => {
    if (!sessionId) {
      setError("No session ID provided")
      setLoading(false)
      return
    }

    async function fetchSessionDetails() {
      try {
        const response = await fetch(`/api/checkout/session?session_id=${sessionId}`)

        if (!response.ok) {
          throw new Error("Failed to fetch session details")
        }

        const data = await response.json()
        setSubscription(data)
      } catch (err) {
        console.error("Error fetching session:", err)
        setError("Failed to load subscription details")
      } finally {
        setLoading(false)
      }
    }

    fetchSessionDetails()
  }, [sessionId])

  if (loading) {
    return (
      <div className="min-h-screen bg-gradient-primary flex items-center justify-center">
        <Card className="w-full max-w-md">
          <CardContent className="pt-10 pb-10 text-center">
            <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto mb-6"></div>
            <p className="text-lg text-gray-600">Loading your subscription details...</p>
          </CardContent>
        </Card>
      </div>
    )
  }

  if (error) {
    return (
      <div className="min-h-screen bg-gradient-primary flex items-center justify-center p-4">
        <Card className="w-full max-w-md">
          <CardHeader>
            <CardTitle className="text-2xl font-bold text-center">Something went wrong</CardTitle>
            <CardDescription className="text-center">{error}</CardDescription>
          </CardHeader>
          <CardContent className="text-center pt-4">
            <Button asChild className="mt-4">
              <Link href="/pricing">Return to Pricing</Link>
            </Button>
          </CardContent>
        </Card>
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-gradient-primary flex items-center justify-center p-4">
      <Card className="w-full max-w-2xl">
        <CardHeader className="text-center pb-8">
          <div className="mx-auto bg-green-100 p-4 rounded-full w-20 h-20 flex items-center justify-center mb-6">
            <CheckCircle className="h-12 w-12 text-green-600" />
          </div>
          <CardTitle className="text-3xl font-bold">Subscription Activated!</CardTitle>
          <CardDescription className="text-lg mt-2">
            Thank you for subscribing to VoltSphere. Your account has been upgraded.
          </CardDescription>
        </CardHeader>

        <CardContent className="space-y-8 pb-8">
          <div className="bg-gray-50 p-6 rounded-xl border border-gray-100">
            <h3 className="font-semibold text-lg mb-4">Subscription Details</h3>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div>
                <p className="text-sm text-gray-500">Plan</p>
                <p className="font-medium">{subscription?.plan || "Pro"}</p>
              </div>
              <div>
                <p className="text-sm text-gray-500">Billing</p>
                <p className="font-medium">{subscription?.billing || "Monthly"}</p>
              </div>
              <div>
                <p className="text-sm text-gray-500">Status</p>
                <p className="font-medium text-green-600">Active</p>
              </div>
              <div>
                <p className="text-sm text-gray-500">Next Steps</p>
                <p className="font-medium">Check your email for confirmation</p>
              </div>
            </div>
          </div>

          <div className="text-center space-y-4">
            <p className="text-gray-600">
              We've sent a confirmation email to your inbox with all the details of your subscription.
            </p>

            <div className="flex flex-col sm:flex-row gap-4 justify-center pt-4">
              <Button asChild size="lg" className="bg-gradient-to-r from-blue-600 to-purple-600">
                <Link href="/simulation">
                  Start Simulating
                  <ArrowRight className="ml-2 h-4 w-4" />
                </Link>
              </Button>

              <Button asChild variant="outline" size="lg">
                <Link href="/profile">View Account</Link>
              </Button>
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  )
}


--------------------------------------------------------------------------------
FILE: app/contact/page.tsx
--------------------------------------------------------------------------------
"use client"

import type React from "react"

import { useState } from "react"
import Link from "next/link"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Textarea } from "@/components/ui/textarea"
import { Label } from "@/components/ui/label"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { SiteHeader } from "@/components/site-header"
import { Mail, Phone, Clock, ArrowRight, Zap } from "lucide-react"

export default function ContactPage() {
  const [formData, setFormData] = useState({
    firstName: "",
    lastName: "",
    email: "",
    message: "",
  })

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    alert("Thank you for your message! We'll get back to you within 1-2 business days.")
    setFormData({ firstName: "", lastName: "", email: "", message: "" })
  }

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    setFormData((prev) => ({
      ...prev,
      [e.target.name]: e.target.value,
    }))
  }

  return (
    <div className="min-h-screen bg-white">
      <SiteHeader />

      {/* Hero Section */}
      <section className="section-spacing bg-gradient-to-r from-blue-600 to-purple-600 text-white">
        <div className="container-clean text-center">
          <h1 className="text-4xl lg:text-5xl font-bold mb-6">Contact Us</h1>
          <p className="text-xl max-w-2xl mx-auto opacity-90">
            Have questions or need support? We're here to help you succeed with VoltSphere.
          </p>
        </div>
      </section>

      {/* Contact Info */}
      <section className="section-spacing-sm bg-gray-50">
        <div className="container-clean">
          <div className="grid md:grid-cols-3 gap-8 max-w-4xl mx-auto">
            <Card className="card-clean text-center">
              <CardHeader>
                <div className="flex justify-center mb-4">
                  <div className="w-12 h-12 bg-blue-100 rounded-xl flex items-center justify-center">
                    <Clock className="h-6 w-6 text-blue-600" />
                  </div>
                </div>
                <CardTitle className="text-lg">Response Time</CardTitle>
              </CardHeader>
              <CardContent>
                <p className="text-gray-600">1-2 business days</p>
              </CardContent>
            </Card>

            <Card className="card-clean text-center">
              <CardHeader>
                <div className="flex justify-center mb-4">
                  <div className="w-12 h-12 bg-blue-100 rounded-xl flex items-center justify-center">
                    <Mail className="h-6 w-6 text-blue-600" />
                  </div>
                </div>
                <CardTitle className="text-lg">Email</CardTitle>
              </CardHeader>
              <CardContent>
                <p className="text-gray-600">voltsphere.sim@gmail.com</p>
              </CardContent>
            </Card>

            <Card className="card-clean text-center">
              <CardHeader>
                <div className="flex justify-center mb-4">
                  <div className="w-12 h-12 bg-blue-100 rounded-xl flex items-center justify-center">
                    <Phone className="h-6 w-6 text-blue-600" />
                  </div>
                </div>
                <CardTitle className="text-lg">Phone</CardTitle>
              </CardHeader>
              <CardContent>
                <p className="text-gray-600">(630) 780-0523</p>
              </CardContent>
            </Card>
          </div>
        </div>
      </section>

      {/* Contact Form */}
      <section className="section-spacing">
        <div className="container-clean">
          <div className="max-w-2xl mx-auto">
            <Card className="card-clean">
              <CardHeader className="text-center">
                <CardTitle className="text-2xl">Send us a Message</CardTitle>
                <p className="text-gray-600 mt-2">
                  Fill out the form below and we'll get back to you as soon as possible.
                </p>
              </CardHeader>
              <CardContent>
                <form onSubmit={handleSubmit} className="space-y-6">
                  <div className="grid md:grid-cols-2 gap-4">
                    <div>
                      <Label htmlFor="firstName" className="text-sm font-medium text-gray-700">
                        First Name
                      </Label>
                      <Input
                        id="firstName"
                        name="firstName"
                        value={formData.firstName}
                        onChange={handleChange}
                        required
                        className="input-clean mt-1"
                      />
                    </div>
                    <div>
                      <Label htmlFor="lastName" className="text-sm font-medium text-gray-700">
                        Last Name
                      </Label>
                      <Input
                        id="lastName"
                        name="lastName"
                        value={formData.lastName}
                        onChange={handleChange}
                        required
                        className="input-clean mt-1"
                      />
                    </div>
                  </div>

                  <div>
                    <Label htmlFor="email" className="text-sm font-medium text-gray-700">
                      Email
                    </Label>
                    <Input
                      id="email"
                      name="email"
                      type="email"
                      value={formData.email}
                      onChange={handleChange}
                      required
                      className="input-clean mt-1"
                    />
                  </div>

                  <div>
                    <Label htmlFor="message" className="text-sm font-medium text-gray-700">
                      Message
                    </Label>
                    <Textarea
                      id="message"
                      name="message"
                      value={formData.message}
                      onChange={handleChange}
                      rows={5}
                      required
                      className="input-clean mt-1 resize-none"
                    />
                  </div>

                  <Button type="submit" className="w-full btn-primary">
                    Send Message
                    <ArrowRight className="ml-2 h-4 w-4" />
                  </Button>
                </form>
              </CardContent>
            </Card>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-gray-900 text-white section-spacing-sm">
        <div className="container-clean">
          <div className="grid md:grid-cols-4 gap-8 mb-8">
            <div className="space-y-4">
              <div className="flex items-center space-x-2">
                <div className="flex h-8 w-8 items-center justify-center rounded-lg bg-gradient-to-r from-blue-600 to-purple-600">
                  <Zap className="h-4 w-4 text-white" />
                </div>
                <span className="text-lg font-bold">VoltSphere</span>
              </div>
              <p className="text-gray-400">Advanced energy simulation and optimization platform for professionals.</p>
            </div>

            <div>
              <h3 className="font-semibold mb-4">Product</h3>
              <ul className="space-y-2 text-gray-400">
                <li>
                  <Link href="/simulations" className="hover:text-white transition-smooth">
                    Simulations
                  </Link>
                </li>
                <li>
                  <Link href="/pricing" className="hover:text-white transition-smooth">
                    Pricing
                  </Link>
                </li>
              </ul>
            </div>

            <div>
              <h3 className="font-semibold mb-4">Company</h3>
              <ul className="space-y-2 text-gray-400">
                <li>
                  <Link href="/about" className="hover:text-white transition-smooth">
                    About
                  </Link>
                </li>
                <li>
                  <Link href="/contact" className="hover:text-white transition-smooth">
                    Contact
                  </Link>
                </li>
              </ul>
            </div>

            <div>
              <h3 className="font-semibold mb-4">Support</h3>
              <ul className="space-y-2 text-gray-400">
                <li>
                  <Link href="/help" className="hover:text-white transition-smooth">
                    Help Center
                  </Link>
                </li>
                <li>
                  <Link href="/docs" className="hover:text-white transition-smooth">
                    Documentation
                  </Link>
                </li>
              </ul>
            </div>
          </div>

          <div className="border-t border-gray-800 pt-8 text-center text-gray-400">
            <p>&copy; 2024 VoltSphere. All rights reserved.</p>
          </div>
        </div>
      </footer>
    </div>
  )
}


--------------------------------------------------------------------------------
FILE: app/globals.css
--------------------------------------------------------------------------------
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  :root {
    --background: 0 0% 100%;
    --foreground: 222.2 84% 4.9%;
    --card: 0 0% 100%;
    --card-foreground: 222.2 84% 4.9%;
    --popover: 0 0% 100%;
    --popover-foreground: 222.2 84% 4.9%;
    --primary: 221.2 83.2% 53.3%;
    --primary-foreground: 210 40% 98%;
    --secondary: 210 40% 96%;
    --secondary-foreground: 222.2 84% 4.9%;
    --muted: 210 40% 96%;
    --muted-foreground: 215.4 16.3% 46.9%;
    --accent: 210 40% 96%;
    --accent-foreground: 222.2 84% 4.9%;
    --destructive: 0 84.2% 60.2%;
    --destructive-foreground: 210 40% 98%;
    --border: 214.3 31.8% 91.4%;
    --input: 214.3 31.8% 91.4%;
    --ring: 221.2 83.2% 53.3%;
    --chart-1: 12 76% 61%;
    --chart-2: 173 58% 39%;
    --chart-3: 197 37% 24%;
    --chart-4: 43 74% 66%;
    --chart-5: 27 87% 67%;
    --radius: 1rem;
    --sidebar-background: 0 0% 98%;
    --sidebar-foreground: 240 5.3% 26.1%;
    --sidebar-primary: 240 5.9% 10%;
    --sidebar-primary-foreground: 0 0% 98%;
    --sidebar-accent: 240 4.8% 95.9%;
    --sidebar-accent-foreground: 240 5.9% 10%;
    --sidebar-border: 220 13% 91%;
    --sidebar-ring: 217.2 91.2% 59.8%;
  }

  .dark {
    --background: 222.2 84% 4.9%;
    --foreground: 210 40% 98%;
    --card: 222.2 84% 4.9%;
    --card-foreground: 210 40% 98%;
    --popover: 222.2 84% 4.9%;
    --popover-foreground: 210 40% 98%;
    --primary: 217.2 91.2% 59.8%;
    --primary-foreground: 222.2 84% 4.9%;
    --secondary: 217.2 32.6% 17.5%;
    --secondary-foreground: 210 40% 98%;
    --muted: 217.2 32.6% 17.5%;
    --muted-foreground: 215 20.2% 65.1%;
    --accent: 217.2 32.6% 17.5%;
    --accent-foreground: 210 40% 98%;
    --destructive: 0 62.8% 30.6%;
    --destructive-foreground: 210 40% 98%;
    --border: 217.2 32.6% 17.5%;
    --input: 217.2 32.6% 17.5%;
    --ring: 224.3 76.3% 94.1%;
    --chart-1: 220 70% 50%;
    --chart-2: 160 60% 45%;
    --chart-3: 30 80% 55%;
    --chart-4: 280 65% 60%;
    --chart-5: 340 75% 55%;
    --sidebar-background: 240 5.9% 10%;
    --sidebar-foreground: 240 4.8% 95.9%;
    --sidebar-primary: 224.3 76.3% 48%;
    --sidebar-primary-foreground: 0 0% 100%;
    --sidebar-accent: 240 3.7% 15.9%;
    --sidebar-accent-foreground: 240 4.8% 95.9%;
    --sidebar-border: 240 3.7% 15.9%;
    --sidebar-ring: 217.2 91.2% 59.8%;
  }
}

@layer base {
  * {
    @apply border-border;
  }

  body {
    @apply bg-gradient-to-br from-slate-50 via-blue-50 to-purple-50 text-gray-900;
    font-family: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  }
}

html {
  scroll-behavior: smooth;
  scroll-padding-top: 80px;
}

@layer utilities {
  /* Animation utilities */
  .animate-fade-in {
    animation: fadeIn 0.8s cubic-bezier(0.4, 0, 0.2, 1) forwards;
  }

  .animate-slide-up {
    animation: slideUp 1s cubic-bezier(0.4, 0, 0.2, 1) forwards;
  }

  .animate-scale-in {
    animation: scaleIn 0.6s cubic-bezier(0.4, 0, 0.2, 1) forwards;
  }

  .animate-float {
    animation: float 4s ease-in-out infinite;
  }

  /* Transition utilities */
  .transition-smooth {
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  }

  .transition-transform-smooth {
    transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  }

  /* Hover effects */
  .hover-lift {
    @apply transition-smooth hover:scale-105 hover:shadow-xl;
  }

  .hover-lift-subtle {
    @apply transition-smooth hover:scale-[1.02] hover:shadow-lg;
  }

  /* Card styles */
  .card-clean {
    @apply bg-white/90 backdrop-blur-sm border border-gray-200/50 rounded-3xl shadow-lg hover:shadow-xl transition-smooth;
  }

  .card-interactive {
    @apply card-clean cursor-pointer hover:scale-105 hover:border-blue-300/50;
  }

  .card-enhanced {
    @apply bg-white/95 backdrop-blur-md border border-gray-200/60 rounded-3xl shadow-xl hover:shadow-2xl transition-smooth;
  }

  /* Button styles */
  .btn-primary {
    @apply bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700 text-white font-semibold px-8 py-4 rounded-2xl shadow-lg hover:shadow-xl transition-smooth;
  }

  .btn-secondary {
    @apply bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-700 hover:to-indigo-700 text-white font-semibold px-8 py-4 rounded-2xl shadow-lg hover:shadow-xl transition-smooth;
  }

  .btn-outline {
    @apply border-2 border-gray-300 hover:border-blue-500 text-gray-700 hover:text-blue-600 hover:bg-blue-50 font-semibold px-8 py-4 rounded-2xl transition-smooth;
  }

  .btn-ghost {
    @apply text-gray-600 hover:text-gray-900 hover:bg-gray-100 font-medium px-6 py-3 rounded-xl transition-smooth;
  }

  /* Layout utilities */
  .container-clean {
    @apply max-w-7xl mx-auto px-8 sm:px-12 lg:px-16;
  }

  .section-spacing {
    @apply py-20 lg:py-32;
  }

  .section-spacing-sm {
    @apply py-16 lg:py-24;
  }

  .content-spacing {
    @apply space-y-12 lg:space-y-16;
  }

  /* Text utilities */
  .text-gradient {
    @apply bg-gradient-to-r from-blue-600 via-purple-600 to-indigo-600 bg-clip-text text-transparent;
  }

  /* Form utilities */
  .input-clean {
    @apply w-full px-6 py-4 border-2 border-gray-300 rounded-2xl focus:ring-4 focus:ring-blue-500/20 focus:border-blue-500 transition-smooth bg-white/80 backdrop-blur-sm;
  }

  /* Background utilities */
  .bg-gradient-primary {
    @apply bg-gradient-to-br from-blue-50 via-indigo-50 to-purple-50;
  }

  .bg-gradient-secondary {
    @apply bg-gradient-to-br from-purple-50 via-blue-50 to-indigo-50;
  }

  .bg-gradient-accent {
    @apply bg-gradient-to-br from-slate-100 via-blue-100 to-purple-100;
  }

  /* Spacing utilities */
  .space-clean > * + * {
    margin-top: 2rem;
  }

  .space-clean-lg > * + * {
    margin-top: 3rem;
  }

  /* Grid utilities */
  .grid-responsive {
    @apply grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 lg:gap-12;
  }

  /* Stagger animations */
  .stagger-children > * {
    opacity: 0;
    animation: fadeIn 0.8s cubic-bezier(0.4, 0, 0.2, 1) forwards;
  }

  .stagger-children > *:nth-child(1) {
    animation-delay: 0.1s;
  }
  .stagger-children > *:nth-child(2) {
    animation-delay: 0.2s;
  }
  .stagger-children > *:nth-child(3) {
    animation-delay: 0.3s;
  }
  .stagger-children > *:nth-child(4) {
    animation-delay: 0.4s;
  }
  .stagger-children > *:nth-child(5) {
    animation-delay: 0.5s;
  }
  .stagger-children > *:nth-child(6) {
    animation-delay: 0.6s;
  }
}

/* Keyframes */
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(50px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes scaleIn {
  from {
    opacity: 0;
    transform: scale(0.9);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

@keyframes float {
  0%,
  100% {
    transform: translateY(0px);
  }
  50% {
    transform: translateY(-10px);
  }
}

/* Focus styles */
*:focus-visible {
  @apply outline-none ring-4 ring-blue-500/30 ring-offset-2;
}

/* Scrollbar */
::-webkit-scrollbar {
  width: 12px;
}

::-webkit-scrollbar-track {
  @apply bg-gray-100 rounded-full;
}

::-webkit-scrollbar-thumb {
  @apply bg-gray-400 rounded-full hover:bg-gray-500;
}


--------------------------------------------------------------------------------
FILE: app/layout.tsx
--------------------------------------------------------------------------------
import type React from "react"
import type { Metadata } from "next"
import { Inter } from "next/font/google"
import "./globals.css"
import { AuthProvider } from "@/lib/auth-context"
import { Toaster } from "@/components/ui/toaster"

const inter = Inter({
  subsets: ["latin"],
  variable: "--font-inter",
  weight: ["300", "400", "500", "600", "700", "800"],
})

export const metadata: Metadata = {
  title: "VoltSphere - Advanced Microgrid Simulation",
  description: "Professional microgrid simulation and energy optimization platform",
  generator: "v0.dev",
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className={`${inter.variable} ${inter.className}`}>
        <AuthProvider>
          {children}
          <Toaster />
        </AuthProvider>
      </body>
    </html>
  )
}


--------------------------------------------------------------------------------
FILE: app/page.tsx
--------------------------------------------------------------------------------
"use client"

import Link from "next/link"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { SiteHeader } from "@/components/site-header"
import { Zap, BarChart3, Shield, Battery, ArrowRight, CheckCircle, Users, TrendingUp, Award } from "lucide-react"

export default function HomePage() {
  const features = [
    {
      icon: BarChart3,
      title: "Advanced Analytics",
      description:
        "Real-time monitoring and predictive analytics for optimal energy management and performance tracking",
    },
    {
      icon: Shield,
      title: "Enterprise Security",
      description: "Bank-grade security with end-to-end encryption and compliance standards for your data protection",
    },
    {
      icon: Battery,
      title: "Smart Storage",
      description: "Intelligent battery management with predictive charging and discharging optimization algorithms",
    },
  ]

  const stats = [
    { icon: Users, value: "10,000+", label: "Active Users" },
    { icon: Zap, value: "50MW", label: "Energy Managed" },
    { icon: TrendingUp, value: "35%", label: "Efficiency Gain" },
    { icon: Award, value: "99.9%", label: "Uptime" },
  ]

  const plans = [
    {
      name: "Free",
      description: "Perfect for getting started with basic simulations",
      features: ["Basic simulations", "Standard components", "Community support", "Export to PDF"],
      href: "/simulation/starter",
    },
    {
      name: "Professional",
      description: "Advanced features for energy professionals",
      features: [
        "Advanced analytics",
        "Custom components",
        "Priority support",
        "Export capabilities",
        "Weather data",
        "Cost analysis",
      ],
      href: "/simulation/pro",
      popular: true,
    },
    {
      name: "Enterprise",
      description: "Full-scale enterprise solutions with unlimited access",
      features: [
        "Unlimited simulations",
        "API access",
        "Custom integrations",
        "Dedicated support",
        "White-label options",
        "Advanced AI",
      ],
      href: "/simulation/enterprise",
    },
  ]

  return (
    <div className="min-h-screen bg-gradient-primary">
      <SiteHeader />

      {/* Hero Section */}
      <section className="section-spacing">
        <div className="container-clean">
          <div className="text-center max-w-5xl mx-auto content-spacing animate-fade-in">
            <h1 className="text-5xl lg:text-7xl font-bold text-gray-900 mb-8 leading-tight">
              Transform Your Energy Future with <span className="text-gradient">VoltSphere</span>
            </h1>
            <p className="text-2xl lg:text-3xl text-gray-700 mb-12 max-w-4xl mx-auto leading-relaxed">
              Experience the power of AI-driven microgrid simulation and optimization. Reduce costs, increase
              efficiency, and build a sustainable energy future with our cutting-edge platform.
            </p>
            <div className="flex flex-col sm:flex-row gap-6 justify-center">
              <Button asChild size="lg" className="btn-primary text-xl">
                <Link href="/simulations">
                  Start Free Simulation
                  <ArrowRight className="ml-3 h-6 w-6" />
                </Link>
              </Button>
              <Button asChild variant="outline" size="lg" className="btn-outline text-xl">
                <Link href="/about">Learn More</Link>
              </Button>
            </div>
          </div>
        </div>
      </section>

      {/* Stats Section */}
      <section className="section-spacing-sm bg-gradient-secondary">
        <div className="container-clean">
          <div className="grid grid-cols-2 lg:grid-cols-4 gap-8 lg:gap-12 stagger-children">
            {stats.map((stat, index) => (
              <div key={index} className="text-center group">
                <div className="flex justify-center mb-6">
                  <div className="w-20 h-20 bg-gradient-to-r from-blue-600 to-purple-600 rounded-3xl flex items-center justify-center group-hover:scale-110 transition-transform-smooth shadow-xl">
                    <stat.icon className="h-10 w-10 text-white" />
                  </div>
                </div>
                <div className="text-4xl lg:text-5xl font-bold text-gradient mb-3">{stat.value}</div>
                <div className="text-gray-700 font-semibold text-lg">{stat.label}</div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="section-spacing bg-gradient-accent">
        <div className="container-clean">
          <div className="text-center mb-20 animate-fade-in">
            <h2 className="text-4xl lg:text-5xl font-bold text-gray-900 mb-8">Powerful Features</h2>
            <p className="text-2xl text-gray-700 max-w-3xl mx-auto leading-relaxed">
              Everything you need to model, analyze, and optimize your energy systems with precision and confidence
            </p>
          </div>

          <div className="grid-responsive stagger-children">
            {features.map((feature, index) => (
              <Card key={index} className="card-enhanced text-center hover-lift">
                <CardHeader className="pb-6">
                  <div className="flex justify-center mb-6">
                    <div className="w-20 h-20 bg-gradient-to-r from-blue-600 to-purple-600 rounded-3xl flex items-center justify-center shadow-xl">
                      <feature.icon className="h-10 w-10 text-white" />
                    </div>
                  </div>
                  <CardTitle className="text-2xl font-bold text-gray-900 mb-4">{feature.title}</CardTitle>
                </CardHeader>
                <CardContent className="px-8 pb-8">
                  <p className="text-gray-700 text-lg leading-relaxed">{feature.description}</p>
                </CardContent>
              </Card>
            ))}
          </div>
        </div>
      </section>

      {/* Plans Section */}
      <section className="section-spacing bg-gradient-primary">
        <div className="container-clean">
          <div className="text-center mb-20 animate-fade-in">
            <h2 className="text-4xl lg:text-5xl font-bold text-gray-900 mb-8">Choose Your Plan</h2>
            <p className="text-2xl text-gray-700 max-w-3xl mx-auto leading-relaxed">
              From basic modeling to enterprise-grade simulations, we have the perfect solution for your energy needs
            </p>
          </div>

          <div className="grid lg:grid-cols-3 gap-8 lg:gap-12 stagger-children">
            {plans.map((plan, index) => (
              <Card
                key={index}
                className={`card-enhanced relative hover-lift ${plan.popular ? "ring-4 ring-blue-500 ring-offset-4 scale-105" : ""}`}
              >
                {plan.popular && (
                  <div className="absolute -top-6 left-1/2 transform -translate-x-1/2">
                    <span className="bg-gradient-to-r from-blue-600 to-purple-600 text-white px-6 py-2 rounded-full text-lg font-bold shadow-lg">
                      Most Popular
                    </span>
                  </div>
                )}
                <CardHeader className="text-center pb-6">
                  <CardTitle className="text-3xl font-bold text-gray-900 mb-4">{plan.name}</CardTitle>
                  <p className="text-gray-700 text-lg leading-relaxed px-4">{plan.description}</p>
                </CardHeader>
                <CardContent className="px-8 pb-8 space-y-8">
                  <ul className="space-y-4">
                    {plan.features.map((feature, featureIndex) => (
                      <li key={featureIndex} className="flex items-center gap-4">
                        <CheckCircle className="h-6 w-6 text-blue-600 flex-shrink-0" />
                        <span className="text-gray-700 text-lg">{feature}</span>
                      </li>
                    ))}
                  </ul>
                  <Button asChild className="w-full btn-primary text-lg">
                    <Link href={plan.href}>
                      Get Started
                      <ArrowRight className="ml-3 h-5 w-5" />
                    </Link>
                  </Button>
                </CardContent>
              </Card>
            ))}
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="section-spacing bg-gradient-to-r from-blue-600 to-purple-600 text-white">
        <div className="container-clean text-center animate-fade-in">
          <h2 className="text-4xl lg:text-5xl font-bold mb-8">Ready to Get Started?</h2>
          <p className="text-2xl mb-12 max-w-3xl mx-auto opacity-90 leading-relaxed">
            Join thousands of energy professionals who trust VoltSphere for their simulation and optimization needs.
          </p>
          <Button
            asChild
            size="lg"
            className="bg-white text-blue-600 hover:bg-gray-100 font-bold px-12 py-6 rounded-2xl transition-smooth text-xl shadow-xl hover:shadow-2xl"
          >
            <Link href="/simulations">
              Start Free Trial
              <ArrowRight className="ml-3 h-6 w-6" />
            </Link>
          </Button>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-gray-900 text-white section-spacing-sm">
        <div className="container-clean">
          <div className="grid md:grid-cols-4 gap-12 mb-12">
            <div className="space-y-6">
              <div className="flex items-center space-x-3">
                <div className="flex h-12 w-12 items-center justify-center rounded-2xl bg-gradient-to-r from-blue-600 to-purple-600">
                  <Zap className="h-6 w-6 text-white" />
                </div>
                <span className="text-2xl font-bold">VoltSphere</span>
              </div>
              <p className="text-gray-400 text-lg leading-relaxed">
                Advanced energy simulation and optimization platform for professionals worldwide.
              </p>
            </div>

            <div>
              <h3 className="font-bold mb-6 text-xl">Product</h3>
              <ul className="space-y-3 text-gray-400">
                <li>
                  <Link href="/simulations" className="hover:text-white transition-smooth text-lg">
                    Simulations
                  </Link>
                </li>
                <li>
                  <Link href="/pricing" className="hover:text-white transition-smooth text-lg">
                    Pricing
                  </Link>
                </li>
              </ul>
            </div>

            <div>
              <h3 className="font-bold mb-6 text-xl">Company</h3>
              <ul className="space-y-3 text-gray-400">
                <li>
                  <Link href="/about" className="hover:text-white transition-smooth text-lg">
                    About
                  </Link>
                </li>
                <li>
                  <Link href="/contact" className="hover:text-white transition-smooth text-lg">
                    Contact
                  </Link>
                </li>
              </ul>
            </div>

            <div>
              <h3 className="font-bold mb-6 text-xl">Support</h3>
              <ul className="space-y-3 text-gray-400">
                <li>
                  <Link href="/help" className="hover:text-white transition-smooth text-lg">
                    Help Center
                  </Link>
                </li>
                <li>
                  <Link href="/docs" className="hover:text-white transition-smooth text-lg">
                    Documentation
                  </Link>
                </li>
              </ul>
            </div>
          </div>

          <div className="border-t border-gray-800 pt-8 text-center text-gray-400">
            <p className="text-lg">&copy; 2024 VoltSphere. All rights reserved.</p>
          </div>
        </div>
      </footer>
    </div>
  )
}


--------------------------------------------------------------------------------
FILE: app/pricing/page.tsx
--------------------------------------------------------------------------------
"use client"

import { useState } from "react"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card"
import { Tabs, TabsList, TabsTrigger } from "@/components/ui/tabs"
import { Check } from "lucide-react"
import { useAuth } from "@/lib/auth-context"
import { LoginDialog } from "@/components/auth/login-dialog"
import { useRouter } from "next/navigation"
import { toast } from "sonner"

export default function PricingPage() {
  const [billingInterval, setBillingInterval] = useState<"monthly" | "yearly">("monthly")
  const { user } = useAuth()
  const [showLoginDialog, setShowLoginDialog] = useState(false)
  const [processingTier, setProcessingTier] = useState<string | null>(null)
  const router = useRouter()

  const handlePurchase = async (tier: string) => {
    if (!user) {
      setShowLoginDialog(true)
      return
    }

    setProcessingTier(tier)

    try {
      const response = await fetch("/api/create-checkout-session", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          tier,
          billing: billingInterval,
          successUrl: `${window.location.origin}/billing/success?session_id={CHECKOUT_SESSION_ID}`,
          cancelUrl: `${window.location.origin}/pricing`,
        }),
      })

      const { url, error } = await response.json()

      if (error) {
        toast.error(error)
        return
      }

      if (url) {
        // Step 2: Redirect to Stripe checkout
        window.location.href = url
      } else {
        toast.error("Failed to create checkout session")
      }
    } catch (error) {
      console.error("Error creating checkout session:", error)
      toast.error("Failed to create checkout session")
    } finally {
      setProcessingTier(null)
    }
  }

  const plans = [
    {
      id: "free",
      name: "Free",
      description: "Basic access to energy simulation tools",
      price: { monthly: 0, yearly: 0 },
      features: ["Basic simulation models", "Standard visualization", "Limited data export", "Community support"],
    },
    {
      id: "pro",
      name: "Pro",
      description: "Advanced simulation tools for professionals",
      price: {
        monthly: 5.99,
        yearly: 599.99,
      },
      features: [
        "Everything in Free",
        "Advanced simulation models",
        "Enhanced visualization",
        "Full data export",
        "Priority email support",
      ],
      popular: true,
    },
    {
      id: "growth",
      name: "Growth",
      description: "Enterprise-grade simulation platform",
      price: {
        monthly: 99,
        yearly: 990,
      },
      features: [
        "Everything in Pro",
        "Custom simulation models",
        "Advanced analytics",
        "API access",
        "Dedicated support",
      ],
    },
  ]

  return (
    <div className="container max-w-6xl px-4 py-16 md:py-24">
      <div className="mx-auto text-center mb-16">
        <h1 className="text-4xl md:text-5xl font-bold mb-6">Simple, Transparent Pricing</h1>
        <p className="text-xl text-gray-600 max-w-3xl mx-auto">
          Choose the plan that best fits your needs. All plans include access to our core simulation features.
        </p>

        <div className="mt-10 flex justify-center">
          <Tabs
            defaultValue="monthly"
            value={billingInterval}
            onValueChange={(value) => setBillingInterval(value as "monthly" | "yearly")}
            className="w-full max-w-md"
          >
            <TabsList className="grid w-full grid-cols-2 bg-gray-100 rounded-xl p-1">
              <TabsTrigger
                value="monthly"
                className="rounded-lg data-[state=active]:bg-white data-[state=active]:text-blue-600 data-[state=active]:shadow-sm py-3"
              >
                Monthly
              </TabsTrigger>
              <TabsTrigger
                value="yearly"
                className="rounded-lg data-[state=active]:bg-white data-[state=active]:text-blue-600 data-[state=active]:shadow-sm py-3"
              >
                Yearly <span className="ml-1 text-sm text-green-600 font-medium">Save 17%</span>
              </TabsTrigger>
            </TabsList>
          </Tabs>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
        {plans.map((plan) => (
          <Card
            key={plan.id}
            className={`border-2 rounded-3xl shadow-lg hover:shadow-xl transition-all duration-300 ${
              plan.popular
                ? "border-blue-200 relative shadow-xl hover:shadow-2xl"
                : "border-gray-200 hover:border-gray-300"
            }`}
          >
            {plan.popular && (
              <div className="absolute top-0 right-0 transform translate-x-2 -translate-y-2">
                <span className="bg-blue-600 text-white text-sm font-semibold px-4 py-1 rounded-full shadow-lg">
                  Popular
                </span>
              </div>
            )}
            <CardHeader className="pb-8 pt-8">
              <CardTitle className="text-2xl">{plan.name}</CardTitle>
              <div className="mt-4 flex items-baseline text-gray-900">
                <span className="text-5xl font-extrabold tracking-tight">
                  ${billingInterval === "monthly" ? plan.price.monthly : plan.price.yearly}
                </span>
                {plan.price.monthly > 0 && (
                  <span className="ml-1 text-xl font-semibold">
                    /{billingInterval === "monthly" ? "month" : "year"}
                  </span>
                )}
              </div>
              <CardDescription className="mt-4 text-gray-500">{plan.description}</CardDescription>
            </CardHeader>
            <CardContent className="pb-8">
              <ul className="space-y-4">
                {plan.features.map((feature, i) => (
                  <li key={i} className="flex items-start">
                    <Check className="h-5 w-5 text-green-500 mr-3 mt-0.5" />
                    <span>{feature}</span>
                  </li>
                ))}
              </ul>
            </CardContent>
            <CardFooter>
              {plan.id === "free" ? (
                <Button
                  variant="outline"
                  className="w-full py-6 text-lg rounded-xl border-2 hover:bg-gray-50"
                  onClick={() => router.push("/simulation")}
                >
                  Get Started
                </Button>
              ) : (
                <Button
                  className={`w-full py-6 text-lg rounded-xl ${
                    plan.popular ? "bg-blue-600 hover:bg-blue-700" : "bg-gray-800 hover:bg-gray-900"
                  }`}
                  onClick={() => handlePurchase(plan.id)}
                  disabled={processingTier === plan.id}
                >
                  {processingTier === plan.id ? (
                    <>
                      <div className="animate-spin rounded-full h-5 w-5 border-b-2 border-white mr-2"></div>
                      Processing...
                    </>
                  ) : user ? (
                    "Upgrade Now"
                  ) : (
                    "Sign In to Purchase"
                  )}
                </Button>
              )}
            </CardFooter>
          </Card>
        ))}
      </div>

      <LoginDialog open={showLoginDialog} onOpenChange={setShowLoginDialog} />
    </div>
  )
}


--------------------------------------------------------------------------------
FILE: app/pro-sim/page.tsx
--------------------------------------------------------------------------------
"use client"

import { useState } from "react"

export default function ProSimulationStandalone() {
  const [batteryCapacity, setBatteryCapacity] = useState(15)
  const [batteryEfficiency, setBatteryEfficiency] = useState(92)
  const [batteryType, setBatteryType] = useState("lithium")
  const [loadProfile, setLoadProfile] = useState("residential")
  const [solarEnabled, setSolarEnabled] = useState(true)
  const [weatherEnabled, setWeatherEnabled] = useState(false)
  const [timeOfUseEnabled, setTimeOfUseEnabled] = useState(false)
  const [isRunning, setIsRunning] = useState(false)
  const [simulationData, setSimulationData] = useState<any>(null)
  const [activeTab, setActiveTab] = useState("simulation")

  const runSimulation = () => {
    setIsRunning(true)

    setTimeout(() => {
      const hours = Array.from({ length: 24 }, (_, i) => `${i}:00`)
      const solarProfile = hours.map((_, i) => {
        if (i < 6 || i > 19) return 0
        return Math.max(
          0,
          Math.sin(((i - 6) * Math.PI) / 13) *
            (batteryCapacity * 0.8) *
            (weatherEnabled ? 0.7 + Math.random() * 0.3 : 1),
        )
      })

      const loadProfile = hours.map((_, i) => {
        const baseLoad = batteryCapacity * 0.3
        const peakMultiplier = i >= 17 && i <= 22 ? 1.8 : i >= 6 && i <= 9 ? 1.4 : 1
        return baseLoad * peakMultiplier * (0.8 + Math.random() * 0.4)
      })

      const batteryStorage = hours.map((_, i) => {
        return Math.max(0, Math.min(batteryCapacity, batteryCapacity * (0.3 + 0.4 * Math.sin((i * Math.PI) / 12))))
      })

      const gridUsage = hours.map((_, i) => {
        return Math.max(0, loadProfile[i] - (solarEnabled ? solarProfile[i] : 0))
      })

      setSimulationData({
        hours,
        solar: solarProfile,
        consumption: loadProfile,
        battery: batteryStorage,
        grid: gridUsage,
      })

      setIsRunning(false)
    }, 1500)
  }

  const SimpleChart = ({ data }: { data: any }) => {
    if (!data) return null

    const maxValue = Math.max(...data.solar, ...data.consumption, ...data.battery, ...data.grid)

    return (
      <div className="w-full h-80 bg-white rounded-lg border p-4">
        <h3 className="text-lg font-semibold mb-4">Energy Flow (kW)</h3>
        <div className="relative h-64">
          <svg width="100%" height="100%" viewBox="0 0 800 200">
            {/* Grid lines */}
            {[0, 1, 2, 3, 4].map((i) => (
              <line key={i} x1="0" y1={i * 40} x2="800" y2={i * 40} stroke="#e5e7eb" strokeWidth="1" />
            ))}

            {/* Solar line */}
            <polyline
              fill="none"
              stroke="#f59e0b"
              strokeWidth="3"
              points={data.hours.map((_, i) => `${(i * 800) / 24},${200 - (data.solar[i] / maxValue) * 180}`).join(" ")}
            />

            {/* Consumption line */}
            <polyline
              fill="none"
              stroke="#ef4444"
              strokeWidth="3"
              points={data.hours
                .map((_, i) => `${(i * 800) / 24},${200 - (data.consumption[i] / maxValue) * 180}`)
                .join(" ")}
            />

            {/* Battery line */}
            <polyline
              fill="none"
              stroke="#10b981"
              strokeWidth="3"
              points={data.hours
                .map((_, i) => `${(i * 800) / 24},${200 - (data.battery[i] / maxValue) * 180}`)
                .join(" ")}
            />

            {/* Grid line */}
            <polyline
              fill="none"
              stroke="#6366f1"
              strokeWidth="3"
              points={data.hours.map((_, i) => `${(i * 800) / 24},${200 - (data.grid[i] / maxValue) * 180}`).join(" ")}
            />
          </svg>
        </div>

        <div className="flex justify-center gap-6 mt-4 text-sm">
          <div className="flex items-center gap-2">
            <div className="w-4 h-1 bg-yellow-500"></div>
            <span>Solar</span>
          </div>
          <div className="flex items-center gap-2">
            <div className="w-4 h-1 bg-red-500"></div>
            <span>Consumption</span>
          </div>
          <div className="flex items-center gap-2">
            <div className="w-4 h-1 bg-green-500"></div>
            <span>Battery</span>
          </div>
          <div className="flex items-center gap-2">
            <div className="w-4 h-1 bg-indigo-500"></div>
            <span>Grid</span>
          </div>
        </div>
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-50 via-blue-50 to-purple-50">
      {/* Header */}
      <div className="bg-white shadow-sm border-b">
        <div className="container mx-auto px-4 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-3">
              <div className="w-8 h-8 bg-gradient-to-r from-purple-600 to-pink-600 rounded-lg flex items-center justify-center">
                <span className="text-white font-bold">V</span>
              </div>
              <h1 className="text-2xl font-bold text-gray-800">VoltSphere Pro</h1>
              <span className="bg-gradient-to-r from-purple-600 to-pink-600 text-white px-3 py-1 rounded-full text-sm font-semibold">
                PRO
              </span>
            </div>
            <a href="/" className="text-gray-600 hover:text-gray-800 px-4 py-2 rounded-lg hover:bg-gray-100">
              Back to Home
            </a>
          </div>
        </div>
      </div>

      <div className="container mx-auto px-4 py-8">
        <div className="text-center mb-8">
          <h2 className="text-4xl font-bold text-gray-800 mb-4">Pro Simulation Suite</h2>
          <p className="text-lg text-gray-600 max-w-4xl mx-auto">
            Advanced microgrid simulation with weather integration, multiple battery types, and comprehensive analytics.
          </p>
        </div>

        {/* Tabs */}
        <div className="flex justify-center mb-8">
          <div className="bg-white rounded-lg p-1 shadow-sm border">
            {[
              { id: "simulation", label: "Simulation" },
              { id: "advanced", label: "Advanced" },
              { id: "analytics", label: "Analytics" },
            ].map((tab) => (
              <button
                key={tab.id}
                onClick={() => setActiveTab(tab.id)}
                className={`px-6 py-3 rounded-md font-medium transition-all ${
                  activeTab === tab.id
                    ? "bg-gradient-to-r from-purple-600 to-pink-600 text-white shadow-md"
                    : "text-gray-600 hover:text-gray-800 hover:bg-gray-50"
                }`}
              >
                {tab.label}
              </button>
            ))}
          </div>
        </div>

        {/* Simulation Tab */}
        {activeTab === "simulation" && (
          <div className="grid lg:grid-cols-4 gap-6">
            <div className="lg:col-span-1">
              <div className="bg-white rounded-xl shadow-lg border p-6">
                <h3 className="text-xl font-semibold mb-6 flex items-center gap-2">Pro Controls</h3>

                <div className="space-y-6">
                  <div>
                    <label className="block text-sm font-semibold text-gray-700 mb-2">
                      Battery Capacity: {batteryCapacity} kWh
                    </label>
                    <input
                      type="range"
                      min="5"
                      max="100"
                      value={batteryCapacity}
                      onChange={(e) => setBatteryCapacity(Number(e.target.value))}
                      className="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer"
                    />
                  </div>

                  <div>
                    <label className="block text-sm font-semibold text-gray-700 mb-2">Battery Type</label>
                    <select
                      value={batteryType}
                      onChange={(e) => setBatteryType(e.target.value)}
                      className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent"
                    >
                      <option value="lithium">Lithium-ion (92% efficiency)</option>
                      <option value="lead-acid">Lead-acid (85% efficiency)</option>
                      <option value="flow">Flow Battery (88% efficiency)</option>
                      <option value="sodium">Sodium-ion (90% efficiency)</option>
                    </select>
                  </div>

                  <div>
                    <label className="block text-sm font-semibold text-gray-700 mb-2">
                      Battery Efficiency: {batteryEfficiency}%
                    </label>
                    <input
                      type="range"
                      min="70"
                      max="98"
                      value={batteryEfficiency}
                      onChange={(e) => setBatteryEfficiency(Number(e.target.value))}
                      className="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer"
                    />
                  </div>

                  <div>
                    <label className="block text-sm font-semibold text-gray-700 mb-2">Load Profile</label>
                    <select
                      value={loadProfile}
                      onChange={(e) => setLoadProfile(e.target.value)}
                      className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent"
                    >
                      <option value="residential">Residential Home</option>
                      <option value="commercial">Commercial Building</option>
                      <option value="industrial">Industrial Facility</option>
                    </select>
                  </div>

                  <div className="flex items-center justify-between p-4 bg-gradient-to-r from-yellow-50 to-orange-50 rounded-xl">
                    <label className="flex items-center gap-2 font-semibold text-yellow-800">Solar Power</label>
                    <input
                      type="checkbox"
                      checked={solarEnabled}
                      onChange={(e) => setSolarEnabled(e.target.checked)}
                      className="w-5 h-5 text-yellow-600 rounded focus:ring-yellow-500"
                    />
                  </div>

                  <div className="flex items-center justify-between p-4 bg-gradient-to-r from-blue-50 to-purple-50 rounded-xl">
                    <label className="flex items-center gap-2 font-semibold text-blue-800">Real Weather Data</label>
                    <input
                      type="checkbox"
                      checked={weatherEnabled}
                      onChange={(e) => setWeatherEnabled(e.target.checked)}
                      className="w-5 h-5 text-blue-600 rounded focus:ring-blue-500"
                    />
                  </div>

                  <div className="flex items-center justify-between p-4 bg-gradient-to-r from-green-50 to-teal-50 rounded-xl">
                    <label className="flex items-center gap-2 font-semibold text-green-800">Time-of-Use Rates</label>
                    <input
                      type="checkbox"
                      checked={timeOfUseEnabled}
                      onChange={(e) => setTimeOfUseEnabled(e.target.checked)}
                      className="w-5 h-5 text-green-600 rounded focus:ring-green-500"
                    />
                  </div>

                  <button
                    onClick={runSimulation}
                    disabled={isRunning}
                    className="w-full bg-gradient-to-r from-purple-600 to-pink-600 hover:from-purple-700 hover:to-pink-700 text-white font-bold py-4 px-6 rounded-xl transition-all transform hover:scale-105 disabled:opacity-50 disabled:transform-none"
                  >
                    {isRunning ? "Running Pro Simulation..." : "Run Pro Simulation"}
                  </button>
                </div>
              </div>
            </div>

            <div className="lg:col-span-3">
              {simulationData ? (
                <div className="bg-white rounded-xl shadow-lg border p-6">
                  <h3 className="text-xl font-semibold mb-4">Pro Simulation Results</h3>
                  <p className="text-gray-600 mb-6">
                    {batteryType} battery • {batteryCapacity}kWh capacity • {batteryEfficiency}% efficiency
                  </p>
                  <SimpleChart data={simulationData} />
                </div>
              ) : (
                <div className="bg-white rounded-xl shadow-lg border p-6 flex items-center justify-center h-96">
                  <div className="text-center">
                    {isRunning ? (
                      <>
                        <div className="animate-spin rounded-full h-16 w-16 border-b-4 border-purple-600 mx-auto mb-4"></div>
                        <h3 className="text-xl font-semibold text-gray-600 mb-2">Running Pro Simulation...</h3>
                        <p className="text-gray-500">Calculating advanced energy flows with weather data</p>
                      </>
                    ) : (
                      <>
                        <div className="text-6xl mb-4">⚡</div>
                        <h3 className="text-xl font-semibold text-gray-600 mb-2">Ready for Pro Simulation</h3>
                        <p className="text-gray-500">Configure your advanced settings and run the simulation</p>
                      </>
                    )}
                  </div>
                </div>
              )}
            </div>
          </div>
        )}

        {/* Advanced Tab */}
        {activeTab === "advanced" && (
          <div className="bg-white rounded-xl shadow-lg border p-6">
            <h3 className="text-xl font-semibold mb-6">Advanced Configuration</h3>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div>
                <label className="block text-sm font-semibold text-gray-700 mb-2">Weather Location</label>
                <select className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500">
                  <option>San Francisco, CA</option>
                  <option>New York, NY</option>
                  <option>Chicago, IL</option>
                  <option>Austin, TX</option>
                  <option>Miami, FL</option>
                </select>
              </div>
              <div>
                <label className="block text-sm font-semibold text-gray-700 mb-2">Simulation Duration</label>
                <select className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500">
                  <option>24 Hours</option>
                  <option>7 Days</option>
                  <option>30 Days</option>
                  <option>1 Year</option>
                </select>
              </div>
            </div>
          </div>
        )}

        {/* Analytics Tab */}
        {activeTab === "analytics" && (
          <div className="bg-white rounded-xl shadow-lg border p-6">
            <h3 className="text-xl font-semibold mb-6">Pro Cost Analysis</h3>
            {simulationData ? (
              <div className="space-y-6">
                <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                  <div className="bg-blue-50 p-6 rounded-lg border border-blue-100">
                    <h4 className="text-lg font-semibold text-blue-700 mb-2">Daily Savings</h4>
                    <p className="text-3xl font-bold text-blue-800">${Math.round(batteryCapacity * 0.15)}</p>
                    <p className="text-sm text-blue-600 mt-1">From solar and battery optimization</p>
                  </div>
                  <div className="bg-green-50 p-6 rounded-lg border border-green-100">
                    <h4 className="text-lg font-semibold text-green-700 mb-2">Monthly Savings</h4>
                    <p className="text-3xl font-bold text-green-800">${Math.round(batteryCapacity * 0.15 * 30)}</p>
                    <p className="text-sm text-green-600 mt-1">Projected for 30 days</p>
                  </div>
                  <div className="bg-purple-50 p-6 rounded-lg border border-purple-100">
                    <h4 className="text-lg font-semibold text-purple-700 mb-2">Annual Savings</h4>
                    <p className="text-3xl font-bold text-purple-800">${Math.round(batteryCapacity * 0.15 * 365)}</p>
                    <p className="text-sm text-purple-600 mt-1">Projected for 365 days</p>
                  </div>
                </div>

                <div className="bg-gray-50 p-6 rounded-lg border border-gray-200">
                  <h4 className="text-lg font-semibold text-gray-700 mb-4">Advanced ROI Analysis</h4>
                  <div className="space-y-3">
                    <div className="flex justify-between items-center">
                      <span className="text-gray-600">System Cost ({batteryType})</span>
                      <span className="font-semibold">${(batteryCapacity * 1200).toLocaleString()}</span>
                    </div>
                    <div className="flex justify-between items-center">
                      <span className="text-gray-600">Annual Savings</span>
                      <span className="font-semibold text-green-600">
                        ${Math.round(batteryCapacity * 0.15 * 365).toLocaleString()}
                      </span>
                    </div>
                    <div className="flex justify-between items-center">
                      <span className="text-gray-600">Payback Period</span>
                      <span className="font-semibold">
                        {Math.round((batteryCapacity * 1200) / (batteryCapacity * 0.15 * 365))} years
                      </span>
                    </div>
                    <div className="flex justify-between items-center">
                      <span className="text-gray-600">10-Year Net Savings</span>
                      <span className="font-semibold text-green-600">
                        ${Math.round(batteryCapacity * 0.15 * 365 * 10 - batteryCapacity * 1200).toLocaleString()}
                      </span>
                    </div>
                    <div className="flex justify-between items-center">
                      <span className="text-gray-600">Carbon Offset (Annual)</span>
                      <span className="font-semibold text-green-600">{Math.round(batteryCapacity * 2.5)} tons CO₂</span>
                    </div>
                  </div>
                </div>
              </div>
            ) : (
              <div className="flex items-center justify-center h-64">
                <div className="text-center">
                  <div className="text-6xl mb-4">📊</div>
                  <p className="text-gray-500">Run a Pro simulation to see advanced cost analytics</p>
                </div>
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  )
}


--------------------------------------------------------------------------------
FILE: app/profile/page.tsx
--------------------------------------------------------------------------------
"use client"

import { useEffect } from "react"
import { useRouter } from "next/navigation"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Badge } from "@/components/ui/badge"
import { useAuth } from "@/lib/auth-context"
import { User, Settings, CreditCard, Star, Zap, Code } from "lucide-react"

export default function ProfilePage() {
  const { user, isLoading } = useAuth()
  const router = useRouter()

  useEffect(() => {
    // Redirect if not logged in
    if (!isLoading && !user) {
      router.push("/")
    }
  }, [user, isLoading, router])

  if (isLoading) {
    return <div className="flex justify-center items-center h-screen">Loading...</div>
  }

  if (!user) {
    return null // Will redirect in useEffect
  }

  const getSubscriptionDetails = () => {
    switch (user.subscriptionTier) {
      case "pro":
        return {
          name: "Pro",
          description: "Advanced simulation with weather integration and project management",
          badge: <Badge className="bg-gradient-to-r from-blue-600 to-purple-600">Pro</Badge>,
          icon: <Star className="h-5 w-5 text-purple-600" />,
        }
      case "starter":
        return {
          name: "Starter API",
          description: "API access with 5,000 calls per month",
          badge: <Badge className="bg-gradient-to-r from-green-600 to-blue-600">Starter API</Badge>,
          icon: <Code className="h-5 w-5 text-green-600" />,
        }
      case "growth":
        return {
          name: "Growth API",
          description: "Enhanced API access with 50,000 calls per month",
          badge: <Badge className="bg-gradient-to-r from-purple-600 to-pink-600">Growth API</Badge>,
          icon: <Code className="h-5 w-5 text-pink-600" />,
        }
      case "enterprise":
        return {
          name: "Enterprise",
          description: "Full access to all features with unlimited API calls",
          badge: <Badge className="bg-gradient-to-r from-yellow-600 to-red-600">Enterprise</Badge>,
          icon: <Star className="h-5 w-5 text-yellow-600" />,
        }
      default:
        return {
          name: "Free",
          description: "Basic simulation with limited features",
          badge: <Badge variant="outline">Free</Badge>,
          icon: <Zap className="h-5 w-5 text-gray-600" />,
        }
    }
  }

  const subscriptionDetails = getSubscriptionDetails()

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-50 to-blue-50">
      {/* Header */}
      <header className="glass-effect border-b sticky top-0 z-40 backdrop-enhanced">
        <nav className="container mx-auto mobile-padding py-3 sm:py-4 flex justify-between items-center">
          <div className="text-xl sm:text-2xl font-bold gradient-text font-display">My Profile</div>
          <Button variant="outline" onClick={() => router.push("/")}>
            Back to Home
          </Button>
        </nav>
      </header>

      <div className="container mx-auto mobile-padding py-8">
        <div className="max-w-3xl mx-auto">
          <Card className="mb-8">
            <CardHeader>
              <CardTitle className="flex items-center gap-3">
                <User className="h-5 w-5 text-blue-600" />
                Account Information
              </CardTitle>
            </CardHeader>
            <CardContent className="space-y-4">
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div>
                  <div className="text-sm text-gray-500">Name</div>
                  <div className="font-medium">{user.name || "Not provided"}</div>
                </div>
                <div>
                  <div className="text-sm text-gray-500">Email</div>
                  <div className="font-medium">{user.email}</div>
                </div>
                <div>
                  <div className="text-sm text-gray-500">Account Type</div>
                  <div className="font-medium flex items-center gap-2">
                    {user.role === "admin" ? "Administrator" : "User"}
                    {user.role === "admin" && <Badge className="bg-red-600">Admin</Badge>}
                  </div>
                </div>
                <div>
                  <div className="text-sm text-gray-500">Member Since</div>
                  <div className="font-medium">June 10, 2024</div>
                </div>
              </div>

              <div className="flex justify-end">
                <Button variant="outline" className="flex items-center gap-2">
                  <Settings className="h-4 w-4" />
                  Edit Profile
                </Button>
              </div>
            </CardContent>
          </Card>

          <Card className="mb-8">
            <CardHeader>
              <CardTitle className="flex items-center gap-3">
                {subscriptionDetails.icon}
                Subscription
              </CardTitle>
            </CardHeader>
            <CardContent className="space-y-4">
              <div className="flex items-center justify-between">
                <div>
                  <div className="text-xl font-semibold flex items-center gap-2">
                    {subscriptionDetails.name} Plan
                    {subscriptionDetails.badge}
                  </div>
                  <div className="text-gray-500">{subscriptionDetails.description}</div>
                </div>

                {user.subscriptionTier === "free" && (
                  <Button
                    className="bg-gradient-to-r from-blue-600 to-purple-600"
                    onClick={() => router.push("/pricing")}
                  >
                    Upgrade
                  </Button>
                )}
              </div>

              {user.subscriptionTier !== "free" && (
                <div className="border-t pt-4 mt-4">
                  <div className="flex justify-between items-center">
                    <div>
                      <div className="font-medium">Billing Information</div>
                      <div className="text-sm text-gray-500">Your next payment is on July 10, 2024</div>
                    </div>
                    <Button
                      variant="outline"
                      className="flex items-center gap-2"
                      onClick={() => router.push("/billing")}
                    >
                      <CreditCard className="h-4 w-4" />
                      Manage Billing
                    </Button>
                  </div>
                </div>
              )}
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle>Simulation Access</CardTitle>
            </CardHeader>
            <CardContent className="space-y-4">
              <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                <Button
                  variant="outline"
                  className="flex items-center gap-2 justify-center h-auto py-4"
                  onClick={() => router.push("/simulation")}
                >
                  <Zap className="h-4 w-4" />
                  Basic Simulation
                </Button>

                <Button
                  variant={
                    user.subscriptionTier === "pro" || user.subscriptionTier === "enterprise" || user.role === "admin"
                      ? "outline"
                      : "ghost"
                  }
                  className="flex items-center gap-2 justify-center h-auto py-4"
                  disabled={
                    !(
                      user.subscriptionTier === "pro" ||
                      user.subscriptionTier === "enterprise" ||
                      user.role === "admin"
                    )
                  }
                  onClick={() => router.push("/simulation/pro")}
                >
                  <Star className="h-4 w-4" />
                  Pro Simulation
                  {!(
                    user.subscriptionTier === "pro" ||
                    user.subscriptionTier === "enterprise" ||
                    user.role === "admin"
                  ) && (
                    <Badge variant="outline" className="ml-2">
                      Locked
                    </Badge>
                  )}
                </Button>

                <Button
                  variant={
                    user.subscriptionTier === "starter" ||
                    user.subscriptionTier === "growth" ||
                    user.subscriptionTier === "enterprise" ||
                    user.role === "admin"
                      ? "outline"
                      : "ghost"
                  }
                  className="flex items-center gap-2 justify-center h-auto py-4"
                  disabled={
                    !(
                      user.subscriptionTier === "starter" ||
                      user.subscriptionTier === "growth" ||
                      user.subscriptionTier === "enterprise" ||
                      user.role === "admin"
                    )
                  }
                  onClick={() => router.push("/simulation/api")}
                >
                  <Code className="h-4 w-4" />
                  API Playground
                  {!(
                    user.subscriptionTier === "starter" ||
                    user.subscriptionTier === "growth" ||
                    user.subscriptionTier === "enterprise" ||
                    user.role === "admin"
                  ) && (
                    <Badge variant="outline" className="ml-2">
                      Locked
                    </Badge>
                  )}
                </Button>
              </div>
            </CardContent>
          </Card>
        </div>
      </div>
    </div>
  )
}


--------------------------------------------------------------------------------
FILE: app/services/page.tsx
--------------------------------------------------------------------------------
"use client"

import { SiteHeader } from "@/components/site-header"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Button } from "@/components/ui/button"
import Link from "next/link"
import {
  Calculator,
  BarChart3,
  Settings,
  Users,
  ArrowRight,
  CheckCircle,
  MessageCircle,
  BookOpen,
  Wrench,
} from "lucide-react"

export default function ServicesPage() {
  const services = [
    {
      icon: <Calculator className="h-8 w-8 text-blue-500" />,
      title: "Energy Simulation",
      description: "Model your energy systems with our easy-to-use simulation platform.",
      features: ["Solar & battery modeling", "Load forecasting", "Cost analysis", "Weather integration"],
      cta: "Try Free Simulation",
      link: "/simulation",
    },
    {
      icon: <BarChart3 className="h-8 w-8 text-green-500" />,
      title: "Custom Analysis",
      description: "Get detailed reports and insights tailored to your specific needs.",
      features: ["Custom reporting", "ROI analysis", "Performance optimization", "Trend analysis"],
      cta: "Contact Us",
      link: "/contact",
    },
    {
      icon: <Settings className="h-8 w-8 text-purple-500" />,
      title: "API Integration",
      description: "Connect VoltSphere with your existing systems and workflows.",
      features: ["RESTful API", "Real-time data", "Custom integrations", "Developer support"],
      cta: "View API Docs",
      link: "/simulation/api",
    },
    {
      icon: <Users className="h-8 w-8 text-orange-500" />,
      title: "Training & Support",
      description: "Get the most out of VoltSphere with our training and support services.",
      features: ["Live training sessions", "24/7 support", "Best practices guide", "Community access"],
      cta: "Get Support",
      link: "/contact",
    },
  ]

  const supportOptions = [
    {
      icon: <MessageCircle className="h-6 w-6 text-blue-500" />,
      title: "Live Chat",
      description: "Get instant help from our support team",
      availability: "24/7",
    },
    {
      icon: <BookOpen className="h-6 w-6 text-green-500" />,
      title: "Documentation",
      description: "Comprehensive guides and tutorials",
      availability: "Always available",
    },
    {
      icon: <Wrench className="h-6 w-6 text-purple-500" />,
      title: "Custom Setup",
      description: "We'll help configure VoltSphere for your needs",
      availability: "By appointment",
    },
  ]

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50/50 via-white to-purple-50/50">
      <SiteHeader />

      {/* Hero Section */}
      <section className="section-padding">
        <div className="container-padding">
          <div className="text-center max-w-3xl mx-auto animate-fade-in">
            <Badge className="mb-6 bg-gradient-to-r from-blue-500 to-purple-500 text-white px-4 py-2">
              Our Services
            </Badge>

            <h1 className="text-4xl md:text-5xl font-bold mb-6 text-gray-900">
              Everything You Need for
              <span className="bg-gradient-to-r from-blue-500 to-purple-500 bg-clip-text text-transparent">
                {" "}
                Energy Success
              </span>
            </h1>

            <p className="text-lg md:text-xl text-gray-600 leading-relaxed">
              From simple simulations to enterprise integrations, we've got you covered.
            </p>
          </div>
        </div>
      </section>

      {/* Services Grid */}
      <section className="section-padding bg-white/70">
        <div className="container-padding">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
            {services.map((service, index) => (
              <Card
                key={index}
                className="border-0 shadow-lg hover:shadow-xl transition-all duration-300 bg-white/80 backdrop-blur-sm animate-scale-in"
                style={{ animationDelay: `${index * 0.1}s` }}
              >
                <CardHeader>
                  <div className="flex items-center gap-4 mb-4">
                    <div className="w-16 h-16 rounded-xl bg-gray-50 flex items-center justify-center">
                      {service.icon}
                    </div>
                    <div>
                      <CardTitle className="text-2xl font-bold text-gray-900">{service.title}</CardTitle>
                    </div>
                  </div>
                  <p className="text-gray-600 leading-relaxed">{service.description}</p>
                </CardHeader>
                <CardContent>
                  <div className="space-y-3 mb-6">
                    {service.features.map((feature, featureIndex) => (
                      <div key={featureIndex} className="flex items-center gap-3">
                        <CheckCircle className="h-5 w-5 text-green-500 flex-shrink-0" />
                        <span className="text-gray-700">{feature}</span>
                      </div>
                    ))}
                  </div>
                  <Button
                    asChild
                    className="w-full bg-gradient-to-r from-blue-500 to-purple-500 hover:from-blue-600 hover:to-purple-600"
                  >
                    <Link href={service.link}>
                      {service.cta}
                      <ArrowRight className="ml-2 h-4 w-4" />
                    </Link>
                  </Button>
                </CardContent>
              </Card>
            ))}
          </div>
        </div>
      </section>

      {/* Support Section */}
      <section className="section-padding">
        <div className="container-padding">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold mb-4 text-gray-900">We're Here to Help</h2>
            <p className="text-lg text-gray-600 max-w-2xl mx-auto">
              Multiple ways to get the support you need, when you need it.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {supportOptions.map((option, index) => (
              <Card
                key={index}
                className="border-0 shadow-lg bg-white/80 backdrop-blur-sm text-center animate-scale-in"
                style={{ animationDelay: `${index * 0.1}s` }}
              >
                <CardContent className="p-8">
                  <div className="w-16 h-16 rounded-xl bg-gray-50 flex items-center justify-center mx-auto mb-4">
                    {option.icon}
                  </div>
                  <h3 className="text-xl font-semibold text-gray-900 mb-2">{option.title}</h3>
                  <p className="text-gray-600 mb-4">{option.description}</p>
                  <Badge variant="secondary" className="bg-blue-50 text-blue-700">
                    {option.availability}
                  </Badge>
                </CardContent>
              </Card>
            ))}
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="section-padding bg-gradient-to-r from-blue-500 via-purple-500 to-indigo-500">
        <div className="container-padding">
          <div className="text-center text-white max-w-3xl mx-auto">
            <h2 className="text-3xl md:text-4xl font-bold mb-6">Ready to Get Started?</h2>
            <p className="text-lg md:text-xl mb-8 opacity-90">
              Choose the service that's right for you, or contact us to discuss your specific needs.
            </p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <Button asChild size="lg" className="bg-white text-blue-600 hover:bg-gray-100 font-semibold px-8">
                <Link href="/simulation">
                  Start Free Trial
                  <ArrowRight className="ml-2 h-5 w-5" />
                </Link>
              </Button>
              <Button asChild variant="outline" size="lg" className="border-white/30 text-white hover:bg-white/10 px-8">
                <Link href="/contact">Talk to Us</Link>
              </Button>
            </div>
          </div>
        </div>
      </section>
    </div>
  )
}


--------------------------------------------------------------------------------
FILE: app/simulation/api/page.tsx
--------------------------------------------------------------------------------
"use client"

import { useState } from "react"
import { SiteHeader } from "@/components/site-header"
import { SimulationNav } from "@/components/simulation/simulation-nav"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
import { Badge } from "@/components/ui/badge"
import { Code, Key, Book, Activity, Copy, CheckCircle, ChevronLeft, ChevronRight } from "lucide-react"
import { useAuth } from "@/lib/auth-context"

// Static code examples to avoid template literal issues
const CURL_EXAMPLE = `curl -X POST https://api.voltsphere.com/v1/simulate \\
-H "Authorization: Bearer vs_sk_1234567890abcdef" \\
-H "Content-Type: application/json" \\
-d '{
  "batteryCapacity": 15,
  "solarCapacity": 8,
  "loadProfile": "residential",
  "location": "San Francisco, CA",
  "duration": "24h"
}'`

const JS_EXAMPLE = `const response = await fetch('https://api.voltsphere.com/v1/simulate', {
  method: 'POST',
  headers: {
    'Authorization': 'Bearer vs_sk_1234567890abcdef',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    batteryCapacity: 15,
    solarCapacity: 8,
    loadProfile: "residential",
    location: "San Francisco, CA",
    duration: "24h"
  })
});

const data = await response.json();
console.log(data);`

const PYTHON_EXAMPLE = `import requests

url = "https://api.voltsphere.com/v1/simulate"
headers = {
  "Authorization": f"Bearer vs_sk_1234567890abcdef",
  "Content-Type": "application/json"
}
data = {
  "batteryCapacity": 15,
  "solarCapacity": 8,
  "loadProfile": "residential",
  "location": "San Francisco, CA",
  "duration": "24h"
}

response = requests.post(url, headers=headers, json=data)
result = response.json()
print(result)`

// Static API examples
const API_EXAMPLES = [
  {
    title: "Basic Residential Simulation",
    description: "Simple home energy system with solar and battery",
    code: `{
  "batteryCapacity": 15,
  "solarCapacity": 8,
  "loadProfile": "residential",
  "location": "San Francisco, CA",
  "duration": "24h"
}`,
  },
  {
    title: "Commercial Building Analysis",
    description: "Office building with peak demand management",
    code: `{
  "batteryCapacity": 50,
  "solarCapacity": 25,
  "loadProfile": "commercial",
  "timeOfUseRates": true,
  "peakShaving": true,
  "location": "New York, NY"
}`,
  },
]

export default function APIPage() {
  const { user } = useAuth()
  const [apiKey] = useState("vs_sk_1234567890abcdef")
  const [copied, setCopied] = useState(false)
  const [currentExample, setCurrentExample] = useState(0)

  const copyToClipboard = (text: string) => {
    navigator.clipboard.writeText(text)
    setCopied(true)
    setTimeout(() => setCopied(false), 2000)
  }

  const nextExample = () => {
    setCurrentExample((prev) => (prev + 1) % API_EXAMPLES.length)
  }

  const prevExample = () => {
    setCurrentExample((prev) => (prev - 1 + API_EXAMPLES.length) % API_EXAMPLES.length)
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-50 via-blue-50 to-purple-50">
      <SiteHeader />

      <div className="container mx-auto py-8">
        {/* Header */}
        <div className="text-center mb-8">
          <div className="flex items-center justify-center gap-2 mb-4">
            <Code className="h-8 w-8 text-blue-600" />
            <h1 className="text-3xl font-bold text-gray-800">VoltSphere API</h1>
            <Badge className="bg-gradient-to-r from-blue-600 to-purple-600 text-white">API</Badge>
          </div>
          <p className="text-lg text-gray-600 max-w-4xl mx-auto">
            Integrate powerful microgrid simulation capabilities directly into your applications with our RESTful API.
          </p>
        </div>

        {/* Navigation */}
        <div className="mb-8">
          <SimulationNav userTier={user?.subscriptionTier || "free"} />
        </div>

        {/* Main Content */}
        <Tabs defaultValue="overview" className="space-y-6">
          <TabsList className="grid w-full grid-cols-5">
            <TabsTrigger value="overview" className="flex items-center gap-2">
              <Book className="h-4 w-4" />
              Overview
            </TabsTrigger>
            <TabsTrigger value="authentication" className="flex items-center gap-2">
              <Key className="h-4 w-4" />
              Authentication
            </TabsTrigger>
            <TabsTrigger value="endpoints" className="flex items-center gap-2">
              <Activity className="h-4 w-4" />
              Endpoints
            </TabsTrigger>
            <TabsTrigger value="examples" className="flex items-center gap-2">
              <Code className="h-4 w-4" />
              Examples
            </TabsTrigger>
            <TabsTrigger value="scenarios" className="flex items-center gap-2">
              <Activity className="h-4 w-4" />
              Use Cases
            </TabsTrigger>
          </TabsList>

          {/* Overview Tab */}
          <TabsContent value="overview">
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
              <Card>
                <CardHeader>
                  <CardTitle className="flex items-center gap-2">
                    <Activity className="h-5 w-5 text-blue-600" />
                    Getting Started
                  </CardTitle>
                </CardHeader>
                <CardContent className="space-y-4">
                  <p className="text-gray-600">
                    The VoltSphere API allows you to run microgrid simulations programmatically.
                  </p>
                  <ul className="space-y-2 text-gray-600">
                    <li className="flex items-center gap-2">
                      <CheckCircle className="h-4 w-4 text-green-600" />
                      Batch processing multiple scenarios
                    </li>
                    <li className="flex items-center gap-2">
                      <CheckCircle className="h-4 w-4 text-green-600" />
                      Integration with existing workflows
                    </li>
                  </ul>
                </CardContent>
              </Card>

              <Card>
                <CardHeader>
                  <CardTitle className="flex items-center gap-2">
                    <Key className="h-5 w-5 text-purple-600" />
                    API Limits
                  </CardTitle>
                </CardHeader>
                <CardContent className="space-y-4">
                  <div className="space-y-3">
                    <div className="flex justify-between items-center p-3 bg-blue-50 rounded-lg">
                      <span className="font-medium">Starter Plan</span>
                      <Badge variant="outline">5,000 calls/month</Badge>
                    </div>
                    <div className="flex justify-between items-center p-3 bg-purple-50 rounded-lg">
                      <span className="font-medium">Growth Plan</span>
                      <Badge variant="outline">50,000 calls/month</Badge>
                    </div>
                  </div>
                </CardContent>
              </Card>
            </div>
          </TabsContent>

          {/* Authentication Tab */}
          <TabsContent value="authentication">
            <Card>
              <CardHeader>
                <CardTitle className="flex items-center gap-2">
                  <Key className="h-5 w-5 text-blue-600" />
                  API Authentication
                </CardTitle>
              </CardHeader>
              <CardContent className="space-y-6">
                <div>
                  <h3 className="text-lg font-semibold mb-3">Your API Key</h3>
                  <div className="flex items-center gap-2">
                    <Input value={apiKey} readOnly className="font-mono text-sm" />
                    <Button onClick={() => copyToClipboard(apiKey)} variant="outline" size="sm">
                      {copied ? <CheckCircle className="h-4 w-4" /> : <Copy className="h-4 w-4" />}
                    </Button>
                  </div>
                </div>
              </CardContent>
            </Card>
          </TabsContent>

          {/* Endpoints Tab */}
          <TabsContent value="endpoints">
            <Card>
              <CardHeader>
                <CardTitle>POST /simulate</CardTitle>
                <p className="text-gray-600">Run a microgrid simulation with specified parameters</p>
              </CardHeader>
              <CardContent>
                <p>See documentation for details</p>
              </CardContent>
            </Card>
          </TabsContent>

          {/* Examples Tab */}
          <TabsContent value="examples">
            <Card>
              <CardHeader>
                <CardTitle>Code Examples</CardTitle>
                <p className="text-gray-600">Ready-to-use code snippets in popular languages</p>
              </CardHeader>
              <CardContent>
                <Tabs defaultValue="curl" className="space-y-4">
                  <TabsList>
                    <TabsTrigger value="curl">cURL</TabsTrigger>
                    <TabsTrigger value="javascript">JavaScript</TabsTrigger>
                    <TabsTrigger value="python">Python</TabsTrigger>
                  </TabsList>

                  <TabsContent value="curl">
                    <div className="relative">
                      <pre className="bg-gray-900 text-gray-100 p-4 rounded-lg text-sm overflow-x-auto">
                        <code>{CURL_EXAMPLE}</code>
                      </pre>
                      <Button
                        onClick={() => copyToClipboard(CURL_EXAMPLE)}
                        variant="outline"
                        size="sm"
                        className="absolute top-2 right-2"
                      >
                        {copied ? <CheckCircle className="h-4 w-4" /> : <Copy className="h-4 w-4" />}
                      </Button>
                    </div>
                  </TabsContent>

                  <TabsContent value="javascript">
                    <div className="relative">
                      <pre className="bg-gray-900 text-gray-100 p-4 rounded-lg text-sm overflow-x-auto">
                        <code>{JS_EXAMPLE}</code>
                      </pre>
                      <Button
                        onClick={() => copyToClipboard(JS_EXAMPLE)}
                        variant="outline"
                        size="sm"
                        className="absolute top-2 right-2"
                      >
                        {copied ? <CheckCircle className="h-4 w-4" /> : <Copy className="h-4 w-4" />}
                      </Button>
                    </div>
                  </TabsContent>

                  <TabsContent value="python">
                    <div className="relative">
                      <pre className="bg-gray-900 text-gray-100 p-4 rounded-lg text-sm overflow-x-auto">
                        <code>{PYTHON_EXAMPLE}</code>
                      </pre>
                      <Button
                        onClick={() => copyToClipboard(PYTHON_EXAMPLE)}
                        variant="outline"
                        size="sm"
                        className="absolute top-2 right-2"
                      >
                        {copied ? <CheckCircle className="h-4 w-4" /> : <Copy className="h-4 w-4" />}
                      </Button>
                    </div>
                  </TabsContent>
                </Tabs>
              </CardContent>
            </Card>
          </TabsContent>

          {/* Use Cases Carousel Tab */}
          <TabsContent value="scenarios">
            <Card>
              <CardHeader>
                <CardTitle className="flex items-center justify-between">
                  <span>API Use Case Examples</span>
                  <div className="flex items-center gap-2">
                    <Button onClick={prevExample} variant="outline" size="sm">
                      <ChevronLeft className="h-4 w-4" />
                    </Button>
                    <span className="text-sm text-gray-500">
                      {currentExample + 1} of {API_EXAMPLES.length}
                    </span>
                    <Button onClick={nextExample} variant="outline" size="sm">
                      <ChevronRight className="h-4 w-4" />
                    </Button>
                  </div>
                </CardTitle>
              </CardHeader>
              <CardContent>
                <div className="space-y-4">
                  <div className="text-center">
                    <h3 className="text-xl font-semibold text-gray-800 mb-2">{API_EXAMPLES[currentExample].title}</h3>
                    <p className="text-gray-600 mb-4">{API_EXAMPLES[currentExample].description}</p>
                  </div>

                  <div className="relative">
                    <pre className="bg-gray-900 text-gray-100 p-4 rounded-lg text-sm overflow-x-auto">
                      <code>{API_EXAMPLES[currentExample].code}</code>
                    </pre>
                    <Button
                      onClick={() => copyToClipboard(API_EXAMPLES[currentExample].code)}
                      variant="outline"
                      size="sm"
                      className="absolute top-2 right-2"
                    >
                      {copied ? <CheckCircle className="h-4 w-4" /> : <Copy className="h-4 w-4" />}
                    </Button>
                  </div>
                </div>
              </CardContent>
            </Card>
          </TabsContent>
        </Tabs>
      </div>
    </div>
  )
}


--------------------------------------------------------------------------------
FILE: app/simulation/enterprise/page.tsx
--------------------------------------------------------------------------------
"use client"

import { useState } from "react"
import { useAuth } from "@/lib/auth-context"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
import { Label } from "@/components/ui/label"
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select"
import { Slider } from "@/components/ui/slider"
import { Switch } from "@/components/ui/switch"
import {
  Crown,
  Book,
  TrendingUp,
  Zap,
  Building2,
  Users,
  Shield,
  Database,
  Cloud,
  BarChart3,
  Download,
  Share2,
} from "lucide-react"

export default function EnterprisePage() {
  const { user } = useAuth()
  const [activeTab, setActiveTab] = useState("overview")
  const [simulationData, setSimulationData] = useState({
    capacity: [5000],
    efficiency: [95],
    location: "",
    weatherPattern: "realistic",
    loadProfile: "commercial",
    batteryType: "lithium-ion",
    gridConnection: true,
    backupPower: true,
    peakShaving: true,
    demandResponse: true,
  })

  const enterpriseFeatures = [
    {
      icon: Building2,
      title: "Multi-Site Management",
      description:
        "Manage and simulate multiple microgrid installations across different locations with centralized control.",
    },
    {
      icon: Users,
      title: "Team Collaboration",
      description: "Advanced user management with role-based access control and team collaboration features.",
    },
    {
      icon: Shield,
      title: "Enterprise Security",
      description: "SOC 2 compliance, SSO integration, and advanced security features for enterprise environments.",
    },
    {
      icon: Database,
      title: "Advanced Analytics",
      description: "Deep dive analytics with custom reporting, data export, and integration with BI tools.",
    },
    {
      icon: Cloud,
      title: "API & Integrations",
      description: "Full API access with webhooks, third-party integrations, and custom development support.",
    },
    {
      icon: BarChart3,
      title: "Custom Modeling",
      description: "Build custom simulation models with advanced parameters and proprietary algorithms.",
    },
  ]

  const simulationResults = {
    annualGeneration: 8750,
    costSavings: 125000,
    co2Reduction: 4.2,
    paybackPeriod: 6.8,
    roi: 18.5,
    peakDemandReduction: 35,
  }

  return (
    <div className="page-container">
      <div className="section-padding">
        {/* Header */}
        <div className="text-center mb-12">
          <div className="flex items-center justify-center gap-2 mb-4">
            <Crown className="h-8 w-8 text-yellow-500" />
            <Badge
              variant="secondary"
              className="bg-gradient-to-r from-yellow-100 to-orange-100 text-yellow-800 border-yellow-200"
            >
              Enterprise
            </Badge>
          </div>
          <h1 className="text-4xl font-bold mb-4 bg-gradient-to-r from-gray-900 to-gray-600 bg-clip-text text-transparent">
            Enterprise Microgrid Simulation
          </h1>
          <p className="text-xl text-gray-600 max-w-3xl mx-auto text-content">
            Advanced simulation platform for large-scale microgrid deployments with enterprise-grade features and
            unlimited customization.
          </p>
        </div>

        {/* Features Grid */}
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6 mb-12">
          {enterpriseFeatures.map((feature, index) => (
            <Card key={index} className="border-2 hover:border-yellow-200 transition-colors">
              <CardHeader className="card-padding-sm">
                <div className="flex items-center gap-3 mb-2">
                  <div className="p-2 bg-yellow-100 rounded-lg">
                    <feature.icon className="h-5 w-5 text-yellow-600" />
                  </div>
                  <CardTitle className="text-lg">{feature.title}</CardTitle>
                </div>
                <CardDescription className="text-content">{feature.description}</CardDescription>
              </CardHeader>
            </Card>
          ))}
        </div>

        {/* Main Simulation Interface */}
        <Card className="border-2">
          <CardHeader className="card-padding">
            <div className="flex items-center justify-between">
              <div>
                <CardTitle className="text-2xl flex items-center gap-2">
                  <Zap className="h-6 w-6 text-yellow-500" />
                  Enterprise Simulation Console
                </CardTitle>
                <CardDescription className="text-content">
                  Advanced microgrid modeling with enterprise-grade features
                </CardDescription>
              </div>
              <div className="flex gap-2">
                <Button variant="outline" size="sm">
                  <Download className="h-4 w-4 mr-2" />
                  Export
                </Button>
                <Button variant="outline" size="sm">
                  <Share2 className="h-4 w-4 mr-2" />
                  Share
                </Button>
              </div>
            </div>
          </CardHeader>
          <CardContent className="card-padding">
            <Tabs value={activeTab} onValueChange={setActiveTab}>
              <TabsList className="grid w-full grid-cols-4 mb-6">
                <TabsTrigger value="overview">Overview</TabsTrigger>
                <TabsTrigger value="configuration">Configuration</TabsTrigger>
                <TabsTrigger value="analytics">Analytics</TabsTrigger>
                <TabsTrigger value="reports">Reports</TabsTrigger>
              </TabsList>

              <TabsContent value="overview" className="space-y-6">
                {/* Key Metrics */}
                <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-4">
                  <Card>
                    <CardContent className="card-padding-sm text-center">
                      <div className="text-2xl font-bold text-green-600">
                        {simulationResults.annualGeneration.toLocaleString()}
                      </div>
                      <div className="text-sm text-gray-600">kWh/year</div>
                    </CardContent>
                  </Card>
                  <Card>
                    <CardContent className="card-padding-sm text-center">
                      <div className="text-2xl font-bold text-blue-600">
                        ${simulationResults.costSavings.toLocaleString()}
                      </div>
                      <div className="text-sm text-gray-600">Annual Savings</div>
                    </CardContent>
                  </Card>
                  <Card>
                    <CardContent className="card-padding-sm text-center">
                      <div className="text-2xl font-bold text-purple-600">{simulationResults.co2Reduction}</div>
                      <div className="text-sm text-gray-600">tons CO₂/year</div>
                    </CardContent>
                  </Card>
                  <Card>
                    <CardContent className="card-padding-sm text-center">
                      <div className="text-2xl font-bold text-orange-600">{simulationResults.paybackPeriod}</div>
                      <div className="text-sm text-gray-600">years payback</div>
                    </CardContent>
                  </Card>
                  <Card>
                    <CardContent className="card-padding-sm text-center">
                      <div className="text-2xl font-bold text-red-600">{simulationResults.roi}%</div>
                      <div className="text-sm text-gray-600">ROI</div>
                    </CardContent>
                  </Card>
                  <Card>
                    <CardContent className="card-padding-sm text-center">
                      <div className="text-2xl font-bold text-indigo-600">{simulationResults.peakDemandReduction}%</div>
                      <div className="text-sm text-gray-600">Peak Reduction</div>
                    </CardContent>
                  </Card>
                </div>

                {/* Chart Placeholder */}
                <Card>
                  <CardHeader className="card-padding-sm">
                    <CardTitle>Energy Flow Analysis</CardTitle>
                  </CardHeader>
                  <CardContent className="card-padding">
                    <div className="h-64 bg-gradient-to-br from-gray-50 to-gray-100 rounded-lg flex items-center justify-center">
                      <div className="text-center text-content">
                        <BarChart3 className="h-12 w-12 text-gray-400 mx-auto mb-2" />
                        <p className="text-gray-600">Advanced energy flow visualization</p>
                        <p className="text-sm text-gray-500">Real-time data integration available</p>
                      </div>
                    </div>
                  </CardContent>
                </Card>
              </TabsContent>

              <TabsContent value="configuration" className="space-y-6">
                <div className="grid md:grid-cols-2 gap-6">
                  <Card>
                    <CardHeader className="card-padding-sm">
                      <CardTitle>System Configuration</CardTitle>
                    </CardHeader>
                    <CardContent className="card-padding space-y-4">
                      <div>
                        <Label htmlFor="capacity">System Capacity (kW)</Label>
                        <Slider
                          id="capacity"
                          min={1000}
                          max={50000}
                          step={500}
                          value={simulationData.capacity}
                          onValueChange={(value) => setSimulationData({ ...simulationData, capacity: value })}
                          className="mt-2"
                        />
                        <div className="text-sm text-gray-600 mt-1">
                          {simulationData.capacity[0].toLocaleString()} kW
                        </div>
                      </div>

                      <div>
                        <Label htmlFor="efficiency">System Efficiency (%)</Label>
                        <Slider
                          id="efficiency"
                          min={80}
                          max={98}
                          step={1}
                          value={simulationData.efficiency}
                          onValueChange={(value) => setSimulationData({ ...simulationData, efficiency: value })}
                          className="mt-2"
                        />
                        <div className="text-sm text-gray-600 mt-1">{simulationData.efficiency[0]}%</div>
                      </div>

                      <div>
                        <Label htmlFor="location">Location</Label>
                        <Select
                          value={simulationData.location}
                          onValueChange={(value) => setSimulationData({ ...simulationData, location: value })}
                        >
                          <SelectTrigger>
                            <SelectValue placeholder="Select location" />
                          </SelectTrigger>
                          <SelectContent>
                            <SelectItem value="california">California, USA</SelectItem>
                            <SelectItem value="texas">Texas, USA</SelectItem>
                            <SelectItem value="florida">Florida, USA</SelectItem>
                            <SelectItem value="germany">Germany</SelectItem>
                            <SelectItem value="australia">Australia</SelectItem>
                            <SelectItem value="custom">Custom Location</SelectItem>
                          </SelectContent>
                        </Select>
                      </div>
                    </CardContent>
                  </Card>

                  <Card>
                    <CardHeader className="card-padding-sm">
                      <CardTitle>Advanced Features</CardTitle>
                    </CardHeader>
                    <CardContent className="card-padding space-y-4">
                      <div className="flex items-center justify-between">
                        <Label htmlFor="grid-connection">Grid Connection</Label>
                        <Switch
                          id="grid-connection"
                          checked={simulationData.gridConnection}
                          onCheckedChange={(checked) =>
                            setSimulationData({ ...simulationData, gridConnection: checked })
                          }
                        />
                      </div>

                      <div className="flex items-center justify-between">
                        <Label htmlFor="backup-power">Backup Power</Label>
                        <Switch
                          id="backup-power"
                          checked={simulationData.backupPower}
                          onCheckedChange={(checked) => setSimulationData({ ...simulationData, backupPower: checked })}
                        />
                      </div>

                      <div className="flex items-center justify-between">
                        <Label htmlFor="peak-shaving">Peak Shaving</Label>
                        <Switch
                          id="peak-shaving"
                          checked={simulationData.peakShaving}
                          onCheckedChange={(checked) => setSimulationData({ ...simulationData, peakShaving: checked })}
                        />
                      </div>

                      <div className="flex items-center justify-between">
                        <Label htmlFor="demand-response">Demand Response</Label>
                        <Switch
                          id="demand-response"
                          checked={simulationData.demandResponse}
                          onCheckedChange={(checked) =>
                            setSimulationData({ ...simulationData, demandResponse: checked })
                          }
                        />
                      </div>
                    </CardContent>
                  </Card>
                </div>
              </TabsContent>

              <TabsContent value="analytics" className="space-y-6">
                <div className="grid md:grid-cols-2 gap-6">
                  <Card>
                    <CardHeader className="card-padding-sm">
                      <CardTitle>Performance Analytics</CardTitle>
                    </CardHeader>
                    <CardContent className="card-padding">
                      <div className="h-48 bg-gradient-to-br from-blue-50 to-indigo-100 rounded-lg flex items-center justify-center">
                        <div className="text-center text-content">
                          <TrendingUp className="h-8 w-8 text-blue-500 mx-auto mb-2" />
                          <p className="text-blue-700">Advanced Performance Metrics</p>
                        </div>
                      </div>
                    </CardContent>
                  </Card>

                  <Card>
                    <CardHeader className="card-padding-sm">
                      <CardTitle>Financial Analysis</CardTitle>
                    </CardHeader>
                    <CardContent className="card-padding">
                      <div className="h-48 bg-gradient-to-br from-green-50 to-emerald-100 rounded-lg flex items-center justify-center">
                        <div className="text-center text-content">
                          <BarChart3 className="h-8 w-8 text-green-500 mx-auto mb-2" />
                          <p className="text-green-700">ROI & Cost Analysis</p>
                        </div>
                      </div>
                    </CardContent>
                  </Card>
                </div>
              </TabsContent>

              <TabsContent value="reports" className="space-y-6">
                <Card>
                  <CardHeader className="card-padding-sm">
                    <CardTitle>Custom Reports</CardTitle>
                    <CardDescription className="text-content">
                      Generate detailed reports for stakeholders and compliance
                    </CardDescription>
                  </CardHeader>
                  <CardContent className="card-padding">
                    <div className="grid md:grid-cols-3 gap-4">
                      <Button variant="outline" className="h-24 flex-col">
                        <Book className="h-6 w-6 mb-2" />
                        Technical Report
                      </Button>
                      <Button variant="outline" className="h-24 flex-col">
                        <BarChart3 className="h-6 w-6 mb-2" />
                        Financial Analysis
                      </Button>
                      <Button variant="outline" className="h-24 flex-col">
                        <Shield className="h-6 w-6 mb-2" />
                        Compliance Report
                      </Button>
                    </div>
                  </CardContent>
                </Card>
              </TabsContent>
            </Tabs>
          </CardContent>
        </Card>

        {/* CTA Section */}
        <Card className="bg-gradient-to-r from-yellow-50 to-orange-50 border-yellow-200 mt-12">
          <CardContent className="card-padding text-center">
            <Crown className="h-12 w-12 text-yellow-500 mx-auto mb-4" />
            <h3 className="text-2xl font-bold mb-4">Ready for Enterprise-Grade Simulation?</h3>
            <p className="text-gray-600 mb-6 max-w-2xl mx-auto text-content">
              Contact our enterprise team to discuss custom implementations, dedicated support, and volume pricing.
            </p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <Button size="lg" className="button-primary">
                <Users className="h-5 w-5 mr-2" />
                Contact Enterprise Sales
              </Button>
              <Button variant="outline" size="lg" className="button-outline">
                <Book className="h-5 w-5 mr-2" />
                View Documentation
              </Button>
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  )
}


--------------------------------------------------------------------------------
FILE: app/simulation/growth/page.tsx
--------------------------------------------------------------------------------
"use client"

import { useState, useEffect } from "react"
import { useRouter } from "next/navigation"
import { SiteHeader } from "@/components/site-header"
import { SimulationNav } from "@/components/simulation/simulation-nav"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
import { Badge } from "@/components/ui/badge"
import { Zap, Key, Book, Activity, Copy, CheckCircle, ChevronLeft, ChevronRight, TrendingUp } from "lucide-react"
import { useAuth } from "@/lib/auth-context"

// Static code examples to avoid template literal issues
const CURL_EXAMPLE = `curl -X POST https://api.voltsphere.com/v1/simulate \\
-H "Authorization: Bearer vs_sk_growth_1234567890abcdef" \\
-H "Content-Type: application/json" \\
-d '{
  "sites": [
    {
      "id": "site_1",
      "batteryCapacity": 100,
      "solarCapacity": 60,
      "loadProfile": "commercial",
      "location": "San Francisco, CA"
    },
    {
      "id": "site_2", 
      "batteryCapacity": 80,
      "solarCapacity": 50,
      "loadProfile": "commercial",
      "location": "Los Angeles, CA"
    }
  ],
  "portfolioOptimization": true,
  "demandResponse": true,
  "duration": "30d"
}'`

const JS_EXAMPLE = `const response = await fetch('https://api.voltsphere.com/v1/simulate', {
  method: 'POST',
  headers: {
    'Authorization': 'Bearer vs_sk_growth_1234567890abcdef',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    sites: [
      {
        id: "site_1",
        batteryCapacity: 100,
        solarCapacity: 60,
        loadProfile: "commercial",
        location: "San Francisco, CA"
      },
      {
        id: "site_2",
        batteryCapacity: 80,
        solarCapacity: 50,
        loadProfile: "commercial",
        location: "Los Angeles, CA"
      }
    ],
    portfolioOptimization: true,
    demandResponse: true,
    duration: "30d"
  })
});

const data = await response.json();
console.log(data);`

const PYTHON_EXAMPLE = `import requests

url = "https://api.voltsphere.com/v1/simulate"
headers = {
  "Authorization": f"Bearer vs_sk_growth_1234567890abcdef",
  "Content-Type": "application/json"
}
data = {
  "sites": [
    {
      "id": "site_1",
      "batteryCapacity": 100,
      "solarCapacity": 60,
      "loadProfile": "commercial",
      "location": "San Francisco, CA"
    },
    {
      "id": "site_2", 
      "batteryCapacity": 80,
      "solarCapacity": 50,
      "loadProfile": "commercial",
      "location": "Los Angeles, CA"
    }
  ],
  "portfolioOptimization": True,
  "demandResponse": True,
  "duration": "30d"
}

response = requests.post(url, headers=headers, json=data)
result = response.json()
print(result)`

// Static API examples
const GROWTH_EXAMPLES = [
  {
    title: "Multi-Site Commercial Portfolio",
    description: "Analyze multiple commercial buildings as a portfolio",
    code: `{
  "sites": [
    {
      "id": "site_1",
      "batteryCapacity": 100,
      "solarCapacity": 60,
      "loadProfile": "commercial",
      "location": "San Francisco, CA"
    },
    {
      "id": "site_2", 
      "batteryCapacity": 80,
      "solarCapacity": 50,
      "loadProfile": "commercial",
      "location": "Los Angeles, CA"
    }
  ],
  "portfolioOptimization": true,
  "demandResponse": true,
  "duration": "30d"
}`,
  },
  {
    title: "Industrial Facility with Peak Shaving",
    description: "Large manufacturing plant with demand management",
    code: `{
  "batteryCapacity": 200,
  "solarCapacity": 120,
  "windCapacity": 50,
  "loadProfile": "industrial",
  "peakShaving": true,
  "demandChargeOptimization": true,
  "timeOfUseRates": true,
  "shiftSchedule": "3x8",
  "location": "Chicago, IL",
  "duration": "7d"
}`,
  },
]

export default function GrowthAPIPage() {
  const { user, isLoading } = useAuth()
  const router = useRouter()
  const [apiKey] = useState("vs_sk_growth_1234567890abcdef")
  const [copied, setCopied] = useState(false)
  const [currentExample, setCurrentExample] = useState(0)

  // Check access - Growth tier or higher
  useEffect(() => {
    if (
      !isLoading &&
      user?.subscriptionTier !== "growth" &&
      user?.subscriptionTier !== "enterprise" &&
      user?.role !== "admin"
    ) {
      router.push("/pricing")
    }
  }, [user, isLoading, router])

  if (isLoading) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-gray-50 via-blue-50 to-purple-50">
        <SiteHeader />
        <div className="container mx-auto py-8">
          <div className="flex items-center justify-center h-96">
            <div className="animate-spin rounded-full h-16 w-16 border-b-2 border-blue-600"></div>
          </div>
        </div>
      </div>
    )
  }

  if (user?.subscriptionTier !== "growth" && user?.subscriptionTier !== "enterprise" && user?.role !== "admin") {
    return (
      <div className="min-h-screen bg-gradient-to-br from-gray-50 via-blue-50 to-purple-50">
        <SiteHeader />
        <div className="container mx-auto py-8">
          <div className="text-center">
            <div className="flex items-center justify-center gap-2 mb-4">
              <Zap className="h-8 w-8 text-purple-600" />
              <h1 className="text-3xl font-bold text-gray-800">Growth API</h1>
              <Badge className="bg-gradient-to-r from-purple-600 to-pink-600 text-white">Growth</Badge>
            </div>
            <p className="text-lg text-gray-600 max-w-2xl mx-auto mb-8">
              Access to Growth API requires a Growth subscription or higher.
            </p>
            <Button
              onClick={() => router.push("/pricing")}
              className="bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700"
            >
              Upgrade to Growth
            </Button>
          </div>
        </div>
      </div>
    )
  }

  const copyToClipboard = (text: string) => {
    navigator.clipboard.writeText(text)
    setCopied(true)
    setTimeout(() => setCopied(false), 2000)
  }

  const nextExample = () => {
    setCurrentExample((prev) => (prev + 1) % GROWTH_EXAMPLES.length)
  }

  const prevExample = () => {
    setCurrentExample((prev) => (prev - 1 + GROWTH_EXAMPLES.length) % GROWTH_EXAMPLES.length)
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-50 via-blue-50 to-purple-50">
      <SiteHeader />

      <div className="container mx-auto py-8">
        {/* Header */}
        <div className="text-center mb-8">
          <div className="flex items-center justify-center gap-2 mb-4">
            <Zap className="h-8 w-8 text-purple-600" />
            <h1 className="text-3xl font-bold text-gray-800">Growth API</h1>
            <Badge className="bg-gradient-to-r from-purple-600 to-pink-600 text-white">Growth</Badge>
          </div>
          <p className="text-lg text-gray-600 max-w-4xl mx-auto">
            Advanced API capabilities for complex simulations, multi-site analysis, and enterprise-grade automation.
          </p>
        </div>

        {/* Navigation */}
        <div className="mb-8">
          <SimulationNav userTier={user?.subscriptionTier || "free"} />
        </div>

        {/* Main Content */}
        <Tabs defaultValue="overview" className="space-y-6">
          <TabsList className="grid w-full grid-cols-5">
            <TabsTrigger value="overview" className="flex items-center gap-2">
              <Book className="h-4 w-4" />
              Overview
            </TabsTrigger>
            <TabsTrigger value="authentication" className="flex items-center gap-2">
              <Key className="h-4 w-4" />
              Authentication
            </TabsTrigger>
            <TabsTrigger value="endpoints" className="flex items-center gap-2">
              <Activity className="h-4 w-4" />
              Endpoints
            </TabsTrigger>
            <TabsTrigger value="examples" className="flex items-center gap-2">
              <Zap className="h-4 w-4" />
              Examples
            </TabsTrigger>
            <TabsTrigger value="advanced" className="flex items-center gap-2">
              <TrendingUp className="h-4 w-4" />
              Advanced
            </TabsTrigger>
          </TabsList>

          {/* Overview Tab */}
          <TabsContent value="overview">
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
              <Card>
                <CardHeader>
                  <CardTitle className="flex items-center gap-2">
                    <Zap className="h-5 w-5 text-purple-600" />
                    Growth Features
                  </CardTitle>
                </CardHeader>
                <CardContent className="space-y-4">
                  <p className="text-gray-600">
                    The Growth API unlocks advanced simulation capabilities for complex projects:
                  </p>
                  <ul className="space-y-2 text-gray-600">
                    <li className="flex items-center gap-2">
                      <CheckCircle className="h-4 w-4 text-green-600" />
                      50,000 API calls per month
                    </li>
                    <li className="flex items-center gap-2">
                      <CheckCircle className="h-4 w-4 text-green-600" />
                      Multi-site portfolio analysis
                    </li>
                  </ul>
                </CardContent>
              </Card>

              <Card>
                <CardHeader>
                  <CardTitle className="flex items-center gap-2">
                    <TrendingUp className="h-5 w-5 text-pink-600" />
                    Enhanced Limits
                  </CardTitle>
                </CardHeader>
                <CardContent className="space-y-4">
                  <div className="space-y-3">
                    <div className="flex justify-between items-center p-3 bg-purple-50 rounded-lg">
                      <span className="font-medium">Monthly Calls</span>
                      <Badge variant="outline">50,000</Badge>
                    </div>
                    <div className="flex justify-between items-center p-3 bg-pink-50 rounded-lg">
                      <span className="font-medium">Rate Limit</span>
                      <Badge variant="outline">200/minute</Badge>
                    </div>
                  </div>
                </CardContent>
              </Card>
            </div>
          </TabsContent>

          {/* Authentication Tab */}
          <TabsContent value="authentication">
            <Card>
              <CardHeader>
                <CardTitle className="flex items-center gap-2">
                  <Key className="h-5 w-5 text-purple-600" />
                  Growth API Authentication
                </CardTitle>
              </CardHeader>
              <CardContent className="space-y-6">
                <div>
                  <h3 className="text-lg font-semibold mb-3">Your Growth API Key</h3>
                  <div className="flex items-center gap-2">
                    <Input value={apiKey} readOnly className="font-mono text-sm" />
                    <Button onClick={() => copyToClipboard(apiKey)} variant="outline" size="sm">
                      {copied ? <CheckCircle className="h-4 w-4" /> : <Copy className="h-4 w-4" />}
                    </Button>
                  </div>
                </div>
              </CardContent>
            </Card>
          </TabsContent>

          {/* Endpoints Tab */}
          <TabsContent value="endpoints">
            <Card>
              <CardHeader>
                <CardTitle>POST /simulate</CardTitle>
                <p className="text-gray-600">Advanced microgrid simulation with Growth tier features</p>
              </CardHeader>
              <CardContent>
                <p>See documentation for details</p>
              </CardContent>
            </Card>
          </TabsContent>

          {/* Examples Tab */}
          <TabsContent value="examples">
            <Card>
              <CardHeader>
                <CardTitle>Growth Code Examples</CardTitle>
                <p className="text-gray-600">Advanced simulation examples for complex use cases</p>
              </CardHeader>
              <CardContent>
                <Tabs defaultValue="curl" className="space-y-4">
                  <TabsList>
                    <TabsTrigger value="curl">cURL</TabsTrigger>
                    <TabsTrigger value="javascript">JavaScript</TabsTrigger>
                    <TabsTrigger value="python">Python</TabsTrigger>
                  </TabsList>

                  <TabsContent value="curl">
                    <div className="relative">
                      <pre className="bg-gray-900 text-gray-100 p-4 rounded-lg text-sm overflow-x-auto">
                        <code>{CURL_EXAMPLE}</code>
                      </pre>
                      <Button
                        onClick={() => copyToClipboard(CURL_EXAMPLE)}
                        variant="outline"
                        size="sm"
                        className="absolute top-2 right-2"
                      >
                        {copied ? <CheckCircle className="h-4 w-4" /> : <Copy className="h-4 w-4" />}
                      </Button>
                    </div>
                  </TabsContent>

                  <TabsContent value="javascript">
                    <div className="relative">
                      <pre className="bg-gray-900 text-gray-100 p-4 rounded-lg text-sm overflow-x-auto">
                        <code>{JS_EXAMPLE}</code>
                      </pre>
                      <Button
                        onClick={() => copyToClipboard(JS_EXAMPLE)}
                        variant="outline"
                        size="sm"
                        className="absolute top-2 right-2"
                      >
                        {copied ? <CheckCircle className="h-4 w-4" /> : <Copy className="h-4 w-4" />}
                      </Button>
                    </div>
                  </TabsContent>

                  <TabsContent value="python">
                    <div className="relative">
                      <pre className="bg-gray-900 text-gray-100 p-4 rounded-lg text-sm overflow-x-auto">
                        <code>{PYTHON_EXAMPLE}</code>
                      </pre>
                      <Button
                        onClick={() => copyToClipboard(PYTHON_EXAMPLE)}
                        variant="outline"
                        size="sm"
                        className="absolute top-2 right-2"
                      >
                        {copied ? <CheckCircle className="h-4 w-4" /> : <Copy className="h-4 w-4" />}
                      </Button>
                    </div>
                  </TabsContent>
                </Tabs>

                {/* Use Cases Carousel */}
                <div className="mt-8">
                  <Card className="border-2 border-purple-200">
                    <CardHeader>
                      <CardTitle className="flex items-center justify-between">
                        <span>Growth Use Cases</span>
                        <div className="flex items-center gap-2">
                          <Button onClick={prevExample} variant="outline" size="sm">
                            <ChevronLeft className="h-4 w-4" />
                          </Button>
                          <span className="text-sm text-gray-500">
                            {currentExample + 1} of {GROWTH_EXAMPLES.length}
                          </span>
                          <Button onClick={nextExample} variant="outline" size="sm">
                            <ChevronRight className="h-4 w-4" />
                          </Button>
                        </div>
                      </CardTitle>
                    </CardHeader>
                    <CardContent>
                      <div className="space-y-4">
                        <div className="text-center">
                          <h3 className="text-xl font-semibold text-gray-800 mb-2">
                            {GROWTH_EXAMPLES[currentExample].title}
                          </h3>
                          <p className="text-gray-600 mb-4">{GROWTH_EXAMPLES[currentExample].description}</p>
                        </div>

                        <div className="relative">
                          <pre className="bg-gray-900 text-gray-100 p-4 rounded-lg text-sm overflow-x-auto max-h-96">
                            <code>{GROWTH_EXAMPLES[currentExample].code}</code>
                          </pre>
                          <Button
                            onClick={() => copyToClipboard(GROWTH_EXAMPLES[currentExample].code)}
                            variant="outline"
                            size="sm"
                            className="absolute top-2 right-2"
                          >
                            {copied ? <CheckCircle className="h-4 w-4" /> : <Copy className="h-4 w-4" />}
                          </Button>
                        </div>
                      </div>
                    </CardContent>
                  </Card>
                </div>
              </CardContent>
            </Card>
          </TabsContent>

          {/* Advanced Features Tab */}
          <TabsContent value="advanced">
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
              <Card>
                <CardHeader>
                  <CardTitle className="flex items-center gap-2">
                    <TrendingUp className="h-5 w-5 text-purple-600" />
                    Advanced Capabilities
                  </CardTitle>
                </CardHeader>
                <CardContent className="space-y-4">
                  <div className="space-y-3">
                    <div className="p-3 bg-purple-50 rounded-lg">
                      <h4 className="font-semibold text-purple-800">Multi-Site Portfolio Analysis</h4>
                      <p className="text-sm text-purple-600">Analyze up to 50 sites as a unified portfolio</p>
                    </div>
                    <div className="p-3 bg-blue-50 rounded-lg">
                      <h4 className="font-semibold text-blue-800">Demand Response Optimization</h4>
                      <p className="text-sm text-blue-600">Automated participation in utility programs</p>
                    </div>
                  </div>
                </CardContent>
              </Card>

              <Card>
                <CardHeader>
                  <CardTitle className="flex items-center gap-2">
                    <Zap className="h-5 w-5 text-pink-600" />
                    Optimization Features
                  </CardTitle>
                </CardHeader>
                <CardContent className="space-y-4">
                  <div className="space-y-3">
                    <div className="p-3 bg-pink-50 rounded-lg">
                      <h4 className="font-semibold text-pink-800">Multi-Objective Optimization</h4>
                      <p className="text-sm text-pink-600">Cost, emissions, and resilience optimization</p>
                    </div>
                    <div className="p-3 bg-indigo-50 rounded-lg">
                      <h4 className="font-semibold text-indigo-800">Time-of-Use Rate Optimization</h4>
                      <p className="text-sm text-indigo-600">Dynamic pricing and demand charge management</p>
                    </div>
                  </div>
                </CardContent>
              </Card>
            </div>
          </TabsContent>
        </Tabs>
      </div>
    </div>
  )
}


--------------------------------------------------------------------------------
FILE: app/simulation/layout.tsx
--------------------------------------------------------------------------------
"use client"

import type React from "react"

export default function SimulationLayout({
  children,
}: {
  children: React.ReactNode
}) {
  // Removed all redirects and auth checks
  return <>{children}</>
}


--------------------------------------------------------------------------------
FILE: app/simulation/page.tsx
--------------------------------------------------------------------------------
"use client"

import { useState, useRef } from "react"
import { SiteHeader } from "@/components/site-header"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Slider } from "@/components/ui/slider"
import { Switch } from "@/components/ui/switch"
import { Label } from "@/components/ui/label"
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select"
import type { SimulationConfig } from "@/lib/simulation/engine"
import { Battery, Sun, Zap, Play, Settings, Lock } from "lucide-react"
import { SimulationEngine } from "@/lib/simulation/engine"
import { MicrogridChart } from "@/components/microgrid-chart"
import { useAuth } from "@/lib/auth-context"
import { LoginDialog } from "@/components/auth/login-dialog"

export default function SimulationPage() {
  const { user, loading } = useAuth() // FIXED: Get loading state
  const [showLoginDialog, setShowLoginDialog] = useState(false)
  const resultsRef = useRef<HTMLDivElement>(null)

  const [config, setConfig] = useState<SimulationConfig>({
    batteryCapacity: 15,
    batteryEfficiency: 90,
    solarEnabled: true,
    batteryType: "lithium",
    loadProfileType: "residential",
    useRealWeather: false,
    weatherLocation: "San Francisco, CA",
    timeOfUseRates: false,
    simulationDuration: "24h",
    solarCapacity: 10,
    inverterEfficiency: 96,
    systemLosses: 14,
    gridCostPerKwh: 0.15,
    solarCostPerWatt: 3.0,
    batteryCostPerKwh: 500,
    discountRate: 0.06,
    systemLifespan: 25,
  })

  const [isRunning, setIsRunning] = useState(false)
  const [results, setResults] = useState<any>(null)

  // FIXED: Completely prevent auto-login - require manual authentication
  const handleSimulationAccess = () => {
    console.log("handleSimulationAccess called, user:", user) // Debug log

    // FIXED: Explicitly check if user is null or undefined
    if (!user) {
      console.log("No user found, showing login dialog") // Debug log
      setShowLoginDialog(true)
      return
    }

    console.log("User found, running simulation") // Debug log
    runSimulation()
  }

  const runSimulation = async () => {
    // FIXED: Double-check user exists before running simulation
    if (!user) {
      setShowLoginDialog(true)
      return
    }

    setIsRunning(true)
    try {
      await new Promise((resolve) => setTimeout(resolve, 2000))
      const simulationResults = await SimulationEngine.runSimulation(config)
      setResults(simulationResults)

      setTimeout(() => {
        resultsRef.current?.scrollIntoView({
          behavior: "smooth",
          block: "start",
        })
      }, 500)
    } catch (error) {
      console.error("Simulation error:", error)
    } finally {
      setIsRunning(false)
    }
  }

  const updateConfig = (updates: Partial<SimulationConfig>) => {
    setConfig((prev) => ({ ...prev, ...updates }))
  }

  // FIXED: Show loading state while checking authentication
  if (loading) {
    return (
      <div className="min-h-screen bg-gradient-primary">
        <SiteHeader />
        <div className="container mx-auto px-8 py-12 text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto"></div>
          <p className="mt-4 text-gray-600">Loading...</p>
        </div>
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-gradient-primary">
      <SiteHeader />

      <section className="section-spacing-sm">
        <div className="container-clean">
          <div className="text-center mb-16 animate-fade-in">
            <div className="flex items-center justify-center gap-6 mb-8">
              <div className="relative">
                <div className="absolute inset-0 bg-gradient-to-r from-blue-400 to-purple-500 rounded-3xl blur-lg opacity-30 animate-float"></div>
                <div className="relative p-6 bg-gradient-to-r from-blue-600 to-purple-600 rounded-3xl text-white shadow-2xl hover-lift animate-float">
                  <Zap className="h-12 w-12" />
                </div>
              </div>
              <div>
                <h1 className="text-4xl lg:text-6xl font-bold text-gray-900 mb-4">Free Simulation</h1>
                <div className="inline-flex items-center px-6 py-3 bg-gradient-to-r from-blue-100 to-purple-100 text-blue-800 font-bold rounded-2xl border border-blue-200">
                  <Zap className="h-5 w-5 mr-2" />
                  Always Free
                </div>
              </div>
            </div>
            <p className="text-2xl text-gray-700 max-w-3xl mx-auto leading-relaxed">
              Design your perfect microgrid in seconds with our powerful simulation engine
            </p>

            {/* FIXED: Show authentication status clearly */}
            {!user && (
              <div className="mt-8 p-6 bg-yellow-50 border border-yellow-200 rounded-2xl max-w-2xl mx-auto">
                <div className="flex items-center justify-center gap-3 text-yellow-800">
                  <Lock className="h-6 w-6" />
                  <span className="text-lg font-semibold">Sign in required to run simulations</span>
                </div>
              </div>
            )}
          </div>

          {/* Configuration Cards */}
          <div className="max-w-6xl mx-auto mb-20 animate-fade-in">
            <div className="grid grid-cols-1 lg:grid-cols-3 gap-8 lg:gap-12 stagger-children">
              {/* Battery Card */}
              <Card className="card-enhanced hover-lift">
                <CardHeader className="pb-6">
                  <div className="flex items-center gap-4 mb-6">
                    <div className="p-4 bg-gradient-to-r from-green-100 to-emerald-100 rounded-2xl">
                      <Battery className="h-8 w-8 text-green-600" />
                    </div>
                    <div>
                      <CardTitle className="text-2xl font-bold text-gray-900">Battery Storage</CardTitle>
                      <p className="text-gray-600 text-lg">Energy storage capacity</p>
                    </div>
                  </div>
                </CardHeader>

                <CardContent className="px-8 pb-8 space-y-8">
                  <div className="space-y-6">
                    <div className="flex items-center justify-between">
                      <span className="text-lg font-semibold text-gray-800">Capacity</span>
                      <div className="px-4 py-2 bg-gray-100 rounded-xl font-bold text-gray-900 text-lg">
                        {config.batteryCapacity} kWh
                      </div>
                    </div>
                    <Slider
                      value={[config.batteryCapacity]}
                      onValueChange={([value]) => updateConfig({ batteryCapacity: value })}
                      max={50}
                      min={5}
                      step={5}
                      className="w-full"
                    />
                    <div className="flex justify-between text-gray-500 font-medium">
                      <span>5 kWh</span>
                      <span>50 kWh</span>
                    </div>
                  </div>

                  <div className="space-y-4">
                    <Label className="text-lg font-semibold text-gray-800">Battery Type</Label>
                    <Select
                      value={config.batteryType}
                      onValueChange={(value: any) => updateConfig({ batteryType: value })}
                    >
                      <SelectTrigger className="input-clean">
                        <SelectValue />
                      </SelectTrigger>
                      <SelectContent>
                        <SelectItem value="lithium">Lithium-ion (High efficiency)</SelectItem>
                        <SelectItem value="lead-acid">Lead-acid (Budget friendly)</SelectItem>
                        <SelectItem value="flow">Flow Battery (Long duration)</SelectItem>
                      </SelectContent>
                    </Select>
                  </div>
                </CardContent>
              </Card>

              {/* Solar Card */}
              <Card className="card-enhanced hover-lift">
                <CardHeader className="pb-6">
                  <div className="flex items-center gap-4 mb-6">
                    <div className="p-4 bg-gradient-to-r from-yellow-100 to-orange-100 rounded-2xl">
                      <Sun className="h-8 w-8 text-yellow-600" />
                    </div>
                    <div>
                      <CardTitle className="text-2xl font-bold text-gray-900">Solar Power</CardTitle>
                      <p className="text-gray-600 text-lg">Clean energy generation</p>
                    </div>
                  </div>
                </CardHeader>

                <CardContent className="px-8 pb-8 space-y-8">
                  <div className="flex items-center justify-between p-6 bg-gradient-to-r from-yellow-50 to-orange-50 rounded-2xl border-2 border-yellow-200">
                    <Label htmlFor="solar-toggle" className="flex items-center gap-3 cursor-pointer">
                      <Sun className="h-6 w-6 text-yellow-600" />
                      <span className="font-bold text-yellow-800 text-lg">Enable Solar Power</span>
                    </Label>
                    <Switch
                      id="solar-toggle"
                      checked={config.solarEnabled}
                      onCheckedChange={(checked) => updateConfig({ solarEnabled: checked })}
                      className="data-[state=checked]:bg-yellow-600"
                    />
                  </div>

                  {config.solarEnabled && (
                    <div className="space-y-6 animate-fade-in">
                      <div className="flex items-center justify-between">
                        <span className="text-lg font-semibold text-gray-800">Capacity</span>
                        <div className="px-4 py-2 bg-gray-100 rounded-xl font-bold text-gray-900 text-lg">
                          {config.solarCapacity} kW
                        </div>
                      </div>
                      <Slider
                        value={[config.solarCapacity]}
                        onValueChange={([value]) => updateConfig({ solarCapacity: value })}
                        max={25}
                        min={5}
                        step={5}
                        className="w-full"
                      />
                      <div className="flex justify-between text-gray-500 font-medium">
                        <span>5 kW</span>
                        <span>25 kW</span>
                      </div>
                    </div>
                  )}
                </CardContent>
              </Card>

              {/* Load Card */}
              <Card className="card-enhanced hover-lift">
                <CardHeader className="pb-6">
                  <div className="flex items-center gap-4 mb-6">
                    <div className="p-4 bg-gradient-to-r from-blue-100 to-indigo-100 rounded-2xl">
                      <Settings className="h-8 w-8 text-blue-600" />
                    </div>
                    <div>
                      <CardTitle className="text-2xl font-bold text-gray-900">Energy Usage</CardTitle>
                      <p className="text-gray-600 text-lg">Power demand profile</p>
                    </div>
                  </div>
                </CardHeader>

                <CardContent className="px-8 pb-8 space-y-8">
                  <div className="space-y-4">
                    <Label className="text-lg font-semibold text-gray-800">Load Profile Type</Label>
                    <div className="grid grid-cols-2 gap-4">
                      <Button
                        variant={config.loadProfileType === "residential" ? "default" : "outline"}
                        onClick={() => updateConfig({ loadProfileType: "residential" })}
                        className={`h-16 text-lg font-semibold rounded-2xl transition-smooth ${
                          config.loadProfileType === "residential"
                            ? "bg-gradient-to-r from-blue-600 to-purple-600 text-white"
                            : "btn-outline"
                        }`}
                      >
                        Home
                      </Button>
                      <Button
                        variant={config.loadProfileType === "commercial" ? "default" : "outline"}
                        onClick={() => updateConfig({ loadProfileType: "commercial" })}
                        className={`h-16 text-lg font-semibold rounded-2xl transition-smooth ${
                          config.loadProfileType === "commercial"
                            ? "bg-gradient-to-r from-blue-600 to-purple-600 text-white"
                            : "btn-outline"
                        }`}
                      >
                        Business
                      </Button>
                    </div>
                  </div>

                  <div className="flex items-center justify-between p-6 bg-gradient-to-r from-blue-50 to-purple-50 rounded-2xl border-2 border-blue-200">
                    <Label htmlFor="tou-toggle" className="flex items-center gap-3 cursor-pointer">
                      <Zap className="h-6 w-6 text-blue-600" />
                      <span className="font-bold text-blue-800 text-lg">Time-of-Use Rates</span>
                    </Label>
                    <Switch
                      id="tou-toggle"
                      checked={config.timeOfUseRates}
                      onCheckedChange={(checked) => updateConfig({ timeOfUseRates: checked })}
                      className="data-[state=checked]:bg-blue-600"
                    />
                  </div>
                </CardContent>
              </Card>
            </div>

            {/* Run Simulation Button */}
            <div className="text-center mt-16 animate-scale-in">
              <Button
                onClick={handleSimulationAccess}
                disabled={isRunning}
                className="h-20 px-16 btn-primary text-2xl rounded-3xl shadow-2xl hover:shadow-3xl hover-lift"
              >
                {/* FIXED: Show different states based on authentication */}
                {!user ? (
                  <>
                    <Lock className="mr-4 h-8 w-8" />
                    Sign In to Run Simulation
                  </>
                ) : isRunning ? (
                  <>
                    <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-white mr-4"></div>
                    Running Simulation...
                  </>
                ) : (
                  <>
                    <Play className="mr-4 h-8 w-8" />
                    Run Free Simulation
                  </>
                )}
              </Button>
            </div>
          </div>

          {/* Results Section - FIXED: Only show if user is authenticated */}
          {user && (
            <div ref={resultsRef} className="max-w-7xl mx-auto scroll-mt-20">
              {results ? (
                <div className="space-y-12 animate-fade-in">
                  {/* Results content here */}
                  <Card className="card-enhanced animate-slide-up">
                    <CardHeader className="p-8">
                      <CardTitle className="text-3xl font-bold text-center text-gray-900 mb-4">
                        Simulation Results
                      </CardTitle>
                    </CardHeader>
                    <CardContent className="p-8">
                      <MicrogridChart data={results} showSolar={config.solarEnabled} />
                    </CardContent>
                  </Card>
                </div>
              ) : (
                <Card className="card-enhanced opacity-60">
                  <CardContent className="flex items-center justify-center h-80">
                    <div className="text-center">
                      <div className="p-8 bg-gray-100 rounded-full w-24 h-24 flex items-center justify-center mx-auto mb-6">
                        <Play className="h-12 w-12 text-gray-400" />
                      </div>
                      <h3 className="text-2xl font-bold text-gray-500 mb-4">Ready to Simulate</h3>
                      <p className="text-gray-500 text-lg">Configure your system above and click run to see results</p>
                    </div>
                  </CardContent>
                </Card>
              )}
            </div>
          )}
        </div>
      </section>

      {/* FIXED: Login dialog for manual authentication */}
      <LoginDialog open={showLoginDialog} onOpenChange={setShowLoginDialog} />
    </div>
  )
}


--------------------------------------------------------------------------------
FILE: app/simulation/pro/page.html
--------------------------------------------------------------------------------
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Pro Simulation - VoltSphere</title>
  <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
  <style>
    body {
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      background: linear-gradient(to bottom right, #f9fafb, #e0f2fe, #f3e8ff);
      min-height: 100vh;
    }
    .card {
      background: white;
      border-radius: 1rem;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
      transition: all 0.3s ease;
    }
    .card:hover {
      box-shadow: 0 8px 30px rgba(0, 0, 0, 0.1);
      transform: translateY(-2px);
    }
    .btn-gradient {
      background: linear-gradient(to right, #8b5cf6, #ec4899);
      color: white;
      transition: all 0.3s ease;
    }
    .btn-gradient:hover {
      opacity: 0.9;
      transform: translateY(-1px);
    }
    .tab {
      padding: 0.75rem 1rem;
      cursor: pointer;
      transition: all 0.3s ease;
    }
    .tab.active {
      background: white;
      border-radius: 0.5rem;
      box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
    }
    .tab-content {
      display: none;
    }
    .tab-content.active {
      display: block;
    }
    .header {
      background: linear-gradient(to right, rgba(255,255,255,0.9), rgba(255,255,255,0.7));
      backdrop-filter: blur(10px);
      border-bottom: 1px solid rgba(0,0,0,0.05);
    }
    .chart-container {
      height: 400px;
      position: relative;
    }
    .slider {
      -webkit-appearance: none;
      width: 100%;
      height: 6px;
      border-radius: 5px;
      background: #e2e8f0;
      outline: none;
    }
    .slider::-webkit-slider-thumb {
      -webkit-appearance: none;
      appearance: none;
      width: 18px;
      height: 18px;
      border-radius: 50%;
      background: #8b5cf6;
      cursor: pointer;
    }
    .toggle {
      position: relative;
      display: inline-block;
      width: 50px;
      height: 24px;
    }
    .toggle input {
      opacity: 0;
      width: 0;
      height: 0;
    }
    .toggle-slider {
      position: absolute;
      cursor: pointer;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background-color: #ccc;
      transition: .4s;
      border-radius: 24px;
    }
    .toggle-slider:before {
      position: absolute;
      content: "";
      height: 18px;
      width: 18px;
      left: 3px;
      bottom: 3px;
      background-color: white;
      transition: .4s;
      border-radius: 50%;
    }
    input:checked + .toggle-slider {
      background-color: #8b5cf6;
    }
    input:checked + .toggle-slider:before {
      transform: translateX(26px);
    }
    .gradient-box {
      border-radius: 0.75rem;
      padding: 1rem;
      margin-bottom: 1rem;
    }
    .yellow-gradient {
      background: linear-gradient(to right, #fffbeb, #fef3c7);
      border: 1px solid #fde68a;
    }
    .blue-gradient {
      background: linear-gradient(to right, #eff6ff, #dbeafe);
      border: 1px solid #bfdbfe;
    }
    .green-gradient {
      background: linear-gradient(to right, #ecfdf5, #d1fae5);
      border: 1px solid #a7f3d0;
    }
  </style>
</head>
<body>
  <!-- Header -->
  <header class="header sticky top-0 z-50 py-4">
    <div class="container mx-auto px-4">
      <div class="flex justify-between items-center">
        <div class="flex items-center">
          <span class="text-2xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-purple-600 to-pink-600">VoltSphere</span>
        </div>
        <nav class="hidden md:flex space-x-8">
          <a href="/" class="text-gray-700 hover:text-purple-600">Home</a>
          <a href="/simulation" class="text-gray-700 hover:text-purple-600">Basic Simulation</a>
          <a href="/simulation/pro" class="text-purple-600 font-medium">Pro Simulation</a>
          <a href="/pricing" class="text-gray-700 hover:text-purple-600">Pricing</a>
        </nav>
        <div>
          <button class="bg-white border border-gray-200 rounded-full px-4 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50">Login</button>
        </div>
      </div>
    </div>
  </header>

  <!-- Main Content -->
  <main class="container mx-auto px-4 py-8">
    <!-- Page Header -->
    <div class="text-center mb-8">
      <div class="flex items-center justify-center gap-2 mb-4">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8 text-purple-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
        </svg>
        <h1 class="text-3xl md:text-4xl font-bold text-gray-800">⚡ Pro Simulation Suite</h1>
        <span class="bg-gradient-to-r from-purple-600 to-pink-600 text-white text-sm font-medium px-3 py-1 rounded-full">Pro</span>
      </div>
      <p class="text-lg text-gray-600 max-w-4xl mx-auto">
        Advanced microgrid simulation with weather integration, multiple battery types, and comprehensive analytics.
      </p>
    </div>

    <!-- Tabs -->
    <div class="mb-6">
      <div class="flex bg-gray-100 p-1 rounded-lg">
        <div class="tab active flex-1 text-center" data-tab="simulation">
          <div class="flex items-center justify-center gap-2">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
            </svg>
            Simulation
          </div>
        </div>
        <div class="tab flex-1 text-center" data-tab="advanced">
          <div class="flex items-center justify-center gap-2">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" />
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
            </svg>
            Advanced Settings
          </div>
        </div>
        <div class="tab flex-1 text-center" data-tab="analytics">
          <div class="flex items-center justify-center gap-2">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
            </svg>
            Cost Analytics
          </div>
        </div>
      </div>
    </div>

    <!-- Tab Content -->
    <div class="tab-content active" id="simulation-content">
      <div class="grid grid-cols-1 lg:grid-cols-4 gap-6">
        <!-- Controls -->
        <div class="lg:col-span-1">
          <div class="card p-6">
            <h2 class="text-xl font-semibold mb-4 flex items-center gap-2">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" />
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
              </svg>
              Pro Controls
            </h2>
            <div class="space-y-6">
              <!-- Battery Capacity -->
              <div class="space-y-3">
                <label class="flex items-center gap-2 font-semibold">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-green-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3v18h18" />
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18.5 3a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5z" />
                  </svg>
                  Battery Capacity: <span id="battery-capacity-value">15</span> kWh
                </label>
                <input type="range" min="5" max="100" value="15" class="slider" id="battery-capacity">
              </div>

              <!-- Battery Type -->
              <div class="space-y-3">
                <label class="font-semibold">Battery Type</label>
                <select class="w-full p-2 border border-gray-300 rounded-lg" id="battery-type">
                  <option value="lithium">Lithium-ion (92% efficiency)</option>
                  <option value="lead-acid">Lead-acid (85% efficiency)</option>
                  <option value="flow">Flow Battery (88% efficiency)</option>
                  <option value="sodium">Sodium-ion (90% efficiency)</option>
                </select>
              </div>

              <!-- Battery Efficiency -->
              <div class="space-y-3">
                <label class="font-semibold">Battery Efficiency: <span id="battery-efficiency-value">92</span>%</label>
                <input type="range" min="70" max="98" value="92" class="slider" id="battery-efficiency">
              </div>

              <!-- Load Profile -->
              <div class="space-y-3">
                <label class="font-semibold">Load Profile</label>
                <select class="w-full p-2 border border-gray-300 rounded-lg" id="load-profile">
                  <option value="residential">Residential Home</option>
                  <option value="commercial">Commercial Building</option>
                  <option value="industrial">Industrial Facility</option>
                </select>
              </div>

              <!-- Solar Power -->
              <div class="gradient-box yellow-gradient">
                <div class="flex items-center justify-between">
                  <label class="flex items-center gap-2 cursor-pointer">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-yellow-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z" />
                    </svg>
                    <span class="font-semibold text-yellow-800">Solar Power</span>
                  </label>
                  <label class="toggle">
                    <input type="checkbox" id="solar-toggle" checked>
                    <span class="toggle-slider"></span>
                  </label>
                </div>
              </div>

              <!-- Weather Data -->
              <div class="gradient-box blue-gradient">
                <div class="flex items-center justify-between">
                  <label class="flex items-center gap-2 cursor-pointer">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 15a4 4 0 004 4h9a5 5 0 10-.1-9.999 5.002 5.002 0 10-9.78 2.096A4.001 4.001 0 003 15z" />
                    </svg>
                    <span class="font-semibold text-blue-800">Real Weather Data</span>
                  </label>
                  <label class="toggle">
                    <input type="checkbox" id="weather-toggle">
                    <span class="toggle-slider"></span>
                  </label>
                </div>
              </div>

              <!-- Time of Use -->
              <div class="gradient-box green-gradient">
                <div class="flex items-center justify-between">
                  <label class="flex items-center gap-2 cursor-pointer">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-green-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
                    </svg>
                    <span class="font-semibold text-green-800">Time-of-Use Rates</span>
                  </label>
                  <label class="toggle">
                    <input type="checkbox" id="tou-toggle">
                    <span class="toggle-slider"></span>
                  </label>
                </div>
              </div>

              <button id="run-simulation" class="w-full btn-gradient py-3 px-4 rounded-lg font-semibold">
                🚀 Run Pro Simulation
              </button>
            </div>
          </div>
        </div>

        <!-- Results -->
        <div class="lg:col-span-3">
          <div class="card p-6">
            <div id="simulation-results" class="hidden">
              <h2 class="text-xl font-semibold mb-2">Pro Simulation Results</h2>
              <p class="text-sm text-gray-600 mb-4">
                <span id="battery-type-display">Lithium-ion</span> battery • 
                <span id="battery-capacity-display">15</span>kWh capacity • 
                <span id="battery-efficiency-display">92</span>% efficiency
              </p>
              <div class="chart-container">
                <canvas id="simulation-chart"></canvas>
              </div>
            </div>
            <div id="simulation-placeholder" class="flex items-center justify-center h-96">
              <div class="text-center">
                <div id="loading-spinner" class="hidden mx-auto mb-4 w-16 h-16 border-4 border-gray-200 border-t-purple-600 rounded-full animate-spin"></div>
                <svg id="ready-icon" xmlns="http://www.w3.org/2000/svg" class="h-16 w-16 mx-auto mb-4 text-gray-300" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
                </svg>
                <h3 id="simulation-status" class="text-xl font-semibold text-gray-600 mb-2">Ready for Pro Simulation</h3>
                <p id="simulation-message" class="text-gray-500">Configure your advanced settings and run the simulation</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="tab-content" id="advanced-content">
      <div class="card p-6">
        <h2 class="text-xl font-semibold mb-6">Advanced Configuration</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div>
            <label class="font-semibold block mb-2">Weather Location</label>
            <select class="w-full p-2 border border-gray-300 rounded-lg">
              <option value="San Francisco, CA">San Francisco, CA</option>
              <option value="New York, NY">New York, NY</option>
              <option value="Chicago, IL">Chicago, IL</option>
              <option value="Austin, TX">Austin, TX</option>
              <option value="Miami, FL">Miami, FL</option>
              <option value="Phoenix, AZ">Phoenix, AZ</option>
              <option value="Seattle, WA">Seattle, WA</option>
            </select>
          </div>
          <div>
            <label class="font-semibold block mb-2">Simulation Duration</label>
            <select class="w-full p-2 border border-gray-300 rounded-lg">
              <option value="24h">24 Hours</option>
              <option value="7d">7 Days</option>
              <option value="30d">30 Days</option>
              <option value="1y">1 Year</option>
            </select>
          </div>
        </div>
      </div>
    </div>

    <div class="tab-content" id="analytics-content">
      <div class="card p-6">
        <h2 class="text-xl font-semibold mb-6">Pro Cost Analysis</h2>
        <div id="analytics-results" class="hidden">
          <div class="space-y-6">
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
              <div class="bg-blue-50 p-4 rounded-lg border border-blue-100">
                <h3 class="text-lg font-semibold text-blue-700 mb-2">Daily Savings</h3>
                <p class="text-2xl font-bold text-blue-800">$<span id="daily-savings">2.25</span></p>
                <p class="text-sm text-blue-600 mt-1">From solar and battery optimization</p>
              </div>
              <div class="bg-green-50 p-4 rounded-lg border border-green-100">
                <h3 class="text-lg font-semibold text-green-700 mb-2">Monthly Savings</h3>
                <p class="text-2xl font-bold text-green-800">$<span id="monthly-savings">67.50</span></p>
                <p class="text-sm text-green-600 mt-1">Projected for 30 days</p>
              </div>
              <div class="bg-purple-50 p-4 rounded-lg border border-purple-100">
                <h3 class="text-lg font-semibold text-purple-700 mb-2">Annual Savings</h3>
                <p class="text-2xl font-bold text-purple-800">$<span id="annual-savings">821.25</span></p>
                <p class="text-sm text-purple-600 mt-1">Projected for 365 days</p>
              </div>
            </div>

            <div class="bg-gray-50 p-6 rounded-lg border border-gray-200">
              <h3 class="text-lg font-semibold text-gray-700 mb-4">Advanced ROI Analysis</h3>
              <div class="space-y-3">
                <div class="flex justify-between items-center">
                  <span class="text-gray-600">System Cost (<span id="roi-battery-type">Lithium-ion</span>)</span>
                  <span class="font-semibold">$<span id="system-cost">18,000</span></span>
                </div>
                <div class="flex justify-between items-center">
                  <span class="text-gray-600">Annual Savings</span>
                  <span class="font-semibold text-green-600">$<span id="roi-annual-savings">821</span></span>
                </div>
                <div class="flex justify-between items-center">
                  <span class="text-gray-600">Payback Period</span>
                  <span class="font-semibold"><span id="payback-period">22</span> years</span>
                </div>
                <div class="flex justify-between items-center">
                  <span class="text-gray-600">10-Year Net Savings</span>
                  <span class="font-semibold text-green-600">$<span id="ten-year-savings">-9,790</span></span>
                </div>
                <div class="flex justify-between items-center">
                  <span class="text-gray-600">Carbon Offset (Annual)</span>
                  <span class="font-semibold text-green-600"><span id="carbon-offset">38</span> tons CO₂</span>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div id="analytics-placeholder" class="flex items-center justify-center h-64">
          <div class="text-center">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-16 w-16 mx-auto mb-4 text-gray-300" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
            </svg>
            <p class="text-gray-500">Run a Pro simulation to see advanced cost analytics</p>
          </div>
        </div>
      </div>
    </div>
  </main>

  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  <script>
    // Tab switching
    document.querySelectorAll('.tab').forEach(tab => {
      tab.addEventListener('click', () => {
        document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
        document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
        
        tab.classList.add('active');
        document.getElementById(`${tab.dataset.tab}-content`).classList.add('active');
      });
    });

    // Sliders
    const batteryCapacity = document.getElementById('battery-capacity');
    const batteryCapacityValue = document.getElementById('battery-capacity-value');
    batteryCapacity.addEventListener('input', () => {
      batteryCapacityValue.textContent = batteryCapacity.value;
    });

    const batteryEfficiency = document.getElementById('battery-efficiency');
    const batteryEfficiencyValue = document.getElementById('battery-efficiency-value');
    batteryEfficiency.addEventListener('input', () => {
      batteryEfficiencyValue.textContent = batteryEfficiency.value;
    });

    // Run simulation
    const runSimulationBtn = document.getElementById('run-simulation');
    const simulationPlaceholder = document.getElementById('simulation-placeholder');
    const simulationResults = document.getElementById('simulation-results');
    const loadingSpinner = document.getElementById('loading-spinner');
    const readyIcon = document.getElementById('ready-icon');
    const simulationStatus = document.getElementById('simulation-status');
    const simulationMessage = document.getElementById('simulation-message');
    const analyticsPlaceholder = document.getElementById('analytics-placeholder');
    const analyticsResults = document.getElementById('analytics-results');

    // Battery type display
    const batteryType = document.getElementById('battery-type');
    const batteryTypeDisplay = document.getElementById('battery-type-display');
    const batteryCapacityDisplay = document.getElementById('battery-capacity-display');
    const batteryEfficiencyDisplay = document.getElementById('battery-efficiency-display');
    const roiBatteryType = document.getElementById('roi-battery-type');

    // Update displays when battery type changes
    batteryType.addEventListener('change', () => {
      const selectedOption = batteryType.options[batteryType.selectedIndex].text;
      batteryTypeDisplay.textContent = selectedOption.split(' ')[0];
      roiBatteryType.textContent = selectedOption.split(' ')[0];
    });

    // Run simulation
    runSimulationBtn.addEventListener('click', () => {
      // Show loading state
      loadingSpinner.classList.remove('hidden');
      readyIcon.classList.add('hidden');
      simulationStatus.textContent = 'Running Pro Simulation...';
      simulationMessage.textContent = 'Calculating advanced energy flows with weather data';
      
      // Update displays
      batteryCapacityDisplay.textContent = batteryCapacity.value;
      batteryEfficiencyDisplay.textContent = batteryEfficiency.value;
      
      // Simulate loading
      setTimeout(() => {
        // Hide placeholder, show results
        simulationPlaceholder.classList.add('hidden');
        simulationResults.classList.remove('hidden');
        analyticsPlaceholder.classList.add('hidden');
        analyticsResults.classList.remove('hidden');
        
        // Update analytics values
        const capacity = parseInt(batteryCapacity.value);
        document.getElementById('daily-savings').textContent = (capacity * 0.15).toFixed(2);
        document.getElementById('monthly-savings').textContent = (capacity * 0.15 * 30).toFixed(2);
        document.getElementById('annual-savings').textContent = (capacity * 0.15 * 365).toFixed(2);
        document.getElementById('system-cost').textContent = (capacity * 1200).toLocaleString();
        document.getElementById('roi-annual-savings').textContent = Math.round(capacity * 0.15 * 365).toLocaleString();
        document.getElementById('payback-period').textContent = Math.round((capacity * 1200) / (capacity * 0.15 * 365));
        document.getElementById('ten-year-savings').textContent = Math.round(capacity * 0.15 * 365 * 10 - capacity * 1200).toLocaleString();
        document.getElementById('carbon-offset').textContent = Math.round(capacity * 2.5);
        
        // Create chart
        createChart();
      }, 1500);
    });

    function createChart() {
      const ctx = document.getElementById('simulation-chart').getContext('2d');
      const capacity = parseInt(batteryCapacity.value);
      const solarEnabled = document.getElementById('solar-toggle').checked;
      const weatherEnabled = document.getElementById('weather-toggle').checked;
      
      // Generate data
      const hours = Array.from({ length: 24 }, (_, i) => `${i}:00`);
      const solarProfile = hours.map((_, i) => {
        if (i < 6 || i > 19) return 0;
        return Math.max(
          0,
          Math.sin(((i - 6) * Math.PI) / 13) *
            (capacity * 0.8) *
            (weatherEnabled ? 0.7 + Math.random() * 0.3 : 1)
        );
      });

      const loadProfile = hours.map((_, i) => {
        const baseLoad = capacity * 0.3;
        const peakMultiplier = i >= 17 && i <= 22 ? 1.8 : i >= 6 && i <= 9 ? 1.4 : 1;
        return baseLoad * peakMultiplier * (0.8 + Math.random() * 0.4);
      });

      const batteryStorage = hours.map((_, i) => {
        return Math.max(0, Math.min(capacity, capacity * (0.3 + 0.4 * Math.sin((i * Math.PI) / 12))));
      });

      const gridUsage = hours.map((_, i) => {
        return Math.max(0, loadProfile[i] - (solarEnabled ? solarProfile[i] : 0));
      });
      
      // Create chart
      new Chart(ctx, {
        type: 'line',
        data: {
          labels: hours,
          datasets: [
            {
              label: 'Solar Generation',
              data: solarEnabled ? solarProfile.map(v => Math.round(v)) : Array(24).fill(0),
              borderColor: '#f59e0b',
              backgroundColor: 'rgba(245, 158, 11, 0.1)',
              borderWidth: 2,
              fill: true,
              tension: 0.4
            },
            {
              label: 'Consumption',
              data: loadProfile.map(v => Math.round(v)),
              borderColor: '#ef4444',
              backgroundColor: 'rgba(239, 68, 68, 0.1)',
              borderWidth: 2,
              fill: true,
              tension: 0.4
            },
            {
              label: 'Battery Level',
              data: batteryStorage.map(v => Math.round(v)),
              borderColor: '#10b981',
              backgroundColor: 'rgba(16, 185, 129, 0.1)',
              borderWidth: 2,
              fill: true,
              tension: 0.4
            },
            {
              label: 'Grid Usage',
              data: gridUsage.map(v => Math.round(v)),
              borderColor: '#6366f1',
              backgroundColor: 'rgba(99, 102, 241, 0.1)',
              borderWidth: 2,
              fill: true,
              tension: 0.4
            }
          ]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            y: {
              beginAtZero: true,
              title: {
                display: true,
                text: 'Energy (kWh)'
              }
            },
            x: {
              title: {
                display: true,
                text: 'Time of Day'
              }
            }
          },
          plugins: {
            legend: {
              position: 'top',
            },
            tooltip: {
              mode: 'index',
              intersect: false
            }
          }
        }
      });
    }
  </script>
</body>
</html>


--------------------------------------------------------------------------------
FILE: app/simulation/pro/page.tsx
--------------------------------------------------------------------------------
"use client"

import { useState, useEffect } from "react"
import { useRouter } from "next/navigation"
import { SiteHeader } from "@/components/site-header"
import { SimulationNav } from "@/components/simulation/simulation-nav"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Slider } from "@/components/ui/slider"
import { Switch } from "@/components/ui/switch"
import { Label } from "@/components/ui/label"
import { Input } from "@/components/ui/input"
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select"
import { Badge } from "@/components/ui/badge"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
import { Crown, Activity, Settings, BarChart3, Battery, Sun, Cloud, DollarSign, Globe } from "lucide-react"
import { SimulationEngine, type SimulationConfig } from "@/lib/simulation/engine"
import { ProChart } from "@/components/simulation/pro-chart"
import { useAuth } from "@/lib/auth-context"
import { canAccessPro } from "@/lib/auth"

export default function ProSimulationPage() {
  const { user, isLoading } = useAuth()
  const router = useRouter()
  const [config, setConfig] = useState<SimulationConfig>({
    batteryCapacity: 15,
    batteryEfficiency: 92,
    solarEnabled: true,
    batteryType: "lithium",
    loadProfileType: "residential",
    useRealWeather: false,
    weatherLocation: "San Francisco, CA",
    timeOfUseRates: false,
    simulationDuration: "24h",
    solarCapacity: 12,
    inverterEfficiency: 96,
    systemLosses: 14,
    gridCostPerKwh: 0.15,
    solarCostPerWatt: 3.0,
    batteryCostPerKwh: 500,
    discountRate: 0.06,
    systemLifespan: 25,
  })

  const [isRunning, setIsRunning] = useState(false)
  const [results, setResults] = useState<any>(null)

  // Check access on component mount - allow admin users regardless of subscription
  useEffect(() => {
    if (!isLoading && !canAccessPro(user) && user?.role !== "admin") {
      router.push("/pricing")
    }
  }, [user, isLoading, router])

  // Show loading while checking auth
  if (isLoading) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-gray-50 via-blue-50 to-purple-50">
        <SiteHeader />
        <div className="container mx-auto mobile-padding py-8">
          <div className="flex items-center justify-center h-96">
            <div className="animate-spin rounded-full h-16 w-16 border-b-2 border-blue-600"></div>
          </div>
        </div>
      </div>
    )
  }

  // Show access denied if user doesn't have pro access and is not admin
  if (!canAccessPro(user) && user?.role !== "admin") {
    return (
      <div className="min-h-screen bg-gradient-to-br from-gray-50 via-blue-50 to-purple-50">
        <SiteHeader />
        <div className="container mx-auto mobile-padding py-8">
          <div className="text-center">
            <div className="flex items-center justify-center gap-2 mb-4">
              <Crown className="h-8 w-8 text-purple-600" />
              <h1 className="mobile-heading-xl text-gray-800">Pro Simulation</h1>
              <Badge className="bg-gradient-to-r from-purple-600 to-pink-600 text-white">Pro</Badge>
            </div>
            <p className="mobile-body-lg text-gray-600 max-w-2xl mx-auto mb-8">
              Access to Pro Simulation requires a Pro subscription or higher.
            </p>
            <Button
              onClick={() => router.push("/pricing")}
              className="bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700 mobile-btn"
            >
              Upgrade to Pro
            </Button>
          </div>
        </div>
      </div>
    )
  }

  const runSimulation = async () => {
    setIsRunning(true)
    try {
      await new Promise((resolve) => setTimeout(resolve, 2000))
      const simulationResults = await SimulationEngine.runSimulation(config)
      setResults(simulationResults)
    } catch (error) {
      console.error("Simulation error:", error)
    } finally {
      setIsRunning(false)
    }
  }

  const updateConfig = (updates: Partial<SimulationConfig>) => {
    setConfig((prev) => ({ ...prev, ...updates }))
  }

  const cities = [
    "San Francisco, CA",
    "New York, NY",
    "Chicago, IL",
    "Austin, TX",
    "Miami, FL",
    "Phoenix, AZ",
    "Seattle, WA",
    "Denver, CO",
    "Los Angeles, CA",
    "Boston, MA",
    "Atlanta, GA",
    "Dallas, TX",
  ]

  // Determine the effective tier for the user - admin gets enterprise tier
  const effectiveTier = user?.role === "admin" ? "enterprise" : user?.subscriptionTier || "free"

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-50 via-blue-50 to-purple-50">
      <SiteHeader />

      <div className="container mx-auto mobile-padding py-8">
        {/* Header */}
        <div className="text-center mb-8 animate-fade-in">
          <div className="flex items-center justify-center gap-2 mb-4">
            <Crown className="h-8 w-8 text-purple-600" />
            <h1 className="mobile-heading-xl text-gray-800">Pro Simulation Suite</h1>
            <Badge className="bg-gradient-to-r from-purple-600 to-pink-600 text-white">Pro</Badge>
          </div>
          <p className="mobile-body-lg text-gray-600 max-w-4xl mx-auto">
            Advanced microgrid simulation with weather integration, multiple battery types, and comprehensive analytics.
          </p>
        </div>

        {/* Navigation */}
        <div className="mb-8">
          <SimulationNav userTier={effectiveTier} />
        </div>

        {/* Main Content */}
        <Tabs defaultValue="simulation" className="space-y-6">
          <TabsList className="grid w-full grid-cols-3 mobile-rounded">
            <TabsTrigger value="simulation" className="flex items-center gap-2">
              <Activity className="h-4 w-4" />
              Simulation
            </TabsTrigger>
            <TabsTrigger value="advanced" className="flex items-center gap-2">
              <Settings className="h-4 w-4" />
              Advanced Settings
            </TabsTrigger>
            <TabsTrigger value="analytics" className="flex items-center gap-2">
              <BarChart3 className="h-4 w-4" />
              Cost Analytics
            </TabsTrigger>
          </TabsList>

          {/* Simulation Tab */}
          <TabsContent value="simulation">
            <div className="grid lg:grid-cols-4 gap-6">
              {/* Controls */}
              <div className="lg:col-span-1">
                <Card className="card-enhanced mobile-rounded">
                  <CardHeader>
                    <CardTitle className="flex items-center gap-3">
                      <Settings className="h-5 w-5 text-blue-600" />
                      Pro Controls
                    </CardTitle>
                  </CardHeader>
                  <CardContent className="space-y-6">
                    <div className="space-y-3">
                      <Label className="flex items-center gap-2 font-semibold">
                        <Battery className="h-4 w-4 text-green-600" />
                        Battery Capacity: {config.batteryCapacity} kWh
                      </Label>
                      <Slider
                        value={[config.batteryCapacity]}
                        onValueChange={([value]) => updateConfig({ batteryCapacity: value })}
                        max={100}
                        min={5}
                        step={1}
                        className="w-full"
                      />
                    </div>

                    <div className="space-y-3">
                      <Label className="font-semibold">Battery Type</Label>
                      <Select
                        value={config.batteryType}
                        onValueChange={(value) => updateConfig({ batteryType: value })}
                      >
                        <SelectTrigger className="mobile-rounded">
                          <SelectValue />
                        </SelectTrigger>
                        <SelectContent>
                          <SelectItem value="lithium">Lithium-ion (92% efficiency)</SelectItem>
                          <SelectItem value="lead-acid">Lead-acid (85% efficiency)</SelectItem>
                          <SelectItem value="flow">Flow Battery (88% efficiency)</SelectItem>
                          <SelectItem value="sodium">Sodium-ion (90% efficiency)</SelectItem>
                        </SelectContent>
                      </Select>
                    </div>

                    <div className="space-y-3">
                      <Label className="font-semibold">Solar Capacity: {config.solarCapacity} kW</Label>
                      <Slider
                        value={[config.solarCapacity]}
                        onValueChange={([value]) => updateConfig({ solarCapacity: value })}
                        max={50}
                        min={0}
                        step={1}
                        className="w-full"
                      />
                    </div>

                    <div className="space-y-3">
                      <Label className="font-semibold">Load Profile</Label>
                      <Select
                        value={config.loadProfileType}
                        onValueChange={(value) => updateConfig({ loadProfileType: value })}
                      >
                        <SelectTrigger className="mobile-rounded">
                          <SelectValue />
                        </SelectTrigger>
                        <SelectContent>
                          <SelectItem value="residential">Residential Home</SelectItem>
                          <SelectItem value="commercial">Commercial Building</SelectItem>
                          <SelectItem value="industrial">Industrial Facility</SelectItem>
                        </SelectContent>
                      </Select>
                    </div>

                    <div className="flex items-center justify-between p-4 bg-gradient-to-r from-yellow-50 to-orange-50 rounded-xl">
                      <Label htmlFor="solar" className="flex items-center gap-2">
                        <Sun className="h-4 w-4 text-yellow-600" />
                        Solar Power
                      </Label>
                      <Switch
                        id="solar"
                        checked={config.solarEnabled}
                        onCheckedChange={(checked) => updateConfig({ solarEnabled: checked })}
                      />
                    </div>

                    <div className="flex items-center justify-between p-4 bg-gradient-to-r from-blue-50 to-purple-50 rounded-xl">
                      <Label htmlFor="weather" className="flex items-center gap-2">
                        <Cloud className="h-4 w-4 text-blue-600" />
                        Real Weather Data
                      </Label>
                      <Switch
                        id="weather"
                        checked={config.useRealWeather}
                        onCheckedChange={(checked) => updateConfig({ useRealWeather: checked })}
                      />
                    </div>

                    <div className="flex items-center justify-between p-4 bg-gradient-to-r from-green-50 to-teal-50 rounded-xl">
                      <Label htmlFor="tou" className="flex items-center gap-2">
                        <Activity className="h-4 w-4 text-green-600" />
                        Time-of-Use Rates
                      </Label>
                      <Switch
                        id="tou"
                        checked={config.timeOfUseRates}
                        onCheckedChange={(checked) => updateConfig({ timeOfUseRates: checked })}
                      />
                    </div>

                    <Button
                      onClick={runSimulation}
                      disabled={isRunning}
                      className="w-full bg-gradient-to-r from-purple-600 to-pink-600 hover:from-purple-700 hover:to-pink-700 mobile-btn mobile-rounded font-semibold"
                    >
                      {isRunning ? "Running Pro Simulation..." : "Run Pro Simulation"}
                    </Button>
                  </CardContent>
                </Card>
              </div>

              {/* Results */}
              <div className="lg:col-span-3">
                {results ? (
                  <div className="space-y-6">
                    {/* Chart */}
                    <Card className="card-enhanced mobile-rounded">
                      <CardHeader>
                        <CardTitle className="flex items-center gap-2">
                          <BarChart3 className="h-5 w-5 text-purple-600" />
                          Pro Energy Analysis
                        </CardTitle>
                      </CardHeader>
                      <CardContent>
                        <ProChart data={results} config={config} />
                      </CardContent>
                    </Card>

                    {/* Summary Stats */}
                    <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
                      <Card className="card-enhanced mobile-rounded">
                        <CardContent className="p-6">
                          <div className="flex items-center gap-3 mb-2">
                            <Sun className="h-5 w-5 text-yellow-600" />
                            <span className="font-semibold">Solar</span>
                          </div>
                          <p className="text-2xl font-bold text-yellow-700">{results.summary.totalSolar} kWh</p>
                          <p className="text-sm text-gray-600">{results.summary.solarUtilization}% utilization</p>
                        </CardContent>
                      </Card>

                      <Card className="card-enhanced mobile-rounded">
                        <CardContent className="p-6">
                          <div className="flex items-center gap-3 mb-2">
                            <Battery className="h-5 w-5 text-green-600" />
                            <span className="font-semibold">Battery</span>
                          </div>
                          <p className="text-2xl font-bold text-green-700">{results.summary.avgBattery}%</p>
                          <p className="text-sm text-gray-600">Average SOC</p>
                        </CardContent>
                      </Card>

                      <Card className="card-enhanced mobile-rounded">
                        <CardContent className="p-6">
                          <div className="flex items-center gap-3 mb-2">
                            <Activity className="h-5 w-5 text-blue-600" />
                            <span className="font-semibold">Grid Independence</span>
                          </div>
                          <p className="text-2xl font-bold text-blue-700">{results.summary.gridIndependence}%</p>
                          <p className="text-sm text-gray-600">Self-sufficiency</p>
                        </CardContent>
                      </Card>

                      <Card className="card-enhanced mobile-rounded">
                        <CardContent className="p-6">
                          <div className="flex items-center gap-3 mb-2">
                            <DollarSign className="h-5 w-5 text-purple-600" />
                            <span className="font-semibold">Daily Cost</span>
                          </div>
                          <p className="text-2xl font-bold text-purple-700">${results.economics.dailyCost}</p>
                          <p className="text-sm text-gray-600">Grid electricity</p>
                        </CardContent>
                      </Card>
                    </div>
                  </div>
                ) : (
                  <Card className="card-enhanced mobile-rounded">
                    <CardContent className="flex items-center justify-center h-96">
                      <div className="text-center">
                        {isRunning ? (
                          <>
                            <div className="animate-spin rounded-full h-16 w-16 border-b-2 border-purple-600 mx-auto mb-4"></div>
                            <h3 className="text-xl font-semibold text-gray-600 mb-2">Running Pro Simulation...</h3>
                            <p className="text-gray-500">Calculating advanced energy flows with weather data</p>
                          </>
                        ) : (
                          <>
                            <Crown className="h-16 w-16 mx-auto mb-4 text-gray-300" />
                            <h3 className="text-xl font-semibold text-gray-600 mb-2">Ready for Pro Simulation</h3>
                            <p className="text-gray-500">Configure your advanced settings and run the simulation</p>
                          </>
                        )}
                      </div>
                    </CardContent>
                  </Card>
                )}
              </div>
            </div>
          </TabsContent>

          {/* Advanced Settings Tab */}
          <TabsContent value="advanced">
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
              {/* Weather & Location */}
              <Card className="card-enhanced mobile-rounded">
                <CardHeader>
                  <CardTitle className="flex items-center gap-3">
                    <Globe className="h-5 w-5 text-blue-600" />
                    Weather & Location
                  </CardTitle>
                </CardHeader>
                <CardContent className="space-y-4">
                  <div>
                    <Label className="font-semibold">Weather Location</Label>
                    <Select
                      value={config.weatherLocation}
                      onValueChange={(value) => updateConfig({ weatherLocation: value })}
                    >
                      <SelectTrigger className="mt-2 mobile-rounded">
                        <SelectValue />
                      </SelectTrigger>
                      <SelectContent>
                        {cities.map((city) => (
                          <SelectItem key={city} value={city}>
                            {city}
                          </SelectItem>
                        ))}
                      </SelectContent>
                    </Select>
                  </div>

                  <div>
                    <Label className="font-semibold">Simulation Duration</Label>
                    <Select
                      value={config.simulationDuration}
                      onValueChange={(value) => updateConfig({ simulationDuration: value })}
                    >
                      <SelectTrigger className="mt-2 mobile-rounded">
                        <SelectValue />
                      </SelectTrigger>
                      <SelectContent>
                        <SelectItem value="24h">24 Hours</SelectItem>
                        <SelectItem value="7d">7 Days</SelectItem>
                        <SelectItem value="30d">30 Days</SelectItem>
                        <SelectItem value="1y">1 Year</SelectItem>
                      </SelectContent>
                    </Select>
                  </div>

                  <div>
                    <Label className="font-semibold">Inverter Efficiency: {config.inverterEfficiency}%</Label>
                    <Slider
                      value={[config.inverterEfficiency]}
                      onValueChange={([value]) => updateConfig({ inverterEfficiency: value })}
                      max={99}
                      min={90}
                      step={0.5}
                      className="mt-2"
                    />
                  </div>

                  <div>
                    <Label className="font-semibold">System Losses: {config.systemLosses}%</Label>
                    <Slider
                      value={[config.systemLosses]}
                      onValueChange={([value]) => updateConfig({ systemLosses: value })}
                      max={25}
                      min={5}
                      step={1}
                      className="mt-2"
                    />
                  </div>
                </CardContent>
              </Card>

              {/* Economic Parameters */}
              <Card className="card-enhanced mobile-rounded">
                <CardHeader>
                  <CardTitle className="flex items-center gap-3">
                    <DollarSign className="h-5 w-5 text-green-600" />
                    Economic Parameters
                  </CardTitle>
                </CardHeader>
                <CardContent className="space-y-4">
                  <div className="grid grid-cols-2 gap-4">
                    <div>
                      <Label className="font-semibold">Grid Cost ($/kWh)</Label>
                      <Input
                        type="number"
                        step="0.01"
                        value={config.gridCostPerKwh}
                        onChange={(e) => updateConfig({ gridCostPerKwh: Number.parseFloat(e.target.value) || 0.15 })}
                        className="mt-1"
                      />
                    </div>

                    <div>
                      <Label className="font-semibold">Solar Cost ($/W)</Label>
                      <Input
                        type="number"
                        step="0.1"
                        value={config.solarCostPerWatt}
                        onChange={(e) => updateConfig({ solarCostPerWatt: Number.parseFloat(e.target.value) || 3.0 })}
                        className="mt-1"
                      />
                    </div>

                    <div>
                      <Label className="font-semibold">Battery Cost ($/kWh)</Label>
                      <Input
                        type="number"
                        step="10"
                        value={config.batteryCostPerKwh}
                        onChange={(e) => updateConfig({ batteryCostPerKwh: Number.parseFloat(e.target.value) || 500 })}
                        className="mt-1"
                      />
                    </div>

                    <div>
                      <Label className="font-semibold">Discount Rate (%)</Label>
                      <Input
                        type="number"
                        step="0.1"
                        value={config.discountRate * 100}
                        onChange={(e) => updateConfig({ discountRate: (Number.parseFloat(e.target.value) || 6) / 100 })}
                        className="mt-1"
                      />
                    </div>
                  </div>

                  <div>
                    <Label className="font-semibold">System Lifespan: {config.systemLifespan} years</Label>
                    <Slider
                      value={[config.systemLifespan]}
                      onValueChange={([value]) => updateConfig({ systemLifespan: value })}
                      max={30}
                      min={15}
                      step={1}
                      className="mt-2"
                    />
                  </div>
                </CardContent>
              </Card>
            </div>
          </TabsContent>

          {/* Analytics Tab */}
          <TabsContent value="analytics">
            <Card className="card-enhanced mobile-rounded">
              <CardHeader>
                <CardTitle className="flex items-center gap-2">
                  <BarChart3 className="h-5 w-5 text-purple-600" />
                  Pro Cost Analysis
                </CardTitle>
              </CardHeader>
              <CardContent>
                {results ? (
                  <div className="space-y-6">
                    {/* Financial Summary */}
                    <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                      <div className="bg-blue-50 p-6 rounded-lg border border-blue-100">
                        <h4 className="text-lg font-semibold text-blue-700 mb-2">Daily Savings</h4>
                        <p className="text-3xl font-bold text-blue-800">${results.economics.dailyCost}</p>
                        <p className="text-sm text-blue-600 mt-1">Current grid cost</p>
                      </div>
                      <div className="bg-green-50 p-6 rounded-lg border border-green-100">
                        <h4 className="text-lg font-semibold text-green-700 mb-2">Annual Savings</h4>
                        <p className="text-3xl font-bold text-green-800">${results.economics.totalSavings}</p>
                        <p className="text-sm text-green-600 mt-1">Projected savings</p>
                      </div>
                      <div className="bg-purple-50 p-6 rounded-lg border border-purple-100">
                        <h4 className="text-lg font-semibold text-purple-700 mb-2">Payback Period</h4>
                        <p className="text-3xl font-bold text-purple-800">{results.economics.paybackPeriod} years</p>
                        <p className="text-sm text-purple-600 mt-1">Return on investment</p>
                      </div>
                    </div>

                    {/* Detailed Analysis */}
                    <div className="bg-gray-50 p-6 rounded-lg border border-gray-200">
                      <h4 className="text-lg font-semibold text-gray-700 mb-4">Advanced Financial Analysis</h4>
                      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div className="space-y-3">
                          <div className="flex justify-between items-center">
                            <span className="text-gray-600">Monthly Cost</span>
                            <span className="font-semibold">${results.economics.monthlyCost}</span>
                          </div>
                          <div className="flex justify-between items-center">
                            <span className="text-gray-600">Annual Cost</span>
                            <span className="font-semibold">${results.economics.annualCost}</span>
                          </div>
                          <div className="flex justify-between items-center">
                            <span className="text-gray-600">ROI</span>
                            <span className="font-semibold text-green-600">{results.economics.roi}%</span>
                          </div>
                        </div>
                        <div className="space-y-3">
                          <div className="flex justify-between items-center">
                            <span className="text-gray-600">Net Present Value</span>
                            <span className="font-semibold">${results.economics.netPresentValue}</span>
                          </div>
                          <div className="flex justify-between items-center">
                            <span className="text-gray-600">CO₂ Saved (Annual)</span>
                            <span className="font-semibold text-green-600">{results.environmental.co2Saved} kg</span>
                          </div>
                          <div className="flex justify-between items-center">
                            <span className="text-gray-600">Trees Equivalent</span>
                            <span className="font-semibold text-green-600">
                              {results.environmental.treesEquivalent}
                            </span>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                ) : (
                  <div className="flex items-center justify-center h-64">
                    <div className="text-center">
                      <BarChart3 className="h-16 w-16 mx-auto mb-4 text-gray-300" />
                      <p className="text-gray-500">Run a Pro simulation to see advanced cost analytics</p>
                    </div>
                  </div>
                )}
              </CardContent>
            </Card>
          </TabsContent>
        </Tabs>
      </div>
    </div>
  )
}


--------------------------------------------------------------------------------
FILE: app/simulation/starter/page.tsx
--------------------------------------------------------------------------------
"use client"

import { useState, useEffect } from "react"
import { useRouter } from "next/navigation"
import { SiteHeader } from "@/components/site-header"
import { SimulationNav } from "@/components/simulation/simulation-nav"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
import { Badge } from "@/components/ui/badge"
import { Key, Book, Activity, Copy, CheckCircle, ChevronLeft, ChevronRight, Code } from "lucide-react"
import { useAuth } from "@/lib/auth-context"

// Static code examples to avoid template literal issues
const CURL_EXAMPLE = `curl -X POST https://api.voltsphere.com/v1/simulate \\
-H "Authorization: Bearer vs_sk_starter_1234567890abcdef" \\
-H "Content-Type: application/json" \\
-d '{
  "batteryCapacity": 15,
  "solarCapacity": 8,
  "loadProfile": "residential",
  "location": "San Francisco, CA",
  "duration": "24h"
}'`

const JS_EXAMPLE = `const response = await fetch('https://api.voltsphere.com/v1/simulate', {
  method: 'POST',
  headers: {
    'Authorization': 'Bearer vs_sk_starter_1234567890abcdef',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    batteryCapacity: 15,
    solarCapacity: 8,
    loadProfile: "residential",
    location: "San Francisco, CA",
    duration: "24h"
  })
});

const data = await response.json();
console.log(data);`

// Static API examples
const STARTER_EXAMPLES = [
  {
    title: "Basic Residential Simulation",
    description: "Simple home energy system with solar and battery",
    code: `{
  "batteryCapacity": 15,
  "solarCapacity": 8,
  "loadProfile": "residential",
  "location": "San Francisco, CA",
  "duration": "24h"
}`,
  },
  {
    title: "Commercial Building Analysis",
    description: "Office building with peak demand management",
    code: `{
  "batteryCapacity": 50,
  "solarCapacity": 25,
  "loadProfile": "commercial",
  "timeOfUseRates": true,
  "peakShaving": true,
  "location": "New York, NY"
}`,
  },
]

export default function StarterAPIPage() {
  const { user, isLoading } = useAuth()
  const router = useRouter()
  const [apiKey] = useState("vs_sk_starter_1234567890abcdef")
  const [copied, setCopied] = useState(false)
  const [currentExample, setCurrentExample] = useState(0)

  // Check access - Starter tier or higher
  useEffect(() => {
    if (
      !isLoading &&
      user?.subscriptionTier !== "starter" &&
      user?.subscriptionTier !== "growth" &&
      user?.subscriptionTier !== "enterprise" &&
      user?.role !== "admin"
    ) {
      router.push("/pricing")
    }
  }, [user, isLoading, router])

  if (isLoading) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-gray-50 via-blue-50 to-purple-50">
        <SiteHeader />
        <div className="container mx-auto py-8">
          <div className="flex items-center justify-center h-96">
            <div className="animate-spin rounded-full h-16 w-16 border-b-2 border-blue-600"></div>
          </div>
        </div>
      </div>
    )
  }

  if (
    user?.subscriptionTier !== "starter" &&
    user?.subscriptionTier !== "growth" &&
    user?.subscriptionTier !== "enterprise" &&
    user?.role !== "admin"
  ) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-gray-50 via-blue-50 to-purple-50">
        <SiteHeader />
        <div className="container mx-auto py-8">
          <div className="text-center">
            <div className="flex items-center justify-center gap-2 mb-4">
              <Code className="h-8 w-8 text-blue-600" />
              <h1 className="text-3xl font-bold text-gray-800">Starter API</h1>
              <Badge className="bg-gradient-to-r from-blue-600 to-purple-600 text-white">API</Badge>
            </div>
            <p className="text-lg text-gray-600 max-w-2xl mx-auto mb-8">
              Access to Starter API requires a Starter subscription or higher.
            </p>
            <Button
              onClick={() => router.push("/pricing")}
              className="bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700"
            >
              Upgrade to Starter
            </Button>
          </div>
        </div>
      </div>
    )
  }

  const copyToClipboard = (text: string) => {
    navigator.clipboard.writeText(text)
    setCopied(true)
    setTimeout(() => setCopied(false), 2000)
  }

  const nextExample = () => {
    setCurrentExample((prev) => (prev + 1) % STARTER_EXAMPLES.length)
  }

  const prevExample = () => {
    setCurrentExample((prev) => (prev - 1 + STARTER_EXAMPLES.length) % STARTER_EXAMPLES.length)
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-50 via-blue-50 to-purple-50">
      <SiteHeader />

      <div className="container mx-auto py-8">
        {/* Header */}
        <div className="text-center mb-8">
          <div className="flex items-center justify-center gap-2 mb-4">
            <Code className="h-8 w-8 text-blue-600" />
            <h1 className="text-3xl font-bold text-gray-800">Starter API</h1>
            <Badge className="bg-gradient-to-r from-blue-600 to-purple-600 text-white">API</Badge>
          </div>
          <p className="text-lg text-gray-600 max-w-4xl mx-auto">
            Begin your API integration journey with our Starter tier. Perfect for small projects and testing.
          </p>
        </div>

        {/* Navigation */}
        <div className="mb-8">
          <SimulationNav userTier={user?.subscriptionTier || "free"} />
        </div>

        {/* Main Content */}
        <Tabs defaultValue="overview" className="space-y-6">
          <TabsList className="grid w-full grid-cols-4">
            <TabsTrigger value="overview" className="flex items-center gap-2">
              <Book className="h-4 w-4" />
              Overview
            </TabsTrigger>
            <TabsTrigger value="authentication" className="flex items-center gap-2">
              <Key className="h-4 w-4" />
              Authentication
            </TabsTrigger>
            <TabsTrigger value="examples" className="flex items-center gap-2">
              <Code className="h-4 w-4" />
              Examples
            </TabsTrigger>
            <TabsTrigger value="documentation" className="flex items-center gap-2">
              <Activity className="h-4 w-4" />
              Documentation
            </TabsTrigger>
          </TabsList>

          {/* Overview Tab */}
          <TabsContent value="overview">
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
              <Card>
                <CardHeader>
                  <CardTitle className="flex items-center gap-2">
                    <Code className="h-5 w-5 text-blue-600" />
                    Starter Features
                  </CardTitle>
                </CardHeader>
                <CardContent className="space-y-4">
                  <p className="text-gray-600">
                    The Starter API provides essential simulation capabilities for your projects:
                  </p>
                  <ul className="space-y-2 text-gray-600">
                    <li className="flex items-center gap-2">
                      <CheckCircle className="h-4 w-4 text-green-600" />
                      5,000 API calls per month
                    </li>
                    <li className="flex items-center gap-2">
                      <CheckCircle className="h-4 w-4 text-green-600" />
                      Basic simulation parameters
                    </li>
                    <li className="flex items-center gap-2">
                      <CheckCircle className="h-4 w-4 text-green-600" />
                      Up to 100kWh battery capacity
                    </li>
                    <li className="flex items-center gap-2">
                      <CheckCircle className="h-4 w-4 text-green-600" />
                      Standard support
                    </li>
                  </ul>
                </CardContent>
              </Card>

              <Card>
                <CardHeader>
                  <CardTitle className="flex items-center gap-2">
                    <Key className="h-5 w-5 text-blue-600" />
                    API Limits
                  </CardTitle>
                </CardHeader>
                <CardContent className="space-y-4">
                  <div className="space-y-3">
                    <div className="flex justify-between items-center p-3 bg-blue-50 rounded-lg">
                      <span className="font-medium">Monthly Calls</span>
                      <Badge variant="outline">5,000</Badge>
                    </div>
                    <div className="flex justify-between items-center p-3 bg-blue-50 rounded-lg">
                      <span className="font-medium">Rate Limit</span>
                      <Badge variant="outline">100/minute</Badge>
                    </div>
                    <div className="flex justify-between items-center p-3 bg-blue-50 rounded-lg">
                      <span className="font-medium">Max Battery Size</span>
                      <Badge variant="outline">100 kWh</Badge>
                    </div>
                  </div>
                </CardContent>
              </Card>
            </div>
          </TabsContent>

          {/* Authentication Tab */}
          <TabsContent value="authentication">
            <Card>
              <CardHeader>
                <CardTitle className="flex items-center gap-2">
                  <Key className="h-5 w-5 text-blue-600" />
                  API Authentication
                </CardTitle>
              </CardHeader>
              <CardContent className="space-y-6">
                <div>
                  <h3 className="text-lg font-semibold mb-3">Your Starter API Key</h3>
                  <div className="flex items-center gap-2">
                    <Input value={apiKey} readOnly className="font-mono text-sm" />
                    <Button onClick={() => copyToClipboard(apiKey)} variant="outline" size="sm">
                      {copied ? <CheckCircle className="h-4 w-4" /> : <Copy className="h-4 w-4" />}
                    </Button>
                  </div>
                  <p className="text-sm text-gray-600 mt-2">Keep your API key secure and never share it publicly.</p>
                </div>

                <div>
                  <h3 className="text-lg font-semibold mb-3">Authentication Method</h3>
                  <p className="text-gray-600 mb-4">
                    Include your API key in the Authorization header of every request:
                  </p>
                  <div className="bg-gray-900 text-gray-100 p-4 rounded-lg font-mono text-sm">
                    Authorization: Bearer {apiKey}
                  </div>
                </div>
              </CardContent>
            </Card>
          </TabsContent>

          {/* Examples Tab */}
          <TabsContent value="examples">
            <div className="space-y-6">
              <Card>
                <CardHeader>
                  <CardTitle>Code Examples</CardTitle>
                  <p className="text-gray-600">Ready-to-use code snippets in popular languages</p>
                </CardHeader>
                <CardContent>
                  <Tabs defaultValue="curl" className="space-y-4">
                    <TabsList>
                      <TabsTrigger value="curl">cURL</TabsTrigger>
                      <TabsTrigger value="javascript">JavaScript</TabsTrigger>
                    </TabsList>

                    <TabsContent value="curl">
                      <div className="relative">
                        <pre className="bg-gray-900 text-gray-100 p-4 rounded-lg text-sm overflow-x-auto">
                          <code>{CURL_EXAMPLE}</code>
                        </pre>
                        <Button
                          onClick={() => copyToClipboard(CURL_EXAMPLE)}
                          variant="outline"
                          size="sm"
                          className="absolute top-2 right-2"
                        >
                          {copied ? <CheckCircle className="h-4 w-4" /> : <Copy className="h-4 w-4" />}
                        </Button>
                      </div>
                    </TabsContent>

                    <TabsContent value="javascript">
                      <div className="relative">
                        <pre className="bg-gray-900 text-gray-100 p-4 rounded-lg text-sm overflow-x-auto">
                          <code>{JS_EXAMPLE}</code>
                        </pre>
                        <Button
                          onClick={() => copyToClipboard(JS_EXAMPLE)}
                          variant="outline"
                          size="sm"
                          className="absolute top-2 right-2"
                        >
                          {copied ? <CheckCircle className="h-4 w-4" /> : <Copy className="h-4 w-4" />}
                        </Button>
                      </div>
                    </TabsContent>
                  </Tabs>

                  {/* Use Cases Carousel */}
                  <div className="mt-8">
                    <Card className="border-2 border-blue-200">
                      <CardHeader>
                        <CardTitle className="flex items-center justify-between">
                          <span>Starter Use Cases</span>
                          <div className="flex items-center gap-2">
                            <Button onClick={prevExample} variant="outline" size="sm">
                              <ChevronLeft className="h-4 w-4" />
                            </Button>
                            <span className="text-sm text-gray-500">
                              {currentExample + 1} of {STARTER_EXAMPLES.length}
                            </span>
                            <Button onClick={nextExample} variant="outline" size="sm">
                              <ChevronRight className="h-4 w-4" />
                            </Button>
                          </div>
                        </CardTitle>
                      </CardHeader>
                      <CardContent>
                        <div className="space-y-4">
                          <div className="text-center">
                            <h3 className="text-xl font-semibold text-gray-800 mb-2">
                              {STARTER_EXAMPLES[currentExample].title}
                            </h3>
                            <p className="text-gray-600 mb-4">{STARTER_EXAMPLES[currentExample].description}</p>
                          </div>

                          <div className="relative">
                            <pre className="bg-gray-900 text-gray-100 p-4 rounded-lg text-sm overflow-x-auto max-h-96">
                              <code>{STARTER_EXAMPLES[currentExample].code}</code>
                            </pre>
                            <Button
                              onClick={() => copyToClipboard(STARTER_EXAMPLES[currentExample].code)}
                              variant="outline"
                              size="sm"
                              className="absolute top-2 right-2"
                            >
                              {copied ? <CheckCircle className="h-4 w-4" /> : <Copy className="h-4 w-4" />}
                            </Button>
                          </div>
                        </div>
                      </CardContent>
                    </Card>
                  </div>
                </CardContent>
              </Card>
            </div>
          </TabsContent>

          {/* Documentation Tab */}
          <TabsContent value="documentation">
            <Card>
              <CardHeader>
                <CardTitle>API Documentation</CardTitle>
              </CardHeader>
              <CardContent>
                <p className="text-gray-600 mb-4">
                  For complete API documentation, please refer to our developer portal.
                </p>
                <Button className="bg-blue-600 hover:bg-blue-700">
                  <Book className="mr-2 h-4 w-4" />
                  View Documentation
                </Button>
              </CardContent>
            </Card>
          </TabsContent>
        </Tabs>
      </div>
    </div>
  )
}


--------------------------------------------------------------------------------
FILE: app/simulations/page.tsx
--------------------------------------------------------------------------------
"use client"

import { useState } from "react"
import Link from "next/link"
import { Card, CardContent } from "@/components/ui/card"
import { SiteHeader } from "@/components/site-header"
import { Zap, Star, Crown, Code, Building } from "lucide-react"
import { useAuth } from "@/lib/auth-context"

export default function SimulationsPage() {
  const { user } = useAuth()
  const [selectedSim, setSelectedSim] = useState<string>("")

  // Determine user access level
  const userTier = user?.subscriptionTier || "free"
  const hasAccess = (requiredTier: string): boolean => {
    if (!user) return requiredTier === "free"

    const tierHierarchy: { [key: string]: string[] } = {
      free: ["free"],
      pro: ["free", "pro"],
      growth: ["free", "pro", "growth"],
      enterprise: ["free", "pro", "growth", "enterprise"],
    }

    const userAccess = tierHierarchy[userTier] || ["free"]
    return userAccess.includes(requiredTier)
  }

  const simulations = [
    {
      id: "free",
      name: "Free Simulation",
      icon: Zap,
      href: "/simulation",
      requiredTier: "free",
    },
    {
      id: "pro",
      name: "Pro Simulation",
      icon: Star,
      href: "/simulation/pro",
      requiredTier: "pro",
    },
    {
      id: "growth",
      name: "Growth Simulation",
      icon: Building,
      href: "/simulation/growth",
      requiredTier: "growth",
    },
    {
      id: "api",
      name: "API Access",
      icon: Code,
      href: "/simulation/api",
      requiredTier: "growth",
    },
    {
      id: "enterprise",
      name: "Enterprise Suite",
      icon: Crown,
      href: "/simulation/enterprise",
      requiredTier: "enterprise",
    },
  ]

  const handleSimulationClick = (sim: any) => {
    if (hasAccess(sim.requiredTier)) {
      window.location.href = sim.href
    }
  }

  return (
    <div className="min-h-screen bg-gradient-primary">
      <SiteHeader />

      <section className="section-spacing">
        <div className="container-clean">
          <div className="text-center mb-20 animate-fade-in">
            <h1 className="text-5xl lg:text-6xl font-bold text-gray-900 mb-8">
              Choose Your <span className="text-gradient">Simulation</span>
            </h1>
            <p className="text-2xl text-gray-700 max-w-4xl mx-auto leading-relaxed">
              Select the simulation tier that fits your needs. Upgrade anytime to unlock more advanced features and
              capabilities.
            </p>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-8 lg:gap-12 max-w-6xl mx-auto stagger-children">
            {simulations.map((sim) => {
              const available = hasAccess(sim.requiredTier)

              return (
                <Card
                  key={sim.id}
                  className={`card-enhanced text-center transition-smooth ${
                    available
                      ? "cursor-pointer hover:scale-110 hover:shadow-2xl"
                      : "opacity-50 cursor-not-allowed bg-gray-100/50"
                  } ${selectedSim === sim.id ? "ring-4 ring-blue-500 ring-offset-4" : ""}`}
                  onClick={() => {
                    setSelectedSim(sim.id)
                    if (available) {
                      setTimeout(() => handleSimulationClick(sim), 300)
                    }
                  }}
                >
                  <CardContent className="p-10">
                    <div className="flex justify-center mb-8">
                      <div
                        className={`w-20 h-20 rounded-3xl flex items-center justify-center shadow-xl transition-smooth ${
                          available ? "bg-gradient-to-r from-blue-600 to-purple-600 hover:scale-110" : "bg-gray-300"
                        }`}
                      >
                        <sim.icon className={`h-10 w-10 ${available ? "text-white" : "text-gray-500"}`} />
                      </div>
                    </div>
                    <h3 className={`text-xl font-bold mb-4 ${available ? "text-gray-900" : "text-gray-500"}`}>
                      {sim.name}
                    </h3>
                    {!available && (
                      <div className="px-4 py-2 bg-gray-200 rounded-xl">
                        <p className="text-sm text-gray-600 font-medium">Upgrade Required</p>
                      </div>
                    )}
                  </CardContent>
                </Card>
              )
            })}
          </div>

          {/* Current Plan Display */}
          <div className="text-center mt-20">
            <div className="inline-flex items-center px-8 py-4 bg-gradient-to-r from-blue-50 to-purple-50 border-2 border-blue-200 rounded-2xl shadow-lg">
              <span className="text-blue-800 font-bold text-xl">
                Current Plan: <span className="text-gradient capitalize text-2xl">{userTier}</span>
              </span>
            </div>
          </div>

          {/* Upgrade CTA */}
          {userTier === "free" && (
            <div className="text-center mt-12 animate-fade-in">
              <Link
                href="/pricing"
                className="inline-flex items-center px-10 py-5 bg-gradient-to-r from-blue-600 to-purple-600 text-white font-bold rounded-2xl hover:scale-105 transition-smooth text-xl shadow-xl hover:shadow-2xl"
              >
                Upgrade to Access More Simulations
              </Link>
            </div>
          )}
        </div>
      </section>
    </div>
  )
}


################################################################################
DIRECTORY: components
################################################################################

--------------------------------------------------------------------------------
FILE: components/auth/login-dialog.tsx
--------------------------------------------------------------------------------
"use client"

import type React from "react"

import { useState } from "react"
import { Button } from "@/components/ui/button"
import { Dialog, DialogContent, DialogDescription, DialogHeader, DialogTitle } from "@/components/ui/dialog"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
import { useAuth } from "@/lib/auth-context"
import { Zap, Loader2, CheckCircle } from "lucide-react"

interface LoginDialogProps {
  open: boolean
  onOpenChange: (open: boolean) => void
}

export function LoginDialog({ open, onOpenChange }: LoginDialogProps) {
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState("")
  const [emailSent, setEmailSent] = useState(false)
  const { login, register } = useAuth()

  const [loginData, setLoginData] = useState({
    email: "",
    password: "",
  })

  const [registerData, setRegisterData] = useState({
    name: "",
    email: "",
    password: "",
  })

  const sendConfirmationEmail = async (email: string, type: string, name?: string) => {
    try {
      const response = await fetch("/api/auth/send-confirmation", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ email, type, name }),
      })

      const result = await response.json()
      if (result.success) {
        setEmailSent(true)
        console.log("Confirmation email sent to:", email)
      }
    } catch (error) {
      console.error("Failed to send confirmation email:", error)
    }
  }

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault()
    setIsLoading(true)
    setError("")
    setEmailSent(false)

    try {
      const success = await login(loginData.email, loginData.password)
      if (success) {
        // Send confirmation email to the user
        await sendConfirmationEmail(loginData.email, "login")

        // Show success message briefly before closing
        setTimeout(() => {
          onOpenChange(false)
          setLoginData({ email: "", password: "" })
        }, 2000)
      } else {
        setError("Invalid email or password")
      }
    } catch (error) {
      setError("Login failed. Please try again.")
    } finally {
      setIsLoading(false)
    }
  }

  const handleRegister = async (e: React.FormEvent) => {
    e.preventDefault()
    setIsLoading(true)
    setError("")
    setEmailSent(false)

    try {
      const success = await register(registerData.email, registerData.password, registerData.name)
      if (success) {
        // Send welcome email to the user
        await sendConfirmationEmail(registerData.email, "register", registerData.name)

        // Show success message briefly before closing
        setTimeout(() => {
          onOpenChange(false)
          setRegisterData({ name: "", email: "", password: "" })
        }, 2000)
      } else {
        setError("Registration failed. Please try again.")
      }
    } catch (error) {
      setError("Registration failed. Please try again.")
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <Dialog open={open} onOpenChange={onOpenChange}>
      <DialogContent className="sm:max-w-md bg-white border border-gray-200 shadow-2xl rounded-3xl max-h-[90vh] overflow-y-auto">
        <DialogHeader className="text-center pb-6">
          <div className="flex items-center justify-center gap-4 mb-4">
            <div className="w-12 h-12 bg-gradient-to-r from-blue-600 to-purple-600 rounded-2xl flex items-center justify-center shadow-lg">
              <Zap className="h-6 w-6 text-white" />
            </div>
            <DialogTitle className="text-3xl font-bold text-gradient">VoltSphere</DialogTitle>
          </div>
          <DialogDescription className="text-gray-700 text-lg">
            Sign in to your account or create a new one to access energy simulation tools.
          </DialogDescription>
        </DialogHeader>

        {emailSent && (
          <div className="mb-6 p-4 bg-green-50 border-2 border-green-200 rounded-2xl">
            <div className="flex items-center justify-center gap-3">
              <CheckCircle className="h-6 w-6 text-green-600" />
              <p className="text-green-700 font-semibold text-center">Confirmation email sent to your inbox!</p>
            </div>
          </div>
        )}

        <Tabs defaultValue="login" className="w-full">
          <TabsList className="grid w-full grid-cols-2 mb-8 bg-gray-100 rounded-2xl p-2">
            <TabsTrigger
              value="login"
              className="font-semibold text-gray-800 data-[state=active]:bg-white data-[state=active]:text-blue-600 rounded-xl py-3"
            >
              Sign In
            </TabsTrigger>
            <TabsTrigger
              value="register"
              className="font-semibold text-gray-800 data-[state=active]:bg-white data-[state=active]:text-blue-600 rounded-xl py-3"
            >
              Sign Up
            </TabsTrigger>
          </TabsList>

          <TabsContent value="login" className="space-y-6">
            <form onSubmit={handleLogin} className="space-y-6">
              <div className="space-y-3">
                <Label htmlFor="login-email" className="text-lg font-semibold text-gray-800">
                  Email Address
                </Label>
                <Input
                  id="login-email"
                  type="email"
                  placeholder="Enter your email"
                  value={loginData.email}
                  onChange={(e) => setLoginData({ ...loginData, email: e.target.value })}
                  className="input-clean h-14 text-lg"
                  required
                />
              </div>

              <div className="space-y-3">
                <Label htmlFor="login-password" className="text-lg font-semibold text-gray-800">
                  Password
                </Label>
                <Input
                  id="login-password"
                  type="password"
                  placeholder="Enter your password"
                  value={loginData.password}
                  onChange={(e) => setLoginData({ ...loginData, password: e.target.value })}
                  className="input-clean h-14 text-lg"
                  required
                />
              </div>

              {error && (
                <div className="p-4 bg-red-50 border-2 border-red-200 rounded-2xl">
                  <p className="text-red-700 font-semibold text-center">{error}</p>
                </div>
              )}

              <Button type="submit" className="w-full h-14 btn-primary text-lg" disabled={isLoading}>
                {isLoading ? (
                  <>
                    <Loader2 className="mr-3 h-5 w-5 animate-spin" />
                    Signing In...
                  </>
                ) : (
                  "Sign In"
                )}
              </Button>
            </form>
          </TabsContent>

          <TabsContent value="register" className="space-y-6">
            <form onSubmit={handleRegister} className="space-y-6">
              <div className="space-y-3">
                <Label htmlFor="register-name" className="text-lg font-semibold text-gray-800">
                  Full Name
                </Label>
                <Input
                  id="register-name"
                  type="text"
                  placeholder="Enter your full name"
                  value={registerData.name}
                  onChange={(e) => setRegisterData({ ...registerData, name: e.target.value })}
                  className="input-clean h-14 text-lg"
                  required
                />
              </div>

              <div className="space-y-3">
                <Label htmlFor="register-email" className="text-lg font-semibold text-gray-800">
                  Email Address
                </Label>
                <Input
                  id="register-email"
                  type="email"
                  placeholder="Enter your email"
                  value={registerData.email}
                  onChange={(e) => setRegisterData({ ...registerData, email: e.target.value })}
                  className="input-clean h-14 text-lg"
                  required
                />
              </div>

              <div className="space-y-3">
                <Label htmlFor="register-password" className="text-lg font-semibold text-gray-800">
                  Password
                </Label>
                <Input
                  id="register-password"
                  type="password"
                  placeholder="Create a secure password"
                  value={registerData.password}
                  onChange={(e) => setRegisterData({ ...registerData, password: e.target.value })}
                  className="input-clean h-14 text-lg"
                  required
                />
              </div>

              {error && (
                <div className="p-4 bg-red-50 border-2 border-red-200 rounded-2xl">
                  <p className="text-red-700 font-semibold text-center">{error}</p>
                </div>
              )}

              <Button type="submit" className="w-full h-14 btn-primary text-lg" disabled={isLoading}>
                {isLoading ? (
                  <>
                    <Loader2 className="mr-3 h-5 w-5 animate-spin" />
                    Creating Account...
                  </>
                ) : (
                  "Create Account"
                )}
              </Button>
            </form>
          </TabsContent>
        </Tabs>
      </DialogContent>
    </Dialog>
  )
}


--------------------------------------------------------------------------------
FILE: components/auth/user-dropdown.tsx
--------------------------------------------------------------------------------
"use client"

import { Button } from "@/components/ui/button"
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"
import { Avatar, AvatarFallback } from "@/components/ui/avatar"
import { useAuth } from "@/lib/auth-context"
import { Settings, LogOut, Zap, Shield } from "lucide-react"
import Link from "next/link"
import { toast } from "sonner"

interface UserType {
  id: string
  email: string
  name: string
  role: "user" | "admin"
  subscription: "free" | "pro" | "enterprise"
}

interface UserDropdownProps {
  user: UserType
}

export function UserDropdown({ user }: UserDropdownProps) {
  const { logout } = useAuth()

  const handleLogout = async () => {
    try {
      await logout()
      toast.success("Logged out successfully")
    } catch (error) {
      toast.error("Logout failed")
    }
  }

  const getInitials = (name: string) => {
    return name
      .split(" ")
      .map((n) => n[0])
      .join("")
      .toUpperCase()
  }

  const getSubscriptionLabel = (subscription: string) => {
    switch (subscription) {
      case "pro":
        return "Pro User"
      case "enterprise":
        return "Enterprise User"
      case "starter":
        return "Starter User"
      case "growth":
        return "Growth User"
      default:
        return "Free User"
    }
  }

  const getSubscriptionColor = (subscription: string) => {
    switch (subscription) {
      case "pro":
        return "text-blue-600"
      case "enterprise":
        return "text-purple-600"
      case "starter":
        return "text-green-600"
      case "growth":
        return "text-amber-600"
      default:
        return "text-gray-600"
    }
  }

  return (
    <DropdownMenu>
      <DropdownMenuTrigger asChild>
        <Button variant="ghost" className="relative h-8 w-8 rounded-full">
          <Avatar className="h-8 w-8">
            <AvatarFallback className="text-xs">{getInitials(user.name)}</AvatarFallback>
          </Avatar>
        </Button>
      </DropdownMenuTrigger>
      <DropdownMenuContent className="w-56" align="end" forceMount>
        <DropdownMenuLabel className="font-normal">
          <div className="flex flex-col space-y-1">
            <p className="text-sm font-medium leading-none">{user.name}</p>
            <p className="text-xs leading-none text-muted-foreground">{user.email}</p>
            <div className="flex items-center gap-2 pt-1">
              <span className={`text-xs font-medium ${getSubscriptionColor(user.subscription)}`}>
                {getSubscriptionLabel(user.subscription)}
              </span>
              {user.role === "admin" && <Shield className="h-3 w-3 text-amber-600" />}
            </div>
          </div>
        </DropdownMenuLabel>
        <DropdownMenuSeparator />

        <DropdownMenuItem asChild>
          <Link href="/profile" className="cursor-pointer">
            <Settings className="mr-2 h-4 w-4" />
            <span>Profile</span>
          </Link>
        </DropdownMenuItem>

        <DropdownMenuItem asChild>
          <Link href="/simulation" className="cursor-pointer">
            <Zap className="mr-2 h-4 w-4" />
            <span>Simulation</span>
          </Link>
        </DropdownMenuItem>

        {user.role === "admin" && (
          <DropdownMenuItem asChild>
            <Link href="/admin/dashboard" className="cursor-pointer">
              <Shield className="mr-2 h-4 w-4" />
              <span>Admin Dashboard</span>
            </Link>
          </DropdownMenuItem>
        )}

        <DropdownMenuItem asChild>
          <Link href="/billing" className="cursor-pointer">
            <Settings className="mr-2 h-4 w-4" />
            <span>Billing</span>
          </Link>
        </DropdownMenuItem>

        <DropdownMenuSeparator />
        <DropdownMenuItem onClick={handleLogout} className="cursor-pointer">
          <LogOut className="mr-2 h-4 w-4" />
          <span>Log out</span>
        </DropdownMenuItem>
      </DropdownMenuContent>
    </DropdownMenu>
  )
}


--------------------------------------------------------------------------------
FILE: components/auth/user-menu.tsx
--------------------------------------------------------------------------------
"use client"

import { Button } from "@/components/ui/button"
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"
import { User, CreditCard, LogOut, ChevronDown } from "lucide-react"
import Link from "next/link"
import { useAuth } from "@/lib/auth-context"

interface UserMenuProps {
  user: {
    id: string
    name: string
    email: string
    subscriptionTier?: string
  }
}

export function UserMenu({ user }: UserMenuProps) {
  const { logout } = useAuth()

  const handleLogout = async () => {
    try {
      await logout()
    } catch (error) {
      console.error("Logout failed:", error)
    }
  }

  return (
    <DropdownMenu>
      <DropdownMenuTrigger asChild>
        <Button variant="ghost" size="sm" className="h-8 w-8 rounded-lg">
          <ChevronDown className="h-4 w-4" />
        </Button>
      </DropdownMenuTrigger>
      <DropdownMenuContent align="end" className="w-56">
        <DropdownMenuLabel className="font-normal">
          <div className="flex flex-col space-y-1">
            <p className="text-sm font-medium leading-none">{user.name}</p>
            <p className="text-xs leading-none text-muted-foreground">{user.email}</p>
            <p className="text-xs leading-none text-blue-600 font-medium">Premium Access</p>
          </div>
        </DropdownMenuLabel>
        <DropdownMenuSeparator />
        <DropdownMenuItem asChild>
          <Link href="/profile" className="cursor-pointer">
            <User className="mr-2 h-4 w-4" />
            <span>Profile</span>
          </Link>
        </DropdownMenuItem>
        <DropdownMenuItem asChild>
          <Link href="/billing" className="cursor-pointer">
            <CreditCard className="mr-2 h-4 w-4" />
            <span>Billing</span>
          </Link>
        </DropdownMenuItem>
        <DropdownMenuSeparator />
        <DropdownMenuItem onClick={handleLogout} className="cursor-pointer text-red-600">
          <LogOut className="mr-2 h-4 w-4" />
          <span>Sign out</span>
        </DropdownMenuItem>
      </DropdownMenuContent>
    </DropdownMenu>
  )
}


--------------------------------------------------------------------------------
FILE: components/error-boundary.tsx
--------------------------------------------------------------------------------
"use client"

import React from "react"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { AlertTriangle, RefreshCw } from "lucide-react"

interface ErrorBoundaryState {
  hasError: boolean
  error?: Error
}

export class ErrorBoundary extends React.Component<React.PropsWithChildren<{}>, ErrorBoundaryState> {
  constructor(props: React.PropsWithChildren<{}>) {
    super(props)
    this.state = { hasError: false }
  }

  static getDerivedStateFromError(error: Error): ErrorBoundaryState {
    return { hasError: true, error }
  }

  componentDidCatch(error: Error, errorInfo: React.ErrorInfo) {
    // Log error but don't break the app
    console.warn("Error caught by boundary:", error, errorInfo)

    // Filter out browser extension errors
    if (
      error.message.includes("Receiving end does not exist") ||
      error.message.includes("Extension context invalidated") ||
      error.message.includes("Could not establish connection")
    ) {
      // These are browser extension errors, ignore them
      this.setState({ hasError: false })
      return
    }
  }

  render() {
    if (this.state.hasError && this.state.error) {
      // Don't show error UI for browser extension errors
      if (
        this.state.error.message.includes("Receiving end does not exist") ||
        this.state.error.message.includes("Extension context invalidated") ||
        this.state.error.message.includes("Could not establish connection")
      ) {
        return this.props.children
      }

      return (
        <div className="min-h-screen flex items-center justify-center p-4">
          <Card className="max-w-md w-full">
            <CardHeader className="text-center">
              <div className="mx-auto w-12 h-12 bg-red-100 rounded-full flex items-center justify-center mb-4">
                <AlertTriangle className="h-6 w-6 text-red-600" />
              </div>
              <CardTitle className="text-xl">Something went wrong</CardTitle>
            </CardHeader>
            <CardContent className="text-center space-y-4">
              <p className="text-gray-600">We encountered an unexpected error. Please try refreshing the page.</p>
              <Button onClick={() => window.location.reload()} className="w-full">
                <RefreshCw className="h-4 w-4 mr-2" />
                Refresh Page
              </Button>
            </CardContent>
          </Card>
        </div>
      )
    }

    return this.props.children
  }
}


--------------------------------------------------------------------------------
FILE: components/microgrid-chart.tsx
--------------------------------------------------------------------------------
"use client"

import { useState } from "react"
import { Line, LineChart, XAxis, YAxis, CartesianGrid, ResponsiveContainer, Tooltip } from "recharts"
import { Button } from "@/components/ui/button"
import { ChartContainer } from "@/components/ui/chart"
import { Sun, Battery, Zap, Activity, Eye, EyeOff } from "lucide-react"

interface MicrogridChartProps {
  data: any
  showSolar?: boolean
}

export function MicrogridChart({ data, showSolar = true }: MicrogridChartProps) {
  const [visibleLines, setVisibleLines] = useState({
    solar: showSolar,
    consumption: true,
    battery: true,
    grid: true,
  })

  if (!data || !data.data) {
    return (
      <div className="h-96 flex items-center justify-center text-gray-500">
        <p>No data available</p>
      </div>
    )
  }

  const toggleLine = (lineKey: keyof typeof visibleLines) => {
    setVisibleLines((prev) => ({
      ...prev,
      [lineKey]: !prev[lineKey],
    }))
  }

  const chartConfig = {
    solar: {
      label: "Solar Generation",
      color: "#f59e0b", // amber-500
    },
    consumption: {
      label: "Energy Consumption",
      color: "#ef4444", // red-500
    },
    battery: {
      label: "Battery Storage",
      color: "#10b981", // emerald-500
    },
    grid: {
      label: "Grid Usage",
      color: "#6366f1", // indigo-500
    },
  }

  const lineControls = [
    { key: "solar" as const, label: "Solar", icon: Sun, color: "bg-amber-500", show: showSolar },
    { key: "consumption" as const, label: "Consumption", icon: Activity, color: "bg-red-500", show: true },
    { key: "battery" as const, label: "Battery", icon: Battery, color: "bg-emerald-500", show: true },
    { key: "grid" as const, label: "Grid", icon: Zap, color: "bg-indigo-500", show: true },
  ]

  return (
    <div className="space-y-6">
      {/* Line Controls */}
      <div className="flex flex-wrap gap-3 justify-center">
        {lineControls.map(({ key, label, icon: Icon, color, show }) => {
          if (!show) return null

          const isVisible = visibleLines[key]
          return (
            <Button
              key={key}
              onClick={() => toggleLine(key)}
              variant={isVisible ? "default" : "outline"}
              className={`flex items-center gap-2 h-10 px-4 rounded-xl transition-all duration-200 ${
                isVisible ? `${color} text-white hover:opacity-90` : "hover:bg-gray-100"
              }`}
            >
              <Icon className="h-4 w-4" />
              <span className="font-medium">{label}</span>
              {isVisible ? <Eye className="h-4 w-4" /> : <EyeOff className="h-4 w-4" />}
            </Button>
          )
        })}
      </div>

      {/* Chart */}
      <div className="w-full">
        <ChartContainer config={chartConfig} className="h-[400px] w-full">
          <ResponsiveContainer width="100%" height="100%">
            <LineChart
              data={data.data.slice(0, 24)}
              margin={{
                top: 20,
                right: 30,
                left: 20,
                bottom: 20,
              }}
            >
              <CartesianGrid strokeDasharray="3 3" className="stroke-gray-200" opacity={0.5} />
              <XAxis
                dataKey="time"
                className="text-sm"
                tick={{ fontSize: 12, fill: "#6b7280" }}
                axisLine={{ stroke: "#d1d5db" }}
                tickLine={{ stroke: "#d1d5db" }}
              />
              <YAxis
                className="text-sm"
                tick={{ fontSize: 12, fill: "#6b7280" }}
                axisLine={{ stroke: "#d1d5db" }}
                tickLine={{ stroke: "#d1d5db" }}
                label={{
                  value: "Power (kW)",
                  angle: -90,
                  position: "insideLeft",
                  style: { textAnchor: "middle", fill: "#6b7280", fontSize: "12px" },
                }}
              />
              <Tooltip
                content={({ active, payload, label }) => {
                  if (!active || !payload || !payload.length) return null

                  return (
                    <div className="bg-white p-4 border border-gray-200 rounded-xl shadow-lg">
                      <p className="font-semibold text-gray-800 mb-2">{`Time: ${label}`}</p>
                      {payload.map((entry, index) => {
                        const lineKey = entry.dataKey as keyof typeof visibleLines
                        if (!visibleLines[lineKey]) return null

                        return (
                          <div key={index} className="flex items-center gap-2 text-sm">
                            <div className="w-3 h-3 rounded-full" style={{ backgroundColor: entry.color }} />
                            <span className="text-gray-600">{entry.name}:</span>
                            <span className="font-semibold">{Number(entry.value).toFixed(2)} kW</span>
                          </div>
                        )
                      })}
                    </div>
                  )
                }}
              />

              {/* Conditional Lines */}
              {showSolar && visibleLines.solar && (
                <Line
                  type="monotone"
                  dataKey="solar"
                  stroke={chartConfig.solar.color}
                  strokeWidth={3}
                  dot={false}
                  name="Solar Generation"
                  connectNulls={false}
                />
              )}

              {visibleLines.consumption && (
                <Line
                  type="monotone"
                  dataKey="consumption"
                  stroke={chartConfig.consumption.color}
                  strokeWidth={3}
                  dot={false}
                  name="Energy Consumption"
                  connectNulls={false}
                />
              )}

              {visibleLines.battery && (
                <Line
                  type="monotone"
                  dataKey="battery"
                  stroke={chartConfig.battery.color}
                  strokeWidth={3}
                  dot={false}
                  name="Battery Storage"
                  connectNulls={false}
                />
              )}

              {visibleLines.grid && (
                <Line
                  type="monotone"
                  dataKey="grid"
                  stroke={chartConfig.grid.color}
                  strokeWidth={3}
                  dot={false}
                  name="Grid Usage"
                  connectNulls={false}
                />
              )}
            </LineChart>
          </ResponsiveContainer>
        </ChartContainer>
      </div>

      {/* Legend Info */}
      <div className="grid grid-cols-2 sm:grid-cols-4 gap-4 text-center">
        {lineControls.map(({ key, label, icon: Icon, color, show }) => {
          if (!show || !visibleLines[key]) return null

          return (
            <div key={key} className="flex flex-col items-center gap-2">
              <div className={`p-2 ${color} rounded-lg text-white`}>
                <Icon className="h-5 w-5" />
              </div>
              <div className="text-sm font-medium text-gray-700">{label}</div>
            </div>
          )
        })}
      </div>
    </div>
  )
}


--------------------------------------------------------------------------------
FILE: components/simulation/pro-chart.tsx
--------------------------------------------------------------------------------
"use client"

import { Line, LineChart, XAxis, YAxis, CartesianGrid, ResponsiveContainer, Legend } from "recharts"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { ChartContainer, ChartTooltip, ChartTooltipContent } from "@/components/ui/chart"

interface ProChartProps {
  data: any
  config: any
}

export function ProChart({ data, config }: ProChartProps) {
  if (!data || !data.data) {
    return (
      <Card className="w-full">
        <CardHeader>
          <CardTitle>Energy Flow Analysis</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="h-96 flex items-center justify-center text-gray-500">
            Run a simulation to see the energy flow chart
          </div>
        </CardContent>
      </Card>
    )
  }

  const chartConfig = {
    solar: {
      label: "Solar Generation",
      color: "hsl(var(--chart-1))",
    },
    consumption: {
      label: "Energy Consumption",
      color: "hsl(var(--chart-2))",
    },
    battery: {
      label: "Battery Storage",
      color: "hsl(var(--chart-3))",
    },
    grid: {
      label: "Grid Usage",
      color: "hsl(var(--chart-4))",
    },
  }

  return (
    <Card className="w-full">
      <CardHeader>
        <CardTitle className="flex items-center gap-2">
          Energy Flow Analysis
          {config.useRealWeather && (
            <span className="text-sm font-normal text-gray-500">({config.weatherLocation})</span>
          )}
        </CardTitle>
      </CardHeader>
      <CardContent>
        <ChartContainer config={chartConfig} className="h-96 w-full">
          <ResponsiveContainer width="100%" height="100%">
            <LineChart
              data={data.data.slice(0, 24)}
              margin={{
                top: 5,
                right: 30,
                left: 20,
                bottom: 5,
              }}
            >
              <CartesianGrid strokeDasharray="3 3" className="stroke-muted" />
              <XAxis dataKey="time" className="text-xs" tick={{ fontSize: 12 }} />
              <YAxis
                className="text-xs"
                tick={{ fontSize: 12 }}
                label={{ value: "Power (kW)", angle: -90, position: "insideLeft" }}
              />
              <ChartTooltip content={<ChartTooltipContent />} />
              <Legend />

              {config.solarEnabled && (
                <Line
                  type="monotone"
                  dataKey="solar"
                  stroke="var(--color-solar)"
                  strokeWidth={2}
                  dot={false}
                  name="Solar Generation"
                />
              )}

              <Line
                type="monotone"
                dataKey="consumption"
                stroke="var(--color-consumption)"
                strokeWidth={2}
                dot={false}
                name="Energy Consumption"
              />

              <Line
                type="monotone"
                dataKey="battery"
                stroke="var(--color-battery)"
                strokeWidth={2}
                dot={false}
                name="Battery Storage"
              />

              <Line
                type="monotone"
                dataKey="grid"
                stroke="var(--color-grid)"
                strokeWidth={2}
                dot={false}
                name="Grid Usage"
              />
            </LineChart>
          </ResponsiveContainer>
        </ChartContainer>
      </CardContent>
    </Card>
  )
}


--------------------------------------------------------------------------------
FILE: components/simulation/pro/advanced-controls.tsx
--------------------------------------------------------------------------------
"use client"

import type React from "react"

import { useState } from "react"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { Textarea } from "@/components/ui/textarea"
import { Switch } from "@/components/ui/switch"
import { Slider } from "@/components/ui/slider"
import type { SimulationConfig } from "@/lib/simulation/engine"
import { Upload, DollarSign, Wrench, FileText } from "lucide-react"

interface AdvancedControlsProps {
  config: SimulationConfig
  onChange: (config: SimulationConfig) => void
  onRun: () => void
  isLoading: boolean
}

export function AdvancedControls({ config, onChange, onRun, isLoading }: AdvancedControlsProps) {
  const [customLoadFile, setCustomLoadFile] = useState<File | null>(null)

  const updateConfig = (updates: Partial<SimulationConfig>) => {
    onChange({ ...config, ...updates })
  }

  const handleFileUpload = async (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0]
    if (!file) return

    setCustomLoadFile(file)

    try {
      const text = await file.text()
      const lines = text.split("\n")
      const data: number[] = []

      for (const line of lines) {
        const value = Number.parseFloat(line.trim())
        if (!isNaN(value)) {
          data.push(value)
        }
      }

      if (data.length === 24) {
        updateConfig({
          customLoadData: data,
          loadProfileType: "custom",
        })
        alert("Load profile uploaded successfully!")
      } else {
        alert("Please upload a CSV file with exactly 24 hourly values")
      }
    } catch (error) {
      alert("Error reading file. Please ensure it's a valid CSV.")
    }
  }

  const handlePasteData = (e: React.ChangeEvent<HTMLTextAreaElement>) => {
    const values = e.target.value
      .split(",")
      .map((v) => Number.parseFloat(v.trim()))
      .filter((v) => !isNaN(v))

    if (values.length === 24) {
      updateConfig({
        customLoadData: values,
        loadProfileType: "custom",
      })
      alert("Load profile data updated successfully!")
    } else if (values.length > 0) {
      alert(`Please provide exactly 24 values. You provided ${values.length} values.`)
    }
  }

  const economicParams = config.economicParams || {
    gridCostPerKwh: 0.12,
    solarCostPerWatt: 3.0,
    batteryCostPerKwh: 500,
    discountRate: 0.06,
    systemLifespan: 25,
  }

  const equipmentSpecs = config.equipmentSpecs || {
    solarPanelEfficiency: 20,
    inverterEfficiency: 96,
    systemLosses: 14,
  }

  return (
    <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
      {/* Custom Load Profile */}
      <Card className="card-enhanced">
        <CardHeader>
          <CardTitle className="flex items-center gap-3">
            <Upload className="h-5 w-5 text-green-600" />
            Custom Load Profile
          </CardTitle>
        </CardHeader>
        <CardContent className="space-y-4">
          <div>
            <Label htmlFor="load-file" className="font-semibold">
              Upload 24-hour Load Data (CSV)
            </Label>
            <Input id="load-file" type="file" accept=".csv,.txt" onChange={handleFileUpload} className="mt-2" />
            <p className="text-sm text-gray-500 mt-1">Upload a CSV file with 24 hourly load values (kW)</p>
          </div>

          {customLoadFile && (
            <div className="p-3 bg-green-50 rounded-lg border border-green-200">
              <p className="text-sm text-green-700 font-medium">✓ Loaded: {customLoadFile.name}</p>
            </div>
          )}

          {config.customLoadData && (
            <div>
              <Label className="font-semibold">Preview (first 12 hours):</Label>
              <div className="grid grid-cols-6 gap-2 mt-2">
                {config.customLoadData.slice(0, 12).map((value, i) => (
                  <div key={i} className="text-center p-2 bg-gray-100 rounded text-sm">
                    <div className="font-medium">{i}h</div>
                    <div>{value.toFixed(1)}</div>
                  </div>
                ))}
              </div>
            </div>
          )}

          <Textarea
            placeholder="Or paste comma-separated values here (24 values)..."
            className="min-h-[100px]"
            onChange={handlePasteData}
          />
        </CardContent>
      </Card>

      {/* Equipment Specifications */}
      <Card className="card-enhanced">
        <CardHeader>
          <CardTitle className="flex items-center gap-3">
            <Wrench className="h-5 w-5 text-blue-600" />
            Equipment Specifications
          </CardTitle>
        </CardHeader>
        <CardContent className="space-y-4">
          <div>
            <Label className="font-semibold">Solar Panel Efficiency: {equipmentSpecs.solarPanelEfficiency}%</Label>
            <Slider
              value={[equipmentSpecs.solarPanelEfficiency]}
              onValueChange={([value]) =>
                updateConfig({
                  equipmentSpecs: { ...equipmentSpecs, solarPanelEfficiency: value },
                })
              }
              max={25}
              min={15}
              step={0.5}
              className="mt-2"
            />
          </div>

          <div>
            <Label className="font-semibold">Inverter Efficiency: {equipmentSpecs.inverterEfficiency}%</Label>
            <Slider
              value={[equipmentSpecs.inverterEfficiency]}
              onValueChange={([value]) =>
                updateConfig({
                  equipmentSpecs: { ...equipmentSpecs, inverterEfficiency: value },
                })
              }
              max={99}
              min={90}
              step={0.5}
              className="mt-2"
            />
          </div>

          <div>
            <Label className="font-semibold">System Losses: {equipmentSpecs.systemLosses}%</Label>
            <Slider
              value={[equipmentSpecs.systemLosses]}
              onValueChange={([value]) =>
                updateConfig({
                  equipmentSpecs: { ...equipmentSpecs, systemLosses: value },
                })
              }
              max={25}
              min={5}
              step={1}
              className="mt-2"
            />
          </div>
        </CardContent>
      </Card>

      {/* Economic Parameters */}
      <Card className="card-enhanced">
        <CardHeader>
          <CardTitle className="flex items-center gap-3">
            <DollarSign className="h-5 w-5 text-green-600" />
            Economic Parameters
          </CardTitle>
        </CardHeader>
        <CardContent className="space-y-4">
          <div className="grid grid-cols-2 gap-4">
            <div>
              <Label className="font-semibold">Grid Cost ($/kWh)</Label>
              <Input
                type="number"
                step="0.01"
                value={economicParams.gridCostPerKwh}
                onChange={(e) =>
                  updateConfig({
                    economicParams: { ...economicParams, gridCostPerKwh: Number.parseFloat(e.target.value) || 0.12 },
                  })
                }
                className="mt-1"
              />
            </div>

            <div>
              <Label className="font-semibold">Solar Cost ($/W)</Label>
              <Input
                type="number"
                step="0.1"
                value={economicParams.solarCostPerWatt}
                onChange={(e) =>
                  updateConfig({
                    economicParams: { ...economicParams, solarCostPerWatt: Number.parseFloat(e.target.value) || 3.0 },
                  })
                }
                className="mt-1"
              />
            </div>

            <div>
              <Label className="font-semibold">Battery Cost ($/kWh)</Label>
              <Input
                type="number"
                step="10"
                value={economicParams.batteryCostPerKwh}
                onChange={(e) =>
                  updateConfig({
                    economicParams: { ...economicParams, batteryCostPerKwh: Number.parseFloat(e.target.value) || 500 },
                  })
                }
                className="mt-1"
              />
            </div>

            <div>
              <Label className="font-semibold">Discount Rate (%)</Label>
              <Input
                type="number"
                step="0.1"
                value={economicParams.discountRate * 100}
                onChange={(e) =>
                  updateConfig({
                    economicParams: { ...economicParams, discountRate: (Number.parseFloat(e.target.value) || 6) / 100 },
                  })
                }
                className="mt-1"
              />
            </div>
          </div>

          <div>
            <Label className="font-semibold">System Lifespan: {economicParams.systemLifespan} years</Label>
            <Slider
              value={[economicParams.systemLifespan]}
              onValueChange={([value]) =>
                updateConfig({
                  economicParams: { ...economicParams, systemLifespan: value },
                })
              }
              max={30}
              min={15}
              step={1}
              className="mt-2"
            />
          </div>
        </CardContent>
      </Card>

      {/* Location Settings */}
      <Card className="card-enhanced">
        <CardHeader>
          <CardTitle className="flex items-center gap-3">
            <FileText className="h-5 w-5 text-purple-600" />
            Location & Weather
          </CardTitle>
        </CardHeader>
        <CardContent className="space-y-4">
          <div>
            <Label className="font-semibold">Weather Location</Label>
            <Input
              placeholder="e.g., Chicago, IL"
              value={config.weatherLocation || ""}
              onChange={(e) => updateConfig({ weatherLocation: e.target.value })}
              className="mt-1"
            />
          </div>

          <div className="flex items-center justify-between p-3 bg-blue-50 rounded-lg">
            <Label htmlFor="real-weather" className="font-semibold">
              Use Real Weather Data
            </Label>
            <Switch
              id="real-weather"
              checked={config.useRealWeather}
              onCheckedChange={(checked) => updateConfig({ useRealWeather: checked })}
            />
          </div>

          {config.location && (
            <div className="p-3 bg-gray-50 rounded-lg">
              <p className="text-sm font-medium">Coordinates:</p>
              <p className="text-sm text-gray-600">
                Lat: {config.location.lat.toFixed(4)}, Lng: {config.location.lng.toFixed(4)}
              </p>
            </div>
          )}
        </CardContent>
      </Card>

      {/* Run Advanced Simulation */}
      <div className="lg:col-span-2">
        <Button
          onClick={onRun}
          disabled={isLoading}
          className="w-full bg-gradient-to-r from-purple-600 to-pink-600 hover:from-purple-700 hover:to-pink-700 mobile-btn mobile-rounded font-semibold"
        >
          {isLoading ? "Running Advanced Simulation..." : "🚀 Run Advanced Simulation"}
        </Button>
      </div>
    </div>
  )
}


--------------------------------------------------------------------------------
FILE: components/simulation/pro/basic-controls.tsx
--------------------------------------------------------------------------------
"use client"

import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Slider } from "@/components/ui/slider"
import { Switch } from "@/components/ui/switch"
import { Label } from "@/components/ui/label"
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select"
import type { SimulationConfig } from "@/lib/simulation/engine"
import { Battery, Sun, Zap, Settings } from "lucide-react"

interface BasicControlsProps {
  config: SimulationConfig
  onChange: (config: SimulationConfig) => void
  onRun: () => void
  isLoading: boolean
}

export function BasicControls({ config, onChange, onRun, isLoading }: BasicControlsProps) {
  const updateConfig = (updates: Partial<SimulationConfig>) => {
    onChange({ ...config, ...updates })
  }

  return (
    <Card className="card-enhanced">
      <CardHeader>
        <CardTitle className="flex items-center gap-3">
          <Settings className="h-5 w-5 text-blue-600" />
          Basic Controls
        </CardTitle>
      </CardHeader>
      <CardContent className="space-y-6">
        {/* Battery Capacity */}
        <div className="space-y-3">
          <Label className="flex items-center gap-2 font-semibold">
            <Battery className="h-4 w-4 text-green-600" />
            Battery Capacity: {config.batteryCapacity} kWh
          </Label>
          <Slider
            value={[config.batteryCapacity]}
            onValueChange={([value]) => updateConfig({ batteryCapacity: value })}
            max={50}
            min={0}
            step={1}
            className="w-full"
          />
          <div className="flex justify-between text-sm text-gray-500">
            <span>0 kWh</span>
            <span>50 kWh</span>
          </div>
        </div>

        {/* Battery Type */}
        <div className="space-y-3">
          <Label className="font-semibold">Battery Type</Label>
          <Select value={config.batteryType} onValueChange={(value: any) => updateConfig({ batteryType: value })}>
            <SelectTrigger>
              <SelectValue />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value="lithium">Lithium-ion (High efficiency)</SelectItem>
              <SelectItem value="lead-acid">Lead-acid (Budget friendly)</SelectItem>
              <SelectItem value="flow">Flow Battery (Long duration)</SelectItem>
              <SelectItem value="sodium">Sodium-ion (Sustainable)</SelectItem>
            </SelectContent>
          </Select>
        </div>

        {/* Battery Efficiency */}
        <div className="space-y-3">
          <Label className="flex items-center gap-2 font-semibold">
            <Zap className="h-4 w-4 text-yellow-600" />
            Battery Efficiency: {config.batteryEfficiency}%
          </Label>
          <Slider
            value={[config.batteryEfficiency]}
            onValueChange={([value]) => updateConfig({ batteryEfficiency: value })}
            max={98}
            min={70}
            step={1}
            className="w-full"
          />
          <div className="flex justify-between text-sm text-gray-500">
            <span>70%</span>
            <span>98%</span>
          </div>
        </div>

        {/* Load Profile Type */}
        <div className="space-y-3">
          <Label className="font-semibold">Load Profile</Label>
          <Select
            value={config.loadProfileType}
            onValueChange={(value: any) => updateConfig({ loadProfileType: value })}
          >
            <SelectTrigger>
              <SelectValue />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value="default">Default Profile</SelectItem>
              <SelectItem value="residential">Residential Home</SelectItem>
              <SelectItem value="commercial">Commercial Building</SelectItem>
              <SelectItem value="custom">Custom Upload</SelectItem>
            </SelectContent>
          </Select>
        </div>

        {/* Solar Power Toggle */}
        <div className="flex items-center justify-between p-4 bg-gradient-to-r from-yellow-50 to-orange-50 rounded-xl border-2 border-yellow-200">
          <Label htmlFor="solar-toggle" className="flex items-center gap-2 cursor-pointer">
            <Sun className="h-4 w-4 text-yellow-600" />
            <span className="font-semibold text-yellow-800">Enable Solar Power</span>
          </Label>
          <Switch
            id="solar-toggle"
            checked={config.solarEnabled}
            onCheckedChange={(checked) => updateConfig({ solarEnabled: checked })}
            className="data-[state=checked]:bg-yellow-600"
          />
        </div>

        {/* Time of Use Rates */}
        <div className="flex items-center justify-between p-4 bg-gradient-to-r from-blue-50 to-purple-50 rounded-xl border-2 border-blue-200">
          <Label htmlFor="tou-toggle" className="flex items-center gap-2 cursor-pointer">
            <Zap className="h-4 w-4 text-blue-600" />
            <span className="font-semibold text-blue-800">Time-of-Use Rates</span>
          </Label>
          <Switch
            id="tou-toggle"
            checked={config.timeOfUseRates}
            onCheckedChange={(checked) => updateConfig({ timeOfUseRates: checked })}
            className="data-[state=checked]:bg-blue-600"
          />
        </div>

        {/* Run Simulation Button */}
        <div className="pt-4">
          <Button
            onClick={onRun}
            disabled={isLoading}
            className="w-full bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700 mobile-btn mobile-rounded font-semibold"
          >
            {isLoading ? "Running..." : "⚡ Run Simulation"}
          </Button>
        </div>
      </CardContent>
    </Card>
  )
}


--------------------------------------------------------------------------------
FILE: components/simulation/pro/cost-analysis.tsx
--------------------------------------------------------------------------------
"use client"

import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
import type { SimulationResult, SimulationConfig } from "@/lib/simulation/engine"
import { DollarSign, TrendingUp, Calendar, BarChart3 } from "lucide-react"

interface CostAnalysisProps {
  data: SimulationResult
  config: SimulationConfig
}

export function CostAnalysis({ data, config }: CostAnalysisProps) {
  const { costAnalysis } = data

  // Format currency
  const formatCurrency = (value: number) => {
    return new Intl.NumberFormat("en-US", {
      style: "currency",
      currency: "USD",
      minimumFractionDigits: 2,
      maximumFractionDigits: 2,
    }).format(value)
  }

  // Calculate annual values
  const annualGridCost = costAnalysis.totalGridCost * 365
  const annualSolarSavings = costAnalysis.solarSavings * 365
  const annualBatterySavings = costAnalysis.batterySavings * 365
  const annualNetCost = costAnalysis.netCost * 365

  // Calculate 10-year values
  const tenYearGridCost = annualGridCost * 10
  const tenYearSolarSavings = annualSolarSavings * 10
  const tenYearBatterySavings = annualBatterySavings * 10
  const tenYearNetCost = annualNetCost * 10

  return (
    <Card className="card-enhanced mobile-rounded">
      <CardHeader>
        <CardTitle className="flex items-center gap-2">
          <DollarSign className="h-5 w-5 text-green-600" />
          Pro Cost Analysis
        </CardTitle>
      </CardHeader>
      <CardContent className="space-y-6">
        <Tabs defaultValue="daily" className="w-full">
          <TabsList className="grid w-full grid-cols-3 mobile-rounded">
            <TabsTrigger value="daily" className="flex items-center gap-2">
              <DollarSign className="h-4 w-4" />
              Daily
            </TabsTrigger>
            <TabsTrigger value="annual" className="flex items-center gap-2">
              <Calendar className="h-4 w-4" />
              Annual
            </TabsTrigger>
            <TabsTrigger value="tenyear" className="flex items-center gap-2">
              <TrendingUp className="h-4 w-4" />
              10-Year
            </TabsTrigger>
          </TabsList>

          <TabsContent value="daily" className="pt-4">
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div className="space-y-4">
                <div className="grid grid-cols-2 gap-4">
                  <Card className="bg-red-50 border-red-100">
                    <CardContent className="p-4">
                      <p className="text-sm font-medium text-red-800">Grid Cost</p>
                      <p className="text-2xl font-bold text-red-700">{formatCurrency(costAnalysis.totalGridCost)}</p>
                    </CardContent>
                  </Card>
                  <Card className="bg-green-50 border-green-100">
                    <CardContent className="p-4">
                      <p className="text-sm font-medium text-green-800">Solar Savings</p>
                      <p className="text-2xl font-bold text-green-700">{formatCurrency(costAnalysis.solarSavings)}</p>
                    </CardContent>
                  </Card>
                </div>
                <div className="grid grid-cols-2 gap-4">
                  <Card className="bg-blue-50 border-blue-100">
                    <CardContent className="p-4">
                      <p className="text-sm font-medium text-blue-800">Battery Savings</p>
                      <p className="text-2xl font-bold text-blue-700">{formatCurrency(costAnalysis.batterySavings)}</p>
                    </CardContent>
                  </Card>
                  <Card className="bg-purple-50 border-purple-100">
                    <CardContent className="p-4">
                      <p className="text-sm font-medium text-purple-800">Net Cost</p>
                      <p className="text-2xl font-bold text-purple-700">{formatCurrency(costAnalysis.netCost)}</p>
                    </CardContent>
                  </Card>
                </div>
              </div>

              <Card>
                <CardHeader className="pb-2">
                  <CardTitle className="text-base flex items-center gap-2">
                    <BarChart3 className="h-4 w-4" />
                    Daily Cost Breakdown
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="h-40 flex items-end gap-4 pt-4">
                    <div className="flex-1 flex flex-col items-center">
                      <div
                        className="w-full bg-red-500 rounded-t-sm"
                        style={{ height: `${(costAnalysis.totalGridCost / 10) * 100}px` }}
                      ></div>
                      <p className="text-xs mt-2">Grid</p>
                    </div>
                    <div className="flex-1 flex flex-col items-center">
                      <div
                        className="w-full bg-green-500 rounded-t-sm"
                        style={{ height: `${(costAnalysis.solarSavings / 10) * 100}px` }}
                      ></div>
                      <p className="text-xs mt-2">Solar</p>
                    </div>
                    <div className="flex-1 flex flex-col items-center">
                      <div
                        className="w-full bg-blue-500 rounded-t-sm"
                        style={{ height: `${(costAnalysis.batterySavings / 10) * 100}px` }}
                      ></div>
                      <p className="text-xs mt-2">Battery</p>
                    </div>
                    <div className="flex-1 flex flex-col items-center">
                      <div
                        className="w-full bg-purple-500 rounded-t-sm"
                        style={{ height: `${(costAnalysis.netCost / 10) * 100}px` }}
                      ></div>
                      <p className="text-xs mt-2">Net</p>
                    </div>
                  </div>
                </CardContent>
              </Card>
            </div>
          </TabsContent>

          <TabsContent value="annual" className="pt-4">
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div className="space-y-4">
                <div className="grid grid-cols-2 gap-4">
                  <Card className="bg-red-50 border-red-100">
                    <CardContent className="p-4">
                      <p className="text-sm font-medium text-red-800">Annual Grid Cost</p>
                      <p className="text-2xl font-bold text-red-700">{formatCurrency(annualGridCost)}</p>
                    </CardContent>
                  </Card>
                  <Card className="bg-green-50 border-green-100">
                    <CardContent className="p-4">
                      <p className="text-sm font-medium text-green-800">Annual Solar Savings</p>
                      <p className="text-2xl font-bold text-green-700">{formatCurrency(annualSolarSavings)}</p>
                    </CardContent>
                  </Card>
                </div>
                <div className="grid grid-cols-2 gap-4">
                  <Card className="bg-blue-50 border-blue-100">
                    <CardContent className="p-4">
                      <p className="text-sm font-medium text-blue-800">Annual Battery Savings</p>
                      <p className="text-2xl font-bold text-blue-700">{formatCurrency(annualBatterySavings)}</p>
                    </CardContent>
                  </Card>
                  <Card className="bg-purple-50 border-purple-100">
                    <CardContent className="p-4">
                      <p className="text-sm font-medium text-purple-800">Annual Net Cost</p>
                      <p className="text-2xl font-bold text-purple-700">{formatCurrency(annualNetCost)}</p>
                    </CardContent>
                  </Card>
                </div>
              </div>

              <Card>
                <CardHeader className="pb-2">
                  <CardTitle className="text-base flex items-center gap-2">
                    <BarChart3 className="h-4 w-4" />
                    Annual Cost Breakdown
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="h-40 flex items-end gap-4 pt-4">
                    <div className="flex-1 flex flex-col items-center">
                      <div
                        className="w-full bg-red-500 rounded-t-sm"
                        style={{ height: `${(annualGridCost / 3000) * 100}px` }}
                      ></div>
                      <p className="text-xs mt-2">Grid</p>
                    </div>
                    <div className="flex-1 flex flex-col items-center">
                      <div
                        className="w-full bg-green-500 rounded-t-sm"
                        style={{ height: `${(annualSolarSavings / 3000) * 100}px` }}
                      ></div>
                      <p className="text-xs mt-2">Solar</p>
                    </div>
                    <div className="flex-1 flex flex-col items-center">
                      <div
                        className="w-full bg-blue-500 rounded-t-sm"
                        style={{ height: `${(annualBatterySavings / 3000) * 100}px` }}
                      ></div>
                      <p className="text-xs mt-2">Battery</p>
                    </div>
                    <div className="flex-1 flex flex-col items-center">
                      <div
                        className="w-full bg-purple-500 rounded-t-sm"
                        style={{ height: `${(annualNetCost / 3000) * 100}px` }}
                      ></div>
                      <p className="text-xs mt-2">Net</p>
                    </div>
                  </div>
                </CardContent>
              </Card>
            </div>
          </TabsContent>

          <TabsContent value="tenyear" className="pt-4">
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div className="space-y-4">
                <div className="grid grid-cols-2 gap-4">
                  <Card className="bg-red-50 border-red-100">
                    <CardContent className="p-4">
                      <p className="text-sm font-medium text-red-800">10-Year Grid Cost</p>
                      <p className="text-2xl font-bold text-red-700">{formatCurrency(tenYearGridCost)}</p>
                    </CardContent>
                  </Card>
                  <Card className="bg-green-50 border-green-100">
                    <CardContent className="p-4">
                      <p className="text-sm font-medium text-green-800">10-Year Solar Savings</p>
                      <p className="text-2xl font-bold text-green-700">{formatCurrency(tenYearSolarSavings)}</p>
                    </CardContent>
                  </Card>
                </div>
                <div className="grid grid-cols-2 gap-4">
                  <Card className="bg-blue-50 border-blue-100">
                    <CardContent className="p-4">
                      <p className="text-sm font-medium text-blue-800">10-Year Battery Savings</p>
                      <p className="text-2xl font-bold text-blue-700">{formatCurrency(tenYearBatterySavings)}</p>
                    </CardContent>
                  </Card>
                  <Card className="bg-purple-50 border-purple-100">
                    <CardContent className="p-4">
                      <p className="text-sm font-medium text-purple-800">10-Year Net Cost</p>
                      <p className="text-2xl font-bold text-purple-700">{formatCurrency(tenYearNetCost)}</p>
                    </CardContent>
                  </Card>
                </div>
              </div>

              <Card>
                <CardHeader className="pb-2">
                  <CardTitle className="text-base flex items-center gap-2">
                    <BarChart3 className="h-4 w-4" />
                    10-Year Cost Breakdown
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="h-40 flex items-end gap-4 pt-4">
                    <div className="flex-1 flex flex-col items-center">
                      <div
                        className="w-full bg-red-500 rounded-t-sm"
                        style={{ height: `${(tenYearGridCost / 30000) * 100}px` }}
                      ></div>
                      <p className="text-xs mt-2">Grid</p>
                    </div>
                    <div className="flex-1 flex flex-col items-center">
                      <div
                        className="w-full bg-green-500 rounded-t-sm"
                        style={{ height: `${(tenYearSolarSavings / 30000) * 100}px` }}
                      ></div>
                      <p className="text-xs mt-2">Solar</p>
                    </div>
                    <div className="flex-1 flex flex-col items-center">
                      <div
                        className="w-full bg-blue-500 rounded-t-sm"
                        style={{ height: `${(tenYearBatterySavings / 30000) * 100}px` }}
                      ></div>
                      <p className="text-xs mt-2">Battery</p>
                    </div>
                    <div className="flex-1 flex flex-col items-center">
                      <div
                        className="w-full bg-purple-500 rounded-t-sm"
                        style={{ height: `${(tenYearNetCost / 30000) * 100}px` }}
                      ></div>
                      <p className="text-xs mt-2">Net</p>
                    </div>
                  </div>
                </CardContent>
              </Card>
            </div>
          </TabsContent>
        </Tabs>

        {/* ROI and Payback Period */}
        {costAnalysis.roi && costAnalysis.paybackPeriod && (
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mt-6">
            <Card className="bg-gradient-to-r from-blue-50 to-purple-50 border-blue-100">
              <CardContent className="p-6">
                <h3 className="text-lg font-semibold text-blue-800 mb-2">Return on Investment (ROI)</h3>
                <p className="text-3xl font-bold text-blue-700">{costAnalysis.roi.toFixed(1)}%</p>
                <p className="text-sm text-blue-600 mt-1">Annual return on investment</p>
              </CardContent>
            </Card>

            <Card className="bg-gradient-to-r from-green-50 to-teal-50 border-green-100">
              <CardContent className="p-6">
                <h3 className="text-lg font-semibold text-green-800 mb-2">Payback Period</h3>
                <p className="text-3xl font-bold text-green-700">{costAnalysis.paybackPeriod.toFixed(1)} years</p>
                <p className="text-sm text-green-600 mt-1">Time to recoup investment</p>
              </CardContent>
            </Card>
          </div>
        )}
      </CardContent>
    </Card>
  )
}


--------------------------------------------------------------------------------
FILE: components/simulation/pro/enhanced-chart.tsx
--------------------------------------------------------------------------------
"use client"

import { useEffect, useRef, useState } from "react"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Tabs, TabsList, TabsTrigger } from "@/components/ui/tabs"
import { Badge } from "@/components/ui/badge"
import type { SimulationResult, SimulationConfig } from "@/lib/simulation/engine"
import { Sun, Cloud, Battery, Zap, TrendingUp } from "lucide-react"

interface EnhancedChartProps {
  data: SimulationResult
  config: SimulationConfig
  showWeather?: boolean
}

export function EnhancedChart({ data, config, showWeather = false }: EnhancedChartProps) {
  const chartRef = useRef<HTMLCanvasElement>(null)
  const [activeTab, setActiveTab] = useState("energy")

  useEffect(() => {
    if (!chartRef.current || !data) return

    const ctx = chartRef.current.getContext("2d")
    if (!ctx) return

    // Clear previous chart
    ctx.clearRect(0, 0, chartRef.current.width, chartRef.current.height)

    // Chart dimensions
    const width = chartRef.current.width
    const height = chartRef.current.height
    const padding = { top: 40, right: 30, bottom: 60, left: 60 }
    const chartWidth = width - padding.left - padding.right
    const chartHeight = height - padding.top - padding.bottom

    // Find max value for scaling
    const allValues = data.data.flatMap((point) => [point.solar, point.consumption, point.grid])
    const maxValue = Math.max(...allValues) * 1.2 // Add 20% headroom

    // Draw axes
    ctx.beginPath()
    ctx.strokeStyle = "#94a3b8" // slate-400
    ctx.lineWidth = 1
    ctx.moveTo(padding.left, padding.top)
    ctx.lineTo(padding.left, height - padding.bottom)
    ctx.lineTo(width - padding.right, height - padding.bottom)
    ctx.stroke()

    // Draw grid lines
    ctx.beginPath()
    ctx.strokeStyle = "#e2e8f0" // slate-200
    ctx.lineWidth = 0.5
    for (let i = 0; i <= 5; i++) {
      const y = padding.top + (chartHeight * i) / 5
      ctx.moveTo(padding.left, y)
      ctx.lineTo(width - padding.right, y)
    }
    ctx.stroke()

    // Draw y-axis labels
    ctx.fillStyle = "#64748b" // slate-500
    ctx.font = "12px Inter, sans-serif"
    ctx.textAlign = "right"
    for (let i = 0; i <= 5; i++) {
      const value = maxValue - (maxValue * i) / 5
      const y = padding.top + (chartHeight * i) / 5
      ctx.fillText(`${Math.round(value)} kW`, padding.left - 10, y + 4)
    }

    // Draw x-axis labels (hours)
    ctx.textAlign = "center"
    const hourStep = Math.ceil(data.data.length / 12) // Show fewer labels on small screens
    for (let i = 0; i < data.data.length; i += hourStep) {
      const x = padding.left + (chartWidth * i) / (data.data.length - 1)
      ctx.fillText(data.data[i].time, x, height - padding.bottom + 20)
    }

    // Draw title
    ctx.fillStyle = "#1e293b" // slate-800
    ctx.font = "bold 16px Inter, sans-serif"
    ctx.textAlign = "center"
    ctx.fillText("Energy Flow Over Time", width / 2, 20)

    // Draw legend
    const legendItems = [
      { label: "Solar", color: "#eab308" }, // yellow-500
      { label: "Consumption", color: "#ef4444" }, // red-500
      { label: "Grid", color: "#3b82f6" }, // blue-500
    ]

    ctx.font = "12px Inter, sans-serif"
    ctx.textAlign = "left"
    let legendX = padding.left
    legendItems.forEach((item) => {
      ctx.fillStyle = item.color
      ctx.fillRect(legendX, height - padding.bottom + 40, 12, 12)
      ctx.fillStyle = "#64748b" // slate-500
      ctx.fillText(item.label, legendX + 16, height - padding.bottom + 50)
      legendX += 100
    })

    // Draw data lines
    if (activeTab === "energy") {
      // Draw solar generation
      if (config.solarEnabled) {
        drawLine(
          ctx,
          data.data.map((point) => point.solar),
          "#eab308", // yellow-500
          padding,
          chartWidth,
          chartHeight,
          maxValue,
          data.data.length,
        )
      }

      // Draw consumption
      drawLine(
        ctx,
        data.data.map((point) => point.consumption),
        "#ef4444", // red-500
        padding,
        chartWidth,
        chartHeight,
        maxValue,
        data.data.length,
      )

      // Draw grid usage
      drawLine(
        ctx,
        data.data.map((point) => point.grid),
        "#3b82f6", // blue-500
        padding,
        chartWidth,
        chartHeight,
        maxValue,
        data.data.length,
      )
    } else if (activeTab === "battery") {
      // Draw battery state
      drawLine(
        ctx,
        data.data.map((point) => (point.battery / 100) * maxValue), // Scale to match chart
        "#22c55e", // green-500
        padding,
        chartWidth,
        chartHeight,
        maxValue,
        data.data.length,
        true,
      )

      // Update legend for battery
      ctx.clearRect(padding.left, height - padding.bottom + 35, width - padding.left - padding.right, 25)
      ctx.fillStyle = "#22c55e" // green-500
      ctx.fillRect(padding.left, height - padding.bottom + 40, 12, 12)
      ctx.fillStyle = "#64748b" // slate-500
      ctx.fillText("Battery State (%)", padding.left + 16, height - padding.bottom + 50)
    } else if (activeTab === "weather" && showWeather) {
      // Draw weather factors
      drawLine(
        ctx,
        data.data.map((point) => (point.weather || 0) * maxValue * 0.8), // Scale to match chart
        "#8b5cf6", // purple-500
        padding,
        chartWidth,
        chartHeight,
        maxValue,
        data.data.length,
        true,
      )

      // Update legend for weather
      ctx.clearRect(padding.left, height - padding.bottom + 35, width - padding.left - padding.right, 25)
      ctx.fillStyle = "#8b5cf6" // purple-500
      ctx.fillRect(padding.left, height - padding.bottom + 40, 12, 12)
      ctx.fillStyle = "#64748b" // slate-500
      ctx.fillText("Weather Factor", padding.left + 16, height - padding.bottom + 50)
    }
  }, [data, activeTab, showWeather, config.solarEnabled])

  // Helper function to draw a line
  const drawLine = (
    ctx: CanvasRenderingContext2D,
    values: number[],
    color: string,
    padding: { top: number; right: number; bottom: number; left: number },
    chartWidth: number,
    chartHeight: number,
    maxValue: number,
    dataLength: number,
    fill = false,
  ) => {
    ctx.beginPath()
    ctx.strokeStyle = color
    ctx.fillStyle = color + "33" // Add transparency for fill
    ctx.lineWidth = 2

    for (let i = 0; i < values.length; i++) {
      const x = padding.left + (chartWidth * i) / (dataLength - 1)
      const y = padding.top + chartHeight - (chartHeight * values[i]) / maxValue

      if (i === 0) {
        ctx.moveTo(x, y)
      } else {
        ctx.lineTo(x, y)
      }
    }

    ctx.stroke()

    if (fill) {
      // Complete the path for filling
      ctx.lineTo(padding.left + chartWidth, padding.top + chartHeight)
      ctx.lineTo(padding.left, padding.top + chartHeight)
      ctx.closePath()
      ctx.fill()
    }
  }

  // Calculate summary statistics
  const totalSolar = data.summary.totalSolar.toFixed(1)
  const totalConsumption = data.summary.totalConsumption.toFixed(1)
  const totalGrid = data.summary.totalGrid.toFixed(1)
  const avgBattery = Math.round(data.summary.avgBattery)
  const solarPercentage = ((data.summary.totalSolar / data.summary.totalConsumption) * 100).toFixed(1)

  return (
    <Card className="card-enhanced mobile-rounded">
      <CardHeader className="pb-2">
        <div className="flex items-center justify-between">
          <CardTitle className="flex items-center gap-2">
            <TrendingUp className="h-5 w-5 text-blue-600" />
            Pro Energy Analysis
          </CardTitle>
          <Tabs value={activeTab} onValueChange={setActiveTab} className="w-auto">
            <TabsList className="mobile-rounded">
              <TabsTrigger value="energy" className="flex items-center gap-1">
                <Zap className="h-3.5 w-3.5" />
                <span className="hidden sm:inline">Energy</span>
              </TabsTrigger>
              <TabsTrigger value="battery" className="flex items-center gap-1">
                <Battery className="h-3.5 w-3.5" />
                <span className="hidden sm:inline">Battery</span>
              </TabsTrigger>
              {showWeather && (
                <TabsTrigger value="weather" className="flex items-center gap-1">
                  <Cloud className="h-3.5 w-3.5" />
                  <span className="hidden sm:inline">Weather</span>
                </TabsTrigger>
              )}
            </TabsList>
          </Tabs>
        </div>
      </CardHeader>
      <CardContent>
        <div className="h-80 w-full">
          <canvas ref={chartRef} width={800} height={400} className="w-full h-full"></canvas>
        </div>

        <div className="grid grid-cols-2 md:grid-cols-5 gap-2 mt-4">
          <div className="bg-yellow-50 p-3 rounded-lg border border-yellow-100">
            <div className="flex items-center gap-2">
              <Sun className="h-4 w-4 text-yellow-600" />
              <span className="text-sm font-medium text-yellow-800">Solar</span>
            </div>
            <p className="text-lg font-bold text-yellow-700 mt-1">{totalSolar} kWh</p>
            <p className="text-xs text-yellow-600">{solarPercentage}% of usage</p>
          </div>

          <div className="bg-red-50 p-3 rounded-lg border border-red-100">
            <div className="flex items-center gap-2">
              <Zap className="h-4 w-4 text-red-600" />
              <span className="text-sm font-medium text-red-800">Usage</span>
            </div>
            <p className="text-lg font-bold text-red-700 mt-1">{totalConsumption} kWh</p>
            <p className="text-xs text-red-600">Total consumption</p>
          </div>

          <div className="bg-blue-50 p-3 rounded-lg border border-blue-100">
            <div className="flex items-center gap-2">
              <TrendingUp className="h-4 w-4 text-blue-600" />
              <span className="text-sm font-medium text-blue-800">Grid</span>
            </div>
            <p className="text-lg font-bold text-blue-700 mt-1">{totalGrid} kWh</p>
            <p className="text-xs text-blue-600">From utility</p>
          </div>

          <div className="bg-green-50 p-3 rounded-lg border border-green-100">
            <div className="flex items-center gap-2">
              <Battery className="h-4 w-4 text-green-600" />
              <span className="text-sm font-medium text-green-800">Battery</span>
            </div>
            <p className="text-lg font-bold text-green-700 mt-1">{avgBattery}%</p>
            <p className="text-xs text-green-600">Avg charge</p>
          </div>

          <div className="bg-purple-50 p-3 rounded-lg border border-purple-100">
            <div className="flex items-center gap-2">
              <Badge className="bg-gradient-to-r from-purple-600 to-pink-600 text-white text-xs">PRO</Badge>
              <span className="text-sm font-medium text-purple-800">Type</span>
            </div>
            <p className="text-lg font-bold text-purple-700 mt-1 capitalize">{config.batteryType || "Standard"}</p>
            <p className="text-xs text-purple-600">{config.batteryEfficiency}% efficient</p>
          </div>
        </div>
      </CardContent>
    </Card>
  )
}


--------------------------------------------------------------------------------
FILE: components/simulation/pro/export-panel.tsx
--------------------------------------------------------------------------------
"use client"

import { useState } from "react"
import Link from "next/link"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Tabs, TabsList, TabsTrigger } from "@/components/ui/tabs"
import { Checkbox } from "@/components/ui/checkbox"
import { Label } from "@/components/ui/label"
import type { SimulationConfig, SimulationResult } from "@/lib/simulation/engine"
import type { Project } from "@/lib/simulation/projects"
import { Download, FileText, ImageIcon, Table, Share2, Copy } from "lucide-react"
import { Input } from "@/components/ui/input"
import { Textarea } from "@/components/ui/textarea"

interface ExportPanelProps {
  results: SimulationResult | null
  config: SimulationConfig
  project: Project | null
}

export function ExportPanel({ results, config, project }: ExportPanelProps) {
  const [exportFormat, setExportFormat] = useState("csv")
  const [includeConfig, setIncludeConfig] = useState(true)
  const [includeCostAnalysis, setIncludeCostAnalysis] = useState(true)
  const [includeWeatherData, setIncludeWeatherData] = useState(true)

  const handleExport = () => {
    if (!results) return

    switch (exportFormat) {
      case "csv":
        exportCSV()
        break
      case "json":
        exportJSON()
        break
      case "pdf":
        alert("PDF export feature coming soon!")
        break
      case "png":
        alert("PNG export feature coming soon!")
        break
    }
  }

  const handleCopyLink = () => {
    if (project) {
      const shareUrl = `${window.location.origin}/simulation/shared/${project.id}`
      navigator.clipboard
        .writeText(shareUrl)
        .then(() => {
          alert("Share link copied to clipboard!")
        })
        .catch(() => {
          alert("Failed to copy link. Please copy manually.")
        })
    }
  }

  const exportCSV = () => {
    if (!results) return

    const rows = [["Hour", "Solar Generation (kW)", "Load Demand (kW)", "Battery Level (kWh)", "Grid Usage (kW)"]]

    // Add hourly data
    results.hours.forEach((hour, i) => {
      rows.push([
        hour.toString(),
        results.solarProfile[i].toFixed(2),
        results.loadProfile[i].toFixed(2),
        results.batteryStorage[i].toFixed(2),
        results.gridUsage[i].toFixed(2),
      ])
    })

    // Add empty row as separator
    rows.push([])

    // Add cost analysis if selected
    if (includeCostAnalysis && results.costAnalysis) {
      rows.push(["Cost Analysis"])
      rows.push(["Total Grid Cost", `$${results.costAnalysis.totalGridCost.toFixed(2)}`])
      rows.push(["Solar Savings", `$${results.costAnalysis.solarSavings.toFixed(2)}`])
      rows.push(["Battery Savings", `$${results.costAnalysis.batterySavings.toFixed(2)}`])
      rows.push(["Net Daily Cost", `$${results.costAnalysis.netCost.toFixed(2)}`])
      rows.push(["Payback Period", `${results.costAnalysis.paybackPeriod.toFixed(1)} years`])

      // Add advanced metrics if available
      if ("lcoe" in results.costAnalysis) {
        rows.push(["LCOE", `$${results.costAnalysis.lcoe.toFixed(4)} per kWh`])
      }
      if ("npv" in results.costAnalysis) {
        rows.push(["NPV", `$${results.costAnalysis.npv.toFixed(2)}`])
      }
      if ("irr" in results.costAnalysis) {
        rows.push(["IRR", `${(results.costAnalysis.irr * 100).toFixed(2)}%`])
      }
    }

    // Add weather data if selected
    if (includeWeatherData && results.weatherData) {
      rows.push([])
      rows.push(["Weather Data"])
      rows.push(["Hour", "Temperature (°C)", "Irradiance (W/m²)", "Cloud Cover (%)"])
      results.hours.forEach((hour, i) => {
        rows.push([
          hour.toString(),
          results.weatherData!.temperature[i].toFixed(1),
          results.weatherData!.irradiance[i].toFixed(0),
          results.weatherData!.cloudCover[i].toFixed(0),
        ])
      })
    }

    // Add configuration if selected
    if (includeConfig) {
      rows.push([])
      rows.push(["Simulation Configuration"])
      rows.push(["Battery Capacity", `${config.batteryCapacity} kWh`])
      rows.push(["Battery Efficiency", `${config.batteryEfficiency}%`])
      rows.push(["Solar Enabled", config.solarEnabled ? "Yes" : "No"])
      if (config.batteryType) {
        rows.push(["Battery Type", config.batteryType])
      }
      if (config.loadProfileType) {
        rows.push(["Load Profile Type", config.loadProfileType])
      }
      if (config.weatherLocation) {
        rows.push(["Weather Location", config.weatherLocation])
      }
      if (config.timeOfUseRates !== undefined) {
        rows.push(["Time-of-Use Rates", config.timeOfUseRates ? "Enabled" : "Disabled"])
      }
    }

    // Convert to CSV
    const csvContent = rows.map((row) => row.join(",")).join("\n")

    // Create and download file
    const blob = new Blob([csvContent], { type: "text/csv" })
    const url = window.URL.createObjectURL(blob)
    const a = document.createElement("a")
    a.href = url
    a.download = `voltsphere-simulation-${new Date().toISOString().split("T")[0]}.csv`
    a.click()
    window.URL.revokeObjectURL(url)
  }

  const exportJSON = () => {
    if (!results) return

    // Create export object
    const exportData: any = {
      simulationResults: {
        hours: results.hours,
        solarProfile: results.solarProfile,
        loadProfile: results.loadProfile,
        batteryStorage: results.batteryStorage,
        gridUsage: results.gridUsage,
      },
    }

    // Add cost analysis if selected
    if (includeCostAnalysis && results.costAnalysis) {
      exportData.costAnalysis = results.costAnalysis
    }

    // Add weather data if selected
    if (includeWeatherData && results.weatherData) {
      exportData.weatherData = results.weatherData
    }

    // Add configuration if selected
    if (includeConfig) {
      exportData.configuration = config
    }

    // Add project metadata if available
    if (project) {
      exportData.project = {
        id: project.id,
        name: project.name,
        description: project.description,
        createdAt: project.createdAt,
        updatedAt: project.updatedAt,
      }
    }

    // Convert to JSON
    const jsonContent = JSON.stringify(exportData, null, 2)

    // Create and download file
    const blob = new Blob([jsonContent], { type: "application/json" })
    const url = window.URL.createObjectURL(blob)
    const a = document.createElement("a")
    a.href = url
    a.download = `voltsphere-simulation-${new Date().toISOString().split("T")[0]}.json`
    a.click()
    window.URL.revokeObjectURL(url)
  }

  return (
    <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
      <div className="lg:col-span-1">
        <Card className="card-enhanced">
          <CardHeader>
            <CardTitle className="flex items-center gap-3">
              <Download className="h-5 w-5 text-blue-600" />
              Export Options
            </CardTitle>
          </CardHeader>
          <CardContent className="space-y-6">
            <div>
              <Label className="font-semibold">Export Format</Label>
              <Tabs value={exportFormat} onValueChange={setExportFormat} className="mt-2">
                <TabsList className="grid grid-cols-4 w-full">
                  <TabsTrigger value="csv" className="flex items-center gap-1">
                    <FileText className="h-4 w-4" />
                    <span className="hidden sm:inline">CSV</span>
                  </TabsTrigger>
                  <TabsTrigger value="json" className="flex items-center gap-1">
                    <Table className="h-4 w-4" />
                    <span className="hidden sm:inline">JSON</span>
                  </TabsTrigger>
                  <TabsTrigger value="pdf" className="flex items-center gap-1">
                    <FileText className="h-4 w-4" />
                    <span className="hidden sm:inline">PDF</span>
                  </TabsTrigger>
                  <TabsTrigger value="png" className="flex items-center gap-1">
                    <ImageIcon className="h-4 w-4" />
                    <span className="hidden sm:inline">PNG</span>
                  </TabsTrigger>
                </TabsList>
              </Tabs>
            </div>

            <div className="space-y-3">
              <Label className="font-semibold">Include in Export</Label>
              <div className="space-y-2">
                <div className="flex items-center space-x-2">
                  <Checkbox
                    id="include-config"
                    checked={includeConfig}
                    onCheckedChange={(checked) => setIncludeConfig(checked as boolean)}
                  />
                  <Label htmlFor="include-config" className="cursor-pointer">
                    Simulation Configuration
                  </Label>
                </div>
                <div className="flex items-center space-x-2">
                  <Checkbox
                    id="include-cost"
                    checked={includeCostAnalysis}
                    onCheckedChange={(checked) => setIncludeCostAnalysis(checked as boolean)}
                  />
                  <Label htmlFor="include-cost" className="cursor-pointer">
                    Cost Analysis
                  </Label>
                </div>
                <div className="flex items-center space-x-2">
                  <Checkbox
                    id="include-weather"
                    checked={includeWeatherData}
                    onCheckedChange={(checked) => setIncludeWeatherData(checked as boolean)}
                    disabled={!results?.weatherData}
                  />
                  <Label
                    htmlFor="include-weather"
                    className={`cursor-pointer ${!results?.weatherData ? "text-gray-400" : ""}`}
                  >
                    Weather Data
                  </Label>
                </div>
              </div>
            </div>

            <Button
              onClick={handleExport}
              disabled={!results}
              className="w-full bg-gradient-to-r from-green-600 to-blue-600 hover:from-green-700 hover:to-blue-700"
            >
              <Download className="h-4 w-4 mr-2" />
              Export {exportFormat.toUpperCase()}
            </Button>
          </CardContent>
        </Card>
      </div>

      <div className="lg:col-span-2">
        <Card className="card-enhanced">
          <CardHeader>
            <CardTitle className="flex items-center gap-3">
              <Share2 className="h-5 w-5 text-purple-600" />
              Share & Embed
            </CardTitle>
          </CardHeader>
          <CardContent className="space-y-6">
            <div>
              <Label className="font-semibold">Share Link</Label>
              <div className="flex gap-2 mt-2">
                <Input
                  readOnly
                  value={
                    project
                      ? `${window.location.origin}/simulation/shared/${project.id}`
                      : "Save your project first to generate a share link"
                  }
                  disabled={!project}
                />
                <Button variant="outline" disabled={!project} onClick={handleCopyLink}>
                  <Copy className="h-4 w-4" />
                </Button>
              </div>
              <p className="text-sm text-gray-500 mt-1">
                {project?.isPublic
                  ? "This link is public and can be accessed by anyone"
                  : "Save and make your project public to share it"}
              </p>
            </div>

            <div>
              <Label className="font-semibold">Embed Code</Label>
              <div className="mt-2">
                <Textarea
                  readOnly
                  value={
                    project
                      ? `<iframe src="${window.location.origin}/simulation/embed/${project.id}" width="800" height="600" frameborder="0"></iframe>`
                      : "Save your project first to generate embed code"
                  }
                  disabled={!project}
                  rows={3}
                />
              </div>
              <p className="text-sm text-gray-500 mt-1">Copy this code to embed the simulation on your website</p>
            </div>

            <div className="p-4 bg-gray-50 rounded-lg">
              <h3 className="font-semibold mb-2">API Access</h3>
              <p className="text-sm text-gray-600 mb-4">
                Access this simulation programmatically via our API. Upgrade to an API tier for full access.
              </p>
              <div className="flex gap-2">
                <Button variant="outline" className="flex-1" onClick={() => alert("API documentation coming soon!")}>
                  View API Docs
                </Button>
                <Link href="/pricing" className="flex-1">
                  <Button className="w-full bg-purple-600 hover:bg-purple-700">Upgrade to API Tier</Button>
                </Link>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  )
}


--------------------------------------------------------------------------------
FILE: components/simulation/pro/project-panel.tsx
--------------------------------------------------------------------------------
"use client"

import { useState } from "react"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { Textarea } from "@/components/ui/textarea"
import { Dialog, DialogContent, DialogHeader, DialogTitle, DialogFooter } from "@/components/ui/dialog"
import { Badge } from "@/components/ui/badge"
import type { Project } from "@/lib/simulation/projects"
import { Save, FolderOpen, Trash2, Calendar, Tag } from "lucide-react"

interface ProjectPanelProps {
  projects: Project[]
  currentProject: Project | null
  onSave: (name: string, description?: string) => void
  onLoad: (project: Project) => void
  onDelete: (id: string) => void
}

export function ProjectPanel({ projects, currentProject, onSave, onLoad, onDelete }: ProjectPanelProps) {
  const [showSaveDialog, setShowSaveDialog] = useState(false)
  const [showDeleteDialog, setShowDeleteDialog] = useState(false)
  const [projectToDelete, setProjectToDelete] = useState<Project | null>(null)
  const [projectName, setProjectName] = useState("")
  const [projectDescription, setProjectDescription] = useState("")

  const handleSave = () => {
    if (projectName.trim()) {
      onSave(projectName, projectDescription)
      setShowSaveDialog(false)
      setProjectName("")
      setProjectDescription("")
    }
  }

  const handleDelete = () => {
    if (projectToDelete) {
      onDelete(projectToDelete.id)
      setShowDeleteDialog(false)
      setProjectToDelete(null)
    }
  }

  const confirmDelete = (project: Project) => {
    setProjectToDelete(project)
    setShowDeleteDialog(true)
  }

  return (
    <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
      <div className="lg:col-span-1">
        <Card className="card-enhanced">
          <CardHeader>
            <CardTitle className="flex items-center gap-3">
              <Save className="h-5 w-5 text-blue-600" />
              Save Project
            </CardTitle>
          </CardHeader>
          <CardContent className="space-y-4">
            <p className="text-gray-600">
              Save your current simulation configuration and results for future reference or sharing.
            </p>

            <Button
              onClick={() => setShowSaveDialog(true)}
              className="w-full bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700"
            >
              <Save className="h-4 w-4 mr-2" />
              Save Current Configuration
            </Button>

            {currentProject && (
              <div className="p-4 bg-blue-50 rounded-lg border border-blue-200">
                <p className="font-medium">Current Project:</p>
                <p className="text-blue-700 font-bold">{currentProject.name}</p>
                <p className="text-sm text-gray-600 mt-1">
                  Last updated: {new Date(currentProject.updatedAt).toLocaleString()}
                </p>
              </div>
            )}
          </CardContent>
        </Card>
      </div>

      <div className="lg:col-span-2">
        <Card className="card-enhanced">
          <CardHeader>
            <CardTitle className="flex items-center gap-3">
              <FolderOpen className="h-5 w-5 text-green-600" />
              Saved Projects
            </CardTitle>
          </CardHeader>
          <CardContent>
            {projects.length === 0 ? (
              <div className="text-center py-12">
                <FolderOpen className="h-16 w-16 mx-auto mb-4 text-gray-300" />
                <p className="text-gray-500">No saved projects yet. Save your first project to see it here.</p>
              </div>
            ) : (
              <div className="space-y-4">
                {projects.map((project) => (
                  <div
                    key={project.id}
                    className={`p-4 rounded-lg border-2 transition-all ${
                      currentProject?.id === project.id
                        ? "border-blue-500 bg-blue-50"
                        : "border-gray-200 hover:border-blue-300 hover:bg-gray-50"
                    }`}
                  >
                    <div className="flex justify-between items-start">
                      <div>
                        <div className="flex items-center gap-2">
                          <h3 className="font-bold text-lg">{project.name}</h3>
                          {project.isPublic && <Badge variant="outline">Public</Badge>}
                        </div>
                        <p className="text-gray-600 text-sm mt-1">{project.description}</p>
                        <div className="flex items-center gap-4 mt-2 text-sm text-gray-500">
                          <div className="flex items-center gap-1">
                            <Calendar className="h-3 w-3" />
                            <span>{new Date(project.createdAt).toLocaleDateString()}</span>
                          </div>
                          {project.tags && project.tags.length > 0 && (
                            <div className="flex items-center gap-1">
                              <Tag className="h-3 w-3" />
                              <span>{project.tags.join(", ")}</span>
                            </div>
                          )}
                        </div>
                      </div>
                      <div className="flex gap-2">
                        <Button
                          variant="outline"
                          size="sm"
                          onClick={() => onLoad(project)}
                          className="text-blue-600 border-blue-200 hover:bg-blue-50"
                        >
                          Load
                        </Button>
                        <Button
                          variant="outline"
                          size="sm"
                          onClick={() => confirmDelete(project)}
                          className="text-red-600 border-red-200 hover:bg-red-50"
                        >
                          <Trash2 className="h-4 w-4" />
                        </Button>
                      </div>
                    </div>

                    <div className="mt-3 grid grid-cols-3 gap-2 text-xs">
                      <div className="p-2 bg-gray-100 rounded">
                        <span className="font-medium">Battery:</span> {project.config.batteryCapacity} kWh
                      </div>
                      <div className="p-2 bg-gray-100 rounded">
                        <span className="font-medium">Solar:</span>{" "}
                        {project.config.solarEnabled ? "Enabled" : "Disabled"}
                      </div>
                      <div className="p-2 bg-gray-100 rounded">
                        <span className="font-medium">Weather:</span>{" "}
                        {project.config.useRealWeather ? "Real" : "Default"}
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            )}
          </CardContent>
        </Card>
      </div>

      {/* Save Dialog */}
      <Dialog open={showSaveDialog} onOpenChange={setShowSaveDialog}>
        <DialogContent className="sm:max-w-md">
          <DialogHeader>
            <DialogTitle>Save Project</DialogTitle>
          </DialogHeader>
          <div className="space-y-4 py-4">
            <div className="space-y-2">
              <Label htmlFor="project-name">Project Name</Label>
              <Input
                id="project-name"
                placeholder="My Simulation Project"
                value={projectName}
                onChange={(e) => setProjectName(e.target.value)}
              />
            </div>
            <div className="space-y-2">
              <Label htmlFor="project-description">Description (Optional)</Label>
              <Textarea
                id="project-description"
                placeholder="Brief description of this simulation setup"
                value={projectDescription}
                onChange={(e) => setProjectDescription(e.target.value)}
              />
            </div>
          </div>
          <DialogFooter>
            <Button variant="outline" onClick={() => setShowSaveDialog(false)}>
              Cancel
            </Button>
            <Button onClick={handleSave} disabled={!projectName.trim()}>
              Save Project
            </Button>
          </DialogFooter>
        </DialogContent>
      </Dialog>

      {/* Delete Confirmation Dialog */}
      <Dialog open={showDeleteDialog} onOpenChange={setShowDeleteDialog}>
        <DialogContent className="sm:max-w-md">
          <DialogHeader>
            <DialogTitle>Delete Project</DialogTitle>
          </DialogHeader>
          <div className="py-4">
            <p>Are you sure you want to delete "{projectToDelete?.name}"? This action cannot be undone.</p>
          </div>
          <DialogFooter>
            <Button variant="outline" onClick={() => setShowDeleteDialog(false)}>
              Cancel
            </Button>
            <Button variant="destructive" onClick={handleDelete}>
              Delete
            </Button>
          </DialogFooter>
        </DialogContent>
      </Dialog>
    </div>
  )
}


--------------------------------------------------------------------------------
FILE: components/simulation/pro/weather-widget.tsx
--------------------------------------------------------------------------------
"use client"

import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { Switch } from "@/components/ui/switch"
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select"
import type { SimulationConfig } from "@/lib/simulation/engine"
import { Cloud, Sun, Thermometer, MapPin } from "lucide-react"

interface WeatherWidgetProps {
  config: SimulationConfig
  onChange: (config: SimulationConfig) => void
  weatherData?: {
    temperature: number[]
    irradiance: number[]
    cloudCover: number[]
  }
}

export function WeatherWidget({ config, onChange, weatherData }: WeatherWidgetProps) {
  const updateConfig = (updates: Partial<SimulationConfig>) => {
    onChange({ ...config, ...updates })
  }

  const popularLocations = [
    { name: "Chicago, IL", lat: 41.8781, lng: -87.6298 },
    { name: "Los Angeles, CA", lat: 34.0522, lng: -118.2437 },
    { name: "New York, NY", lat: 40.7128, lng: -74.006 },
    { name: "Miami, FL", lat: 25.7617, lng: -80.1918 },
    { name: "Seattle, WA", lat: 47.6062, lng: -122.3321 },
    { name: "Phoenix, AZ", lat: 33.4484, lng: -112.074 },
  ]

  const handleLocationSelect = (locationName: string) => {
    const location = popularLocations.find((loc) => loc.name === locationName)
    if (location) {
      updateConfig({
        weatherLocation: location.name,
        location: { lat: location.lat, lng: location.lng },
      })
    }
  }

  return (
    <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
      <Card className="card-enhanced">
        <CardHeader>
          <CardTitle className="flex items-center gap-3">
            <MapPin className="h-5 w-5 text-blue-600" />
            Location Settings
          </CardTitle>
        </CardHeader>
        <CardContent className="space-y-6">
          <div>
            <Label className="font-semibold">Weather Location</Label>
            <div className="flex gap-2 mt-2">
              <Input
                placeholder="e.g., Chicago, IL"
                value={config.weatherLocation || ""}
                onChange={(e) => updateConfig({ weatherLocation: e.target.value })}
              />
              <Button variant="outline">Search</Button>
            </div>
          </div>

          <div>
            <Label className="font-semibold">Popular Locations</Label>
            <Select onValueChange={handleLocationSelect}>
              <SelectTrigger className="mt-2">
                <SelectValue placeholder="Select a location" />
              </SelectTrigger>
              <SelectContent>
                {popularLocations.map((location) => (
                  <SelectItem key={location.name} value={location.name}>
                    {location.name}
                  </SelectItem>
                ))}
              </SelectContent>
            </Select>
          </div>

          <div className="flex items-center justify-between p-4 bg-gradient-to-r from-blue-50 to-purple-50 rounded-xl border-2 border-blue-200">
            <Label htmlFor="weather-toggle" className="flex items-center gap-2 cursor-pointer">
              <Cloud className="h-4 w-4 text-blue-600" />
              <span className="font-semibold text-blue-800">Use Real Weather Data</span>
            </Label>
            <Switch
              id="weather-toggle"
              checked={config.useRealWeather || false}
              onCheckedChange={(checked) => updateConfig({ useRealWeather: checked })}
              className="data-[state=checked]:bg-blue-600"
            />
          </div>

          {config.location && (
            <div className="p-4 bg-gray-50 rounded-lg">
              <p className="text-sm font-medium">Selected Location:</p>
              <p className="text-sm text-gray-600">
                {config.weatherLocation} (Lat: {config.location.lat.toFixed(4)}, Lng: {config.location.lng.toFixed(4)})
              </p>
            </div>
          )}
        </CardContent>
      </Card>

      <Card className="card-enhanced">
        <CardHeader>
          <CardTitle className="flex items-center gap-3">
            <Cloud className="h-5 w-5 text-blue-600" />
            Weather Conditions
          </CardTitle>
        </CardHeader>
        <CardContent className="space-y-6">
          {weatherData ? (
            <div className="space-y-6">
              <div className="grid grid-cols-3 gap-4">
                <div className="text-center p-4 bg-blue-50 rounded-lg">
                  <Thermometer className="h-8 w-8 mx-auto mb-2 text-red-500" />
                  <p className="text-sm font-medium">Avg. Temperature</p>
                  <p className="text-xl font-bold">
                    {(weatherData.temperature.reduce((a, b) => a + b, 0) / weatherData.temperature.length).toFixed(1)}°C
                  </p>
                </div>

                <div className="text-center p-4 bg-yellow-50 rounded-lg">
                  <Sun className="h-8 w-8 mx-auto mb-2 text-yellow-500" />
                  <p className="text-sm font-medium">Peak Irradiance</p>
                  <p className="text-xl font-bold">{Math.max(...weatherData.irradiance).toFixed(0)} W/m²</p>
                </div>

                <div className="text-center p-4 bg-gray-50 rounded-lg">
                  <Cloud className="h-8 w-8 mx-auto mb-2 text-gray-500" />
                  <p className="text-sm font-medium">Avg. Cloud Cover</p>
                  <p className="text-xl font-bold">
                    {(weatherData.cloudCover.reduce((a, b) => a + b, 0) / weatherData.cloudCover.length).toFixed(0)}%
                  </p>
                </div>
              </div>

              <div>
                <Label className="font-semibold">Daily Temperature Profile</Label>
                <div className="h-24 mt-2 flex items-end">
                  {weatherData.temperature.map((temp, i) => (
                    <div
                      key={i}
                      className="flex-1 bg-gradient-to-t from-blue-500 to-red-500 rounded-t"
                      style={{
                        height: `${((temp - 10) / 30) * 100}%`,
                        minHeight: "10%",
                        maxHeight: "100%",
                      }}
                      title={`Hour ${i}: ${temp.toFixed(1)}°C`}
                    ></div>
                  ))}
                </div>
                <div className="flex justify-between text-xs text-gray-500 mt-1">
                  <span>12 AM</span>
                  <span>6 AM</span>
                  <span>12 PM</span>
                  <span>6 PM</span>
                  <span>12 AM</span>
                </div>
              </div>

              <div>
                <Label className="font-semibold">Solar Irradiance</Label>
                <div className="h-24 mt-2 flex items-end">
                  {weatherData.irradiance.map((irr, i) => (
                    <div
                      key={i}
                      className="flex-1 bg-gradient-to-t from-yellow-200 to-yellow-500 rounded-t"
                      style={{
                        height: `${(irr / 1000) * 100}%`,
                        minHeight: "0%",
                      }}
                      title={`Hour ${i}: ${irr.toFixed(0)} W/m²`}
                    ></div>
                  ))}
                </div>
                <div className="flex justify-between text-xs text-gray-500 mt-1">
                  <span>12 AM</span>
                  <span>6 AM</span>
                  <span>12 PM</span>
                  <span>6 PM</span>
                  <span>12 AM</span>
                </div>
              </div>
            </div>
          ) : (
            <div className="text-center py-12">
              <Cloud className="h-16 w-16 mx-auto mb-4 text-gray-300" />
              <p className="text-gray-500">
                {config.useRealWeather
                  ? "Run the simulation to fetch weather data"
                  : "Enable real weather data to see conditions"}
              </p>
            </div>
          )}
        </CardContent>
      </Card>
    </div>
  )
}


--------------------------------------------------------------------------------
FILE: components/simulation/simulation-nav.tsx
--------------------------------------------------------------------------------
"use client"

import Link from "next/link"
import { Badge } from "@/components/ui/badge"
import { Card } from "@/components/ui/card"
import { Zap, Crown, Code, Building, Star, Globe } from "lucide-react"

interface SimulationNavProps {
  userTier: string
}

export function SimulationNav({ userTier }: SimulationNavProps) {
  // Function to check if a user has access to a specific tier
  const hasAccess = (requiredTier: string): boolean => {
    // Admin always has access to everything (treat as having bought all 4 simulations)
    if (userTier === "admin") return true

    // Tier hierarchy - each tier includes access to all lower tiers
    const tierHierarchy: { [key: string]: string[] } = {
      free: ["free"],
      pro: ["free", "pro"],
      starter: ["free", "pro", "starter"],
      growth: ["free", "pro", "starter", "growth"],
      enterprise: ["free", "pro", "starter", "growth", "enterprise"],
    }

    const userAccess = tierHierarchy[userTier] || ["free"]
    return userAccess.includes(requiredTier)
  }

  const simulations = [
    {
      id: "free",
      name: "Free Simulation",
      description: "Basic energy modeling",
      icon: <Zap className="h-5 w-5" />,
      href: "/simulation",
      badge: "Free",
      badgeColor: "gradient-success",
      requiredTier: "free",
      features: ["24h simulation", "Basic profiles", "2 battery types"],
    },
    {
      id: "pro",
      name: "Pro Simulation",
      description: "Advanced features & analytics",
      icon: <Star className="h-5 w-5" />,
      href: "/simulation/pro",
      badge: "Pro",
      badgeColor: "gradient-secondary",
      requiredTier: "pro",
      features: ["Multi-duration", "Weather data", "4 battery types", "Cost analysis"],
    },
    {
      id: "starter",
      name: "Starter API",
      description: "Basic API automation",
      icon: <Code className="h-5 w-5" />,
      href: "/simulation/starter",
      badge: "API",
      badgeColor: "gradient-primary",
      requiredTier: "starter",
      features: ["5K calls/month", "6 examples", "Basic automation", "Up to 100kWh"],
    },
    {
      id: "growth",
      name: "Growth API",
      description: "Advanced API features",
      icon: <Building className="h-5 w-5" />,
      href: "/simulation/growth",
      badge: "Growth",
      badgeColor: "gradient-warning",
      requiredTier: "growth",
      features: ["50K calls/month", "10 examples", "Multi-site", "Peak shaving"],
    },
    {
      id: "enterprise",
      name: "Enterprise Suite",
      description: "Industrial-scale modeling",
      icon: <Crown className="h-5 w-5" />,
      href: "/simulation/enterprise",
      badge: "Enterprise",
      badgeColor: "gradient-accent",
      requiredTier: "enterprise",
      features: ["Unlimited calls", "AI optimization", "Multi-MW", "5-year sims"],
    },
  ]

  return (
    <div className="w-full">
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-6 lg:gap-8">
        {simulations.map((sim) => {
          const available = hasAccess(sim.requiredTier)

          return (
            <Card
              key={sim.id}
              className={`relative overflow-hidden transition-all duration-300 rounded-xl border-0 shadow-lg ${
                available
                  ? "bg-white hover:shadow-xl hover:scale-105 cursor-pointer"
                  : "bg-gray-50/80 opacity-60 cursor-not-allowed"
              }`}
            >
              <Link href={available ? sim.href : "/pricing"} className="block p-6 lg:p-8 h-full">
                {/* Header */}
                <div className="flex items-center justify-between mb-6">
                  <div className={`p-3 lg:p-4 rounded-xl ${available ? "bg-gray-100" : "bg-gray-200"}`}>
                    <div className={available ? "text-gray-700" : "text-gray-400"}>{sim.icon}</div>
                  </div>
                  <Badge
                    className={`${sim.badgeColor} text-white text-xs font-semibold px-3 py-1 rounded-xl shadow-sm`}
                  >
                    {sim.badge}
                  </Badge>
                </div>

                {/* Content */}
                <div className="space-y-4">
                  <h3 className={`font-bold text-lg leading-tight ${available ? "text-gray-900" : "text-gray-500"}`}>
                    {sim.name}
                  </h3>
                  <p className={`text-sm leading-relaxed ${available ? "text-gray-600" : "text-gray-400"}`}>
                    {sim.description}
                  </p>

                  {/* Features */}
                  <div className="space-y-3 pt-2">
                    {sim.features.slice(0, 2).map((feature, index) => (
                      <div key={index} className="flex items-center gap-3">
                        <div className={`w-2 h-2 rounded-full ${available ? "bg-green-500" : "bg-gray-400"}`} />
                        <span className={`text-xs ${available ? "text-gray-600" : "text-gray-400"}`}>{feature}</span>
                      </div>
                    ))}
                    {sim.features.length > 2 && (
                      <div className="flex items-center gap-3">
                        <div className={`w-2 h-2 rounded-full ${available ? "bg-green-500" : "bg-gray-400"}`} />
                        <span className={`text-xs ${available ? "text-gray-600" : "text-gray-400"}`}>
                          +{sim.features.length - 2} more
                        </span>
                      </div>
                    )}
                  </div>
                </div>

                {/* Upgrade indicator for locked features */}
                {!available && (
                  <div className="absolute inset-0 bg-gradient-to-t from-gray-900/20 to-transparent flex items-end justify-center pb-6 rounded-xl">
                    <Badge className="bg-white/90 text-gray-700 text-xs font-medium rounded-lg flex items-center px-3 py-1">
                      Upgrade Required
                    </Badge>
                  </div>
                )}
              </Link>
            </Card>
          )
        })}
      </div>

      {/* Current Tier Indicator */}
      <div className="mt-12 text-center">
        <Card className="inline-flex items-center gap-4 px-8 py-4 gradient-primary text-white rounded-xl shadow-lg">
          <Globe className="h-6 w-6" />
          <span className="font-medium text-lg">
            Current Plan:{" "}
            <span className="font-bold capitalize">
              {userTier === "admin" ? "Enterprise (Admin Access)" : userTier}
            </span>
          </span>
        </Card>
      </div>
    </div>
  )
}


--------------------------------------------------------------------------------
FILE: components/site-header.tsx
--------------------------------------------------------------------------------
"use client"

import Link from "next/link"
import { useState, useEffect } from "react"
import { Button } from "@/components/ui/button"
import { Sheet, SheetContent, SheetTrigger } from "@/components/ui/sheet"
import { Menu, Zap, X, LogOut, User } from "lucide-react"
import { useAuth } from "@/lib/auth-context"
import { LoginDialog } from "@/components/auth/login-dialog"

export function SiteHeader() {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false)
  const [showLogin, setShowLogin] = useState(false)
  const [isScrolled, setIsScrolled] = useState(false)
  const { user, loading, logout } = useAuth()

  useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 10)
    }
    window.addEventListener("scroll", handleScroll)
    return () => window.removeEventListener("scroll", handleScroll)
  }, [])

  const navigation = user
    ? [
        { name: "Home", href: "/" },
        { name: "Simulations", href: "/simulations" },
        { name: "About", href: "/about" },
        { name: "Contact", href: "/contact" },
      ]
    : [
        { name: "Home", href: "/" },
        { name: "Simulations", href: "/simulations" },
        { name: "Pricing", href: "/pricing" },
        { name: "About", href: "/about" },
        { name: "Contact", href: "/contact" },
      ]

  const handleLogout = () => {
    logout()
  }

  return (
    <>
      <header
        className={`sticky top-0 z-50 w-full transition-smooth ${
          isScrolled
            ? "bg-white/95 backdrop-blur-xl border-b border-gray-200/50 shadow-lg"
            : "bg-white/90 backdrop-blur-lg border-b border-gray-200/30"
        }`}
      >
        <div className="container-clean">
          <div className="flex h-20 items-center justify-between">
            {/* Logo */}
            <Link href="/" className="flex items-center space-x-4 hover-lift">
              <div className="flex h-12 w-12 items-center justify-center rounded-2xl bg-gradient-to-r from-blue-600 to-purple-600 shadow-lg animate-float">
                <Zap className="h-6 w-6 text-white" />
              </div>
              <span className="text-2xl font-bold text-gradient">VoltSphere</span>
            </Link>

            {/* Desktop Navigation */}
            <nav className="hidden lg:flex items-center space-x-12">
              {navigation.map((item) => (
                <Link
                  key={item.name}
                  href={item.href}
                  className="text-gray-700 hover:text-blue-600 font-semibold text-lg transition-smooth relative group"
                >
                  {item.name}
                  <span className="absolute -bottom-1 left-0 w-0 h-0.5 bg-blue-600 transition-smooth group-hover:w-full rounded-full"></span>
                </Link>
              ))}
            </nav>

            {/* Desktop Auth */}
            <div className="hidden lg:flex items-center space-x-6">
              {loading ? (
                <div className="h-10 w-10 animate-spin rounded-full border-4 border-gray-300 border-t-blue-600" />
              ) : user ? (
                <div className="flex items-center space-x-4">
                  <div className="flex items-center space-x-3 px-4 py-3 bg-gradient-to-r from-blue-50 to-purple-50 rounded-2xl border border-blue-200/50">
                    <div className="w-10 h-10 bg-gradient-to-r from-blue-600 to-purple-600 rounded-xl flex items-center justify-center text-white font-bold shadow-lg">
                      {user.name?.charAt(0).toUpperCase()}
                    </div>
                    <div>
                      <div className="font-semibold text-gray-900">{user.name}</div>
                      <div className="text-sm text-blue-600">Premium User</div>
                    </div>
                  </div>
                  <Button asChild variant="outline" className="btn-outline">
                    <Link href="/profile">
                      <User className="h-4 w-4 mr-2" />
                      Profile
                    </Link>
                  </Button>
                  <Button
                    onClick={handleLogout}
                    variant="ghost"
                    className="btn-ghost text-red-600 hover:text-red-700 hover:bg-red-50"
                  >
                    <LogOut className="h-4 w-4" />
                  </Button>
                </div>
              ) : (
                <div className="flex items-center space-x-4">
                  <Button onClick={() => setShowLogin(true)} variant="ghost" className="btn-ghost text-lg">
                    Sign In
                  </Button>
                  <Button asChild className="btn-primary">
                    <Link href="/simulations">Get Started</Link>
                  </Button>
                </div>
              )}
            </div>

            {/* Mobile Menu Button */}
            <Sheet open={mobileMenuOpen} onOpenChange={setMobileMenuOpen}>
              <SheetTrigger asChild>
                <Button variant="ghost" size="sm" className="lg:hidden p-3 rounded-xl">
                  <Menu className="h-6 w-6" />
                </Button>
              </SheetTrigger>
              <SheetContent side="right" className="w-80 p-0 bg-white/95 backdrop-blur-xl">
                <div className="flex flex-col h-full">
                  {/* Mobile Header */}
                  <div className="flex items-center justify-between p-8 border-b border-gray-200/50">
                    <Link href="/" className="flex items-center space-x-3">
                      <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-gradient-to-r from-blue-600 to-purple-600">
                        <Zap className="h-5 w-5 text-white" />
                      </div>
                      <span className="text-xl font-bold text-gradient">VoltSphere</span>
                    </Link>
                    <Button
                      variant="ghost"
                      size="sm"
                      onClick={() => setMobileMenuOpen(false)}
                      className="p-2 rounded-xl"
                    >
                      <X className="h-5 w-5" />
                    </Button>
                  </div>

                  {/* Mobile Navigation */}
                  <nav className="flex-1 p-8">
                    <div className="space-y-4">
                      {navigation.map((item) => (
                        <Link
                          key={item.name}
                          href={item.href}
                          onClick={() => setMobileMenuOpen(false)}
                          className="block px-6 py-4 text-gray-700 hover:text-blue-600 hover:bg-blue-50 rounded-2xl transition-smooth font-semibold text-lg"
                        >
                          {item.name}
                        </Link>
                      ))}
                    </div>
                  </nav>

                  {/* Mobile Auth */}
                  <div className="p-8 border-t border-gray-200/50">
                    {loading ? (
                      <div className="h-12 bg-gray-100 rounded-2xl animate-pulse" />
                    ) : user ? (
                      <div className="space-y-4">
                        <div className="flex items-center space-x-3 p-4 bg-gradient-to-r from-blue-50 to-purple-50 rounded-2xl">
                          <div className="w-12 h-12 bg-gradient-to-r from-blue-600 to-purple-600 rounded-xl flex items-center justify-center text-white font-bold">
                            {user.name?.charAt(0).toUpperCase()}
                          </div>
                          <div>
                            <div className="font-semibold text-gray-900">{user.name}</div>
                            <div className="text-sm text-blue-600">Premium User</div>
                          </div>
                        </div>
                        <div className="space-y-3">
                          <Button asChild variant="outline" className="w-full btn-outline">
                            <Link href="/profile" onClick={() => setMobileMenuOpen(false)}>
                              <User className="h-4 w-4 mr-2" />
                              Profile
                            </Link>
                          </Button>
                          <Button
                            onClick={() => {
                              handleLogout()
                              setMobileMenuOpen(false)
                            }}
                            variant="ghost"
                            className="w-full btn-ghost text-red-600 hover:text-red-700 hover:bg-red-50"
                          >
                            <LogOut className="h-4 w-4 mr-2" />
                            Sign Out
                          </Button>
                        </div>
                      </div>
                    ) : (
                      <div className="space-y-4">
                        <Button
                          onClick={() => {
                            setShowLogin(true)
                            setMobileMenuOpen(false)
                          }}
                          variant="outline"
                          className="w-full btn-outline"
                        >
                          Sign In
                        </Button>
                        <Button asChild className="w-full btn-primary">
                          <Link href="/simulations" onClick={() => setMobileMenuOpen(false)}>
                            Get Started
                          </Link>
                        </Button>
                      </div>
                    )}
                  </div>
                </div>
              </SheetContent>
            </Sheet>
          </div>
        </div>
      </header>

      <LoginDialog open={showLogin} onOpenChange={setShowLogin} />
    </>
  )
}


--------------------------------------------------------------------------------
FILE: components/theme-provider.tsx
--------------------------------------------------------------------------------
'use client'

import * as React from 'react'
import {
  ThemeProvider as NextThemesProvider,
  type ThemeProviderProps,
} from 'next-themes'

export function ThemeProvider({ children, ...props }: ThemeProviderProps) {
  return <NextThemesProvider {...props}>{children}</NextThemesProvider>
}


--------------------------------------------------------------------------------
FILE: components/ui/accordion.tsx
--------------------------------------------------------------------------------
"use client"

import * as React from "react"
import * as AccordionPrimitive from "@radix-ui/react-accordion"
import { ChevronDown } from "lucide-react"

import { cn } from "@/lib/utils"

const Accordion = AccordionPrimitive.Root

const AccordionItem = React.forwardRef<
  React.ElementRef<typeof AccordionPrimitive.Item>,
  React.ComponentPropsWithoutRef<typeof AccordionPrimitive.Item>
>(({ className, ...props }, ref) => (
  <AccordionPrimitive.Item
    ref={ref}
    className={cn("border-b", className)}
    {...props}
  />
))
AccordionItem.displayName = "AccordionItem"

const AccordionTrigger = React.forwardRef<
  React.ElementRef<typeof AccordionPrimitive.Trigger>,
  React.ComponentPropsWithoutRef<typeof AccordionPrimitive.Trigger>
>(({ className, children, ...props }, ref) => (
  <AccordionPrimitive.Header className="flex">
    <AccordionPrimitive.Trigger
      ref={ref}
      className={cn(
        "flex flex-1 items-center justify-between py-4 font-medium transition-all hover:underline [&[data-state=open]>svg]:rotate-180",
        className
      )}
      {...props}
    >
      {children}
      <ChevronDown className="h-4 w-4 shrink-0 transition-transform duration-200" />
    </AccordionPrimitive.Trigger>
  </AccordionPrimitive.Header>
))
AccordionTrigger.displayName = AccordionPrimitive.Trigger.displayName

const AccordionContent = React.forwardRef<
  React.ElementRef<typeof AccordionPrimitive.Content>,
  React.ComponentPropsWithoutRef<typeof AccordionPrimitive.Content>
>(({ className, children, ...props }, ref) => (
  <AccordionPrimitive.Content
    ref={ref}
    className="overflow-hidden text-sm transition-all data-[state=closed]:animate-accordion-up data-[state=open]:animate-accordion-down"
    {...props}
  >
    <div className={cn("pb-4 pt-0", className)}>{children}</div>
  </AccordionPrimitive.Content>
))

AccordionContent.displayName = AccordionPrimitive.Content.displayName

export { Accordion, AccordionItem, AccordionTrigger, AccordionContent }


--------------------------------------------------------------------------------
FILE: components/ui/alert-dialog.tsx
--------------------------------------------------------------------------------
"use client"

import * as React from "react"
import * as AlertDialogPrimitive from "@radix-ui/react-alert-dialog"

import { cn } from "@/lib/utils"
import { buttonVariants } from "@/components/ui/button"

const AlertDialog = AlertDialogPrimitive.Root

const AlertDialogTrigger = AlertDialogPrimitive.Trigger

const AlertDialogPortal = AlertDialogPrimitive.Portal

const AlertDialogOverlay = React.forwardRef<
  React.ElementRef<typeof AlertDialogPrimitive.Overlay>,
  React.ComponentPropsWithoutRef<typeof AlertDialogPrimitive.Overlay>
>(({ className, ...props }, ref) => (
  <AlertDialogPrimitive.Overlay
    className={cn(
      "fixed inset-0 z-50 bg-black/80  data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0",
      className
    )}
    {...props}
    ref={ref}
  />
))
AlertDialogOverlay.displayName = AlertDialogPrimitive.Overlay.displayName

const AlertDialogContent = React.forwardRef<
  React.ElementRef<typeof AlertDialogPrimitive.Content>,
  React.ComponentPropsWithoutRef<typeof AlertDialogPrimitive.Content>
>(({ className, ...props }, ref) => (
  <AlertDialogPortal>
    <AlertDialogOverlay />
    <AlertDialogPrimitive.Content
      ref={ref}
      className={cn(
        "fixed left-[50%] top-[50%] z-50 grid w-full max-w-lg translate-x-[-50%] translate-y-[-50%] gap-4 border bg-background p-6 shadow-lg duration-200 data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[state=closed]:slide-out-to-left-1/2 data-[state=closed]:slide-out-to-top-[48%] data-[state=open]:slide-in-from-left-1/2 data-[state=open]:slide-in-from-top-[48%] sm:rounded-lg",
        className
      )}
      {...props}
    />
  </AlertDialogPortal>
))
AlertDialogContent.displayName = AlertDialogPrimitive.Content.displayName

const AlertDialogHeader = ({
  className,
  ...props
}: React.HTMLAttributes<HTMLDivElement>) => (
  <div
    className={cn(
      "flex flex-col space-y-2 text-center sm:text-left",
      className
    )}
    {...props}
  />
)
AlertDialogHeader.displayName = "AlertDialogHeader"

const AlertDialogFooter = ({
  className,
  ...props
}: React.HTMLAttributes<HTMLDivElement>) => (
  <div
    className={cn(
      "flex flex-col-reverse sm:flex-row sm:justify-end sm:space-x-2",
      className
    )}
    {...props}
  />
)
AlertDialogFooter.displayName = "AlertDialogFooter"

const AlertDialogTitle = React.forwardRef<
  React.ElementRef<typeof AlertDialogPrimitive.Title>,
  React.ComponentPropsWithoutRef<typeof AlertDialogPrimitive.Title>
>(({ className, ...props }, ref) => (
  <AlertDialogPrimitive.Title
    ref={ref}
    className={cn("text-lg font-semibold", className)}
    {...props}
  />
))
AlertDialogTitle.displayName = AlertDialogPrimitive.Title.displayName

const AlertDialogDescription = React.forwardRef<
  React.ElementRef<typeof AlertDialogPrimitive.Description>,
  React.ComponentPropsWithoutRef<typeof AlertDialogPrimitive.Description>
>(({ className, ...props }, ref) => (
  <AlertDialogPrimitive.Description
    ref={ref}
    className={cn("text-sm text-muted-foreground", className)}
    {...props}
  />
))
AlertDialogDescription.displayName =
  AlertDialogPrimitive.Description.displayName

const AlertDialogAction = React.forwardRef<
  React.ElementRef<typeof AlertDialogPrimitive.Action>,
  React.ComponentPropsWithoutRef<typeof AlertDialogPrimitive.Action>
>(({ className, ...props }, ref) => (
  <AlertDialogPrimitive.Action
    ref={ref}
    className={cn(buttonVariants(), className)}
    {...props}
  />
))
AlertDialogAction.displayName = AlertDialogPrimitive.Action.displayName

const AlertDialogCancel = React.forwardRef<
  React.ElementRef<typeof AlertDialogPrimitive.Cancel>,
  React.ComponentPropsWithoutRef<typeof AlertDialogPrimitive.Cancel>
>(({ className, ...props }, ref) => (
  <AlertDialogPrimitive.Cancel
    ref={ref}
    className={cn(
      buttonVariants({ variant: "outline" }),
      "mt-2 sm:mt-0",
      className
    )}
    {...props}
  />
))
AlertDialogCancel.displayName = AlertDialogPrimitive.Cancel.displayName

export {
  AlertDialog,
  AlertDialogPortal,
  AlertDialogOverlay,
  AlertDialogTrigger,
  AlertDialogContent,
  AlertDialogHeader,
  AlertDialogFooter,
  AlertDialogTitle,
  AlertDialogDescription,
  AlertDialogAction,
  AlertDialogCancel,
}


--------------------------------------------------------------------------------
FILE: components/ui/alert.tsx
--------------------------------------------------------------------------------
import * as React from "react"
import { cva, type VariantProps } from "class-variance-authority"

import { cn } from "@/lib/utils"

const alertVariants = cva(
  "relative w-full rounded-lg border p-4 [&>svg~*]:pl-7 [&>svg+div]:translate-y-[-3px] [&>svg]:absolute [&>svg]:left-4 [&>svg]:top-4 [&>svg]:text-foreground",
  {
    variants: {
      variant: {
        default: "bg-background text-foreground",
        destructive:
          "border-destructive/50 text-destructive dark:border-destructive [&>svg]:text-destructive",
      },
    },
    defaultVariants: {
      variant: "default",
    },
  }
)

const Alert = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement> & VariantProps<typeof alertVariants>
>(({ className, variant, ...props }, ref) => (
  <div
    ref={ref}
    role="alert"
    className={cn(alertVariants({ variant }), className)}
    {...props}
  />
))
Alert.displayName = "Alert"

const AlertTitle = React.forwardRef<
  HTMLParagraphElement,
  React.HTMLAttributes<HTMLHeadingElement>
>(({ className, ...props }, ref) => (
  <h5
    ref={ref}
    className={cn("mb-1 font-medium leading-none tracking-tight", className)}
    {...props}
  />
))
AlertTitle.displayName = "AlertTitle"

const AlertDescription = React.forwardRef<
  HTMLParagraphElement,
  React.HTMLAttributes<HTMLParagraphElement>
>(({ className, ...props }, ref) => (
  <div
    ref={ref}
    className={cn("text-sm [&_p]:leading-relaxed", className)}
    {...props}
  />
))
AlertDescription.displayName = "AlertDescription"

export { Alert, AlertTitle, AlertDescription }


--------------------------------------------------------------------------------
FILE: components/ui/aspect-ratio.tsx
--------------------------------------------------------------------------------
"use client"

import * as AspectRatioPrimitive from "@radix-ui/react-aspect-ratio"

const AspectRatio = AspectRatioPrimitive.Root

export { AspectRatio }


--------------------------------------------------------------------------------
FILE: components/ui/avatar.tsx
--------------------------------------------------------------------------------
"use client"

import * as React from "react"
import * as AvatarPrimitive from "@radix-ui/react-avatar"

import { cn } from "@/lib/utils"

const Avatar = React.forwardRef<
  React.ElementRef<typeof AvatarPrimitive.Root>,
  React.ComponentPropsWithoutRef<typeof AvatarPrimitive.Root>
>(({ className, ...props }, ref) => (
  <AvatarPrimitive.Root
    ref={ref}
    className={cn(
      "relative flex h-10 w-10 shrink-0 overflow-hidden rounded-full",
      className
    )}
    {...props}
  />
))
Avatar.displayName = AvatarPrimitive.Root.displayName

const AvatarImage = React.forwardRef<
  React.ElementRef<typeof AvatarPrimitive.Image>,
  React.ComponentPropsWithoutRef<typeof AvatarPrimitive.Image>
>(({ className, ...props }, ref) => (
  <AvatarPrimitive.Image
    ref={ref}
    className={cn("aspect-square h-full w-full", className)}
    {...props}
  />
))
AvatarImage.displayName = AvatarPrimitive.Image.displayName

const AvatarFallback = React.forwardRef<
  React.ElementRef<typeof AvatarPrimitive.Fallback>,
  React.ComponentPropsWithoutRef<typeof AvatarPrimitive.Fallback>
>(({ className, ...props }, ref) => (
  <AvatarPrimitive.Fallback
    ref={ref}
    className={cn(
      "flex h-full w-full items-center justify-center rounded-full bg-muted",
      className
    )}
    {...props}
  />
))
AvatarFallback.displayName = AvatarPrimitive.Fallback.displayName

export { Avatar, AvatarImage, AvatarFallback }


--------------------------------------------------------------------------------
FILE: components/ui/badge.tsx
--------------------------------------------------------------------------------
import * as React from "react"
import { cva, type VariantProps } from "class-variance-authority"

import { cn } from "@/lib/utils"

const badgeVariants = cva(
  "inline-flex items-center rounded-full border px-2.5 py-0.5 text-xs font-semibold transition-colors focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2",
  {
    variants: {
      variant: {
        default:
          "border-transparent bg-primary text-primary-foreground hover:bg-primary/80",
        secondary:
          "border-transparent bg-secondary text-secondary-foreground hover:bg-secondary/80",
        destructive:
          "border-transparent bg-destructive text-destructive-foreground hover:bg-destructive/80",
        outline: "text-foreground",
      },
    },
    defaultVariants: {
      variant: "default",
    },
  }
)

export interface BadgeProps
  extends React.HTMLAttributes<HTMLDivElement>,
    VariantProps<typeof badgeVariants> {}

function Badge({ className, variant, ...props }: BadgeProps) {
  return (
    <div className={cn(badgeVariants({ variant }), className)} {...props} />
  )
}

export { Badge, badgeVariants }


--------------------------------------------------------------------------------
FILE: components/ui/breadcrumb.tsx
--------------------------------------------------------------------------------
import * as React from "react"
import { Slot } from "@radix-ui/react-slot"
import { ChevronRight, MoreHorizontal } from "lucide-react"

import { cn } from "@/lib/utils"

const Breadcrumb = React.forwardRef<
  HTMLElement,
  React.ComponentPropsWithoutRef<"nav"> & {
    separator?: React.ReactNode
  }
>(({ ...props }, ref) => <nav ref={ref} aria-label="breadcrumb" {...props} />)
Breadcrumb.displayName = "Breadcrumb"

const BreadcrumbList = React.forwardRef<
  HTMLOListElement,
  React.ComponentPropsWithoutRef<"ol">
>(({ className, ...props }, ref) => (
  <ol
    ref={ref}
    className={cn(
      "flex flex-wrap items-center gap-1.5 break-words text-sm text-muted-foreground sm:gap-2.5",
      className
    )}
    {...props}
  />
))
BreadcrumbList.displayName = "BreadcrumbList"

const BreadcrumbItem = React.forwardRef<
  HTMLLIElement,
  React.ComponentPropsWithoutRef<"li">
>(({ className, ...props }, ref) => (
  <li
    ref={ref}
    className={cn("inline-flex items-center gap-1.5", className)}
    {...props}
  />
))
BreadcrumbItem.displayName = "BreadcrumbItem"

const BreadcrumbLink = React.forwardRef<
  HTMLAnchorElement,
  React.ComponentPropsWithoutRef<"a"> & {
    asChild?: boolean
  }
>(({ asChild, className, ...props }, ref) => {
  const Comp = asChild ? Slot : "a"

  return (
    <Comp
      ref={ref}
      className={cn("transition-colors hover:text-foreground", className)}
      {...props}
    />
  )
})
BreadcrumbLink.displayName = "BreadcrumbLink"

const BreadcrumbPage = React.forwardRef<
  HTMLSpanElement,
  React.ComponentPropsWithoutRef<"span">
>(({ className, ...props }, ref) => (
  <span
    ref={ref}
    role="link"
    aria-disabled="true"
    aria-current="page"
    className={cn("font-normal text-foreground", className)}
    {...props}
  />
))
BreadcrumbPage.displayName = "BreadcrumbPage"

const BreadcrumbSeparator = ({
  children,
  className,
  ...props
}: React.ComponentProps<"li">) => (
  <li
    role="presentation"
    aria-hidden="true"
    className={cn("[&>svg]:w-3.5 [&>svg]:h-3.5", className)}
    {...props}
  >
    {children ?? <ChevronRight />}
  </li>
)
BreadcrumbSeparator.displayName = "BreadcrumbSeparator"

const BreadcrumbEllipsis = ({
  className,
  ...props
}: React.ComponentProps<"span">) => (
  <span
    role="presentation"
    aria-hidden="true"
    className={cn("flex h-9 w-9 items-center justify-center", className)}
    {...props}
  >
    <MoreHorizontal className="h-4 w-4" />
    <span className="sr-only">More</span>
  </span>
)
BreadcrumbEllipsis.displayName = "BreadcrumbElipssis"

export {
  Breadcrumb,
  BreadcrumbList,
  BreadcrumbItem,
  BreadcrumbLink,
  BreadcrumbPage,
  BreadcrumbSeparator,
  BreadcrumbEllipsis,
}


--------------------------------------------------------------------------------
FILE: components/ui/button.tsx
--------------------------------------------------------------------------------
import * as React from "react"
import { Slot } from "@radix-ui/react-slot"
import { cva, type VariantProps } from "class-variance-authority"

import { cn } from "@/lib/utils"

const buttonVariants = cva(
  "inline-flex items-center justify-center gap-2 whitespace-nowrap rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 [&_svg]:pointer-events-none [&_svg]:size-4 [&_svg]:shrink-0",
  {
    variants: {
      variant: {
        default: "bg-primary text-primary-foreground hover:bg-primary/90",
        destructive:
          "bg-destructive text-destructive-foreground hover:bg-destructive/90",
        outline:
          "border border-input bg-background hover:bg-accent hover:text-accent-foreground",
        secondary:
          "bg-secondary text-secondary-foreground hover:bg-secondary/80",
        ghost: "hover:bg-accent hover:text-accent-foreground",
        link: "text-primary underline-offset-4 hover:underline",
      },
      size: {
        default: "h-10 px-4 py-2",
        sm: "h-9 rounded-md px-3",
        lg: "h-11 rounded-md px-8",
        icon: "h-10 w-10",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
    },
  }
)

export interface ButtonProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement>,
    VariantProps<typeof buttonVariants> {
  asChild?: boolean
}

const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
  ({ className, variant, size, asChild = false, ...props }, ref) => {
    const Comp = asChild ? Slot : "button"
    return (
      <Comp
        className={cn(buttonVariants({ variant, size, className }))}
        ref={ref}
        {...props}
      />
    )
  }
)
Button.displayName = "Button"

export { Button, buttonVariants }


--------------------------------------------------------------------------------
FILE: components/ui/calendar.tsx
--------------------------------------------------------------------------------
"use client"

import * as React from "react"
import { ChevronLeft, ChevronRight } from "lucide-react"
import { DayPicker } from "react-day-picker"

import { cn } from "@/lib/utils"
import { buttonVariants } from "@/components/ui/button"

export type CalendarProps = React.ComponentProps<typeof DayPicker>

function Calendar({
  className,
  classNames,
  showOutsideDays = true,
  ...props
}: CalendarProps) {
  return (
    <DayPicker
      showOutsideDays={showOutsideDays}
      className={cn("p-3", className)}
      classNames={{
        months: "flex flex-col sm:flex-row space-y-4 sm:space-x-4 sm:space-y-0",
        month: "space-y-4",
        caption: "flex justify-center pt-1 relative items-center",
        caption_label: "text-sm font-medium",
        nav: "space-x-1 flex items-center",
        nav_button: cn(
          buttonVariants({ variant: "outline" }),
          "h-7 w-7 bg-transparent p-0 opacity-50 hover:opacity-100"
        ),
        nav_button_previous: "absolute left-1",
        nav_button_next: "absolute right-1",
        table: "w-full border-collapse space-y-1",
        head_row: "flex",
        head_cell:
          "text-muted-foreground rounded-md w-9 font-normal text-[0.8rem]",
        row: "flex w-full mt-2",
        cell: "h-9 w-9 text-center text-sm p-0 relative [&:has([aria-selected].day-range-end)]:rounded-r-md [&:has([aria-selected].day-outside)]:bg-accent/50 [&:has([aria-selected])]:bg-accent first:[&:has([aria-selected])]:rounded-l-md last:[&:has([aria-selected])]:rounded-r-md focus-within:relative focus-within:z-20",
        day: cn(
          buttonVariants({ variant: "ghost" }),
          "h-9 w-9 p-0 font-normal aria-selected:opacity-100"
        ),
        day_range_end: "day-range-end",
        day_selected:
          "bg-primary text-primary-foreground hover:bg-primary hover:text-primary-foreground focus:bg-primary focus:text-primary-foreground",
        day_today: "bg-accent text-accent-foreground",
        day_outside:
          "day-outside text-muted-foreground aria-selected:bg-accent/50 aria-selected:text-muted-foreground",
        day_disabled: "text-muted-foreground opacity-50",
        day_range_middle:
          "aria-selected:bg-accent aria-selected:text-accent-foreground",
        day_hidden: "invisible",
        ...classNames,
      }}
      components={{
        IconLeft: ({ ...props }) => <ChevronLeft className="h-4 w-4" />,
        IconRight: ({ ...props }) => <ChevronRight className="h-4 w-4" />,
      }}
      {...props}
    />
  )
}
Calendar.displayName = "Calendar"

export { Calendar }


--------------------------------------------------------------------------------
FILE: components/ui/card.tsx
--------------------------------------------------------------------------------
import * as React from "react"

import { cn } from "@/lib/utils"

const Card = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement>
>(({ className, ...props }, ref) => (
  <div
    ref={ref}
    className={cn(
      "rounded-lg border bg-card text-card-foreground shadow-sm",
      className
    )}
    {...props}
  />
))
Card.displayName = "Card"

const CardHeader = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement>
>(({ className, ...props }, ref) => (
  <div
    ref={ref}
    className={cn("flex flex-col space-y-1.5 p-6", className)}
    {...props}
  />
))
CardHeader.displayName = "CardHeader"

const CardTitle = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement>
>(({ className, ...props }, ref) => (
  <div
    ref={ref}
    className={cn(
      "text-2xl font-semibold leading-none tracking-tight",
      className
    )}
    {...props}
  />
))
CardTitle.displayName = "CardTitle"

const CardDescription = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement>
>(({ className, ...props }, ref) => (
  <div
    ref={ref}
    className={cn("text-sm text-muted-foreground", className)}
    {...props}
  />
))
CardDescription.displayName = "CardDescription"

const CardContent = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement>
>(({ className, ...props }, ref) => (
  <div ref={ref} className={cn("p-6 pt-0", className)} {...props} />
))
CardContent.displayName = "CardContent"

const CardFooter = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement>
>(({ className, ...props }, ref) => (
  <div
    ref={ref}
    className={cn("flex items-center p-6 pt-0", className)}
    {...props}
  />
))
CardFooter.displayName = "CardFooter"

export { Card, CardHeader, CardFooter, CardTitle, CardDescription, CardContent }


--------------------------------------------------------------------------------
FILE: components/ui/carousel.tsx
--------------------------------------------------------------------------------
"use client"

import * as React from "react"
import useEmblaCarousel, {
  type UseEmblaCarouselType,
} from "embla-carousel-react"
import { ArrowLeft, ArrowRight } from "lucide-react"

import { cn } from "@/lib/utils"
import { Button } from "@/components/ui/button"

type CarouselApi = UseEmblaCarouselType[1]
type UseCarouselParameters = Parameters<typeof useEmblaCarousel>
type CarouselOptions = UseCarouselParameters[0]
type CarouselPlugin = UseCarouselParameters[1]

type CarouselProps = {
  opts?: CarouselOptions
  plugins?: CarouselPlugin
  orientation?: "horizontal" | "vertical"
  setApi?: (api: CarouselApi) => void
}

type CarouselContextProps = {
  carouselRef: ReturnType<typeof useEmblaCarousel>[0]
  api: ReturnType<typeof useEmblaCarousel>[1]
  scrollPrev: () => void
  scrollNext: () => void
  canScrollPrev: boolean
  canScrollNext: boolean
} & CarouselProps

const CarouselContext = React.createContext<CarouselContextProps | null>(null)

function useCarousel() {
  const context = React.useContext(CarouselContext)

  if (!context) {
    throw new Error("useCarousel must be used within a <Carousel />")
  }

  return context
}

const Carousel = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement> & CarouselProps
>(
  (
    {
      orientation = "horizontal",
      opts,
      setApi,
      plugins,
      className,
      children,
      ...props
    },
    ref
  ) => {
    const [carouselRef, api] = useEmblaCarousel(
      {
        ...opts,
        axis: orientation === "horizontal" ? "x" : "y",
      },
      plugins
    )
    const [canScrollPrev, setCanScrollPrev] = React.useState(false)
    const [canScrollNext, setCanScrollNext] = React.useState(false)

    const onSelect = React.useCallback((api: CarouselApi) => {
      if (!api) {
        return
      }

      setCanScrollPrev(api.canScrollPrev())
      setCanScrollNext(api.canScrollNext())
    }, [])

    const scrollPrev = React.useCallback(() => {
      api?.scrollPrev()
    }, [api])

    const scrollNext = React.useCallback(() => {
      api?.scrollNext()
    }, [api])

    const handleKeyDown = React.useCallback(
      (event: React.KeyboardEvent<HTMLDivElement>) => {
        if (event.key === "ArrowLeft") {
          event.preventDefault()
          scrollPrev()
        } else if (event.key === "ArrowRight") {
          event.preventDefault()
          scrollNext()
        }
      },
      [scrollPrev, scrollNext]
    )

    React.useEffect(() => {
      if (!api || !setApi) {
        return
      }

      setApi(api)
    }, [api, setApi])

    React.useEffect(() => {
      if (!api) {
        return
      }

      onSelect(api)
      api.on("reInit", onSelect)
      api.on("select", onSelect)

      return () => {
        api?.off("select", onSelect)
      }
    }, [api, onSelect])

    return (
      <CarouselContext.Provider
        value={{
          carouselRef,
          api: api,
          opts,
          orientation:
            orientation || (opts?.axis === "y" ? "vertical" : "horizontal"),
          scrollPrev,
          scrollNext,
          canScrollPrev,
          canScrollNext,
        }}
      >
        <div
          ref={ref}
          onKeyDownCapture={handleKeyDown}
          className={cn("relative", className)}
          role="region"
          aria-roledescription="carousel"
          {...props}
        >
          {children}
        </div>
      </CarouselContext.Provider>
    )
  }
)
Carousel.displayName = "Carousel"

const CarouselContent = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement>
>(({ className, ...props }, ref) => {
  const { carouselRef, orientation } = useCarousel()

  return (
    <div ref={carouselRef} className="overflow-hidden">
      <div
        ref={ref}
        className={cn(
          "flex",
          orientation === "horizontal" ? "-ml-4" : "-mt-4 flex-col",
          className
        )}
        {...props}
      />
    </div>
  )
})
CarouselContent.displayName = "CarouselContent"

const CarouselItem = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement>
>(({ className, ...props }, ref) => {
  const { orientation } = useCarousel()

  return (
    <div
      ref={ref}
      role="group"
      aria-roledescription="slide"
      className={cn(
        "min-w-0 shrink-0 grow-0 basis-full",
        orientation === "horizontal" ? "pl-4" : "pt-4",
        className
      )}
      {...props}
    />
  )
})
CarouselItem.displayName = "CarouselItem"

const CarouselPrevious = React.forwardRef<
  HTMLButtonElement,
  React.ComponentProps<typeof Button>
>(({ className, variant = "outline", size = "icon", ...props }, ref) => {
  const { orientation, scrollPrev, canScrollPrev } = useCarousel()

  return (
    <Button
      ref={ref}
      variant={variant}
      size={size}
      className={cn(
        "absolute  h-8 w-8 rounded-full",
        orientation === "horizontal"
          ? "-left-12 top-1/2 -translate-y-1/2"
          : "-top-12 left-1/2 -translate-x-1/2 rotate-90",
        className
      )}
      disabled={!canScrollPrev}
      onClick={scrollPrev}
      {...props}
    >
      <ArrowLeft className="h-4 w-4" />
      <span className="sr-only">Previous slide</span>
    </Button>
  )
})
CarouselPrevious.displayName = "CarouselPrevious"

const CarouselNext = React.forwardRef<
  HTMLButtonElement,
  React.ComponentProps<typeof Button>
>(({ className, variant = "outline", size = "icon", ...props }, ref) => {
  const { orientation, scrollNext, canScrollNext } = useCarousel()

  return (
    <Button
      ref={ref}
      variant={variant}
      size={size}
      className={cn(
        "absolute h-8 w-8 rounded-full",
        orientation === "horizontal"
          ? "-right-12 top-1/2 -translate-y-1/2"
          : "-bottom-12 left-1/2 -translate-x-1/2 rotate-90",
        className
      )}
      disabled={!canScrollNext}
      onClick={scrollNext}
      {...props}
    >
      <ArrowRight className="h-4 w-4" />
      <span className="sr-only">Next slide</span>
    </Button>
  )
})
CarouselNext.displayName = "CarouselNext"

export {
  type CarouselApi,
  Carousel,
  CarouselContent,
  CarouselItem,
  CarouselPrevious,
  CarouselNext,
}


--------------------------------------------------------------------------------
FILE: components/ui/chart.tsx
--------------------------------------------------------------------------------
"use client"

import * as React from "react"
import * as RechartsPrimitive from "recharts"

import { cn } from "@/lib/utils"

// Format: { THEME_NAME: CSS_SELECTOR }
const THEMES = { light: "", dark: ".dark" } as const

export type ChartConfig = {
  [k in string]: {
    label?: React.ReactNode
    icon?: React.ComponentType
  } & (
    | { color?: string; theme?: never }
    | { color?: never; theme: Record<keyof typeof THEMES, string> }
  )
}

type ChartContextProps = {
  config: ChartConfig
}

const ChartContext = React.createContext<ChartContextProps | null>(null)

function useChart() {
  const context = React.useContext(ChartContext)

  if (!context) {
    throw new Error("useChart must be used within a <ChartContainer />")
  }

  return context
}

const ChartContainer = React.forwardRef<
  HTMLDivElement,
  React.ComponentProps<"div"> & {
    config: ChartConfig
    children: React.ComponentProps<
      typeof RechartsPrimitive.ResponsiveContainer
    >["children"]
  }
>(({ id, className, children, config, ...props }, ref) => {
  const uniqueId = React.useId()
  const chartId = `chart-${id || uniqueId.replace(/:/g, "")}`

  return (
    <ChartContext.Provider value={{ config }}>
      <div
        data-chart={chartId}
        ref={ref}
        className={cn(
          "flex aspect-video justify-center text-xs [&_.recharts-cartesian-axis-tick_text]:fill-muted-foreground [&_.recharts-cartesian-grid_line[stroke='#ccc']]:stroke-border/50 [&_.recharts-curve.recharts-tooltip-cursor]:stroke-border [&_.recharts-dot[stroke='#fff']]:stroke-transparent [&_.recharts-layer]:outline-none [&_.recharts-polar-grid_[stroke='#ccc']]:stroke-border [&_.recharts-radial-bar-background-sector]:fill-muted [&_.recharts-rectangle.recharts-tooltip-cursor]:fill-muted [&_.recharts-reference-line_[stroke='#ccc']]:stroke-border [&_.recharts-sector[stroke='#fff']]:stroke-transparent [&_.recharts-sector]:outline-none [&_.recharts-surface]:outline-none",
          className
        )}
        {...props}
      >
        <ChartStyle id={chartId} config={config} />
        <RechartsPrimitive.ResponsiveContainer>
          {children}
        </RechartsPrimitive.ResponsiveContainer>
      </div>
    </ChartContext.Provider>
  )
})
ChartContainer.displayName = "Chart"

const ChartStyle = ({ id, config }: { id: string; config: ChartConfig }) => {
  const colorConfig = Object.entries(config).filter(
    ([_, config]) => config.theme || config.color
  )

  if (!colorConfig.length) {
    return null
  }

  return (
    <style
      dangerouslySetInnerHTML={{
        __html: Object.entries(THEMES)
          .map(
            ([theme, prefix]) => `
${prefix} [data-chart=${id}] {
${colorConfig
  .map(([key, itemConfig]) => {
    const color =
      itemConfig.theme?.[theme as keyof typeof itemConfig.theme] ||
      itemConfig.color
    return color ? `  --color-${key}: ${color};` : null
  })
  .join("\n")}
}
`
          )
          .join("\n"),
      }}
    />
  )
}

const ChartTooltip = RechartsPrimitive.Tooltip

const ChartTooltipContent = React.forwardRef<
  HTMLDivElement,
  React.ComponentProps<typeof RechartsPrimitive.Tooltip> &
    React.ComponentProps<"div"> & {
      hideLabel?: boolean
      hideIndicator?: boolean
      indicator?: "line" | "dot" | "dashed"
      nameKey?: string
      labelKey?: string
    }
>(
  (
    {
      active,
      payload,
      className,
      indicator = "dot",
      hideLabel = false,
      hideIndicator = false,
      label,
      labelFormatter,
      labelClassName,
      formatter,
      color,
      nameKey,
      labelKey,
    },
    ref
  ) => {
    const { config } = useChart()

    const tooltipLabel = React.useMemo(() => {
      if (hideLabel || !payload?.length) {
        return null
      }

      const [item] = payload
      const key = `${labelKey || item.dataKey || item.name || "value"}`
      const itemConfig = getPayloadConfigFromPayload(config, item, key)
      const value =
        !labelKey && typeof label === "string"
          ? config[label as keyof typeof config]?.label || label
          : itemConfig?.label

      if (labelFormatter) {
        return (
          <div className={cn("font-medium", labelClassName)}>
            {labelFormatter(value, payload)}
          </div>
        )
      }

      if (!value) {
        return null
      }

      return <div className={cn("font-medium", labelClassName)}>{value}</div>
    }, [
      label,
      labelFormatter,
      payload,
      hideLabel,
      labelClassName,
      config,
      labelKey,
    ])

    if (!active || !payload?.length) {
      return null
    }

    const nestLabel = payload.length === 1 && indicator !== "dot"

    return (
      <div
        ref={ref}
        className={cn(
          "grid min-w-[8rem] items-start gap-1.5 rounded-lg border border-border/50 bg-background px-2.5 py-1.5 text-xs shadow-xl",
          className
        )}
      >
        {!nestLabel ? tooltipLabel : null}
        <div className="grid gap-1.5">
          {payload.map((item, index) => {
            const key = `${nameKey || item.name || item.dataKey || "value"}`
            const itemConfig = getPayloadConfigFromPayload(config, item, key)
            const indicatorColor = color || item.payload.fill || item.color

            return (
              <div
                key={item.dataKey}
                className={cn(
                  "flex w-full flex-wrap items-stretch gap-2 [&>svg]:h-2.5 [&>svg]:w-2.5 [&>svg]:text-muted-foreground",
                  indicator === "dot" && "items-center"
                )}
              >
                {formatter && item?.value !== undefined && item.name ? (
                  formatter(item.value, item.name, item, index, item.payload)
                ) : (
                  <>
                    {itemConfig?.icon ? (
                      <itemConfig.icon />
                    ) : (
                      !hideIndicator && (
                        <div
                          className={cn(
                            "shrink-0 rounded-[2px] border-[--color-border] bg-[--color-bg]",
                            {
                              "h-2.5 w-2.5": indicator === "dot",
                              "w-1": indicator === "line",
                              "w-0 border-[1.5px] border-dashed bg-transparent":
                                indicator === "dashed",
                              "my-0.5": nestLabel && indicator === "dashed",
                            }
                          )}
                          style={
                            {
                              "--color-bg": indicatorColor,
                              "--color-border": indicatorColor,
                            } as React.CSSProperties
                          }
                        />
                      )
                    )}
                    <div
                      className={cn(
                        "flex flex-1 justify-between leading-none",
                        nestLabel ? "items-end" : "items-center"
                      )}
                    >
                      <div className="grid gap-1.5">
                        {nestLabel ? tooltipLabel : null}
                        <span className="text-muted-foreground">
                          {itemConfig?.label || item.name}
                        </span>
                      </div>
                      {item.value && (
                        <span className="font-mono font-medium tabular-nums text-foreground">
                          {item.value.toLocaleString()}
                        </span>
                      )}
                    </div>
                  </>
                )}
              </div>
            )
          })}
        </div>
      </div>
    )
  }
)
ChartTooltipContent.displayName = "ChartTooltip"

const ChartLegend = RechartsPrimitive.Legend

const ChartLegendContent = React.forwardRef<
  HTMLDivElement,
  React.ComponentProps<"div"> &
    Pick<RechartsPrimitive.LegendProps, "payload" | "verticalAlign"> & {
      hideIcon?: boolean
      nameKey?: string
    }
>(
  (
    { className, hideIcon = false, payload, verticalAlign = "bottom", nameKey },
    ref
  ) => {
    const { config } = useChart()

    if (!payload?.length) {
      return null
    }

    return (
      <div
        ref={ref}
        className={cn(
          "flex items-center justify-center gap-4",
          verticalAlign === "top" ? "pb-3" : "pt-3",
          className
        )}
      >
        {payload.map((item) => {
          const key = `${nameKey || item.dataKey || "value"}`
          const itemConfig = getPayloadConfigFromPayload(config, item, key)

          return (
            <div
              key={item.value}
              className={cn(
                "flex items-center gap-1.5 [&>svg]:h-3 [&>svg]:w-3 [&>svg]:text-muted-foreground"
              )}
            >
              {itemConfig?.icon && !hideIcon ? (
                <itemConfig.icon />
              ) : (
                <div
                  className="h-2 w-2 shrink-0 rounded-[2px]"
                  style={{
                    backgroundColor: item.color,
                  }}
                />
              )}
              {itemConfig?.label}
            </div>
          )
        })}
      </div>
    )
  }
)
ChartLegendContent.displayName = "ChartLegend"

// Helper to extract item config from a payload.
function getPayloadConfigFromPayload(
  config: ChartConfig,
  payload: unknown,
  key: string
) {
  if (typeof payload !== "object" || payload === null) {
    return undefined
  }

  const payloadPayload =
    "payload" in payload &&
    typeof payload.payload === "object" &&
    payload.payload !== null
      ? payload.payload
      : undefined

  let configLabelKey: string = key

  if (
    key in payload &&
    typeof payload[key as keyof typeof payload] === "string"
  ) {
    configLabelKey = payload[key as keyof typeof payload] as string
  } else if (
    payloadPayload &&
    key in payloadPayload &&
    typeof payloadPayload[key as keyof typeof payloadPayload] === "string"
  ) {
    configLabelKey = payloadPayload[
      key as keyof typeof payloadPayload
    ] as string
  }

  return configLabelKey in config
    ? config[configLabelKey]
    : config[key as keyof typeof config]
}

export {
  ChartContainer,
  ChartTooltip,
  ChartTooltipContent,
  ChartLegend,
  ChartLegendContent,
  ChartStyle,
}


--------------------------------------------------------------------------------
FILE: components/ui/checkbox.tsx
--------------------------------------------------------------------------------
"use client"

import * as React from "react"
import * as CheckboxPrimitive from "@radix-ui/react-checkbox"
import { Check } from "lucide-react"

import { cn } from "@/lib/utils"

const Checkbox = React.forwardRef<
  React.ElementRef<typeof CheckboxPrimitive.Root>,
  React.ComponentPropsWithoutRef<typeof CheckboxPrimitive.Root>
>(({ className, ...props }, ref) => (
  <CheckboxPrimitive.Root
    ref={ref}
    className={cn(
      "peer h-4 w-4 shrink-0 rounded-sm border border-primary ring-offset-background focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50 data-[state=checked]:bg-primary data-[state=checked]:text-primary-foreground",
      className
    )}
    {...props}
  >
    <CheckboxPrimitive.Indicator
      className={cn("flex items-center justify-center text-current")}
    >
      <Check className="h-4 w-4" />
    </CheckboxPrimitive.Indicator>
  </CheckboxPrimitive.Root>
))
Checkbox.displayName = CheckboxPrimitive.Root.displayName

export { Checkbox }


--------------------------------------------------------------------------------
FILE: components/ui/collapsible.tsx
--------------------------------------------------------------------------------
"use client"

import * as CollapsiblePrimitive from "@radix-ui/react-collapsible"

const Collapsible = CollapsiblePrimitive.Root

const CollapsibleTrigger = CollapsiblePrimitive.CollapsibleTrigger

const CollapsibleContent = CollapsiblePrimitive.CollapsibleContent

export { Collapsible, CollapsibleTrigger, CollapsibleContent }


--------------------------------------------------------------------------------
FILE: components/ui/command.tsx
--------------------------------------------------------------------------------
"use client"

import * as React from "react"
import { type DialogProps } from "@radix-ui/react-dialog"
import { Command as CommandPrimitive } from "cmdk"
import { Search } from "lucide-react"

import { cn } from "@/lib/utils"
import { Dialog, DialogContent } from "@/components/ui/dialog"

const Command = React.forwardRef<
  React.ElementRef<typeof CommandPrimitive>,
  React.ComponentPropsWithoutRef<typeof CommandPrimitive>
>(({ className, ...props }, ref) => (
  <CommandPrimitive
    ref={ref}
    className={cn(
      "flex h-full w-full flex-col overflow-hidden rounded-md bg-popover text-popover-foreground",
      className
    )}
    {...props}
  />
))
Command.displayName = CommandPrimitive.displayName

const CommandDialog = ({ children, ...props }: DialogProps) => {
  return (
    <Dialog {...props}>
      <DialogContent className="overflow-hidden p-0 shadow-lg">
        <Command className="[&_[cmdk-group-heading]]:px-2 [&_[cmdk-group-heading]]:font-medium [&_[cmdk-group-heading]]:text-muted-foreground [&_[cmdk-group]:not([hidden])_~[cmdk-group]]:pt-0 [&_[cmdk-group]]:px-2 [&_[cmdk-input-wrapper]_svg]:h-5 [&_[cmdk-input-wrapper]_svg]:w-5 [&_[cmdk-input]]:h-12 [&_[cmdk-item]]:px-2 [&_[cmdk-item]]:py-3 [&_[cmdk-item]_svg]:h-5 [&_[cmdk-item]_svg]:w-5">
          {children}
        </Command>
      </DialogContent>
    </Dialog>
  )
}

const CommandInput = React.forwardRef<
  React.ElementRef<typeof CommandPrimitive.Input>,
  React.ComponentPropsWithoutRef<typeof CommandPrimitive.Input>
>(({ className, ...props }, ref) => (
  <div className="flex items-center border-b px-3" cmdk-input-wrapper="">
    <Search className="mr-2 h-4 w-4 shrink-0 opacity-50" />
    <CommandPrimitive.Input
      ref={ref}
      className={cn(
        "flex h-11 w-full rounded-md bg-transparent py-3 text-sm outline-none placeholder:text-muted-foreground disabled:cursor-not-allowed disabled:opacity-50",
        className
      )}
      {...props}
    />
  </div>
))

CommandInput.displayName = CommandPrimitive.Input.displayName

const CommandList = React.forwardRef<
  React.ElementRef<typeof CommandPrimitive.List>,
  React.ComponentPropsWithoutRef<typeof CommandPrimitive.List>
>(({ className, ...props }, ref) => (
  <CommandPrimitive.List
    ref={ref}
    className={cn("max-h-[300px] overflow-y-auto overflow-x-hidden", className)}
    {...props}
  />
))

CommandList.displayName = CommandPrimitive.List.displayName

const CommandEmpty = React.forwardRef<
  React.ElementRef<typeof CommandPrimitive.Empty>,
  React.ComponentPropsWithoutRef<typeof CommandPrimitive.Empty>
>((props, ref) => (
  <CommandPrimitive.Empty
    ref={ref}
    className="py-6 text-center text-sm"
    {...props}
  />
))

CommandEmpty.displayName = CommandPrimitive.Empty.displayName

const CommandGroup = React.forwardRef<
  React.ElementRef<typeof CommandPrimitive.Group>,
  React.ComponentPropsWithoutRef<typeof CommandPrimitive.Group>
>(({ className, ...props }, ref) => (
  <CommandPrimitive.Group
    ref={ref}
    className={cn(
      "overflow-hidden p-1 text-foreground [&_[cmdk-group-heading]]:px-2 [&_[cmdk-group-heading]]:py-1.5 [&_[cmdk-group-heading]]:text-xs [&_[cmdk-group-heading]]:font-medium [&_[cmdk-group-heading]]:text-muted-foreground",
      className
    )}
    {...props}
  />
))

CommandGroup.displayName = CommandPrimitive.Group.displayName

const CommandSeparator = React.forwardRef<
  React.ElementRef<typeof CommandPrimitive.Separator>,
  React.ComponentPropsWithoutRef<typeof CommandPrimitive.Separator>
>(({ className, ...props }, ref) => (
  <CommandPrimitive.Separator
    ref={ref}
    className={cn("-mx-1 h-px bg-border", className)}
    {...props}
  />
))
CommandSeparator.displayName = CommandPrimitive.Separator.displayName

const CommandItem = React.forwardRef<
  React.ElementRef<typeof CommandPrimitive.Item>,
  React.ComponentPropsWithoutRef<typeof CommandPrimitive.Item>
>(({ className, ...props }, ref) => (
  <CommandPrimitive.Item
    ref={ref}
    className={cn(
      "relative flex cursor-default gap-2 select-none items-center rounded-sm px-2 py-1.5 text-sm outline-none data-[disabled=true]:pointer-events-none data-[selected='true']:bg-accent data-[selected=true]:text-accent-foreground data-[disabled=true]:opacity-50 [&_svg]:pointer-events-none [&_svg]:size-4 [&_svg]:shrink-0",
      className
    )}
    {...props}
  />
))

CommandItem.displayName = CommandPrimitive.Item.displayName

const CommandShortcut = ({
  className,
  ...props
}: React.HTMLAttributes<HTMLSpanElement>) => {
  return (
    <span
      className={cn(
        "ml-auto text-xs tracking-widest text-muted-foreground",
        className
      )}
      {...props}
    />
  )
}
CommandShortcut.displayName = "CommandShortcut"

export {
  Command,
  CommandDialog,
  CommandInput,
  CommandList,
  CommandEmpty,
  CommandGroup,
  CommandItem,
  CommandShortcut,
  CommandSeparator,
}


--------------------------------------------------------------------------------
FILE: components/ui/context-menu.tsx
--------------------------------------------------------------------------------
"use client"

import * as React from "react"
import * as ContextMenuPrimitive from "@radix-ui/react-context-menu"
import { Check, ChevronRight, Circle } from "lucide-react"

import { cn } from "@/lib/utils"

const ContextMenu = ContextMenuPrimitive.Root

const ContextMenuTrigger = ContextMenuPrimitive.Trigger

const ContextMenuGroup = ContextMenuPrimitive.Group

const ContextMenuPortal = ContextMenuPrimitive.Portal

const ContextMenuSub = ContextMenuPrimitive.Sub

const ContextMenuRadioGroup = ContextMenuPrimitive.RadioGroup

const ContextMenuSubTrigger = React.forwardRef<
  React.ElementRef<typeof ContextMenuPrimitive.SubTrigger>,
  React.ComponentPropsWithoutRef<typeof ContextMenuPrimitive.SubTrigger> & {
    inset?: boolean
  }
>(({ className, inset, children, ...props }, ref) => (
  <ContextMenuPrimitive.SubTrigger
    ref={ref}
    className={cn(
      "flex cursor-default select-none items-center rounded-sm px-2 py-1.5 text-sm outline-none focus:bg-accent focus:text-accent-foreground data-[state=open]:bg-accent data-[state=open]:text-accent-foreground",
      inset && "pl-8",
      className
    )}
    {...props}
  >
    {children}
    <ChevronRight className="ml-auto h-4 w-4" />
  </ContextMenuPrimitive.SubTrigger>
))
ContextMenuSubTrigger.displayName = ContextMenuPrimitive.SubTrigger.displayName

const ContextMenuSubContent = React.forwardRef<
  React.ElementRef<typeof ContextMenuPrimitive.SubContent>,
  React.ComponentPropsWithoutRef<typeof ContextMenuPrimitive.SubContent>
>(({ className, ...props }, ref) => (
  <ContextMenuPrimitive.SubContent
    ref={ref}
    className={cn(
      "z-50 min-w-[8rem] overflow-hidden rounded-md border bg-popover p-1 text-popover-foreground shadow-md data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2",
      className
    )}
    {...props}
  />
))
ContextMenuSubContent.displayName = ContextMenuPrimitive.SubContent.displayName

const ContextMenuContent = React.forwardRef<
  React.ElementRef<typeof ContextMenuPrimitive.Content>,
  React.ComponentPropsWithoutRef<typeof ContextMenuPrimitive.Content>
>(({ className, ...props }, ref) => (
  <ContextMenuPrimitive.Portal>
    <ContextMenuPrimitive.Content
      ref={ref}
      className={cn(
        "z-50 min-w-[8rem] overflow-hidden rounded-md border bg-popover p-1 text-popover-foreground shadow-md animate-in fade-in-80 data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2",
        className
      )}
      {...props}
    />
  </ContextMenuPrimitive.Portal>
))
ContextMenuContent.displayName = ContextMenuPrimitive.Content.displayName

const ContextMenuItem = React.forwardRef<
  React.ElementRef<typeof ContextMenuPrimitive.Item>,
  React.ComponentPropsWithoutRef<typeof ContextMenuPrimitive.Item> & {
    inset?: boolean
  }
>(({ className, inset, ...props }, ref) => (
  <ContextMenuPrimitive.Item
    ref={ref}
    className={cn(
      "relative flex cursor-default select-none items-center rounded-sm px-2 py-1.5 text-sm outline-none focus:bg-accent focus:text-accent-foreground data-[disabled]:pointer-events-none data-[disabled]:opacity-50",
      inset && "pl-8",
      className
    )}
    {...props}
  />
))
ContextMenuItem.displayName = ContextMenuPrimitive.Item.displayName

const ContextMenuCheckboxItem = React.forwardRef<
  React.ElementRef<typeof ContextMenuPrimitive.CheckboxItem>,
  React.ComponentPropsWithoutRef<typeof ContextMenuPrimitive.CheckboxItem>
>(({ className, children, checked, ...props }, ref) => (
  <ContextMenuPrimitive.CheckboxItem
    ref={ref}
    className={cn(
      "relative flex cursor-default select-none items-center rounded-sm py-1.5 pl-8 pr-2 text-sm outline-none focus:bg-accent focus:text-accent-foreground data-[disabled]:pointer-events-none data-[disabled]:opacity-50",
      className
    )}
    checked={checked}
    {...props}
  >
    <span className="absolute left-2 flex h-3.5 w-3.5 items-center justify-center">
      <ContextMenuPrimitive.ItemIndicator>
        <Check className="h-4 w-4" />
      </ContextMenuPrimitive.ItemIndicator>
    </span>
    {children}
  </ContextMenuPrimitive.CheckboxItem>
))
ContextMenuCheckboxItem.displayName =
  ContextMenuPrimitive.CheckboxItem.displayName

const ContextMenuRadioItem = React.forwardRef<
  React.ElementRef<typeof ContextMenuPrimitive.RadioItem>,
  React.ComponentPropsWithoutRef<typeof ContextMenuPrimitive.RadioItem>
>(({ className, children, ...props }, ref) => (
  <ContextMenuPrimitive.RadioItem
    ref={ref}
    className={cn(
      "relative flex cursor-default select-none items-center rounded-sm py-1.5 pl-8 pr-2 text-sm outline-none focus:bg-accent focus:text-accent-foreground data-[disabled]:pointer-events-none data-[disabled]:opacity-50",
      className
    )}
    {...props}
  >
    <span className="absolute left-2 flex h-3.5 w-3.5 items-center justify-center">
      <ContextMenuPrimitive.ItemIndicator>
        <Circle className="h-2 w-2 fill-current" />
      </ContextMenuPrimitive.ItemIndicator>
    </span>
    {children}
  </ContextMenuPrimitive.RadioItem>
))
ContextMenuRadioItem.displayName = ContextMenuPrimitive.RadioItem.displayName

const ContextMenuLabel = React.forwardRef<
  React.ElementRef<typeof ContextMenuPrimitive.Label>,
  React.ComponentPropsWithoutRef<typeof ContextMenuPrimitive.Label> & {
    inset?: boolean
  }
>(({ className, inset, ...props }, ref) => (
  <ContextMenuPrimitive.Label
    ref={ref}
    className={cn(
      "px-2 py-1.5 text-sm font-semibold text-foreground",
      inset && "pl-8",
      className
    )}
    {...props}
  />
))
ContextMenuLabel.displayName = ContextMenuPrimitive.Label.displayName

const ContextMenuSeparator = React.forwardRef<
  React.ElementRef<typeof ContextMenuPrimitive.Separator>,
  React.ComponentPropsWithoutRef<typeof ContextMenuPrimitive.Separator>
>(({ className, ...props }, ref) => (
  <ContextMenuPrimitive.Separator
    ref={ref}
    className={cn("-mx-1 my-1 h-px bg-border", className)}
    {...props}
  />
))
ContextMenuSeparator.displayName = ContextMenuPrimitive.Separator.displayName

const ContextMenuShortcut = ({
  className,
  ...props
}: React.HTMLAttributes<HTMLSpanElement>) => {
  return (
    <span
      className={cn(
        "ml-auto text-xs tracking-widest text-muted-foreground",
        className
      )}
      {...props}
    />
  )
}
ContextMenuShortcut.displayName = "ContextMenuShortcut"

export {
  ContextMenu,
  ContextMenuTrigger,
  ContextMenuContent,
  ContextMenuItem,
  ContextMenuCheckboxItem,
  ContextMenuRadioItem,
  ContextMenuLabel,
  ContextMenuSeparator,
  ContextMenuShortcut,
  ContextMenuGroup,
  ContextMenuPortal,
  ContextMenuSub,
  ContextMenuSubContent,
  ContextMenuSubTrigger,
  ContextMenuRadioGroup,
}


--------------------------------------------------------------------------------
FILE: components/ui/dialog.tsx
--------------------------------------------------------------------------------
"use client"

import * as React from "react"
import * as DialogPrimitive from "@radix-ui/react-dialog"
import { X } from "lucide-react"

import { cn } from "@/lib/utils"

const Dialog = DialogPrimitive.Root

const DialogTrigger = DialogPrimitive.Trigger

const DialogPortal = DialogPrimitive.Portal

const DialogClose = DialogPrimitive.Close

const DialogOverlay = React.forwardRef<
  React.ElementRef<typeof DialogPrimitive.Overlay>,
  React.ComponentPropsWithoutRef<typeof DialogPrimitive.Overlay>
>(({ className, ...props }, ref) => (
  <DialogPrimitive.Overlay
    ref={ref}
    className={cn(
      "fixed inset-0 z-50 bg-black/80  data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0",
      className
    )}
    {...props}
  />
))
DialogOverlay.displayName = DialogPrimitive.Overlay.displayName

const DialogContent = React.forwardRef<
  React.ElementRef<typeof DialogPrimitive.Content>,
  React.ComponentPropsWithoutRef<typeof DialogPrimitive.Content>
>(({ className, children, ...props }, ref) => (
  <DialogPortal>
    <DialogOverlay />
    <DialogPrimitive.Content
      ref={ref}
      className={cn(
        "fixed left-[50%] top-[50%] z-50 grid w-full max-w-lg translate-x-[-50%] translate-y-[-50%] gap-4 border bg-background p-6 shadow-lg duration-200 data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[state=closed]:slide-out-to-left-1/2 data-[state=closed]:slide-out-to-top-[48%] data-[state=open]:slide-in-from-left-1/2 data-[state=open]:slide-in-from-top-[48%] sm:rounded-lg",
        className
      )}
      {...props}
    >
      {children}
      <DialogPrimitive.Close className="absolute right-4 top-4 rounded-sm opacity-70 ring-offset-background transition-opacity hover:opacity-100 focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2 disabled:pointer-events-none data-[state=open]:bg-accent data-[state=open]:text-muted-foreground">
        <X className="h-4 w-4" />
        <span className="sr-only">Close</span>
      </DialogPrimitive.Close>
    </DialogPrimitive.Content>
  </DialogPortal>
))
DialogContent.displayName = DialogPrimitive.Content.displayName

const DialogHeader = ({
  className,
  ...props
}: React.HTMLAttributes<HTMLDivElement>) => (
  <div
    className={cn(
      "flex flex-col space-y-1.5 text-center sm:text-left",
      className
    )}
    {...props}
  />
)
DialogHeader.displayName = "DialogHeader"

const DialogFooter = ({
  className,
  ...props
}: React.HTMLAttributes<HTMLDivElement>) => (
  <div
    className={cn(
      "flex flex-col-reverse sm:flex-row sm:justify-end sm:space-x-2",
      className
    )}
    {...props}
  />
)
DialogFooter.displayName = "DialogFooter"

const DialogTitle = React.forwardRef<
  React.ElementRef<typeof DialogPrimitive.Title>,
  React.ComponentPropsWithoutRef<typeof DialogPrimitive.Title>
>(({ className, ...props }, ref) => (
  <DialogPrimitive.Title
    ref={ref}
    className={cn(
      "text-lg font-semibold leading-none tracking-tight",
      className
    )}
    {...props}
  />
))
DialogTitle.displayName = DialogPrimitive.Title.displayName

const DialogDescription = React.forwardRef<
  React.ElementRef<typeof DialogPrimitive.Description>,
  React.ComponentPropsWithoutRef<typeof DialogPrimitive.Description>
>(({ className, ...props }, ref) => (
  <DialogPrimitive.Description
    ref={ref}
    className={cn("text-sm text-muted-foreground", className)}
    {...props}
  />
))
DialogDescription.displayName = DialogPrimitive.Description.displayName

export {
  Dialog,
  DialogPortal,
  DialogOverlay,
  DialogClose,
  DialogTrigger,
  DialogContent,
  DialogHeader,
  DialogFooter,
  DialogTitle,
  DialogDescription,
}


--------------------------------------------------------------------------------
FILE: components/ui/drawer.tsx
--------------------------------------------------------------------------------
"use client"

import * as React from "react"
import { Drawer as DrawerPrimitive } from "vaul"

import { cn } from "@/lib/utils"

const Drawer = ({
  shouldScaleBackground = true,
  ...props
}: React.ComponentProps<typeof DrawerPrimitive.Root>) => (
  <DrawerPrimitive.Root
    shouldScaleBackground={shouldScaleBackground}
    {...props}
  />
)
Drawer.displayName = "Drawer"

const DrawerTrigger = DrawerPrimitive.Trigger

const DrawerPortal = DrawerPrimitive.Portal

const DrawerClose = DrawerPrimitive.Close

const DrawerOverlay = React.forwardRef<
  React.ElementRef<typeof DrawerPrimitive.Overlay>,
  React.ComponentPropsWithoutRef<typeof DrawerPrimitive.Overlay>
>(({ className, ...props }, ref) => (
  <DrawerPrimitive.Overlay
    ref={ref}
    className={cn("fixed inset-0 z-50 bg-black/80", className)}
    {...props}
  />
))
DrawerOverlay.displayName = DrawerPrimitive.Overlay.displayName

const DrawerContent = React.forwardRef<
  React.ElementRef<typeof DrawerPrimitive.Content>,
  React.ComponentPropsWithoutRef<typeof DrawerPrimitive.Content>
>(({ className, children, ...props }, ref) => (
  <DrawerPortal>
    <DrawerOverlay />
    <DrawerPrimitive.Content
      ref={ref}
      className={cn(
        "fixed inset-x-0 bottom-0 z-50 mt-24 flex h-auto flex-col rounded-t-[10px] border bg-background",
        className
      )}
      {...props}
    >
      <div className="mx-auto mt-4 h-2 w-[100px] rounded-full bg-muted" />
      {children}
    </DrawerPrimitive.Content>
  </DrawerPortal>
))
DrawerContent.displayName = "DrawerContent"

const DrawerHeader = ({
  className,
  ...props
}: React.HTMLAttributes<HTMLDivElement>) => (
  <div
    className={cn("grid gap-1.5 p-4 text-center sm:text-left", className)}
    {...props}
  />
)
DrawerHeader.displayName = "DrawerHeader"

const DrawerFooter = ({
  className,
  ...props
}: React.HTMLAttributes<HTMLDivElement>) => (
  <div
    className={cn("mt-auto flex flex-col gap-2 p-4", className)}
    {...props}
  />
)
DrawerFooter.displayName = "DrawerFooter"

const DrawerTitle = React.forwardRef<
  React.ElementRef<typeof DrawerPrimitive.Title>,
  React.ComponentPropsWithoutRef<typeof DrawerPrimitive.Title>
>(({ className, ...props }, ref) => (
  <DrawerPrimitive.Title
    ref={ref}
    className={cn(
      "text-lg font-semibold leading-none tracking-tight",
      className
    )}
    {...props}
  />
))
DrawerTitle.displayName = DrawerPrimitive.Title.displayName

const DrawerDescription = React.forwardRef<
  React.ElementRef<typeof DrawerPrimitive.Description>,
  React.ComponentPropsWithoutRef<typeof DrawerPrimitive.Description>
>(({ className, ...props }, ref) => (
  <DrawerPrimitive.Description
    ref={ref}
    className={cn("text-sm text-muted-foreground", className)}
    {...props}
  />
))
DrawerDescription.displayName = DrawerPrimitive.Description.displayName

export {
  Drawer,
  DrawerPortal,
  DrawerOverlay,
  DrawerTrigger,
  DrawerClose,
  DrawerContent,
  DrawerHeader,
  DrawerFooter,
  DrawerTitle,
  DrawerDescription,
}


--------------------------------------------------------------------------------
FILE: components/ui/dropdown-menu.tsx
--------------------------------------------------------------------------------
"use client"

import * as React from "react"
import * as DropdownMenuPrimitive from "@radix-ui/react-dropdown-menu"
import { Check, ChevronRight, Circle } from "lucide-react"

import { cn } from "@/lib/utils"

const DropdownMenu = DropdownMenuPrimitive.Root

const DropdownMenuTrigger = DropdownMenuPrimitive.Trigger

const DropdownMenuGroup = DropdownMenuPrimitive.Group

const DropdownMenuPortal = DropdownMenuPrimitive.Portal

const DropdownMenuSub = DropdownMenuPrimitive.Sub

const DropdownMenuRadioGroup = DropdownMenuPrimitive.RadioGroup

const DropdownMenuSubTrigger = React.forwardRef<
  React.ElementRef<typeof DropdownMenuPrimitive.SubTrigger>,
  React.ComponentPropsWithoutRef<typeof DropdownMenuPrimitive.SubTrigger> & {
    inset?: boolean
  }
>(({ className, inset, children, ...props }, ref) => (
  <DropdownMenuPrimitive.SubTrigger
    ref={ref}
    className={cn(
      "flex cursor-default gap-2 select-none items-center rounded-sm px-2 py-1.5 text-sm outline-none focus:bg-accent data-[state=open]:bg-accent [&_svg]:pointer-events-none [&_svg]:size-4 [&_svg]:shrink-0",
      inset && "pl-8",
      className
    )}
    {...props}
  >
    {children}
    <ChevronRight className="ml-auto" />
  </DropdownMenuPrimitive.SubTrigger>
))
DropdownMenuSubTrigger.displayName =
  DropdownMenuPrimitive.SubTrigger.displayName

const DropdownMenuSubContent = React.forwardRef<
  React.ElementRef<typeof DropdownMenuPrimitive.SubContent>,
  React.ComponentPropsWithoutRef<typeof DropdownMenuPrimitive.SubContent>
>(({ className, ...props }, ref) => (
  <DropdownMenuPrimitive.SubContent
    ref={ref}
    className={cn(
      "z-50 min-w-[8rem] overflow-hidden rounded-md border bg-popover p-1 text-popover-foreground shadow-lg data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2",
      className
    )}
    {...props}
  />
))
DropdownMenuSubContent.displayName =
  DropdownMenuPrimitive.SubContent.displayName

const DropdownMenuContent = React.forwardRef<
  React.ElementRef<typeof DropdownMenuPrimitive.Content>,
  React.ComponentPropsWithoutRef<typeof DropdownMenuPrimitive.Content>
>(({ className, sideOffset = 4, ...props }, ref) => (
  <DropdownMenuPrimitive.Portal>
    <DropdownMenuPrimitive.Content
      ref={ref}
      sideOffset={sideOffset}
      className={cn(
        "z-50 min-w-[8rem] overflow-hidden rounded-md border bg-popover p-1 text-popover-foreground shadow-md data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2",
        className
      )}
      {...props}
    />
  </DropdownMenuPrimitive.Portal>
))
DropdownMenuContent.displayName = DropdownMenuPrimitive.Content.displayName

const DropdownMenuItem = React.forwardRef<
  React.ElementRef<typeof DropdownMenuPrimitive.Item>,
  React.ComponentPropsWithoutRef<typeof DropdownMenuPrimitive.Item> & {
    inset?: boolean
  }
>(({ className, inset, ...props }, ref) => (
  <DropdownMenuPrimitive.Item
    ref={ref}
    className={cn(
      "relative flex cursor-default select-none items-center gap-2 rounded-sm px-2 py-1.5 text-sm outline-none transition-colors focus:bg-accent focus:text-accent-foreground data-[disabled]:pointer-events-none data-[disabled]:opacity-50 [&_svg]:pointer-events-none [&_svg]:size-4 [&_svg]:shrink-0",
      inset && "pl-8",
      className
    )}
    {...props}
  />
))
DropdownMenuItem.displayName = DropdownMenuPrimitive.Item.displayName

const DropdownMenuCheckboxItem = React.forwardRef<
  React.ElementRef<typeof DropdownMenuPrimitive.CheckboxItem>,
  React.ComponentPropsWithoutRef<typeof DropdownMenuPrimitive.CheckboxItem>
>(({ className, children, checked, ...props }, ref) => (
  <DropdownMenuPrimitive.CheckboxItem
    ref={ref}
    className={cn(
      "relative flex cursor-default select-none items-center rounded-sm py-1.5 pl-8 pr-2 text-sm outline-none transition-colors focus:bg-accent focus:text-accent-foreground data-[disabled]:pointer-events-none data-[disabled]:opacity-50",
      className
    )}
    checked={checked}
    {...props}
  >
    <span className="absolute left-2 flex h-3.5 w-3.5 items-center justify-center">
      <DropdownMenuPrimitive.ItemIndicator>
        <Check className="h-4 w-4" />
      </DropdownMenuPrimitive.ItemIndicator>
    </span>
    {children}
  </DropdownMenuPrimitive.CheckboxItem>
))
DropdownMenuCheckboxItem.displayName =
  DropdownMenuPrimitive.CheckboxItem.displayName

const DropdownMenuRadioItem = React.forwardRef<
  React.ElementRef<typeof DropdownMenuPrimitive.RadioItem>,
  React.ComponentPropsWithoutRef<typeof DropdownMenuPrimitive.RadioItem>
>(({ className, children, ...props }, ref) => (
  <DropdownMenuPrimitive.RadioItem
    ref={ref}
    className={cn(
      "relative flex cursor-default select-none items-center rounded-sm py-1.5 pl-8 pr-2 text-sm outline-none transition-colors focus:bg-accent focus:text-accent-foreground data-[disabled]:pointer-events-none data-[disabled]:opacity-50",
      className
    )}
    {...props}
  >
    <span className="absolute left-2 flex h-3.5 w-3.5 items-center justify-center">
      <DropdownMenuPrimitive.ItemIndicator>
        <Circle className="h-2 w-2 fill-current" />
      </DropdownMenuPrimitive.ItemIndicator>
    </span>
    {children}
  </DropdownMenuPrimitive.RadioItem>
))
DropdownMenuRadioItem.displayName = DropdownMenuPrimitive.RadioItem.displayName

const DropdownMenuLabel = React.forwardRef<
  React.ElementRef<typeof DropdownMenuPrimitive.Label>,
  React.ComponentPropsWithoutRef<typeof DropdownMenuPrimitive.Label> & {
    inset?: boolean
  }
>(({ className, inset, ...props }, ref) => (
  <DropdownMenuPrimitive.Label
    ref={ref}
    className={cn(
      "px-2 py-1.5 text-sm font-semibold",
      inset && "pl-8",
      className
    )}
    {...props}
  />
))
DropdownMenuLabel.displayName = DropdownMenuPrimitive.Label.displayName

const DropdownMenuSeparator = React.forwardRef<
  React.ElementRef<typeof DropdownMenuPrimitive.Separator>,
  React.ComponentPropsWithoutRef<typeof DropdownMenuPrimitive.Separator>
>(({ className, ...props }, ref) => (
  <DropdownMenuPrimitive.Separator
    ref={ref}
    className={cn("-mx-1 my-1 h-px bg-muted", className)}
    {...props}
  />
))
DropdownMenuSeparator.displayName = DropdownMenuPrimitive.Separator.displayName

const DropdownMenuShortcut = ({
  className,
  ...props
}: React.HTMLAttributes<HTMLSpanElement>) => {
  return (
    <span
      className={cn("ml-auto text-xs tracking-widest opacity-60", className)}
      {...props}
    />
  )
}
DropdownMenuShortcut.displayName = "DropdownMenuShortcut"

export {
  DropdownMenu,
  DropdownMenuTrigger,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuCheckboxItem,
  DropdownMenuRadioItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuShortcut,
  DropdownMenuGroup,
  DropdownMenuPortal,
  DropdownMenuSub,
  DropdownMenuSubContent,
  DropdownMenuSubTrigger,
  DropdownMenuRadioGroup,
}


--------------------------------------------------------------------------------
FILE: components/ui/form.tsx
--------------------------------------------------------------------------------
"use client"

import * as React from "react"
import * as LabelPrimitive from "@radix-ui/react-label"
import { Slot } from "@radix-ui/react-slot"
import {
  Controller,
  ControllerProps,
  FieldPath,
  FieldValues,
  FormProvider,
  useFormContext,
} from "react-hook-form"

import { cn } from "@/lib/utils"
import { Label } from "@/components/ui/label"

const Form = FormProvider

type FormFieldContextValue<
  TFieldValues extends FieldValues = FieldValues,
  TName extends FieldPath<TFieldValues> = FieldPath<TFieldValues>
> = {
  name: TName
}

const FormFieldContext = React.createContext<FormFieldContextValue>(
  {} as FormFieldContextValue
)

const FormField = <
  TFieldValues extends FieldValues = FieldValues,
  TName extends FieldPath<TFieldValues> = FieldPath<TFieldValues>
>({
  ...props
}: ControllerProps<TFieldValues, TName>) => {
  return (
    <FormFieldContext.Provider value={{ name: props.name }}>
      <Controller {...props} />
    </FormFieldContext.Provider>
  )
}

const useFormField = () => {
  const fieldContext = React.useContext(FormFieldContext)
  const itemContext = React.useContext(FormItemContext)
  const { getFieldState, formState } = useFormContext()

  const fieldState = getFieldState(fieldContext.name, formState)

  if (!fieldContext) {
    throw new Error("useFormField should be used within <FormField>")
  }

  const { id } = itemContext

  return {
    id,
    name: fieldContext.name,
    formItemId: `${id}-form-item`,
    formDescriptionId: `${id}-form-item-description`,
    formMessageId: `${id}-form-item-message`,
    ...fieldState,
  }
}

type FormItemContextValue = {
  id: string
}

const FormItemContext = React.createContext<FormItemContextValue>(
  {} as FormItemContextValue
)

const FormItem = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement>
>(({ className, ...props }, ref) => {
  const id = React.useId()

  return (
    <FormItemContext.Provider value={{ id }}>
      <div ref={ref} className={cn("space-y-2", className)} {...props} />
    </FormItemContext.Provider>
  )
})
FormItem.displayName = "FormItem"

const FormLabel = React.forwardRef<
  React.ElementRef<typeof LabelPrimitive.Root>,
  React.ComponentPropsWithoutRef<typeof LabelPrimitive.Root>
>(({ className, ...props }, ref) => {
  const { error, formItemId } = useFormField()

  return (
    <Label
      ref={ref}
      className={cn(error && "text-destructive", className)}
      htmlFor={formItemId}
      {...props}
    />
  )
})
FormLabel.displayName = "FormLabel"

const FormControl = React.forwardRef<
  React.ElementRef<typeof Slot>,
  React.ComponentPropsWithoutRef<typeof Slot>
>(({ ...props }, ref) => {
  const { error, formItemId, formDescriptionId, formMessageId } = useFormField()

  return (
    <Slot
      ref={ref}
      id={formItemId}
      aria-describedby={
        !error
          ? `${formDescriptionId}`
          : `${formDescriptionId} ${formMessageId}`
      }
      aria-invalid={!!error}
      {...props}
    />
  )
})
FormControl.displayName = "FormControl"

const FormDescription = React.forwardRef<
  HTMLParagraphElement,
  React.HTMLAttributes<HTMLParagraphElement>
>(({ className, ...props }, ref) => {
  const { formDescriptionId } = useFormField()

  return (
    <p
      ref={ref}
      id={formDescriptionId}
      className={cn("text-sm text-muted-foreground", className)}
      {...props}
    />
  )
})
FormDescription.displayName = "FormDescription"

const FormMessage = React.forwardRef<
  HTMLParagraphElement,
  React.HTMLAttributes<HTMLParagraphElement>
>(({ className, children, ...props }, ref) => {
  const { error, formMessageId } = useFormField()
  const body = error ? String(error?.message) : children

  if (!body) {
    return null
  }

  return (
    <p
      ref={ref}
      id={formMessageId}
      className={cn("text-sm font-medium text-destructive", className)}
      {...props}
    >
      {body}
    </p>
  )
})
FormMessage.displayName = "FormMessage"

export {
  useFormField,
  Form,
  FormItem,
  FormLabel,
  FormControl,
  FormDescription,
  FormMessage,
  FormField,
}


--------------------------------------------------------------------------------
FILE: components/ui/hover-card.tsx
--------------------------------------------------------------------------------
"use client"

import * as React from "react"
import * as HoverCardPrimitive from "@radix-ui/react-hover-card"

import { cn } from "@/lib/utils"

const HoverCard = HoverCardPrimitive.Root

const HoverCardTrigger = HoverCardPrimitive.Trigger

const HoverCardContent = React.forwardRef<
  React.ElementRef<typeof HoverCardPrimitive.Content>,
  React.ComponentPropsWithoutRef<typeof HoverCardPrimitive.Content>
>(({ className, align = "center", sideOffset = 4, ...props }, ref) => (
  <HoverCardPrimitive.Content
    ref={ref}
    align={align}
    sideOffset={sideOffset}
    className={cn(
      "z-50 w-64 rounded-md border bg-popover p-4 text-popover-foreground shadow-md outline-none data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2",
      className
    )}
    {...props}
  />
))
HoverCardContent.displayName = HoverCardPrimitive.Content.displayName

export { HoverCard, HoverCardTrigger, HoverCardContent }


--------------------------------------------------------------------------------
FILE: components/ui/input-otp.tsx
--------------------------------------------------------------------------------
"use client"

import * as React from "react"
import { OTPInput, OTPInputContext } from "input-otp"
import { Dot } from "lucide-react"

import { cn } from "@/lib/utils"

const InputOTP = React.forwardRef<
  React.ElementRef<typeof OTPInput>,
  React.ComponentPropsWithoutRef<typeof OTPInput>
>(({ className, containerClassName, ...props }, ref) => (
  <OTPInput
    ref={ref}
    containerClassName={cn(
      "flex items-center gap-2 has-[:disabled]:opacity-50",
      containerClassName
    )}
    className={cn("disabled:cursor-not-allowed", className)}
    {...props}
  />
))
InputOTP.displayName = "InputOTP"

const InputOTPGroup = React.forwardRef<
  React.ElementRef<"div">,
  React.ComponentPropsWithoutRef<"div">
>(({ className, ...props }, ref) => (
  <div ref={ref} className={cn("flex items-center", className)} {...props} />
))
InputOTPGroup.displayName = "InputOTPGroup"

const InputOTPSlot = React.forwardRef<
  React.ElementRef<"div">,
  React.ComponentPropsWithoutRef<"div"> & { index: number }
>(({ index, className, ...props }, ref) => {
  const inputOTPContext = React.useContext(OTPInputContext)
  const { char, hasFakeCaret, isActive } = inputOTPContext.slots[index]

  return (
    <div
      ref={ref}
      className={cn(
        "relative flex h-10 w-10 items-center justify-center border-y border-r border-input text-sm transition-all first:rounded-l-md first:border-l last:rounded-r-md",
        isActive && "z-10 ring-2 ring-ring ring-offset-background",
        className
      )}
      {...props}
    >
      {char}
      {hasFakeCaret && (
        <div className="pointer-events-none absolute inset-0 flex items-center justify-center">
          <div className="h-4 w-px animate-caret-blink bg-foreground duration-1000" />
        </div>
      )}
    </div>
  )
})
InputOTPSlot.displayName = "InputOTPSlot"

const InputOTPSeparator = React.forwardRef<
  React.ElementRef<"div">,
  React.ComponentPropsWithoutRef<"div">
>(({ ...props }, ref) => (
  <div ref={ref} role="separator" {...props}>
    <Dot />
  </div>
))
InputOTPSeparator.displayName = "InputOTPSeparator"

export { InputOTP, InputOTPGroup, InputOTPSlot, InputOTPSeparator }


--------------------------------------------------------------------------------
FILE: components/ui/input.tsx
--------------------------------------------------------------------------------
import * as React from "react"

import { cn } from "@/lib/utils"

const Input = React.forwardRef<HTMLInputElement, React.ComponentProps<"input">>(
  ({ className, type, ...props }, ref) => {
    return (
      <input
        type={type}
        className={cn(
          "flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-base ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium file:text-foreground placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50 md:text-sm",
          className
        )}
        ref={ref}
        {...props}
      />
    )
  }
)
Input.displayName = "Input"

export { Input }


--------------------------------------------------------------------------------
FILE: components/ui/label.tsx
--------------------------------------------------------------------------------
"use client"

import * as React from "react"
import * as LabelPrimitive from "@radix-ui/react-label"
import { cva, type VariantProps } from "class-variance-authority"

import { cn } from "@/lib/utils"

const labelVariants = cva(
  "text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
)

const Label = React.forwardRef<
  React.ElementRef<typeof LabelPrimitive.Root>,
  React.ComponentPropsWithoutRef<typeof LabelPrimitive.Root> &
    VariantProps<typeof labelVariants>
>(({ className, ...props }, ref) => (
  <LabelPrimitive.Root
    ref={ref}
    className={cn(labelVariants(), className)}
    {...props}
  />
))
Label.displayName = LabelPrimitive.Root.displayName

export { Label }


--------------------------------------------------------------------------------
FILE: components/ui/menubar.tsx
--------------------------------------------------------------------------------
"use client"

import * as React from "react"
import * as MenubarPrimitive from "@radix-ui/react-menubar"
import { Check, ChevronRight, Circle } from "lucide-react"

import { cn } from "@/lib/utils"

const MenubarMenu = MenubarPrimitive.Menu

const MenubarGroup = MenubarPrimitive.Group

const MenubarPortal = MenubarPrimitive.Portal

const MenubarSub = MenubarPrimitive.Sub

const MenubarRadioGroup = MenubarPrimitive.RadioGroup

const Menubar = React.forwardRef<
  React.ElementRef<typeof MenubarPrimitive.Root>,
  React.ComponentPropsWithoutRef<typeof MenubarPrimitive.Root>
>(({ className, ...props }, ref) => (
  <MenubarPrimitive.Root
    ref={ref}
    className={cn(
      "flex h-10 items-center space-x-1 rounded-md border bg-background p-1",
      className
    )}
    {...props}
  />
))
Menubar.displayName = MenubarPrimitive.Root.displayName

const MenubarTrigger = React.forwardRef<
  React.ElementRef<typeof MenubarPrimitive.Trigger>,
  React.ComponentPropsWithoutRef<typeof MenubarPrimitive.Trigger>
>(({ className, ...props }, ref) => (
  <MenubarPrimitive.Trigger
    ref={ref}
    className={cn(
      "flex cursor-default select-none items-center rounded-sm px-3 py-1.5 text-sm font-medium outline-none focus:bg-accent focus:text-accent-foreground data-[state=open]:bg-accent data-[state=open]:text-accent-foreground",
      className
    )}
    {...props}
  />
))
MenubarTrigger.displayName = MenubarPrimitive.Trigger.displayName

const MenubarSubTrigger = React.forwardRef<
  React.ElementRef<typeof MenubarPrimitive.SubTrigger>,
  React.ComponentPropsWithoutRef<typeof MenubarPrimitive.SubTrigger> & {
    inset?: boolean
  }
>(({ className, inset, children, ...props }, ref) => (
  <MenubarPrimitive.SubTrigger
    ref={ref}
    className={cn(
      "flex cursor-default select-none items-center rounded-sm px-2 py-1.5 text-sm outline-none focus:bg-accent focus:text-accent-foreground data-[state=open]:bg-accent data-[state=open]:text-accent-foreground",
      inset && "pl-8",
      className
    )}
    {...props}
  >
    {children}
    <ChevronRight className="ml-auto h-4 w-4" />
  </MenubarPrimitive.SubTrigger>
))
MenubarSubTrigger.displayName = MenubarPrimitive.SubTrigger.displayName

const MenubarSubContent = React.forwardRef<
  React.ElementRef<typeof MenubarPrimitive.SubContent>,
  React.ComponentPropsWithoutRef<typeof MenubarPrimitive.SubContent>
>(({ className, ...props }, ref) => (
  <MenubarPrimitive.SubContent
    ref={ref}
    className={cn(
      "z-50 min-w-[8rem] overflow-hidden rounded-md border bg-popover p-1 text-popover-foreground data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2",
      className
    )}
    {...props}
  />
))
MenubarSubContent.displayName = MenubarPrimitive.SubContent.displayName

const MenubarContent = React.forwardRef<
  React.ElementRef<typeof MenubarPrimitive.Content>,
  React.ComponentPropsWithoutRef<typeof MenubarPrimitive.Content>
>(
  (
    { className, align = "start", alignOffset = -4, sideOffset = 8, ...props },
    ref
  ) => (
    <MenubarPrimitive.Portal>
      <MenubarPrimitive.Content
        ref={ref}
        align={align}
        alignOffset={alignOffset}
        sideOffset={sideOffset}
        className={cn(
          "z-50 min-w-[12rem] overflow-hidden rounded-md border bg-popover p-1 text-popover-foreground shadow-md data-[state=open]:animate-in data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2",
          className
        )}
        {...props}
      />
    </MenubarPrimitive.Portal>
  )
)
MenubarContent.displayName = MenubarPrimitive.Content.displayName

const MenubarItem = React.forwardRef<
  React.ElementRef<typeof MenubarPrimitive.Item>,
  React.ComponentPropsWithoutRef<typeof MenubarPrimitive.Item> & {
    inset?: boolean
  }
>(({ className, inset, ...props }, ref) => (
  <MenubarPrimitive.Item
    ref={ref}
    className={cn(
      "relative flex cursor-default select-none items-center rounded-sm px-2 py-1.5 text-sm outline-none focus:bg-accent focus:text-accent-foreground data-[disabled]:pointer-events-none data-[disabled]:opacity-50",
      inset && "pl-8",
      className
    )}
    {...props}
  />
))
MenubarItem.displayName = MenubarPrimitive.Item.displayName

const MenubarCheckboxItem = React.forwardRef<
  React.ElementRef<typeof MenubarPrimitive.CheckboxItem>,
  React.ComponentPropsWithoutRef<typeof MenubarPrimitive.CheckboxItem>
>(({ className, children, checked, ...props }, ref) => (
  <MenubarPrimitive.CheckboxItem
    ref={ref}
    className={cn(
      "relative flex cursor-default select-none items-center rounded-sm py-1.5 pl-8 pr-2 text-sm outline-none focus:bg-accent focus:text-accent-foreground data-[disabled]:pointer-events-none data-[disabled]:opacity-50",
      className
    )}
    checked={checked}
    {...props}
  >
    <span className="absolute left-2 flex h-3.5 w-3.5 items-center justify-center">
      <MenubarPrimitive.ItemIndicator>
        <Check className="h-4 w-4" />
      </MenubarPrimitive.ItemIndicator>
    </span>
    {children}
  </MenubarPrimitive.CheckboxItem>
))
MenubarCheckboxItem.displayName = MenubarPrimitive.CheckboxItem.displayName

const MenubarRadioItem = React.forwardRef<
  React.ElementRef<typeof MenubarPrimitive.RadioItem>,
  React.ComponentPropsWithoutRef<typeof MenubarPrimitive.RadioItem>
>(({ className, children, ...props }, ref) => (
  <MenubarPrimitive.RadioItem
    ref={ref}
    className={cn(
      "relative flex cursor-default select-none items-center rounded-sm py-1.5 pl-8 pr-2 text-sm outline-none focus:bg-accent focus:text-accent-foreground data-[disabled]:pointer-events-none data-[disabled]:opacity-50",
      className
    )}
    {...props}
  >
    <span className="absolute left-2 flex h-3.5 w-3.5 items-center justify-center">
      <MenubarPrimitive.ItemIndicator>
        <Circle className="h-2 w-2 fill-current" />
      </MenubarPrimitive.ItemIndicator>
    </span>
    {children}
  </MenubarPrimitive.RadioItem>
))
MenubarRadioItem.displayName = MenubarPrimitive.RadioItem.displayName

const MenubarLabel = React.forwardRef<
  React.ElementRef<typeof MenubarPrimitive.Label>,
  React.ComponentPropsWithoutRef<typeof MenubarPrimitive.Label> & {
    inset?: boolean
  }
>(({ className, inset, ...props }, ref) => (
  <MenubarPrimitive.Label
    ref={ref}
    className={cn(
      "px-2 py-1.5 text-sm font-semibold",
      inset && "pl-8",
      className
    )}
    {...props}
  />
))
MenubarLabel.displayName = MenubarPrimitive.Label.displayName

const MenubarSeparator = React.forwardRef<
  React.ElementRef<typeof MenubarPrimitive.Separator>,
  React.ComponentPropsWithoutRef<typeof MenubarPrimitive.Separator>
>(({ className, ...props }, ref) => (
  <MenubarPrimitive.Separator
    ref={ref}
    className={cn("-mx-1 my-1 h-px bg-muted", className)}
    {...props}
  />
))
MenubarSeparator.displayName = MenubarPrimitive.Separator.displayName

const MenubarShortcut = ({
  className,
  ...props
}: React.HTMLAttributes<HTMLSpanElement>) => {
  return (
    <span
      className={cn(
        "ml-auto text-xs tracking-widest text-muted-foreground",
        className
      )}
      {...props}
    />
  )
}
MenubarShortcut.displayname = "MenubarShortcut"

export {
  Menubar,
  MenubarMenu,
  MenubarTrigger,
  MenubarContent,
  MenubarItem,
  MenubarSeparator,
  MenubarLabel,
  MenubarCheckboxItem,
  MenubarRadioGroup,
  MenubarRadioItem,
  MenubarPortal,
  MenubarSubContent,
  MenubarSubTrigger,
  MenubarGroup,
  MenubarSub,
  MenubarShortcut,
}


--------------------------------------------------------------------------------
FILE: components/ui/navigation-menu.tsx
--------------------------------------------------------------------------------
import * as React from "react"
import * as NavigationMenuPrimitive from "@radix-ui/react-navigation-menu"
import { cva } from "class-variance-authority"
import { ChevronDown } from "lucide-react"

import { cn } from "@/lib/utils"

const NavigationMenu = React.forwardRef<
  React.ElementRef<typeof NavigationMenuPrimitive.Root>,
  React.ComponentPropsWithoutRef<typeof NavigationMenuPrimitive.Root>
>(({ className, children, ...props }, ref) => (
  <NavigationMenuPrimitive.Root
    ref={ref}
    className={cn(
      "relative z-10 flex max-w-max flex-1 items-center justify-center",
      className
    )}
    {...props}
  >
    {children}
    <NavigationMenuViewport />
  </NavigationMenuPrimitive.Root>
))
NavigationMenu.displayName = NavigationMenuPrimitive.Root.displayName

const NavigationMenuList = React.forwardRef<
  React.ElementRef<typeof NavigationMenuPrimitive.List>,
  React.ComponentPropsWithoutRef<typeof NavigationMenuPrimitive.List>
>(({ className, ...props }, ref) => (
  <NavigationMenuPrimitive.List
    ref={ref}
    className={cn(
      "group flex flex-1 list-none items-center justify-center space-x-1",
      className
    )}
    {...props}
  />
))
NavigationMenuList.displayName = NavigationMenuPrimitive.List.displayName

const NavigationMenuItem = NavigationMenuPrimitive.Item

const navigationMenuTriggerStyle = cva(
  "group inline-flex h-10 w-max items-center justify-center rounded-md bg-background px-4 py-2 text-sm font-medium transition-colors hover:bg-accent hover:text-accent-foreground focus:bg-accent focus:text-accent-foreground focus:outline-none disabled:pointer-events-none disabled:opacity-50 data-[active]:bg-accent/50 data-[state=open]:bg-accent/50"
)

const NavigationMenuTrigger = React.forwardRef<
  React.ElementRef<typeof NavigationMenuPrimitive.Trigger>,
  React.ComponentPropsWithoutRef<typeof NavigationMenuPrimitive.Trigger>
>(({ className, children, ...props }, ref) => (
  <NavigationMenuPrimitive.Trigger
    ref={ref}
    className={cn(navigationMenuTriggerStyle(), "group", className)}
    {...props}
  >
    {children}{" "}
    <ChevronDown
      className="relative top-[1px] ml-1 h-3 w-3 transition duration-200 group-data-[state=open]:rotate-180"
      aria-hidden="true"
    />
  </NavigationMenuPrimitive.Trigger>
))
NavigationMenuTrigger.displayName = NavigationMenuPrimitive.Trigger.displayName

const NavigationMenuContent = React.forwardRef<
  React.ElementRef<typeof NavigationMenuPrimitive.Content>,
  React.ComponentPropsWithoutRef<typeof NavigationMenuPrimitive.Content>
>(({ className, ...props }, ref) => (
  <NavigationMenuPrimitive.Content
    ref={ref}
    className={cn(
      "left-0 top-0 w-full data-[motion^=from-]:animate-in data-[motion^=to-]:animate-out data-[motion^=from-]:fade-in data-[motion^=to-]:fade-out data-[motion=from-end]:slide-in-from-right-52 data-[motion=from-start]:slide-in-from-left-52 data-[motion=to-end]:slide-out-to-right-52 data-[motion=to-start]:slide-out-to-left-52 md:absolute md:w-auto ",
      className
    )}
    {...props}
  />
))
NavigationMenuContent.displayName = NavigationMenuPrimitive.Content.displayName

const NavigationMenuLink = NavigationMenuPrimitive.Link

const NavigationMenuViewport = React.forwardRef<
  React.ElementRef<typeof NavigationMenuPrimitive.Viewport>,
  React.ComponentPropsWithoutRef<typeof NavigationMenuPrimitive.Viewport>
>(({ className, ...props }, ref) => (
  <div className={cn("absolute left-0 top-full flex justify-center")}>
    <NavigationMenuPrimitive.Viewport
      className={cn(
        "origin-top-center relative mt-1.5 h-[var(--radix-navigation-menu-viewport-height)] w-full overflow-hidden rounded-md border bg-popover text-popover-foreground shadow-lg data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-90 md:w-[var(--radix-navigation-menu-viewport-width)]",
        className
      )}
      ref={ref}
      {...props}
    />
  </div>
))
NavigationMenuViewport.displayName =
  NavigationMenuPrimitive.Viewport.displayName

const NavigationMenuIndicator = React.forwardRef<
  React.ElementRef<typeof NavigationMenuPrimitive.Indicator>,
  React.ComponentPropsWithoutRef<typeof NavigationMenuPrimitive.Indicator>
>(({ className, ...props }, ref) => (
  <NavigationMenuPrimitive.Indicator
    ref={ref}
    className={cn(
      "top-full z-[1] flex h-1.5 items-end justify-center overflow-hidden data-[state=visible]:animate-in data-[state=hidden]:animate-out data-[state=hidden]:fade-out data-[state=visible]:fade-in",
      className
    )}
    {...props}
  >
    <div className="relative top-[60%] h-2 w-2 rotate-45 rounded-tl-sm bg-border shadow-md" />
  </NavigationMenuPrimitive.Indicator>
))
NavigationMenuIndicator.displayName =
  NavigationMenuPrimitive.Indicator.displayName

export {
  navigationMenuTriggerStyle,
  NavigationMenu,
  NavigationMenuList,
  NavigationMenuItem,
  NavigationMenuContent,
  NavigationMenuTrigger,
  NavigationMenuLink,
  NavigationMenuIndicator,
  NavigationMenuViewport,
}


--------------------------------------------------------------------------------
FILE: components/ui/pagination.tsx
--------------------------------------------------------------------------------
import * as React from "react"
import { ChevronLeft, ChevronRight, MoreHorizontal } from "lucide-react"

import { cn } from "@/lib/utils"
import { ButtonProps, buttonVariants } from "@/components/ui/button"

const Pagination = ({ className, ...props }: React.ComponentProps<"nav">) => (
  <nav
    role="navigation"
    aria-label="pagination"
    className={cn("mx-auto flex w-full justify-center", className)}
    {...props}
  />
)
Pagination.displayName = "Pagination"

const PaginationContent = React.forwardRef<
  HTMLUListElement,
  React.ComponentProps<"ul">
>(({ className, ...props }, ref) => (
  <ul
    ref={ref}
    className={cn("flex flex-row items-center gap-1", className)}
    {...props}
  />
))
PaginationContent.displayName = "PaginationContent"

const PaginationItem = React.forwardRef<
  HTMLLIElement,
  React.ComponentProps<"li">
>(({ className, ...props }, ref) => (
  <li ref={ref} className={cn("", className)} {...props} />
))
PaginationItem.displayName = "PaginationItem"

type PaginationLinkProps = {
  isActive?: boolean
} & Pick<ButtonProps, "size"> &
  React.ComponentProps<"a">

const PaginationLink = ({
  className,
  isActive,
  size = "icon",
  ...props
}: PaginationLinkProps) => (
  <a
    aria-current={isActive ? "page" : undefined}
    className={cn(
      buttonVariants({
        variant: isActive ? "outline" : "ghost",
        size,
      }),
      className
    )}
    {...props}
  />
)
PaginationLink.displayName = "PaginationLink"

const PaginationPrevious = ({
  className,
  ...props
}: React.ComponentProps<typeof PaginationLink>) => (
  <PaginationLink
    aria-label="Go to previous page"
    size="default"
    className={cn("gap-1 pl-2.5", className)}
    {...props}
  >
    <ChevronLeft className="h-4 w-4" />
    <span>Previous</span>
  </PaginationLink>
)
PaginationPrevious.displayName = "PaginationPrevious"

const PaginationNext = ({
  className,
  ...props
}: React.ComponentProps<typeof PaginationLink>) => (
  <PaginationLink
    aria-label="Go to next page"
    size="default"
    className={cn("gap-1 pr-2.5", className)}
    {...props}
  >
    <span>Next</span>
    <ChevronRight className="h-4 w-4" />
  </PaginationLink>
)
PaginationNext.displayName = "PaginationNext"

const PaginationEllipsis = ({
  className,
  ...props
}: React.ComponentProps<"span">) => (
  <span
    aria-hidden
    className={cn("flex h-9 w-9 items-center justify-center", className)}
    {...props}
  >
    <MoreHorizontal className="h-4 w-4" />
    <span className="sr-only">More pages</span>
  </span>
)
PaginationEllipsis.displayName = "PaginationEllipsis"

export {
  Pagination,
  PaginationContent,
  PaginationEllipsis,
  PaginationItem,
  PaginationLink,
  PaginationNext,
  PaginationPrevious,
}


--------------------------------------------------------------------------------
FILE: components/ui/popover.tsx
--------------------------------------------------------------------------------
"use client"

import * as React from "react"
import * as PopoverPrimitive from "@radix-ui/react-popover"

import { cn } from "@/lib/utils"

const Popover = PopoverPrimitive.Root

const PopoverTrigger = PopoverPrimitive.Trigger

const PopoverContent = React.forwardRef<
  React.ElementRef<typeof PopoverPrimitive.Content>,
  React.ComponentPropsWithoutRef<typeof PopoverPrimitive.Content>
>(({ className, align = "center", sideOffset = 4, ...props }, ref) => (
  <PopoverPrimitive.Portal>
    <PopoverPrimitive.Content
      ref={ref}
      align={align}
      sideOffset={sideOffset}
      className={cn(
        "z-50 w-72 rounded-md border bg-popover p-4 text-popover-foreground shadow-md outline-none data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2",
        className
      )}
      {...props}
    />
  </PopoverPrimitive.Portal>
))
PopoverContent.displayName = PopoverPrimitive.Content.displayName

export { Popover, PopoverTrigger, PopoverContent }


--------------------------------------------------------------------------------
FILE: components/ui/progress.tsx
--------------------------------------------------------------------------------
"use client"

import * as React from "react"
import * as ProgressPrimitive from "@radix-ui/react-progress"

import { cn } from "@/lib/utils"

const Progress = React.forwardRef<
  React.ElementRef<typeof ProgressPrimitive.Root>,
  React.ComponentPropsWithoutRef<typeof ProgressPrimitive.Root>
>(({ className, value, ...props }, ref) => (
  <ProgressPrimitive.Root
    ref={ref}
    className={cn(
      "relative h-4 w-full overflow-hidden rounded-full bg-secondary",
      className
    )}
    {...props}
  >
    <ProgressPrimitive.Indicator
      className="h-full w-full flex-1 bg-primary transition-all"
      style={{ transform: `translateX(-${100 - (value || 0)}%)` }}
    />
  </ProgressPrimitive.Root>
))
Progress.displayName = ProgressPrimitive.Root.displayName

export { Progress }


--------------------------------------------------------------------------------
FILE: components/ui/radio-group.tsx
--------------------------------------------------------------------------------
"use client"

import * as React from "react"
import * as RadioGroupPrimitive from "@radix-ui/react-radio-group"
import { Circle } from "lucide-react"

import { cn } from "@/lib/utils"

const RadioGroup = React.forwardRef<
  React.ElementRef<typeof RadioGroupPrimitive.Root>,
  React.ComponentPropsWithoutRef<typeof RadioGroupPrimitive.Root>
>(({ className, ...props }, ref) => {
  return (
    <RadioGroupPrimitive.Root
      className={cn("grid gap-2", className)}
      {...props}
      ref={ref}
    />
  )
})
RadioGroup.displayName = RadioGroupPrimitive.Root.displayName

const RadioGroupItem = React.forwardRef<
  React.ElementRef<typeof RadioGroupPrimitive.Item>,
  React.ComponentPropsWithoutRef<typeof RadioGroupPrimitive.Item>
>(({ className, ...props }, ref) => {
  return (
    <RadioGroupPrimitive.Item
      ref={ref}
      className={cn(
        "aspect-square h-4 w-4 rounded-full border border-primary text-primary ring-offset-background focus:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50",
        className
      )}
      {...props}
    >
      <RadioGroupPrimitive.Indicator className="flex items-center justify-center">
        <Circle className="h-2.5 w-2.5 fill-current text-current" />
      </RadioGroupPrimitive.Indicator>
    </RadioGroupPrimitive.Item>
  )
})
RadioGroupItem.displayName = RadioGroupPrimitive.Item.displayName

export { RadioGroup, RadioGroupItem }


--------------------------------------------------------------------------------
FILE: components/ui/resizable.tsx
--------------------------------------------------------------------------------
"use client"

import { GripVertical } from "lucide-react"
import * as ResizablePrimitive from "react-resizable-panels"

import { cn } from "@/lib/utils"

const ResizablePanelGroup = ({
  className,
  ...props
}: React.ComponentProps<typeof ResizablePrimitive.PanelGroup>) => (
  <ResizablePrimitive.PanelGroup
    className={cn(
      "flex h-full w-full data-[panel-group-direction=vertical]:flex-col",
      className
    )}
    {...props}
  />
)

const ResizablePanel = ResizablePrimitive.Panel

const ResizableHandle = ({
  withHandle,
  className,
  ...props
}: React.ComponentProps<typeof ResizablePrimitive.PanelResizeHandle> & {
  withHandle?: boolean
}) => (
  <ResizablePrimitive.PanelResizeHandle
    className={cn(
      "relative flex w-px items-center justify-center bg-border after:absolute after:inset-y-0 after:left-1/2 after:w-1 after:-translate-x-1/2 focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring focus-visible:ring-offset-1 data-[panel-group-direction=vertical]:h-px data-[panel-group-direction=vertical]:w-full data-[panel-group-direction=vertical]:after:left-0 data-[panel-group-direction=vertical]:after:h-1 data-[panel-group-direction=vertical]:after:w-full data-[panel-group-direction=vertical]:after:-translate-y-1/2 data-[panel-group-direction=vertical]:after:translate-x-0 [&[data-panel-group-direction=vertical]>div]:rotate-90",
      className
    )}
    {...props}
  >
    {withHandle && (
      <div className="z-10 flex h-4 w-3 items-center justify-center rounded-sm border bg-border">
        <GripVertical className="h-2.5 w-2.5" />
      </div>
    )}
  </ResizablePrimitive.PanelResizeHandle>
)

export { ResizablePanelGroup, ResizablePanel, ResizableHandle }


--------------------------------------------------------------------------------
FILE: components/ui/scroll-area.tsx
--------------------------------------------------------------------------------
"use client"

import * as React from "react"
import * as ScrollAreaPrimitive from "@radix-ui/react-scroll-area"

import { cn } from "@/lib/utils"

const ScrollArea = React.forwardRef<
  React.ElementRef<typeof ScrollAreaPrimitive.Root>,
  React.ComponentPropsWithoutRef<typeof ScrollAreaPrimitive.Root>
>(({ className, children, ...props }, ref) => (
  <ScrollAreaPrimitive.Root
    ref={ref}
    className={cn("relative overflow-hidden", className)}
    {...props}
  >
    <ScrollAreaPrimitive.Viewport className="h-full w-full rounded-[inherit]">
      {children}
    </ScrollAreaPrimitive.Viewport>
    <ScrollBar />
    <ScrollAreaPrimitive.Corner />
  </ScrollAreaPrimitive.Root>
))
ScrollArea.displayName = ScrollAreaPrimitive.Root.displayName

const ScrollBar = React.forwardRef<
  React.ElementRef<typeof ScrollAreaPrimitive.ScrollAreaScrollbar>,
  React.ComponentPropsWithoutRef<typeof ScrollAreaPrimitive.ScrollAreaScrollbar>
>(({ className, orientation = "vertical", ...props }, ref) => (
  <ScrollAreaPrimitive.ScrollAreaScrollbar
    ref={ref}
    orientation={orientation}
    className={cn(
      "flex touch-none select-none transition-colors",
      orientation === "vertical" &&
        "h-full w-2.5 border-l border-l-transparent p-[1px]",
      orientation === "horizontal" &&
        "h-2.5 flex-col border-t border-t-transparent p-[1px]",
      className
    )}
    {...props}
  >
    <ScrollAreaPrimitive.ScrollAreaThumb className="relative flex-1 rounded-full bg-border" />
  </ScrollAreaPrimitive.ScrollAreaScrollbar>
))
ScrollBar.displayName = ScrollAreaPrimitive.ScrollAreaScrollbar.displayName

export { ScrollArea, ScrollBar }


--------------------------------------------------------------------------------
FILE: components/ui/select.tsx
--------------------------------------------------------------------------------
"use client"

import * as React from "react"
import * as SelectPrimitive from "@radix-ui/react-select"
import { Check, ChevronDown, ChevronUp } from "lucide-react"

import { cn } from "@/lib/utils"

const Select = SelectPrimitive.Root

const SelectGroup = SelectPrimitive.Group

const SelectValue = SelectPrimitive.Value

const SelectTrigger = React.forwardRef<
  React.ElementRef<typeof SelectPrimitive.Trigger>,
  React.ComponentPropsWithoutRef<typeof SelectPrimitive.Trigger>
>(({ className, children, ...props }, ref) => (
  <SelectPrimitive.Trigger
    ref={ref}
    className={cn(
      "flex h-10 w-full items-center justify-between rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background placeholder:text-muted-foreground focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50 [&>span]:line-clamp-1",
      className
    )}
    {...props}
  >
    {children}
    <SelectPrimitive.Icon asChild>
      <ChevronDown className="h-4 w-4 opacity-50" />
    </SelectPrimitive.Icon>
  </SelectPrimitive.Trigger>
))
SelectTrigger.displayName = SelectPrimitive.Trigger.displayName

const SelectScrollUpButton = React.forwardRef<
  React.ElementRef<typeof SelectPrimitive.ScrollUpButton>,
  React.ComponentPropsWithoutRef<typeof SelectPrimitive.ScrollUpButton>
>(({ className, ...props }, ref) => (
  <SelectPrimitive.ScrollUpButton
    ref={ref}
    className={cn(
      "flex cursor-default items-center justify-center py-1",
      className
    )}
    {...props}
  >
    <ChevronUp className="h-4 w-4" />
  </SelectPrimitive.ScrollUpButton>
))
SelectScrollUpButton.displayName = SelectPrimitive.ScrollUpButton.displayName

const SelectScrollDownButton = React.forwardRef<
  React.ElementRef<typeof SelectPrimitive.ScrollDownButton>,
  React.ComponentPropsWithoutRef<typeof SelectPrimitive.ScrollDownButton>
>(({ className, ...props }, ref) => (
  <SelectPrimitive.ScrollDownButton
    ref={ref}
    className={cn(
      "flex cursor-default items-center justify-center py-1",
      className
    )}
    {...props}
  >
    <ChevronDown className="h-4 w-4" />
  </SelectPrimitive.ScrollDownButton>
))
SelectScrollDownButton.displayName =
  SelectPrimitive.ScrollDownButton.displayName

const SelectContent = React.forwardRef<
  React.ElementRef<typeof SelectPrimitive.Content>,
  React.ComponentPropsWithoutRef<typeof SelectPrimitive.Content>
>(({ className, children, position = "popper", ...props }, ref) => (
  <SelectPrimitive.Portal>
    <SelectPrimitive.Content
      ref={ref}
      className={cn(
        "relative z-50 max-h-96 min-w-[8rem] overflow-hidden rounded-md border bg-popover text-popover-foreground shadow-md data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2",
        position === "popper" &&
          "data-[side=bottom]:translate-y-1 data-[side=left]:-translate-x-1 data-[side=right]:translate-x-1 data-[side=top]:-translate-y-1",
        className
      )}
      position={position}
      {...props}
    >
      <SelectScrollUpButton />
      <SelectPrimitive.Viewport
        className={cn(
          "p-1",
          position === "popper" &&
            "h-[var(--radix-select-trigger-height)] w-full min-w-[var(--radix-select-trigger-width)]"
        )}
      >
        {children}
      </SelectPrimitive.Viewport>
      <SelectScrollDownButton />
    </SelectPrimitive.Content>
  </SelectPrimitive.Portal>
))
SelectContent.displayName = SelectPrimitive.Content.displayName

const SelectLabel = React.forwardRef<
  React.ElementRef<typeof SelectPrimitive.Label>,
  React.ComponentPropsWithoutRef<typeof SelectPrimitive.Label>
>(({ className, ...props }, ref) => (
  <SelectPrimitive.Label
    ref={ref}
    className={cn("py-1.5 pl-8 pr-2 text-sm font-semibold", className)}
    {...props}
  />
))
SelectLabel.displayName = SelectPrimitive.Label.displayName

const SelectItem = React.forwardRef<
  React.ElementRef<typeof SelectPrimitive.Item>,
  React.ComponentPropsWithoutRef<typeof SelectPrimitive.Item>
>(({ className, children, ...props }, ref) => (
  <SelectPrimitive.Item
    ref={ref}
    className={cn(
      "relative flex w-full cursor-default select-none items-center rounded-sm py-1.5 pl-8 pr-2 text-sm outline-none focus:bg-accent focus:text-accent-foreground data-[disabled]:pointer-events-none data-[disabled]:opacity-50",
      className
    )}
    {...props}
  >
    <span className="absolute left-2 flex h-3.5 w-3.5 items-center justify-center">
      <SelectPrimitive.ItemIndicator>
        <Check className="h-4 w-4" />
      </SelectPrimitive.ItemIndicator>
    </span>

    <SelectPrimitive.ItemText>{children}</SelectPrimitive.ItemText>
  </SelectPrimitive.Item>
))
SelectItem.displayName = SelectPrimitive.Item.displayName

const SelectSeparator = React.forwardRef<
  React.ElementRef<typeof SelectPrimitive.Separator>,
  React.ComponentPropsWithoutRef<typeof SelectPrimitive.Separator>
>(({ className, ...props }, ref) => (
  <SelectPrimitive.Separator
    ref={ref}
    className={cn("-mx-1 my-1 h-px bg-muted", className)}
    {...props}
  />
))
SelectSeparator.displayName = SelectPrimitive.Separator.displayName

export {
  Select,
  SelectGroup,
  SelectValue,
  SelectTrigger,
  SelectContent,
  SelectLabel,
  SelectItem,
  SelectSeparator,
  SelectScrollUpButton,
  SelectScrollDownButton,
}


--------------------------------------------------------------------------------
FILE: components/ui/separator.tsx
--------------------------------------------------------------------------------
"use client"

import * as React from "react"
import * as SeparatorPrimitive from "@radix-ui/react-separator"

import { cn } from "@/lib/utils"

const Separator = React.forwardRef<
  React.ElementRef<typeof SeparatorPrimitive.Root>,
  React.ComponentPropsWithoutRef<typeof SeparatorPrimitive.Root>
>(
  (
    { className, orientation = "horizontal", decorative = true, ...props },
    ref
  ) => (
    <SeparatorPrimitive.Root
      ref={ref}
      decorative={decorative}
      orientation={orientation}
      className={cn(
        "shrink-0 bg-border",
        orientation === "horizontal" ? "h-[1px] w-full" : "h-full w-[1px]",
        className
      )}
      {...props}
    />
  )
)
Separator.displayName = SeparatorPrimitive.Root.displayName

export { Separator }


--------------------------------------------------------------------------------
FILE: components/ui/sheet.tsx
--------------------------------------------------------------------------------
"use client"

import * as React from "react"
import * as SheetPrimitive from "@radix-ui/react-dialog"
import { cva, type VariantProps } from "class-variance-authority"
import { X } from "lucide-react"

import { cn } from "@/lib/utils"

const Sheet = SheetPrimitive.Root

const SheetTrigger = SheetPrimitive.Trigger

const SheetClose = SheetPrimitive.Close

const SheetPortal = SheetPrimitive.Portal

const SheetOverlay = React.forwardRef<
  React.ElementRef<typeof SheetPrimitive.Overlay>,
  React.ComponentPropsWithoutRef<typeof SheetPrimitive.Overlay>
>(({ className, ...props }, ref) => (
  <SheetPrimitive.Overlay
    className={cn(
      "fixed inset-0 z-50 bg-black/80  data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0",
      className
    )}
    {...props}
    ref={ref}
  />
))
SheetOverlay.displayName = SheetPrimitive.Overlay.displayName

const sheetVariants = cva(
  "fixed z-50 gap-4 bg-background p-6 shadow-lg transition ease-in-out data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:duration-300 data-[state=open]:duration-500",
  {
    variants: {
      side: {
        top: "inset-x-0 top-0 border-b data-[state=closed]:slide-out-to-top data-[state=open]:slide-in-from-top",
        bottom:
          "inset-x-0 bottom-0 border-t data-[state=closed]:slide-out-to-bottom data-[state=open]:slide-in-from-bottom",
        left: "inset-y-0 left-0 h-full w-3/4 border-r data-[state=closed]:slide-out-to-left data-[state=open]:slide-in-from-left sm:max-w-sm",
        right:
          "inset-y-0 right-0 h-full w-3/4  border-l data-[state=closed]:slide-out-to-right data-[state=open]:slide-in-from-right sm:max-w-sm",
      },
    },
    defaultVariants: {
      side: "right",
    },
  }
)

interface SheetContentProps
  extends React.ComponentPropsWithoutRef<typeof SheetPrimitive.Content>,
    VariantProps<typeof sheetVariants> {}

const SheetContent = React.forwardRef<
  React.ElementRef<typeof SheetPrimitive.Content>,
  SheetContentProps
>(({ side = "right", className, children, ...props }, ref) => (
  <SheetPortal>
    <SheetOverlay />
    <SheetPrimitive.Content
      ref={ref}
      className={cn(sheetVariants({ side }), className)}
      {...props}
    >
      {children}
      <SheetPrimitive.Close className="absolute right-4 top-4 rounded-sm opacity-70 ring-offset-background transition-opacity hover:opacity-100 focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2 disabled:pointer-events-none data-[state=open]:bg-secondary">
        <X className="h-4 w-4" />
        <span className="sr-only">Close</span>
      </SheetPrimitive.Close>
    </SheetPrimitive.Content>
  </SheetPortal>
))
SheetContent.displayName = SheetPrimitive.Content.displayName

const SheetHeader = ({
  className,
  ...props
}: React.HTMLAttributes<HTMLDivElement>) => (
  <div
    className={cn(
      "flex flex-col space-y-2 text-center sm:text-left",
      className
    )}
    {...props}
  />
)
SheetHeader.displayName = "SheetHeader"

const SheetFooter = ({
  className,
  ...props
}: React.HTMLAttributes<HTMLDivElement>) => (
  <div
    className={cn(
      "flex flex-col-reverse sm:flex-row sm:justify-end sm:space-x-2",
      className
    )}
    {...props}
  />
)
SheetFooter.displayName = "SheetFooter"

const SheetTitle = React.forwardRef<
  React.ElementRef<typeof SheetPrimitive.Title>,
  React.ComponentPropsWithoutRef<typeof SheetPrimitive.Title>
>(({ className, ...props }, ref) => (
  <SheetPrimitive.Title
    ref={ref}
    className={cn("text-lg font-semibold text-foreground", className)}
    {...props}
  />
))
SheetTitle.displayName = SheetPrimitive.Title.displayName

const SheetDescription = React.forwardRef<
  React.ElementRef<typeof SheetPrimitive.Description>,
  React.ComponentPropsWithoutRef<typeof SheetPrimitive.Description>
>(({ className, ...props }, ref) => (
  <SheetPrimitive.Description
    ref={ref}
    className={cn("text-sm text-muted-foreground", className)}
    {...props}
  />
))
SheetDescription.displayName = SheetPrimitive.Description.displayName

export {
  Sheet,
  SheetPortal,
  SheetOverlay,
  SheetTrigger,
  SheetClose,
  SheetContent,
  SheetHeader,
  SheetFooter,
  SheetTitle,
  SheetDescription,
}


--------------------------------------------------------------------------------
FILE: components/ui/sidebar.tsx
--------------------------------------------------------------------------------
"use client"

import * as React from "react"
import { Slot } from "@radix-ui/react-slot"
import { VariantProps, cva } from "class-variance-authority"
import { PanelLeft } from "lucide-react"

import { useIsMobile } from "@/hooks/use-mobile"
import { cn } from "@/lib/utils"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Separator } from "@/components/ui/separator"
import { Sheet, SheetContent } from "@/components/ui/sheet"
import { Skeleton } from "@/components/ui/skeleton"
import {
  Tooltip,
  TooltipContent,
  TooltipProvider,
  TooltipTrigger,
} from "@/components/ui/tooltip"

const SIDEBAR_COOKIE_NAME = "sidebar:state"
const SIDEBAR_COOKIE_MAX_AGE = 60 * 60 * 24 * 7
const SIDEBAR_WIDTH = "16rem"
const SIDEBAR_WIDTH_MOBILE = "18rem"
const SIDEBAR_WIDTH_ICON = "3rem"
const SIDEBAR_KEYBOARD_SHORTCUT = "b"

type SidebarContext = {
  state: "expanded" | "collapsed"
  open: boolean
  setOpen: (open: boolean) => void
  openMobile: boolean
  setOpenMobile: (open: boolean) => void
  isMobile: boolean
  toggleSidebar: () => void
}

const SidebarContext = React.createContext<SidebarContext | null>(null)

function useSidebar() {
  const context = React.useContext(SidebarContext)
  if (!context) {
    throw new Error("useSidebar must be used within a SidebarProvider.")
  }

  return context
}

const SidebarProvider = React.forwardRef<
  HTMLDivElement,
  React.ComponentProps<"div"> & {
    defaultOpen?: boolean
    open?: boolean
    onOpenChange?: (open: boolean) => void
  }
>(
  (
    {
      defaultOpen = true,
      open: openProp,
      onOpenChange: setOpenProp,
      className,
      style,
      children,
      ...props
    },
    ref
  ) => {
    const isMobile = useIsMobile()
    const [openMobile, setOpenMobile] = React.useState(false)

    // This is the internal state of the sidebar.
    // We use openProp and setOpenProp for control from outside the component.
    const [_open, _setOpen] = React.useState(defaultOpen)
    const open = openProp ?? _open
    const setOpen = React.useCallback(
      (value: boolean | ((value: boolean) => boolean)) => {
        const openState = typeof value === "function" ? value(open) : value
        if (setOpenProp) {
          setOpenProp(openState)
        } else {
          _setOpen(openState)
        }

        // This sets the cookie to keep the sidebar state.
        document.cookie = `${SIDEBAR_COOKIE_NAME}=${openState}; path=/; max-age=${SIDEBAR_COOKIE_MAX_AGE}`
      },
      [setOpenProp, open]
    )

    // Helper to toggle the sidebar.
    const toggleSidebar = React.useCallback(() => {
      return isMobile
        ? setOpenMobile((open) => !open)
        : setOpen((open) => !open)
    }, [isMobile, setOpen, setOpenMobile])

    // Adds a keyboard shortcut to toggle the sidebar.
    React.useEffect(() => {
      const handleKeyDown = (event: KeyboardEvent) => {
        if (
          event.key === SIDEBAR_KEYBOARD_SHORTCUT &&
          (event.metaKey || event.ctrlKey)
        ) {
          event.preventDefault()
          toggleSidebar()
        }
      }

      window.addEventListener("keydown", handleKeyDown)
      return () => window.removeEventListener("keydown", handleKeyDown)
    }, [toggleSidebar])

    // We add a state so that we can do data-state="expanded" or "collapsed".
    // This makes it easier to style the sidebar with Tailwind classes.
    const state = open ? "expanded" : "collapsed"

    const contextValue = React.useMemo<SidebarContext>(
      () => ({
        state,
        open,
        setOpen,
        isMobile,
        openMobile,
        setOpenMobile,
        toggleSidebar,
      }),
      [state, open, setOpen, isMobile, openMobile, setOpenMobile, toggleSidebar]
    )

    return (
      <SidebarContext.Provider value={contextValue}>
        <TooltipProvider delayDuration={0}>
          <div
            style={
              {
                "--sidebar-width": SIDEBAR_WIDTH,
                "--sidebar-width-icon": SIDEBAR_WIDTH_ICON,
                ...style,
              } as React.CSSProperties
            }
            className={cn(
              "group/sidebar-wrapper flex min-h-svh w-full has-[[data-variant=inset]]:bg-sidebar",
              className
            )}
            ref={ref}
            {...props}
          >
            {children}
          </div>
        </TooltipProvider>
      </SidebarContext.Provider>
    )
  }
)
SidebarProvider.displayName = "SidebarProvider"

const Sidebar = React.forwardRef<
  HTMLDivElement,
  React.ComponentProps<"div"> & {
    side?: "left" | "right"
    variant?: "sidebar" | "floating" | "inset"
    collapsible?: "offcanvas" | "icon" | "none"
  }
>(
  (
    {
      side = "left",
      variant = "sidebar",
      collapsible = "offcanvas",
      className,
      children,
      ...props
    },
    ref
  ) => {
    const { isMobile, state, openMobile, setOpenMobile } = useSidebar()

    if (collapsible === "none") {
      return (
        <div
          className={cn(
            "flex h-full w-[--sidebar-width] flex-col bg-sidebar text-sidebar-foreground",
            className
          )}
          ref={ref}
          {...props}
        >
          {children}
        </div>
      )
    }

    if (isMobile) {
      return (
        <Sheet open={openMobile} onOpenChange={setOpenMobile} {...props}>
          <SheetContent
            data-sidebar="sidebar"
            data-mobile="true"
            className="w-[--sidebar-width] bg-sidebar p-0 text-sidebar-foreground [&>button]:hidden"
            style={
              {
                "--sidebar-width": SIDEBAR_WIDTH_MOBILE,
              } as React.CSSProperties
            }
            side={side}
          >
            <div className="flex h-full w-full flex-col">{children}</div>
          </SheetContent>
        </Sheet>
      )
    }

    return (
      <div
        ref={ref}
        className="group peer hidden md:block text-sidebar-foreground"
        data-state={state}
        data-collapsible={state === "collapsed" ? collapsible : ""}
        data-variant={variant}
        data-side={side}
      >
        {/* This is what handles the sidebar gap on desktop */}
        <div
          className={cn(
            "duration-200 relative h-svh w-[--sidebar-width] bg-transparent transition-[width] ease-linear",
            "group-data-[collapsible=offcanvas]:w-0",
            "group-data-[side=right]:rotate-180",
            variant === "floating" || variant === "inset"
              ? "group-data-[collapsible=icon]:w-[calc(var(--sidebar-width-icon)_+_theme(spacing.4))]"
              : "group-data-[collapsible=icon]:w-[--sidebar-width-icon]"
          )}
        />
        <div
          className={cn(
            "duration-200 fixed inset-y-0 z-10 hidden h-svh w-[--sidebar-width] transition-[left,right,width] ease-linear md:flex",
            side === "left"
              ? "left-0 group-data-[collapsible=offcanvas]:left-[calc(var(--sidebar-width)*-1)]"
              : "right-0 group-data-[collapsible=offcanvas]:right-[calc(var(--sidebar-width)*-1)]",
            // Adjust the padding for floating and inset variants.
            variant === "floating" || variant === "inset"
              ? "p-2 group-data-[collapsible=icon]:w-[calc(var(--sidebar-width-icon)_+_theme(spacing.4)_+2px)]"
              : "group-data-[collapsible=icon]:w-[--sidebar-width-icon] group-data-[side=left]:border-r group-data-[side=right]:border-l",
            className
          )}
          {...props}
        >
          <div
            data-sidebar="sidebar"
            className="flex h-full w-full flex-col bg-sidebar group-data-[variant=floating]:rounded-lg group-data-[variant=floating]:border group-data-[variant=floating]:border-sidebar-border group-data-[variant=floating]:shadow"
          >
            {children}
          </div>
        </div>
      </div>
    )
  }
)
Sidebar.displayName = "Sidebar"

const SidebarTrigger = React.forwardRef<
  React.ElementRef<typeof Button>,
  React.ComponentProps<typeof Button>
>(({ className, onClick, ...props }, ref) => {
  const { toggleSidebar } = useSidebar()

  return (
    <Button
      ref={ref}
      data-sidebar="trigger"
      variant="ghost"
      size="icon"
      className={cn("h-7 w-7", className)}
      onClick={(event) => {
        onClick?.(event)
        toggleSidebar()
      }}
      {...props}
    >
      <PanelLeft />
      <span className="sr-only">Toggle Sidebar</span>
    </Button>
  )
})
SidebarTrigger.displayName = "SidebarTrigger"

const SidebarRail = React.forwardRef<
  HTMLButtonElement,
  React.ComponentProps<"button">
>(({ className, ...props }, ref) => {
  const { toggleSidebar } = useSidebar()

  return (
    <button
      ref={ref}
      data-sidebar="rail"
      aria-label="Toggle Sidebar"
      tabIndex={-1}
      onClick={toggleSidebar}
      title="Toggle Sidebar"
      className={cn(
        "absolute inset-y-0 z-20 hidden w-4 -translate-x-1/2 transition-all ease-linear after:absolute after:inset-y-0 after:left-1/2 after:w-[2px] hover:after:bg-sidebar-border group-data-[side=left]:-right-4 group-data-[side=right]:left-0 sm:flex",
        "[[data-side=left]_&]:cursor-w-resize [[data-side=right]_&]:cursor-e-resize",
        "[[data-side=left][data-state=collapsed]_&]:cursor-e-resize [[data-side=right][data-state=collapsed]_&]:cursor-w-resize",
        "group-data-[collapsible=offcanvas]:translate-x-0 group-data-[collapsible=offcanvas]:after:left-full group-data-[collapsible=offcanvas]:hover:bg-sidebar",
        "[[data-side=left][data-collapsible=offcanvas]_&]:-right-2",
        "[[data-side=right][data-collapsible=offcanvas]_&]:-left-2",
        className
      )}
      {...props}
    />
  )
})
SidebarRail.displayName = "SidebarRail"

const SidebarInset = React.forwardRef<
  HTMLDivElement,
  React.ComponentProps<"main">
>(({ className, ...props }, ref) => {
  return (
    <main
      ref={ref}
      className={cn(
        "relative flex min-h-svh flex-1 flex-col bg-background",
        "peer-data-[variant=inset]:min-h-[calc(100svh-theme(spacing.4))] md:peer-data-[variant=inset]:m-2 md:peer-data-[state=collapsed]:peer-data-[variant=inset]:ml-2 md:peer-data-[variant=inset]:ml-0 md:peer-data-[variant=inset]:rounded-xl md:peer-data-[variant=inset]:shadow",
        className
      )}
      {...props}
    />
  )
})
SidebarInset.displayName = "SidebarInset"

const SidebarInput = React.forwardRef<
  React.ElementRef<typeof Input>,
  React.ComponentProps<typeof Input>
>(({ className, ...props }, ref) => {
  return (
    <Input
      ref={ref}
      data-sidebar="input"
      className={cn(
        "h-8 w-full bg-background shadow-none focus-visible:ring-2 focus-visible:ring-sidebar-ring",
        className
      )}
      {...props}
    />
  )
})
SidebarInput.displayName = "SidebarInput"

const SidebarHeader = React.forwardRef<
  HTMLDivElement,
  React.ComponentProps<"div">
>(({ className, ...props }, ref) => {
  return (
    <div
      ref={ref}
      data-sidebar="header"
      className={cn("flex flex-col gap-2 p-2", className)}
      {...props}
    />
  )
})
SidebarHeader.displayName = "SidebarHeader"

const SidebarFooter = React.forwardRef<
  HTMLDivElement,
  React.ComponentProps<"div">
>(({ className, ...props }, ref) => {
  return (
    <div
      ref={ref}
      data-sidebar="footer"
      className={cn("flex flex-col gap-2 p-2", className)}
      {...props}
    />
  )
})
SidebarFooter.displayName = "SidebarFooter"

const SidebarSeparator = React.forwardRef<
  React.ElementRef<typeof Separator>,
  React.ComponentProps<typeof Separator>
>(({ className, ...props }, ref) => {
  return (
    <Separator
      ref={ref}
      data-sidebar="separator"
      className={cn("mx-2 w-auto bg-sidebar-border", className)}
      {...props}
    />
  )
})
SidebarSeparator.displayName = "SidebarSeparator"

const SidebarContent = React.forwardRef<
  HTMLDivElement,
  React.ComponentProps<"div">
>(({ className, ...props }, ref) => {
  return (
    <div
      ref={ref}
      data-sidebar="content"
      className={cn(
        "flex min-h-0 flex-1 flex-col gap-2 overflow-auto group-data-[collapsible=icon]:overflow-hidden",
        className
      )}
      {...props}
    />
  )
})
SidebarContent.displayName = "SidebarContent"

const SidebarGroup = React.forwardRef<
  HTMLDivElement,
  React.ComponentProps<"div">
>(({ className, ...props }, ref) => {
  return (
    <div
      ref={ref}
      data-sidebar="group"
      className={cn("relative flex w-full min-w-0 flex-col p-2", className)}
      {...props}
    />
  )
})
SidebarGroup.displayName = "SidebarGroup"

const SidebarGroupLabel = React.forwardRef<
  HTMLDivElement,
  React.ComponentProps<"div"> & { asChild?: boolean }
>(({ className, asChild = false, ...props }, ref) => {
  const Comp = asChild ? Slot : "div"

  return (
    <Comp
      ref={ref}
      data-sidebar="group-label"
      className={cn(
        "duration-200 flex h-8 shrink-0 items-center rounded-md px-2 text-xs font-medium text-sidebar-foreground/70 outline-none ring-sidebar-ring transition-[margin,opa] ease-linear focus-visible:ring-2 [&>svg]:size-4 [&>svg]:shrink-0",
        "group-data-[collapsible=icon]:-mt-8 group-data-[collapsible=icon]:opacity-0",
        className
      )}
      {...props}
    />
  )
})
SidebarGroupLabel.displayName = "SidebarGroupLabel"

const SidebarGroupAction = React.forwardRef<
  HTMLButtonElement,
  React.ComponentProps<"button"> & { asChild?: boolean }
>(({ className, asChild = false, ...props }, ref) => {
  const Comp = asChild ? Slot : "button"

  return (
    <Comp
      ref={ref}
      data-sidebar="group-action"
      className={cn(
        "absolute right-3 top-3.5 flex aspect-square w-5 items-center justify-center rounded-md p-0 text-sidebar-foreground outline-none ring-sidebar-ring transition-transform hover:bg-sidebar-accent hover:text-sidebar-accent-foreground focus-visible:ring-2 [&>svg]:size-4 [&>svg]:shrink-0",
        // Increases the hit area of the button on mobile.
        "after:absolute after:-inset-2 after:md:hidden",
        "group-data-[collapsible=icon]:hidden",
        className
      )}
      {...props}
    />
  )
})
SidebarGroupAction.displayName = "SidebarGroupAction"

const SidebarGroupContent = React.forwardRef<
  HTMLDivElement,
  React.ComponentProps<"div">
>(({ className, ...props }, ref) => (
  <div
    ref={ref}
    data-sidebar="group-content"
    className={cn("w-full text-sm", className)}
    {...props}
  />
))
SidebarGroupContent.displayName = "SidebarGroupContent"

const SidebarMenu = React.forwardRef<
  HTMLUListElement,
  React.ComponentProps<"ul">
>(({ className, ...props }, ref) => (
  <ul
    ref={ref}
    data-sidebar="menu"
    className={cn("flex w-full min-w-0 flex-col gap-1", className)}
    {...props}
  />
))
SidebarMenu.displayName = "SidebarMenu"

const SidebarMenuItem = React.forwardRef<
  HTMLLIElement,
  React.ComponentProps<"li">
>(({ className, ...props }, ref) => (
  <li
    ref={ref}
    data-sidebar="menu-item"
    className={cn("group/menu-item relative", className)}
    {...props}
  />
))
SidebarMenuItem.displayName = "SidebarMenuItem"

const sidebarMenuButtonVariants = cva(
  "peer/menu-button flex w-full items-center gap-2 overflow-hidden rounded-md p-2 text-left text-sm outline-none ring-sidebar-ring transition-[width,height,padding] hover:bg-sidebar-accent hover:text-sidebar-accent-foreground focus-visible:ring-2 active:bg-sidebar-accent active:text-sidebar-accent-foreground disabled:pointer-events-none disabled:opacity-50 group-has-[[data-sidebar=menu-action]]/menu-item:pr-8 aria-disabled:pointer-events-none aria-disabled:opacity-50 data-[active=true]:bg-sidebar-accent data-[active=true]:font-medium data-[active=true]:text-sidebar-accent-foreground data-[state=open]:hover:bg-sidebar-accent data-[state=open]:hover:text-sidebar-accent-foreground group-data-[collapsible=icon]:!size-8 group-data-[collapsible=icon]:!p-2 [&>span:last-child]:truncate [&>svg]:size-4 [&>svg]:shrink-0",
  {
    variants: {
      variant: {
        default: "hover:bg-sidebar-accent hover:text-sidebar-accent-foreground",
        outline:
          "bg-background shadow-[0_0_0_1px_hsl(var(--sidebar-border))] hover:bg-sidebar-accent hover:text-sidebar-accent-foreground hover:shadow-[0_0_0_1px_hsl(var(--sidebar-accent))]",
      },
      size: {
        default: "h-8 text-sm",
        sm: "h-7 text-xs",
        lg: "h-12 text-sm group-data-[collapsible=icon]:!p-0",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
    },
  }
)

const SidebarMenuButton = React.forwardRef<
  HTMLButtonElement,
  React.ComponentProps<"button"> & {
    asChild?: boolean
    isActive?: boolean
    tooltip?: string | React.ComponentProps<typeof TooltipContent>
  } & VariantProps<typeof sidebarMenuButtonVariants>
>(
  (
    {
      asChild = false,
      isActive = false,
      variant = "default",
      size = "default",
      tooltip,
      className,
      ...props
    },
    ref
  ) => {
    const Comp = asChild ? Slot : "button"
    const { isMobile, state } = useSidebar()

    const button = (
      <Comp
        ref={ref}
        data-sidebar="menu-button"
        data-size={size}
        data-active={isActive}
        className={cn(sidebarMenuButtonVariants({ variant, size }), className)}
        {...props}
      />
    )

    if (!tooltip) {
      return button
    }

    if (typeof tooltip === "string") {
      tooltip = {
        children: tooltip,
      }
    }

    return (
      <Tooltip>
        <TooltipTrigger asChild>{button}</TooltipTrigger>
        <TooltipContent
          side="right"
          align="center"
          hidden={state !== "collapsed" || isMobile}
          {...tooltip}
        />
      </Tooltip>
    )
  }
)
SidebarMenuButton.displayName = "SidebarMenuButton"

const SidebarMenuAction = React.forwardRef<
  HTMLButtonElement,
  React.ComponentProps<"button"> & {
    asChild?: boolean
    showOnHover?: boolean
  }
>(({ className, asChild = false, showOnHover = false, ...props }, ref) => {
  const Comp = asChild ? Slot : "button"

  return (
    <Comp
      ref={ref}
      data-sidebar="menu-action"
      className={cn(
        "absolute right-1 top-1.5 flex aspect-square w-5 items-center justify-center rounded-md p-0 text-sidebar-foreground outline-none ring-sidebar-ring transition-transform hover:bg-sidebar-accent hover:text-sidebar-accent-foreground focus-visible:ring-2 peer-hover/menu-button:text-sidebar-accent-foreground [&>svg]:size-4 [&>svg]:shrink-0",
        // Increases the hit area of the button on mobile.
        "after:absolute after:-inset-2 after:md:hidden",
        "peer-data-[size=sm]/menu-button:top-1",
        "peer-data-[size=default]/menu-button:top-1.5",
        "peer-data-[size=lg]/menu-button:top-2.5",
        "group-data-[collapsible=icon]:hidden",
        showOnHover &&
          "group-focus-within/menu-item:opacity-100 group-hover/menu-item:opacity-100 data-[state=open]:opacity-100 peer-data-[active=true]/menu-button:text-sidebar-accent-foreground md:opacity-0",
        className
      )}
      {...props}
    />
  )
})
SidebarMenuAction.displayName = "SidebarMenuAction"

const SidebarMenuBadge = React.forwardRef<
  HTMLDivElement,
  React.ComponentProps<"div">
>(({ className, ...props }, ref) => (
  <div
    ref={ref}
    data-sidebar="menu-badge"
    className={cn(
      "absolute right-1 flex h-5 min-w-5 items-center justify-center rounded-md px-1 text-xs font-medium tabular-nums text-sidebar-foreground select-none pointer-events-none",
      "peer-hover/menu-button:text-sidebar-accent-foreground peer-data-[active=true]/menu-button:text-sidebar-accent-foreground",
      "peer-data-[size=sm]/menu-button:top-1",
      "peer-data-[size=default]/menu-button:top-1.5",
      "peer-data-[size=lg]/menu-button:top-2.5",
      "group-data-[collapsible=icon]:hidden",
      className
    )}
    {...props}
  />
))
SidebarMenuBadge.displayName = "SidebarMenuBadge"

const SidebarMenuSkeleton = React.forwardRef<
  HTMLDivElement,
  React.ComponentProps<"div"> & {
    showIcon?: boolean
  }
>(({ className, showIcon = false, ...props }, ref) => {
  // Random width between 50 to 90%.
  const width = React.useMemo(() => {
    return `${Math.floor(Math.random() * 40) + 50}%`
  }, [])

  return (
    <div
      ref={ref}
      data-sidebar="menu-skeleton"
      className={cn("rounded-md h-8 flex gap-2 px-2 items-center", className)}
      {...props}
    >
      {showIcon && (
        <Skeleton
          className="size-4 rounded-md"
          data-sidebar="menu-skeleton-icon"
        />
      )}
      <Skeleton
        className="h-4 flex-1 max-w-[--skeleton-width]"
        data-sidebar="menu-skeleton-text"
        style={
          {
            "--skeleton-width": width,
          } as React.CSSProperties
        }
      />
    </div>
  )
})
SidebarMenuSkeleton.displayName = "SidebarMenuSkeleton"

const SidebarMenuSub = React.forwardRef<
  HTMLUListElement,
  React.ComponentProps<"ul">
>(({ className, ...props }, ref) => (
  <ul
    ref={ref}
    data-sidebar="menu-sub"
    className={cn(
      "mx-3.5 flex min-w-0 translate-x-px flex-col gap-1 border-l border-sidebar-border px-2.5 py-0.5",
      "group-data-[collapsible=icon]:hidden",
      className
    )}
    {...props}
  />
))
SidebarMenuSub.displayName = "SidebarMenuSub"

const SidebarMenuSubItem = React.forwardRef<
  HTMLLIElement,
  React.ComponentProps<"li">
>(({ ...props }, ref) => <li ref={ref} {...props} />)
SidebarMenuSubItem.displayName = "SidebarMenuSubItem"

const SidebarMenuSubButton = React.forwardRef<
  HTMLAnchorElement,
  React.ComponentProps<"a"> & {
    asChild?: boolean
    size?: "sm" | "md"
    isActive?: boolean
  }
>(({ asChild = false, size = "md", isActive, className, ...props }, ref) => {
  const Comp = asChild ? Slot : "a"

  return (
    <Comp
      ref={ref}
      data-sidebar="menu-sub-button"
      data-size={size}
      data-active={isActive}
      className={cn(
        "flex h-7 min-w-0 -translate-x-px items-center gap-2 overflow-hidden rounded-md px-2 text-sidebar-foreground outline-none ring-sidebar-ring hover:bg-sidebar-accent hover:text-sidebar-accent-foreground focus-visible:ring-2 active:bg-sidebar-accent active:text-sidebar-accent-foreground disabled:pointer-events-none disabled:opacity-50 aria-disabled:pointer-events-none aria-disabled:opacity-50 [&>span:last-child]:truncate [&>svg]:size-4 [&>svg]:shrink-0 [&>svg]:text-sidebar-accent-foreground",
        "data-[active=true]:bg-sidebar-accent data-[active=true]:text-sidebar-accent-foreground",
        size === "sm" && "text-xs",
        size === "md" && "text-sm",
        "group-data-[collapsible=icon]:hidden",
        className
      )}
      {...props}
    />
  )
})
SidebarMenuSubButton.displayName = "SidebarMenuSubButton"

export {
  Sidebar,
  SidebarContent,
  SidebarFooter,
  SidebarGroup,
  SidebarGroupAction,
  SidebarGroupContent,
  SidebarGroupLabel,
  SidebarHeader,
  SidebarInput,
  SidebarInset,
  SidebarMenu,
  SidebarMenuAction,
  SidebarMenuBadge,
  SidebarMenuButton,
  SidebarMenuItem,
  SidebarMenuSkeleton,
  SidebarMenuSub,
  SidebarMenuSubButton,
  SidebarMenuSubItem,
  SidebarProvider,
  SidebarRail,
  SidebarSeparator,
  SidebarTrigger,
  useSidebar,
}


--------------------------------------------------------------------------------
FILE: components/ui/skeleton.tsx
--------------------------------------------------------------------------------
import { cn } from "@/lib/utils"

function Skeleton({
  className,
  ...props
}: React.HTMLAttributes<HTMLDivElement>) {
  return (
    <div
      className={cn("animate-pulse rounded-md bg-muted", className)}
      {...props}
    />
  )
}

export { Skeleton }


--------------------------------------------------------------------------------
FILE: components/ui/slider.tsx
--------------------------------------------------------------------------------
"use client"

import * as React from "react"
import * as SliderPrimitive from "@radix-ui/react-slider"

import { cn } from "@/lib/utils"

const Slider = React.forwardRef<
  React.ElementRef<typeof SliderPrimitive.Root>,
  React.ComponentPropsWithoutRef<typeof SliderPrimitive.Root>
>(({ className, ...props }, ref) => (
  <SliderPrimitive.Root
    ref={ref}
    className={cn(
      "relative flex w-full touch-none select-none items-center",
      className
    )}
    {...props}
  >
    <SliderPrimitive.Track className="relative h-2 w-full grow overflow-hidden rounded-full bg-secondary">
      <SliderPrimitive.Range className="absolute h-full bg-primary" />
    </SliderPrimitive.Track>
    <SliderPrimitive.Thumb className="block h-5 w-5 rounded-full border-2 border-primary bg-background ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50" />
  </SliderPrimitive.Root>
))
Slider.displayName = SliderPrimitive.Root.displayName

export { Slider }


--------------------------------------------------------------------------------
FILE: components/ui/sonner.tsx
--------------------------------------------------------------------------------
"use client"

import { useTheme } from "next-themes"
import { Toaster as Sonner } from "sonner"

type ToasterProps = React.ComponentProps<typeof Sonner>

const Toaster = ({ ...props }: ToasterProps) => {
  const { theme = "system" } = useTheme()

  return (
    <Sonner
      theme={theme as ToasterProps["theme"]}
      className="toaster group"
      toastOptions={{
        classNames: {
          toast:
            "group toast group-[.toaster]:bg-background group-[.toaster]:text-foreground group-[.toaster]:border-border group-[.toaster]:shadow-lg",
          description: "group-[.toast]:text-muted-foreground",
          actionButton:
            "group-[.toast]:bg-primary group-[.toast]:text-primary-foreground",
          cancelButton:
            "group-[.toast]:bg-muted group-[.toast]:text-muted-foreground",
        },
      }}
      {...props}
    />
  )
}

export { Toaster }


--------------------------------------------------------------------------------
FILE: components/ui/switch.tsx
--------------------------------------------------------------------------------
"use client"

import * as React from "react"
import * as SwitchPrimitives from "@radix-ui/react-switch"

import { cn } from "@/lib/utils"

const Switch = React.forwardRef<
  React.ElementRef<typeof SwitchPrimitives.Root>,
  React.ComponentPropsWithoutRef<typeof SwitchPrimitives.Root>
>(({ className, ...props }, ref) => (
  <SwitchPrimitives.Root
    className={cn(
      "peer inline-flex h-6 w-11 shrink-0 cursor-pointer items-center rounded-full border-2 border-transparent transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 focus-visible:ring-offset-background disabled:cursor-not-allowed disabled:opacity-50 data-[state=checked]:bg-primary data-[state=unchecked]:bg-input",
      className
    )}
    {...props}
    ref={ref}
  >
    <SwitchPrimitives.Thumb
      className={cn(
        "pointer-events-none block h-5 w-5 rounded-full bg-background shadow-lg ring-0 transition-transform data-[state=checked]:translate-x-5 data-[state=unchecked]:translate-x-0"
      )}
    />
  </SwitchPrimitives.Root>
))
Switch.displayName = SwitchPrimitives.Root.displayName

export { Switch }


--------------------------------------------------------------------------------
FILE: components/ui/table.tsx
--------------------------------------------------------------------------------
import * as React from "react"

import { cn } from "@/lib/utils"

const Table = React.forwardRef<
  HTMLTableElement,
  React.HTMLAttributes<HTMLTableElement>
>(({ className, ...props }, ref) => (
  <div className="relative w-full overflow-auto">
    <table
      ref={ref}
      className={cn("w-full caption-bottom text-sm", className)}
      {...props}
    />
  </div>
))
Table.displayName = "Table"

const TableHeader = React.forwardRef<
  HTMLTableSectionElement,
  React.HTMLAttributes<HTMLTableSectionElement>
>(({ className, ...props }, ref) => (
  <thead ref={ref} className={cn("[&_tr]:border-b", className)} {...props} />
))
TableHeader.displayName = "TableHeader"

const TableBody = React.forwardRef<
  HTMLTableSectionElement,
  React.HTMLAttributes<HTMLTableSectionElement>
>(({ className, ...props }, ref) => (
  <tbody
    ref={ref}
    className={cn("[&_tr:last-child]:border-0", className)}
    {...props}
  />
))
TableBody.displayName = "TableBody"

const TableFooter = React.forwardRef<
  HTMLTableSectionElement,
  React.HTMLAttributes<HTMLTableSectionElement>
>(({ className, ...props }, ref) => (
  <tfoot
    ref={ref}
    className={cn(
      "border-t bg-muted/50 font-medium [&>tr]:last:border-b-0",
      className
    )}
    {...props}
  />
))
TableFooter.displayName = "TableFooter"

const TableRow = React.forwardRef<
  HTMLTableRowElement,
  React.HTMLAttributes<HTMLTableRowElement>
>(({ className, ...props }, ref) => (
  <tr
    ref={ref}
    className={cn(
      "border-b transition-colors hover:bg-muted/50 data-[state=selected]:bg-muted",
      className
    )}
    {...props}
  />
))
TableRow.displayName = "TableRow"

const TableHead = React.forwardRef<
  HTMLTableCellElement,
  React.ThHTMLAttributes<HTMLTableCellElement>
>(({ className, ...props }, ref) => (
  <th
    ref={ref}
    className={cn(
      "h-12 px-4 text-left align-middle font-medium text-muted-foreground [&:has([role=checkbox])]:pr-0",
      className
    )}
    {...props}
  />
))
TableHead.displayName = "TableHead"

const TableCell = React.forwardRef<
  HTMLTableCellElement,
  React.TdHTMLAttributes<HTMLTableCellElement>
>(({ className, ...props }, ref) => (
  <td
    ref={ref}
    className={cn("p-4 align-middle [&:has([role=checkbox])]:pr-0", className)}
    {...props}
  />
))
TableCell.displayName = "TableCell"

const TableCaption = React.forwardRef<
  HTMLTableCaptionElement,
  React.HTMLAttributes<HTMLTableCaptionElement>
>(({ className, ...props }, ref) => (
  <caption
    ref={ref}
    className={cn("mt-4 text-sm text-muted-foreground", className)}
    {...props}
  />
))
TableCaption.displayName = "TableCaption"

export {
  Table,
  TableHeader,
  TableBody,
  TableFooter,
  TableHead,
  TableRow,
  TableCell,
  TableCaption,
}


--------------------------------------------------------------------------------
FILE: components/ui/tabs.tsx
--------------------------------------------------------------------------------
"use client"

import * as React from "react"
import * as TabsPrimitive from "@radix-ui/react-tabs"

import { cn } from "@/lib/utils"

const Tabs = TabsPrimitive.Root

const TabsList = React.forwardRef<
  React.ElementRef<typeof TabsPrimitive.List>,
  React.ComponentPropsWithoutRef<typeof TabsPrimitive.List>
>(({ className, ...props }, ref) => (
  <TabsPrimitive.List
    ref={ref}
    className={cn(
      "inline-flex h-10 items-center justify-center rounded-md bg-muted p-1 text-muted-foreground",
      className
    )}
    {...props}
  />
))
TabsList.displayName = TabsPrimitive.List.displayName

const TabsTrigger = React.forwardRef<
  React.ElementRef<typeof TabsPrimitive.Trigger>,
  React.ComponentPropsWithoutRef<typeof TabsPrimitive.Trigger>
>(({ className, ...props }, ref) => (
  <TabsPrimitive.Trigger
    ref={ref}
    className={cn(
      "inline-flex items-center justify-center whitespace-nowrap rounded-sm px-3 py-1.5 text-sm font-medium ring-offset-background transition-all focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 data-[state=active]:bg-background data-[state=active]:text-foreground data-[state=active]:shadow-sm",
      className
    )}
    {...props}
  />
))
TabsTrigger.displayName = TabsPrimitive.Trigger.displayName

const TabsContent = React.forwardRef<
  React.ElementRef<typeof TabsPrimitive.Content>,
  React.ComponentPropsWithoutRef<typeof TabsPrimitive.Content>
>(({ className, ...props }, ref) => (
  <TabsPrimitive.Content
    ref={ref}
    className={cn(
      "mt-2 ring-offset-background focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2",
      className
    )}
    {...props}
  />
))
TabsContent.displayName = TabsPrimitive.Content.displayName

export { Tabs, TabsList, TabsTrigger, TabsContent }


--------------------------------------------------------------------------------
FILE: components/ui/textarea.tsx
--------------------------------------------------------------------------------
import * as React from "react"

import { cn } from "@/lib/utils"

const Textarea = React.forwardRef<
  HTMLTextAreaElement,
  React.ComponentProps<"textarea">
>(({ className, ...props }, ref) => {
  return (
    <textarea
      className={cn(
        "flex min-h-[80px] w-full rounded-md border border-input bg-background px-3 py-2 text-base ring-offset-background placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50 md:text-sm",
        className
      )}
      ref={ref}
      {...props}
    />
  )
})
Textarea.displayName = "Textarea"

export { Textarea }


--------------------------------------------------------------------------------
FILE: components/ui/toast.tsx
--------------------------------------------------------------------------------
"use client"

import * as React from "react"
import * as ToastPrimitives from "@radix-ui/react-toast"
import { cva, type VariantProps } from "class-variance-authority"
import { X } from "lucide-react"

import { cn } from "@/lib/utils"

const ToastProvider = ToastPrimitives.Provider

const ToastViewport = React.forwardRef<
  React.ElementRef<typeof ToastPrimitives.Viewport>,
  React.ComponentPropsWithoutRef<typeof ToastPrimitives.Viewport>
>(({ className, ...props }, ref) => (
  <ToastPrimitives.Viewport
    ref={ref}
    className={cn(
      "fixed top-0 z-[100] flex max-h-screen w-full flex-col-reverse p-4 sm:bottom-0 sm:right-0 sm:top-auto sm:flex-col md:max-w-[420px]",
      className
    )}
    {...props}
  />
))
ToastViewport.displayName = ToastPrimitives.Viewport.displayName

const toastVariants = cva(
  "group pointer-events-auto relative flex w-full items-center justify-between space-x-4 overflow-hidden rounded-md border p-6 pr-8 shadow-lg transition-all data-[swipe=cancel]:translate-x-0 data-[swipe=end]:translate-x-[var(--radix-toast-swipe-end-x)] data-[swipe=move]:translate-x-[var(--radix-toast-swipe-move-x)] data-[swipe=move]:transition-none data-[state=open]:animate-in data-[state=closed]:animate-out data-[swipe=end]:animate-out data-[state=closed]:fade-out-80 data-[state=closed]:slide-out-to-right-full data-[state=open]:slide-in-from-top-full data-[state=open]:sm:slide-in-from-bottom-full",
  {
    variants: {
      variant: {
        default: "border bg-background text-foreground",
        destructive:
          "destructive group border-destructive bg-destructive text-destructive-foreground",
      },
    },
    defaultVariants: {
      variant: "default",
    },
  }
)

const Toast = React.forwardRef<
  React.ElementRef<typeof ToastPrimitives.Root>,
  React.ComponentPropsWithoutRef<typeof ToastPrimitives.Root> &
    VariantProps<typeof toastVariants>
>(({ className, variant, ...props }, ref) => {
  return (
    <ToastPrimitives.Root
      ref={ref}
      className={cn(toastVariants({ variant }), className)}
      {...props}
    />
  )
})
Toast.displayName = ToastPrimitives.Root.displayName

const ToastAction = React.forwardRef<
  React.ElementRef<typeof ToastPrimitives.Action>,
  React.ComponentPropsWithoutRef<typeof ToastPrimitives.Action>
>(({ className, ...props }, ref) => (
  <ToastPrimitives.Action
    ref={ref}
    className={cn(
      "inline-flex h-8 shrink-0 items-center justify-center rounded-md border bg-transparent px-3 text-sm font-medium ring-offset-background transition-colors hover:bg-secondary focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 group-[.destructive]:border-muted/40 group-[.destructive]:hover:border-destructive/30 group-[.destructive]:hover:bg-destructive group-[.destructive]:hover:text-destructive-foreground group-[.destructive]:focus:ring-destructive",
      className
    )}
    {...props}
  />
))
ToastAction.displayName = ToastPrimitives.Action.displayName

const ToastClose = React.forwardRef<
  React.ElementRef<typeof ToastPrimitives.Close>,
  React.ComponentPropsWithoutRef<typeof ToastPrimitives.Close>
>(({ className, ...props }, ref) => (
  <ToastPrimitives.Close
    ref={ref}
    className={cn(
      "absolute right-2 top-2 rounded-md p-1 text-foreground/50 opacity-0 transition-opacity hover:text-foreground focus:opacity-100 focus:outline-none focus:ring-2 group-hover:opacity-100 group-[.destructive]:text-red-300 group-[.destructive]:hover:text-red-50 group-[.destructive]:focus:ring-red-400 group-[.destructive]:focus:ring-offset-red-600",
      className
    )}
    toast-close=""
    {...props}
  >
    <X className="h-4 w-4" />
  </ToastPrimitives.Close>
))
ToastClose.displayName = ToastPrimitives.Close.displayName

const ToastTitle = React.forwardRef<
  React.ElementRef<typeof ToastPrimitives.Title>,
  React.ComponentPropsWithoutRef<typeof ToastPrimitives.Title>
>(({ className, ...props }, ref) => (
  <ToastPrimitives.Title
    ref={ref}
    className={cn("text-sm font-semibold", className)}
    {...props}
  />
))
ToastTitle.displayName = ToastPrimitives.Title.displayName

const ToastDescription = React.forwardRef<
  React.ElementRef<typeof ToastPrimitives.Description>,
  React.ComponentPropsWithoutRef<typeof ToastPrimitives.Description>
>(({ className, ...props }, ref) => (
  <ToastPrimitives.Description
    ref={ref}
    className={cn("text-sm opacity-90", className)}
    {...props}
  />
))
ToastDescription.displayName = ToastPrimitives.Description.displayName

type ToastProps = React.ComponentPropsWithoutRef<typeof Toast>

type ToastActionElement = React.ReactElement<typeof ToastAction>

export {
  type ToastProps,
  type ToastActionElement,
  ToastProvider,
  ToastViewport,
  Toast,
  ToastTitle,
  ToastDescription,
  ToastClose,
  ToastAction,
}


--------------------------------------------------------------------------------
FILE: components/ui/toaster.tsx
--------------------------------------------------------------------------------
"use client"

import { useToast } from "@/hooks/use-toast"
import {
  Toast,
  ToastClose,
  ToastDescription,
  ToastProvider,
  ToastTitle,
  ToastViewport,
} from "@/components/ui/toast"

export function Toaster() {
  const { toasts } = useToast()

  return (
    <ToastProvider>
      {toasts.map(function ({ id, title, description, action, ...props }) {
        return (
          <Toast key={id} {...props}>
            <div className="grid gap-1">
              {title && <ToastTitle>{title}</ToastTitle>}
              {description && (
                <ToastDescription>{description}</ToastDescription>
              )}
            </div>
            {action}
            <ToastClose />
          </Toast>
        )
      })}
      <ToastViewport />
    </ToastProvider>
  )
}


--------------------------------------------------------------------------------
FILE: components/ui/toggle-group.tsx
--------------------------------------------------------------------------------
"use client"

import * as React from "react"
import * as ToggleGroupPrimitive from "@radix-ui/react-toggle-group"
import { type VariantProps } from "class-variance-authority"

import { cn } from "@/lib/utils"
import { toggleVariants } from "@/components/ui/toggle"

const ToggleGroupContext = React.createContext<
  VariantProps<typeof toggleVariants>
>({
  size: "default",
  variant: "default",
})

const ToggleGroup = React.forwardRef<
  React.ElementRef<typeof ToggleGroupPrimitive.Root>,
  React.ComponentPropsWithoutRef<typeof ToggleGroupPrimitive.Root> &
    VariantProps<typeof toggleVariants>
>(({ className, variant, size, children, ...props }, ref) => (
  <ToggleGroupPrimitive.Root
    ref={ref}
    className={cn("flex items-center justify-center gap-1", className)}
    {...props}
  >
    <ToggleGroupContext.Provider value={{ variant, size }}>
      {children}
    </ToggleGroupContext.Provider>
  </ToggleGroupPrimitive.Root>
))

ToggleGroup.displayName = ToggleGroupPrimitive.Root.displayName

const ToggleGroupItem = React.forwardRef<
  React.ElementRef<typeof ToggleGroupPrimitive.Item>,
  React.ComponentPropsWithoutRef<typeof ToggleGroupPrimitive.Item> &
    VariantProps<typeof toggleVariants>
>(({ className, children, variant, size, ...props }, ref) => {
  const context = React.useContext(ToggleGroupContext)

  return (
    <ToggleGroupPrimitive.Item
      ref={ref}
      className={cn(
        toggleVariants({
          variant: context.variant || variant,
          size: context.size || size,
        }),
        className
      )}
      {...props}
    >
      {children}
    </ToggleGroupPrimitive.Item>
  )
})

ToggleGroupItem.displayName = ToggleGroupPrimitive.Item.displayName

export { ToggleGroup, ToggleGroupItem }


--------------------------------------------------------------------------------
FILE: components/ui/toggle.tsx
--------------------------------------------------------------------------------
"use client"

import * as React from "react"
import * as TogglePrimitive from "@radix-ui/react-toggle"
import { cva, type VariantProps } from "class-variance-authority"

import { cn } from "@/lib/utils"

const toggleVariants = cva(
  "inline-flex items-center justify-center rounded-md text-sm font-medium ring-offset-background transition-colors hover:bg-muted hover:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 data-[state=on]:bg-accent data-[state=on]:text-accent-foreground [&_svg]:pointer-events-none [&_svg]:size-4 [&_svg]:shrink-0 gap-2",
  {
    variants: {
      variant: {
        default: "bg-transparent",
        outline:
          "border border-input bg-transparent hover:bg-accent hover:text-accent-foreground",
      },
      size: {
        default: "h-10 px-3 min-w-10",
        sm: "h-9 px-2.5 min-w-9",
        lg: "h-11 px-5 min-w-11",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
    },
  }
)

const Toggle = React.forwardRef<
  React.ElementRef<typeof TogglePrimitive.Root>,
  React.ComponentPropsWithoutRef<typeof TogglePrimitive.Root> &
    VariantProps<typeof toggleVariants>
>(({ className, variant, size, ...props }, ref) => (
  <TogglePrimitive.Root
    ref={ref}
    className={cn(toggleVariants({ variant, size, className }))}
    {...props}
  />
))

Toggle.displayName = TogglePrimitive.Root.displayName

export { Toggle, toggleVariants }


--------------------------------------------------------------------------------
FILE: components/ui/tooltip.tsx
--------------------------------------------------------------------------------
"use client"

import * as React from "react"
import * as TooltipPrimitive from "@radix-ui/react-tooltip"

import { cn } from "@/lib/utils"

const TooltipProvider = TooltipPrimitive.Provider

const Tooltip = TooltipPrimitive.Root

const TooltipTrigger = TooltipPrimitive.Trigger

const TooltipContent = React.forwardRef<
  React.ElementRef<typeof TooltipPrimitive.Content>,
  React.ComponentPropsWithoutRef<typeof TooltipPrimitive.Content>
>(({ className, sideOffset = 4, ...props }, ref) => (
  <TooltipPrimitive.Content
    ref={ref}
    sideOffset={sideOffset}
    className={cn(
      "z-50 overflow-hidden rounded-md border bg-popover px-3 py-1.5 text-sm text-popover-foreground shadow-md animate-in fade-in-0 zoom-in-95 data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=closed]:zoom-out-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2",
      className
    )}
    {...props}
  />
))
TooltipContent.displayName = TooltipPrimitive.Content.displayName

export { Tooltip, TooltipTrigger, TooltipContent, TooltipProvider }


--------------------------------------------------------------------------------
FILE: components/ui/use-mobile.tsx
--------------------------------------------------------------------------------
import * as React from "react"

const MOBILE_BREAKPOINT = 768

export function useIsMobile() {
  const [isMobile, setIsMobile] = React.useState<boolean | undefined>(undefined)

  React.useEffect(() => {
    const mql = window.matchMedia(`(max-width: ${MOBILE_BREAKPOINT - 1}px)`)
    const onChange = () => {
      setIsMobile(window.innerWidth < MOBILE_BREAKPOINT)
    }
    mql.addEventListener("change", onChange)
    setIsMobile(window.innerWidth < MOBILE_BREAKPOINT)
    return () => mql.removeEventListener("change", onChange)
  }, [])

  return !!isMobile
}


--------------------------------------------------------------------------------
FILE: components/ui/use-toast.ts
--------------------------------------------------------------------------------
"use client"

// Inspired by react-hot-toast library
import * as React from "react"

import type {
  ToastActionElement,
  ToastProps,
} from "@/components/ui/toast"

const TOAST_LIMIT = 1
const TOAST_REMOVE_DELAY = 1000000

type ToasterToast = ToastProps & {
  id: string
  title?: React.ReactNode
  description?: React.ReactNode
  action?: ToastActionElement
}

const actionTypes = {
  ADD_TOAST: "ADD_TOAST",
  UPDATE_TOAST: "UPDATE_TOAST",
  DISMISS_TOAST: "DISMISS_TOAST",
  REMOVE_TOAST: "REMOVE_TOAST",
} as const

let count = 0

function genId() {
  count = (count + 1) % Number.MAX_SAFE_INTEGER
  return count.toString()
}

type ActionType = typeof actionTypes

type Action =
  | {
      type: ActionType["ADD_TOAST"]
      toast: ToasterToast
    }
  | {
      type: ActionType["UPDATE_TOAST"]
      toast: Partial<ToasterToast>
    }
  | {
      type: ActionType["DISMISS_TOAST"]
      toastId?: ToasterToast["id"]
    }
  | {
      type: ActionType["REMOVE_TOAST"]
      toastId?: ToasterToast["id"]
    }

interface State {
  toasts: ToasterToast[]
}

const toastTimeouts = new Map<string, ReturnType<typeof setTimeout>>()

const addToRemoveQueue = (toastId: string) => {
  if (toastTimeouts.has(toastId)) {
    return
  }

  const timeout = setTimeout(() => {
    toastTimeouts.delete(toastId)
    dispatch({
      type: "REMOVE_TOAST",
      toastId: toastId,
    })
  }, TOAST_REMOVE_DELAY)

  toastTimeouts.set(toastId, timeout)
}

export const reducer = (state: State, action: Action): State => {
  switch (action.type) {
    case "ADD_TOAST":
      return {
        ...state,
        toasts: [action.toast, ...state.toasts].slice(0, TOAST_LIMIT),
      }

    case "UPDATE_TOAST":
      return {
        ...state,
        toasts: state.toasts.map((t) =>
          t.id === action.toast.id ? { ...t, ...action.toast } : t
        ),
      }

    case "DISMISS_TOAST": {
      const { toastId } = action

      // ! Side effects ! - This could be extracted into a dismissToast() action,
      // but I'll keep it here for simplicity
      if (toastId) {
        addToRemoveQueue(toastId)
      } else {
        state.toasts.forEach((toast) => {
          addToRemoveQueue(toast.id)
        })
      }

      return {
        ...state,
        toasts: state.toasts.map((t) =>
          t.id === toastId || toastId === undefined
            ? {
                ...t,
                open: false,
              }
            : t
        ),
      }
    }
    case "REMOVE_TOAST":
      if (action.toastId === undefined) {
        return {
          ...state,
          toasts: [],
        }
      }
      return {
        ...state,
        toasts: state.toasts.filter((t) => t.id !== action.toastId),
      }
  }
}

const listeners: Array<(state: State) => void> = []

let memoryState: State = { toasts: [] }

function dispatch(action: Action) {
  memoryState = reducer(memoryState, action)
  listeners.forEach((listener) => {
    listener(memoryState)
  })
}

type Toast = Omit<ToasterToast, "id">

function toast({ ...props }: Toast) {
  const id = genId()

  const update = (props: ToasterToast) =>
    dispatch({
      type: "UPDATE_TOAST",
      toast: { ...props, id },
    })
  const dismiss = () => dispatch({ type: "DISMISS_TOAST", toastId: id })

  dispatch({
    type: "ADD_TOAST",
    toast: {
      ...props,
      id,
      open: true,
      onOpenChange: (open) => {
        if (!open) dismiss()
      },
    },
  })

  return {
    id: id,
    dismiss,
    update,
  }
}

function useToast() {
  const [state, setState] = React.useState<State>(memoryState)

  React.useEffect(() => {
    listeners.push(setState)
    return () => {
      const index = listeners.indexOf(setState)
      if (index > -1) {
        listeners.splice(index, 1)
      }
    }
  }, [state])

  return {
    ...state,
    toast,
    dismiss: (toastId?: string) => dispatch({ type: "DISMISS_TOAST", toastId }),
  }
}

export { useToast, toast }


################################################################################
DIRECTORY: hooks
################################################################################

--------------------------------------------------------------------------------
FILE: hooks/use-mobile.tsx
--------------------------------------------------------------------------------
import * as React from "react"

const MOBILE_BREAKPOINT = 768

export function useIsMobile() {
  const [isMobile, setIsMobile] = React.useState<boolean | undefined>(undefined)

  React.useEffect(() => {
    const mql = window.matchMedia(`(max-width: ${MOBILE_BREAKPOINT - 1}px)`)
    const onChange = () => {
      setIsMobile(window.innerWidth < MOBILE_BREAKPOINT)
    }
    mql.addEventListener("change", onChange)
    setIsMobile(window.innerWidth < MOBILE_BREAKPOINT)
    return () => mql.removeEventListener("change", onChange)
  }, [])

  return !!isMobile
}


--------------------------------------------------------------------------------
FILE: hooks/use-toast.ts
--------------------------------------------------------------------------------
"use client"

// Inspired by react-hot-toast library
import * as React from "react"

import type {
  ToastActionElement,
  ToastProps,
} from "@/components/ui/toast"

const TOAST_LIMIT = 1
const TOAST_REMOVE_DELAY = 1000000

type ToasterToast = ToastProps & {
  id: string
  title?: React.ReactNode
  description?: React.ReactNode
  action?: ToastActionElement
}

const actionTypes = {
  ADD_TOAST: "ADD_TOAST",
  UPDATE_TOAST: "UPDATE_TOAST",
  DISMISS_TOAST: "DISMISS_TOAST",
  REMOVE_TOAST: "REMOVE_TOAST",
} as const

let count = 0

function genId() {
  count = (count + 1) % Number.MAX_SAFE_INTEGER
  return count.toString()
}

type ActionType = typeof actionTypes

type Action =
  | {
      type: ActionType["ADD_TOAST"]
      toast: ToasterToast
    }
  | {
      type: ActionType["UPDATE_TOAST"]
      toast: Partial<ToasterToast>
    }
  | {
      type: ActionType["DISMISS_TOAST"]
      toastId?: ToasterToast["id"]
    }
  | {
      type: ActionType["REMOVE_TOAST"]
      toastId?: ToasterToast["id"]
    }

interface State {
  toasts: ToasterToast[]
}

const toastTimeouts = new Map<string, ReturnType<typeof setTimeout>>()

const addToRemoveQueue = (toastId: string) => {
  if (toastTimeouts.has(toastId)) {
    return
  }

  const timeout = setTimeout(() => {
    toastTimeouts.delete(toastId)
    dispatch({
      type: "REMOVE_TOAST",
      toastId: toastId,
    })
  }, TOAST_REMOVE_DELAY)

  toastTimeouts.set(toastId, timeout)
}

export const reducer = (state: State, action: Action): State => {
  switch (action.type) {
    case "ADD_TOAST":
      return {
        ...state,
        toasts: [action.toast, ...state.toasts].slice(0, TOAST_LIMIT),
      }

    case "UPDATE_TOAST":
      return {
        ...state,
        toasts: state.toasts.map((t) =>
          t.id === action.toast.id ? { ...t, ...action.toast } : t
        ),
      }

    case "DISMISS_TOAST": {
      const { toastId } = action

      // ! Side effects ! - This could be extracted into a dismissToast() action,
      // but I'll keep it here for simplicity
      if (toastId) {
        addToRemoveQueue(toastId)
      } else {
        state.toasts.forEach((toast) => {
          addToRemoveQueue(toast.id)
        })
      }

      return {
        ...state,
        toasts: state.toasts.map((t) =>
          t.id === toastId || toastId === undefined
            ? {
                ...t,
                open: false,
              }
            : t
        ),
      }
    }
    case "REMOVE_TOAST":
      if (action.toastId === undefined) {
        return {
          ...state,
          toasts: [],
        }
      }
      return {
        ...state,
        toasts: state.toasts.filter((t) => t.id !== action.toastId),
      }
  }
}

const listeners: Array<(state: State) => void> = []

let memoryState: State = { toasts: [] }

function dispatch(action: Action) {
  memoryState = reducer(memoryState, action)
  listeners.forEach((listener) => {
    listener(memoryState)
  })
}

type Toast = Omit<ToasterToast, "id">

function toast({ ...props }: Toast) {
  const id = genId()

  const update = (props: ToasterToast) =>
    dispatch({
      type: "UPDATE_TOAST",
      toast: { ...props, id },
    })
  const dismiss = () => dispatch({ type: "DISMISS_TOAST", toastId: id })

  dispatch({
    type: "ADD_TOAST",
    toast: {
      ...props,
      id,
      open: true,
      onOpenChange: (open) => {
        if (!open) dismiss()
      },
    },
  })

  return {
    id: id,
    dismiss,
    update,
  }
}

function useToast() {
  const [state, setState] = React.useState<State>(memoryState)

  React.useEffect(() => {
    listeners.push(setState)
    return () => {
      const index = listeners.indexOf(setState)
      if (index > -1) {
        listeners.splice(index, 1)
      }
    }
  }, [state])

  return {
    ...state,
    toast,
    dismiss: (toastId?: string) => dispatch({ type: "DISMISS_TOAST", toastId }),
  }
}

export { useToast, toast }


################################################################################
DIRECTORY: lib
################################################################################

--------------------------------------------------------------------------------
FILE: lib/auth-context.tsx
--------------------------------------------------------------------------------
"use client"

import { createContext, useContext, useEffect, useState, type ReactNode } from "react"

interface User {
  id: string
  email: string
  name: string
  role: "user" | "admin"
  subscriptionTier: "free" | "starter" | "growth" | "pro" | "enterprise"
}

interface AuthContextType {
  user: User | null
  loading: boolean
  login: (email: string, password: string) => Promise<boolean>
  logout: () => Promise<void>
  register: (email: string, password: string, name: string) => Promise<boolean>
}

const AuthContext = createContext<AuthContextType | null>(null)

export function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<User | null>(null) // FIXED: Start with null, no auto-login
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    checkAuth()
  }, [])

  const checkAuth = async () => {
    try {
      // FIXED: Only check auth, don't auto-login
      const response = await fetch("/api/auth/me", {
        credentials: "include", // Include cookies
      })

      if (response.ok) {
        const data = await response.json()
        // FIXED: Only set user if there's actually a valid session
        if (data.success && data.user) {
          setUser(data.user)
        } else {
          setUser(null) // FIXED: Explicitly set to null if no valid session
        }
      } else {
        setUser(null) // FIXED: Set to null on failed response
      }
    } catch (error) {
      console.error("Auth check failed:", error)
      setUser(null) // FIXED: Set to null on error
    } finally {
      setLoading(false)
    }
  }

  const login = async (email: string, password: string): Promise<boolean> => {
    try {
      const response = await fetch("/api/auth/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        credentials: "include", // Include cookies
        body: JSON.stringify({ email, password }),
      })

      const data = await response.json()

      if (data.success && data.user) {
        setUser(data.user)
        return true
      }
      return false
    } catch (error) {
      console.error("Login error:", error)
      return false
    }
  }

  const logout = async () => {
    try {
      await fetch("/api/auth/logout", {
        method: "POST",
        credentials: "include", // Include cookies
      })
      setUser(null) // FIXED: Always clear user on logout
    } catch (error) {
      console.error("Logout error:", error)
      setUser(null) // FIXED: Clear user even on error
    }
  }

  const register = async (email: string, password: string, name: string): Promise<boolean> => {
    try {
      const response = await fetch("/api/auth/register", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        credentials: "include", // Include cookies
        body: JSON.stringify({ email, password, name }),
      })

      const data = await response.json()

      if (data.success && data.user) {
        setUser(data.user)
        return true
      }
      return false
    } catch (error) {
      console.error("Registration error:", error)
      return false
    }
  }

  return <AuthContext.Provider value={{ user, loading, login, logout, register }}>{children}</AuthContext.Provider>
}

export function useAuth() {
  const context = useContext(AuthContext)
  if (!context) {
    throw new Error("useAuth must be used within AuthProvider")
  }
  return context
}


--------------------------------------------------------------------------------
FILE: lib/auth-server.ts
--------------------------------------------------------------------------------
import { cookies } from "next/headers"
import jwt from "jsonwebtoken"
import { config } from "./config"

// User data structure
export interface User {
  id: string
  email: string
  name?: string
  role: "user" | "admin"
  subscription?: {
    tier: "free" | "starter" | "pro" | "growth" | "enterprise"
    status: "active" | "canceled" | "past_due" | "trialing"
    currentPeriodEnd?: string
  }
}

// Mock user database (replace with actual database in production)
const users: Record<string, User & { password: string }> = {
  "user-1": {
    id: "user-1",
    email: "user@example.com",
    password: "password123", // In production, this would be hashed
    name: "Demo User",
    role: "user",
    subscription: {
      tier: "free",
      status: "active",
    },
  },
  "admin-1": {
    id: "admin-1",
    email: "admin@example.com",
    password: "admin123", // In production, this would be hashed
    name: "Admin User",
    role: "admin",
    subscription: {
      tier: "enterprise",
      status: "active",
    },
  },
}

// Get user by email and password
export async function getUserByCredentials(email: string, password: string): Promise<User | null> {
  // In production, you would query your database and verify the password hash
  const user = Object.values(users).find(
    (u) => u.email.toLowerCase() === email.toLowerCase() && u.password === password,
  )

  if (!user) return null

  // Return user without password
  const { password: _, ...userWithoutPassword } = user
  return userWithoutPassword
}

// Create a new user
export async function createUser(email: string, password: string, name?: string): Promise<User | null> {
  // Check if user already exists
  const existingUser = Object.values(users).find((u) => u.email.toLowerCase() === email.toLowerCase())
  if (existingUser) return null

  // In production, you would hash the password and store in your database
  const id = `user-${Date.now()}`
  const newUser: User & { password: string } = {
    id,
    email,
    password, // In production, this would be hashed
    name,
    role: "user",
    subscription: {
      tier: "free",
      status: "active",
    },
  }

  users[id] = newUser

  // Return user without password
  const { password: _, ...userWithoutPassword } = newUser
  return userWithoutPassword
}

// Create a session for a user
export async function createSession(user: User): Promise<string> {
  // In production, use a proper JWT library with a secure secret
  const token = jwt.sign({ userId: user.id }, config.jwt.secret, { expiresIn: "7d" })

  // Set the token in a cookie
  cookies().set("auth-token", token, {
    httpOnly: true,
    secure: process.env.NODE_ENV === "production",
    sameSite: "lax",
    maxAge: 7 * 24 * 60 * 60, // 7 days
    path: "/",
  })

  return token
}

// Get the current user from the session
export async function getCurrentUser(): Promise<User | null> {
  try {
    const token = cookies().get("auth-token")?.value
    if (!token) return null

    // Verify the token
    const decoded = jwt.verify(token, config.jwt.secret) as { userId: string }
    const user = users[decoded.userId]

    if (!user) return null

    // Return user without password
    const { password: _, ...userWithoutPassword } = user
    return userWithoutPassword
  } catch (error) {
    console.error("Error getting current user:", error)
    return null
  }
}

// Clear the session
export async function clearSession(): Promise<void> {
  cookies().delete("auth-token")
}

// Authenticate a user with email and password
export async function authenticateUser(email: string, password: string): Promise<{ user: User; token: string } | null> {
  try {
    // Get user by credentials
    const user = await getUserByCredentials(email, password)
    if (!user) return null

    // Create a session
    const token = await createSession(user)

    return { user, token }
  } catch (error) {
    console.error("Error authenticating user:", error)
    return null
  }
}


--------------------------------------------------------------------------------
FILE: lib/auth.ts
--------------------------------------------------------------------------------
export interface User {
  id: string
  email: string
  name: string
  role: "user" | "premium" // Changed from admin to premium
  subscriptionTier: "free" | "pro" | "starter" | "growth" | "enterprise"
  subscriptionStatus: "active" | "inactive" | "canceled"
  stripeCustomerId?: string
  stripeSubscriptionId?: string
  createdAt: Date
  updatedAt: Date
}

// All logged-in users get full access (premium customer treatment)
export function canAccessPro(user: User | null): boolean {
  if (!user) return false
  return true // All logged-in users can access Pro
}

export function canAccessAPI(user: User | null): boolean {
  if (!user) return false
  return true // All logged-in users can access API
}

export function canAccessGrowthAPI(user: User | null): boolean {
  if (!user) return false
  return true // All logged-in users can access Growth API
}

export function canAccessEnterprise(user: User | null): boolean {
  if (!user) return false
  return true // All logged-in users can access Enterprise
}

// Return maximum tier level for all logged-in users
export function getUserTierLevel(user: User | null): number {
  if (!user) return 0
  return 5 // Maximum tier level for all logged-in users (premium customer)
}


--------------------------------------------------------------------------------
FILE: lib/config.ts
--------------------------------------------------------------------------------
// Helper function to safely get environment variables
const getEnv = (key: string, defaultValue = ""): string => {
  if (typeof process !== "undefined" && process.env[key]) {
    return process.env[key] || defaultValue
  }
  return defaultValue
}

export const config = {
  stripe: {
    secretKey: getEnv("STRIPE_SECRET_KEY"),
    publishableKey: getEnv("NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY"),
    webhookSecret: getEnv("STRIPE_WEBHOOK_SECRET"),
  },
  url: getEnv("NEXT_PUBLIC_URL", "http://localhost:3000"),
  email: {
    host: getEnv("EMAIL_SERVER_HOST"),
    port: Number(getEnv("EMAIL_SERVER_PORT", "587")),
    user: getEnv("EMAIL_SERVER_USER"),
    pass: getEnv("EMAIL_SERVER_PASSWORD"),
    from: getEnv("EMAIL_FROM", "noreply@voltsphere.com"),
    secure: getEnv("EMAIL_SERVER_SECURE") === "true",
  },
  jwt: {
    secret: getEnv("JWT_SECRET", "default-jwt-secret-for-development-only"),
  },
}


--------------------------------------------------------------------------------
FILE: lib/error-handler.ts
--------------------------------------------------------------------------------
// Global error handler for browser extension errors
export function setupGlobalErrorHandler() {
  if (typeof window !== "undefined") {
    // Handle unhandled promise rejections
    window.addEventListener("unhandledrejection", (event) => {
      const error = event.reason

      // Check if it's a browser extension error
      if (
        error?.message?.includes("Receiving end does not exist") ||
        error?.message?.includes("Extension context invalidated") ||
        error?.message?.includes("Could not establish connection") ||
        error?.message?.includes("chrome-extension://") ||
        error?.message?.includes("moz-extension://")
      ) {
        // Prevent the error from being logged to console
        event.preventDefault()
        console.warn("Browser extension error suppressed:", error.message)
        return
      }

      // Log other errors normally
      console.error("Unhandled promise rejection:", error)
    })

    // Handle general errors
    window.addEventListener("error", (event) => {
      const error = event.error

      // Check if it's a browser extension error
      if (
        error?.message?.includes("Receiving end does not exist") ||
        error?.message?.includes("Extension context invalidated") ||
        error?.message?.includes("Could not establish connection") ||
        event.filename?.includes("chrome-extension://") ||
        event.filename?.includes("moz-extension://")
      ) {
        // Prevent the error from being logged
        event.preventDefault()
        console.warn("Browser extension error suppressed:", error?.message || "Unknown extension error")
        return
      }
    })
  }
}


--------------------------------------------------------------------------------
FILE: lib/simulation/engine.ts
--------------------------------------------------------------------------------
// Advanced Simulation Engine for VoltSphere

export interface SimulationConfig {
  // Basic Configuration
  batteryCapacity: number
  batteryEfficiency: number
  solarEnabled: boolean
  batteryType: string
  loadProfileType: string

  // Advanced Configuration
  useRealWeather: boolean
  weatherLocation: string
  timeOfUseRates: boolean
  simulationDuration: string
  solarCapacity: number
  inverterEfficiency: number
  systemLosses: number

  // Economic Parameters
  gridCostPerKwh: number
  solarCostPerWatt: number
  batteryCostPerKwh: number
  discountRate: number
  systemLifespan: number

  // Location
  location?: {
    lat: number
    lng: number
    city: string
    country: string
  }
}

export interface SimulationDataPoint {
  time: string
  hour: number
  solar: number
  consumption: number
  battery: number
  batterySOC: number
  grid: number
  gridCost: number
  weather: {
    temperature: number
    cloudCover: number
    condition: string
    solarIrradiance: number
  }
}

export interface SimulationResult {
  data: SimulationDataPoint[]
  summary: {
    totalSolar: number
    totalConsumption: number
    totalGrid: number
    avgBattery: number
    peakDemand: number
    solarUtilization: number
    gridIndependence: number
  }
  economics: {
    dailyCost: number
    monthlyCost: number
    annualCost: number
    totalSavings: number
    paybackPeriod: number
    roi: number
    netPresentValue: number
  }
  environmental: {
    co2Saved: number
    treesEquivalent: number
    coalAvoided: number
  }
}

export class SimulationEngine {
  private static readonly BATTERY_SPECS = {
    lithium: { efficiency: 0.92, cycleLife: 6000, costPerKwh: 500 },
    "lead-acid": { efficiency: 0.85, cycleLife: 2000, costPerKwh: 200 },
    flow: { efficiency: 0.88, cycleLife: 10000, costPerKwh: 800 },
    sodium: { efficiency: 0.9, cycleLife: 4000, costPerKwh: 400 },
  }

  private static readonly LOAD_PROFILES = {
    residential: [
      2.1, 1.9, 1.7, 1.5, 1.4, 1.8, 2.5, 3.2, 3.8, 3.5, 3.2, 3.0, 3.1, 3.0, 2.9, 3.1, 3.5, 4.2, 5.0, 5.2, 4.8, 4.0, 3.2,
      2.5,
    ],
    commercial: [
      2.0, 1.8, 1.7, 1.6, 1.8, 2.5, 3.5, 5.0, 6.5, 7.0, 7.2, 7.0, 6.8, 7.0, 7.2, 7.0, 6.5, 5.5, 4.5, 3.8, 3.2, 2.8, 2.4,
      2.1,
    ],
    industrial: [
      4.5, 4.2, 4.0, 3.8, 4.0, 4.5, 5.5, 6.8, 7.5, 8.0, 8.2, 8.0, 7.8, 8.0, 8.2, 8.0, 7.5, 6.8, 6.0, 5.5, 5.0, 4.8, 4.6,
      4.5,
    ],
  }

  private static readonly WEATHER_DATA = {
    "San Francisco, CA": { lat: 37.7749, lng: -122.4194, avgTemp: 15, cloudiness: 0.3 },
    "New York, NY": { lat: 40.7128, lng: -74.006, avgTemp: 12, cloudiness: 0.4 },
    "Chicago, IL": { lat: 41.8781, lng: -87.6298, avgTemp: 10, cloudiness: 0.5 },
    "Austin, TX": { lat: 30.2672, lng: -97.7431, avgTemp: 22, cloudiness: 0.2 },
    "Miami, FL": { lat: 25.7617, lng: -80.1918, avgTemp: 25, cloudiness: 0.3 },
    "Phoenix, AZ": { lat: 33.4484, lng: -112.074, avgTemp: 28, cloudiness: 0.1 },
    "Seattle, WA": { lat: 47.6062, lng: -122.3321, avgTemp: 11, cloudiness: 0.6 },
    "Denver, CO": { lat: 39.7392, lng: -104.9903, avgTemp: 10, cloudiness: 0.3 },
    "Los Angeles, CA": { lat: 34.0522, lng: -118.2437, avgTemp: 18, cloudiness: 0.2 },
    "Boston, MA": { lat: 42.3601, lng: -71.0589, avgTemp: 10, cloudiness: 0.4 },
    "Atlanta, GA": { lat: 33.749, lng: -84.388, avgTemp: 16, cloudiness: 0.4 },
    "Dallas, TX": { lat: 32.7767, lng: -96.797, avgTemp: 19, cloudiness: 0.3 },
  }

  static async runSimulation(config: SimulationConfig): Promise<SimulationResult> {
    const hours = this.getSimulationHours(config.simulationDuration)
    const batterySpec = this.BATTERY_SPECS[config.batteryType as keyof typeof this.BATTERY_SPECS]
    const loadProfile = this.LOAD_PROFILES[config.loadProfileType as keyof typeof this.LOAD_PROFILES]
    const weatherData = this.WEATHER_DATA[config.weatherLocation as keyof typeof this.WEATHER_DATA]

    let batterySOC = 50 // Start at 50% state of charge
    const data: SimulationDataPoint[] = []

    for (let i = 0; i < hours; i++) {
      const hour = i % 24
      const day = Math.floor(i / 24)

      // Generate weather conditions
      const weather = this.generateWeatherConditions(hour, day, weatherData, config.useRealWeather)

      // Calculate solar generation
      const solarGeneration = config.solarEnabled
        ? this.calculateSolarGeneration(
            hour,
            config.solarCapacity,
            weather,
            config.inverterEfficiency,
            config.systemLosses,
          )
        : 0

      // Calculate load consumption
      const baseLoad = loadProfile[hour] * (config.batteryCapacity / 15) // Scale based on system size
      const consumption = baseLoad * (0.9 + Math.random() * 0.2) // Add 10% variation

      // Calculate energy balance
      const energyBalance = solarGeneration - consumption

      // Battery and grid calculations
      let gridUsage = 0
      let gridCost = 0

      if (energyBalance < 0) {
        // Need energy - try battery first
        const energyNeeded = -energyBalance
        const maxFromBattery = (batterySOC * config.batteryCapacity) / 100
        const energyFromBattery = Math.min(energyNeeded, maxFromBattery) * batterySpec.efficiency

        batterySOC -= (energyFromBattery / config.batteryCapacity) * 100
        gridUsage = Math.max(0, energyNeeded - energyFromBattery)

        // Calculate grid cost with time-of-use rates
        const electricityRate = config.timeOfUseRates ? this.getTimeOfUseRate(hour) : config.gridCostPerKwh
        gridCost = gridUsage * electricityRate
      } else {
        // Excess energy - charge battery
        const energyAvailable = energyBalance
        const batterySpaceAvailable = ((100 - batterySOC) * config.batteryCapacity) / 100
        const energyToBattery = Math.min(energyAvailable, batterySpaceAvailable) * batterySpec.efficiency

        batterySOC += (energyToBattery / config.batteryCapacity) * 100
      }

      // Ensure battery SOC stays within bounds
      batterySOC = Math.max(0, Math.min(100, batterySOC))

      data.push({
        time: `${String(hour).padStart(2, "0")}:00`,
        hour,
        solar: Math.round(solarGeneration * 100) / 100,
        consumption: Math.round(consumption * 100) / 100,
        battery: Math.round(((batterySOC * config.batteryCapacity) / 100) * 100) / 100,
        batterySOC: Math.round(batterySOC * 100) / 100,
        grid: Math.round(gridUsage * 100) / 100,
        gridCost: Math.round(gridCost * 100) / 100,
        weather,
      })
    }

    // Calculate summary statistics
    const summary = this.calculateSummary(data, config)
    const economics = this.calculateEconomics(data, config, batterySpec)
    const environmental = this.calculateEnvironmentalImpact(data)

    return {
      data,
      summary,
      economics,
      environmental,
    }
  }

  private static getSimulationHours(duration: string): number {
    switch (duration) {
      case "24h":
        return 24
      case "7d":
        return 168
      case "30d":
        return 720
      case "1y":
        return 8760
      default:
        return 24
    }
  }

  private static generateWeatherConditions(hour: number, day: number, weatherData: any, useRealWeather: boolean) {
    if (!useRealWeather || !weatherData) {
      return {
        temperature: 20,
        cloudCover: 20,
        condition: "Clear",
        solarIrradiance: hour >= 6 && hour <= 18 ? 800 : 0,
      }
    }

    // Simulate realistic weather patterns
    const baseTemp = weatherData.avgTemp
    const tempVariation = 5 * Math.sin(((hour - 6) * Math.PI) / 12) // Daily temperature cycle
    const temperature = baseTemp + tempVariation + (Math.random() - 0.5) * 4

    const baseCloudCover = weatherData.cloudiness * 100
    const cloudCover = Math.max(0, Math.min(100, baseCloudCover + (Math.random() - 0.5) * 40))

    const conditions = ["Clear", "Partly Cloudy", "Cloudy", "Overcast"]
    const condition =
      cloudCover < 25
        ? conditions[0]
        : cloudCover < 50
          ? conditions[1]
          : cloudCover < 75
            ? conditions[2]
            : conditions[3]

    const maxIrradiance = 1000 // W/m²
    const solarIrradiance =
      hour >= 6 && hour <= 18 ? maxIrradiance * Math.sin(((hour - 6) * Math.PI) / 12) * (1 - cloudCover / 150) : 0

    return {
      temperature: Math.round(temperature * 10) / 10,
      cloudCover: Math.round(cloudCover),
      condition,
      solarIrradiance: Math.round(solarIrradiance),
    }
  }

  private static calculateSolarGeneration(
    hour: number,
    solarCapacity: number,
    weather: any,
    inverterEfficiency: number,
    systemLosses: number,
  ): number {
    if (hour < 6 || hour > 18) return 0

    const peakSunHours = Math.sin(((hour - 6) * Math.PI) / 12)
    const weatherFactor = weather.solarIrradiance / 1000
    const efficiencyFactor = (inverterEfficiency / 100) * (1 - systemLosses / 100)

    return solarCapacity * peakSunHours * weatherFactor * efficiencyFactor
  }

  private static getTimeOfUseRate(hour: number): number {
    // Peak hours: 4-9 PM
    if (hour >= 16 && hour <= 21) return 0.35
    // Mid-peak hours: 10 AM - 4 PM
    if (hour >= 10 && hour <= 15) return 0.25
    // Off-peak hours: 9 PM - 10 AM
    return 0.15
  }

  private static calculateSummary(data: SimulationDataPoint[], config: SimulationConfig) {
    const totalSolar = data.reduce((sum, point) => sum + point.solar, 0)
    const totalConsumption = data.reduce((sum, point) => sum + point.consumption, 0)
    const totalGrid = data.reduce((sum, point) => sum + point.grid, 0)
    const avgBattery = data.reduce((sum, point) => sum + point.batterySOC, 0) / data.length
    const peakDemand = Math.max(...data.map((point) => point.consumption))
    const solarUtilization = totalConsumption > 0 ? (totalSolar / totalConsumption) * 100 : 0
    const gridIndependence = totalConsumption > 0 ? ((totalConsumption - totalGrid) / totalConsumption) * 100 : 0

    return {
      totalSolar: Math.round(totalSolar * 100) / 100,
      totalConsumption: Math.round(totalConsumption * 100) / 100,
      totalGrid: Math.round(totalGrid * 100) / 100,
      avgBattery: Math.round(avgBattery * 100) / 100,
      peakDemand: Math.round(peakDemand * 100) / 100,
      solarUtilization: Math.round(solarUtilization * 100) / 100,
      gridIndependence: Math.round(gridIndependence * 100) / 100,
    }
  }

  private static calculateEconomics(data: SimulationDataPoint[], config: SimulationConfig, batterySpec: any) {
    const dailyCost = data.reduce((sum, point) => sum + point.gridCost, 0)
    const monthlyCost = dailyCost * 30
    const annualCost = dailyCost * 365

    // Calculate system costs
    const solarSystemCost = config.solarEnabled ? config.solarCapacity * 1000 * config.solarCostPerWatt : 0
    const batterySystemCost = config.batteryCapacity * batterySpec.costPerKwh
    const totalSystemCost = solarSystemCost + batterySystemCost

    // Calculate savings
    const baselineAnnualCost = data.reduce((sum, point) => sum + point.consumption * config.gridCostPerKwh, 0) * 365
    const totalSavings = baselineAnnualCost - annualCost

    // Calculate financial metrics
    const paybackPeriod = totalSavings > 0 ? totalSystemCost / totalSavings : 0
    const roi = totalSavings > 0 ? (totalSavings / totalSystemCost) * 100 : 0

    // Net Present Value calculation
    let npv = -totalSystemCost
    for (let year = 1; year <= config.systemLifespan; year++) {
      npv += totalSavings / Math.pow(1 + config.discountRate, year)
    }

    return {
      dailyCost: Math.round(dailyCost * 100) / 100,
      monthlyCost: Math.round(monthlyCost * 100) / 100,
      annualCost: Math.round(annualCost * 100) / 100,
      totalSavings: Math.round(totalSavings * 100) / 100,
      paybackPeriod: Math.round(paybackPeriod * 100) / 100,
      roi: Math.round(roi * 100) / 100,
      netPresentValue: Math.round(npv * 100) / 100,
    }
  }

  private static calculateEnvironmentalImpact(data: SimulationDataPoint[]) {
    const totalSolar = data.reduce((sum, point) => sum + point.solar, 0)

    // CO2 emissions factor: 0.5 kg CO2 per kWh from grid
    const co2Saved = totalSolar * 0.5

    // Trees equivalent: 1 tree absorbs ~22 kg CO2 per year
    const treesEquivalent = co2Saved / 22

    // Coal avoided: 1 kWh solar = ~0.5 kg coal avoided
    const coalAvoided = totalSolar * 0.5

    return {
      co2Saved: Math.round(co2Saved * 100) / 100,
      treesEquivalent: Math.round(treesEquivalent * 100) / 100,
      coalAvoided: Math.round(coalAvoided * 100) / 100,
    }
  }
}


--------------------------------------------------------------------------------
FILE: lib/simulation/projects.ts
--------------------------------------------------------------------------------
import type { SimulationConfig, SimulationResult } from "./simulationConfig" // Assuming SimulationConfig and SimulationResult are defined in another file

export interface Project {
  id: string
  name: string
  description?: string
  config: SimulationConfig
  results?: SimulationResult
  createdAt: Date
  updatedAt: Date
  userId: string
  isPublic: boolean
  tags: string[]
}

export class ProjectManager {
  static async saveProject(project: Omit<Project, "id" | "createdAt" | "updatedAt">): Promise<Project> {
    const newProject: Project = {
      ...project,
      id: this.generateId(),
      createdAt: new Date(),
      updatedAt: new Date(),
    }

    // In production, save to database
    const projects = this.getStoredProjects()
    projects.push(newProject)
    localStorage.setItem("voltsphere_projects", JSON.stringify(projects))

    return newProject
  }

  static async getProjects(userId: string): Promise<Project[]> {
    // In production, fetch from database
    const projects = this.getStoredProjects()
    return projects.filter((p) => p.userId === userId)
  }

  static async getProject(id: string): Promise<Project | null> {
    const projects = this.getStoredProjects()
    return projects.find((p) => p.id === id) || null
  }

  static async updateProject(id: string, updates: Partial<Project>): Promise<Project | null> {
    const projects = this.getStoredProjects()
    const index = projects.findIndex((p) => p.id === id)

    if (index === -1) return null

    projects[index] = {
      ...projects[index],
      ...updates,
      updatedAt: new Date(),
    }

    localStorage.setItem("voltsphere_projects", JSON.stringify(projects))
    return projects[index]
  }

  static async deleteProject(id: string): Promise<boolean> {
    const projects = this.getStoredProjects()
    const filteredProjects = projects.filter((p) => p.id !== id)

    if (filteredProjects.length === projects.length) return false

    localStorage.setItem("voltsphere_projects", JSON.stringify(filteredProjects))
    return true
  }

  private static getStoredProjects(): Project[] {
    if (typeof window === "undefined") return []

    try {
      const stored = localStorage.getItem("voltsphere_projects")
      return stored ? JSON.parse(stored) : []
    } catch {
      return []
    }
  }

  private static generateId(): string {
    return Math.random().toString(36).substr(2, 9)
  }
}


--------------------------------------------------------------------------------
FILE: lib/simulation/simulationConfig.ts
--------------------------------------------------------------------------------
// Re-export types from engine.ts to fix import issues
export type { SimulationConfig, SimulationResult } from "./engine"


--------------------------------------------------------------------------------
FILE: lib/stripe-client.ts
--------------------------------------------------------------------------------
import { loadStripe } from "@stripe/stripe-js"
import { config } from "./config"

// Initialize Stripe.js with your publishable key
export const stripePromise = loadStripe(config.stripe.publishableKey)

// Helper function to get Stripe instance
export const getStripeInstance = async () => {
  const stripe = await stripePromise
  if (!stripe) {
    throw new Error("Failed to initialize Stripe")
  }
  return stripe
}


--------------------------------------------------------------------------------
FILE: lib/stripe-products.ts
--------------------------------------------------------------------------------
// Stripe product configuration with your actual product IDs
export const STRIPE_PRODUCT_CONFIG = {
  starter: {
    productId: "prod_SSsFu4AsGI7SNy",
    name: "Starter Plan",
    description: "Perfect for small residential projects",
    features: ["Basic solar simulation", "Up to 5 projects", "Standard weather data", "Email support"],
  },
  pro: {
    productId: "prod_SSsCk4SnLK47w5",
    name: "Pro Plan",
    description: "Advanced features for professionals",
    features: [
      "Advanced simulation engine",
      "Unlimited projects",
      "Real-time weather data",
      "Priority support",
      "Export capabilities",
    ],
  },
  growth: {
    productId: "prod_SSsGm02p67BVi8",
    name: "Growth Plan",
    description: "Comprehensive solution for growing businesses",
    features: ["Everything in Pro", "Team collaboration", "API access", "Custom integrations", "Dedicated support"],
  },
}

// Function to get product config by tier
export function getProductConfig(tier: string) {
  return STRIPE_PRODUCT_CONFIG[tier as keyof typeof STRIPE_PRODUCT_CONFIG]
}


--------------------------------------------------------------------------------
FILE: lib/stripe.ts
--------------------------------------------------------------------------------
import Stripe from "stripe"
import { config } from "./config"

// Initialize stripe only if the secret key is available
let stripeInstance: Stripe | null = null

if (typeof process !== "undefined" && process.env.STRIPE_SECRET_KEY) {
  stripeInstance = new Stripe(process.env.STRIPE_SECRET_KEY, {
    apiVersion: "2024-06-20",
    typescript: true,
  })
} else if (config.stripe.secretKey) {
  stripeInstance = new Stripe(config.stripe.secretKey, {
    apiVersion: "2024-06-20",
    typescript: true,
  })
}

export const stripe = stripeInstance

export const webhookSecret = config.stripe.webhookSecret

// Stripe Product IDs
export const STRIPE_PRODUCTS = {
  starter: "prod_SSsFu4AsGI7SNy",
  pro: "prod_SSsCk4SnLK47w5",
  growth: "prod_SSsGm02p67BVi8",
  enterprise: "prod_enterprise_placeholder", // Add when available
}

// Stripe Price IDs with Monthly and Yearly options - FIXED STRUCTURE
export const STRIPE_PRICES = {
  starter: {
    monthly: "price_1RXwUlRrbGbUFaw4ZDUrkDuw", // $29/month
    yearly: "price_1RXxFvRrbGbUFaw4sy7qC10I", // $290/year
  },
  pro: {
    monthly: "price_1RXwSZRrbGbUFaw4b6XcsfzZ", // $5.99/month
    yearly: "price_1RXxGpRrbGbUFaw4QSy8Onqo", // $599.99/year
  },
  growth: {
    monthly: "price_1RXwVWRrbGbUFaw45MImf6dO", // $99/month
    yearly: "price_1RXxELRrbGbUFaw40CcIvd2f", // $990/year
  },
  enterprise: {
    monthly: "price_enterprise_monthly", // Add when available
    yearly: "price_enterprise_yearly", // Add when available
  },
}

// Pricing information for display
export const PRICING_INFO = {
  starter: {
    name: "Starter",
    monthly: { price: 29, priceId: "price_1RXwUlRrbGbUFaw4ZDUrkDuw" },
    yearly: { price: 290, priceId: "price_1RXxFvRrbGbUFaw4sy7qC10I", savings: "17%" },
  },
  pro: {
    name: "Pro",
    monthly: { price: 5.99, priceId: "price_1RXwSZRrbGbUFaw4b6XcsfzZ" },
    yearly: { price: 599.99, priceId: "price_1RXxGpRrbGbUFaw4QSy8Onqo", savings: "17%" },
  },
  growth: {
    name: "Growth",
    monthly: { price: 99, priceId: "price_1RXwVWRrbGbUFaw45MImf6dO" },
    yearly: { price: 990, priceId: "price_1RXxELRrbGbUFaw40CcIvd2f", savings: "17%" },
  },
}

// Define the SubscriptionTier type
export type SubscriptionTier = "free" | "starter" | "pro" | "growth" | "enterprise"
export type BillingInterval = "monthly" | "yearly"

// Helper function to get price ID by tier and interval
export function getPriceId(tier: SubscriptionTier, interval: BillingInterval = "monthly"): string | null {
  if (tier === "free") return null

  const tierPrices = STRIPE_PRICES[tier as keyof typeof STRIPE_PRICES]
  if (!tierPrices) return null

  return tierPrices[interval] || null
}

// Helper function to get product ID by tier
export function getProductId(tier: SubscriptionTier): string | null {
  if (tier === "free") return null
  return STRIPE_PRODUCTS[tier as keyof typeof STRIPE_PRODUCTS] || null
}

// Helper function to get pricing info
export function getPricingInfo(tier: SubscriptionTier) {
  if (tier === "free") return null
  return PRICING_INFO[tier as keyof typeof PRICING_INFO] || null
}

// Function to get Stripe for client-side
export function getStripe() {
  return stripe
}

// Check if Stripe is properly initialized
export function isStripeConfigured(): boolean {
  return !!stripe
}


--------------------------------------------------------------------------------
FILE: lib/subscription.ts
--------------------------------------------------------------------------------
import { stripe } from "./stripe"
import { config } from "./config"
import type { SubscriptionTier } from "./stripe"

export async function createCheckoutSession(
  email: string,
  priceId: string,
  tier: SubscriptionTier,
  successUrl?: string,
  cancelUrl?: string,
) {
  try {
    const session = await stripe.checkout.sessions.create({
      customer_email: email,
      payment_method_types: ["card"],
      line_items: [
        {
          price: priceId,
          quantity: 1,
        },
      ],
      mode: "subscription",
      success_url: successUrl || `${config.app.url}/billing/success?session_id={CHECKOUT_SESSION_ID}`,
      cancel_url: cancelUrl || `${config.app.url}/pricing`,
      metadata: {
        tier,
        email,
      },
      subscription_data: {
        metadata: {
          tier,
          email,
        },
      },
    })

    return {
      url: session.url,
      sessionId: session.id,
    }
  } catch (error) {
    console.error("Error creating checkout session:", error)
    throw error
  }
}

// Add the missing createCustomerPortalSession export
export async function createCustomerPortalSession(customerId: string) {
  try {
    const session = await stripe.billingPortal.sessions.create({
      customer: customerId,
      return_url: `${config.app.url}/billing`,
    })

    return { url: session.url }
  } catch (error) {
    console.error("Error creating customer portal session:", error)
    throw error
  }
}

// Keep the existing createPortalSession function for backward compatibility
export async function createPortalSession(customerId: string) {
  return createCustomerPortalSession(customerId)
}

export function getSubscriptionLimits(tier: SubscriptionTier) {
  switch (tier) {
    case "free":
      return {
        simulationsPerDay: 3,
        canExport: false,
        canSaveProjects: false,
        apiCalls: 0,
      }
    case "pro":
      return {
        simulationsPerDay: -1, // unlimited
        canExport: true,
        canSaveProjects: true,
        apiCalls: 0,
      }
    case "starter":
      return {
        simulationsPerDay: -1,
        canExport: true,
        canSaveProjects: true,
        apiCalls: 5000,
      }
    case "growth":
      return {
        simulationsPerDay: -1,
        canExport: true,
        canSaveProjects: true,
        apiCalls: 50000,
      }
    case "enterprise":
      return {
        simulationsPerDay: -1,
        canExport: true,
        canSaveProjects: true,
        apiCalls: -1, // unlimited
      }
    default:
      return getSubscriptionLimits("free")
  }
}


--------------------------------------------------------------------------------
FILE: lib/utils.ts
--------------------------------------------------------------------------------
import { clsx, type ClassValue } from "clsx"
import { twMerge } from "tailwind-merge"

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}


################################################################################
DIRECTORY: public
################################################################################

--------------------------------------------------------------------------------
FILE: public/placeholder-logo.png
--------------------------------------------------------------------------------
[Could not read file: 'utf-8' codec can't decode byte 0x89 in position 0: invalid start byte]

--------------------------------------------------------------------------------
FILE: public/placeholder-logo.svg
--------------------------------------------------------------------------------
<svg xmlns="http://www.w3.org/2000/svg" width="215" height="48" fill="none"><path fill="#000" d="M57.588 9.6h6L73.828 38h-5.2l-2.36-6.88h-11.36L52.548 38h-5.2l10.24-28.4Zm7.16 17.16-4.16-12.16-4.16 12.16h8.32Zm23.694-2.24c-.186-1.307-.706-2.32-1.56-3.04-.853-.72-1.866-1.08-3.04-1.08-1.68 0-2.986.613-3.92 1.84-.906 1.227-1.36 2.947-1.36 5.16s.454 3.933 1.36 5.16c.934 1.227 2.24 1.84 3.92 1.84 1.254 0 2.307-.373 3.16-1.12.854-.773 1.387-1.867 1.6-3.28l5.12.24c-.186 1.68-.733 3.147-1.64 4.4-.906 1.227-2.08 2.173-3.52 2.84-1.413.667-2.986 1-4.72 1-2.08 0-3.906-.453-5.48-1.36-1.546-.907-2.76-2.2-3.64-3.88-.853-1.68-1.28-3.627-1.28-5.84 0-2.24.427-4.187 1.28-5.84.88-1.68 2.094-2.973 3.64-3.88 1.574-.907 3.4-1.36 5.48-1.36 1.68 0 3.227.32 4.64.96 1.414.64 2.56 1.56 3.44 2.76.907 1.2 1.454 2.6 1.64 4.2l-5.12.28Zm11.486-7.72.12 3.4c.534-1.227 1.307-2.173 2.32-2.84 1.04-.693 2.267-1.04 3.68-1.04 1.494 0 2.76.387 3.8 1.16 1.067.747 1.827 1.813 2.28 3.2.507-1.44 1.294-2.52 2.36-3.24 1.094-.747 2.414-1.12 3.96-1.12 1.414 0 2.64.307 3.68.92s1.84 1.52 2.4 2.72c.56 1.2.84 2.667.84 4.4V38h-4.96V25.92c0-1.813-.293-3.187-.88-4.12-.56-.96-1.413-1.44-2.56-1.44-.906 0-1.68.213-2.32.64-.64.427-1.133 1.053-1.48 1.88-.32.827-.48 1.84-.48 3.04V38h-4.56V25.92c0-1.2-.133-2.213-.4-3.04-.24-.827-.626-1.453-1.16-1.88-.506-.427-1.133-.64-1.88-.64-.906 0-1.68.227-2.32.68-.64.427-1.133 1.053-1.48 1.88-.32.827-.48 1.827-.48 3V38h-4.96V16.8h4.48Zm26.723 10.6c0-2.24.427-4.187 1.28-5.84.854-1.68 2.067-2.973 3.64-3.88 1.574-.907 3.4-1.36 5.48-1.36 1.84 0 3.494.413 4.96 1.24 1.467.827 2.64 2.08 3.52 3.76.88 1.653 1.347 3.693 1.4 6.12v1.32h-15.08c.107 1.813.614 3.227 1.52 4.24.907.987 2.134 1.48 3.68 1.48.987 0 1.88-.253 2.68-.76a4.803 4.803 0 0 0 1.84-2.2l5.08.36c-.64 2.027-1.84 3.64-3.6 4.84-1.733 1.173-3.733 1.76-6 1.76-2.08 0-3.906-.453-5.48-1.36-1.573-.907-2.786-2.2-3.64-3.88-.853-1.68-1.28-3.627-1.28-5.84Zm15.16-2.04c-.213-1.733-.76-3.013-1.64-3.84-.853-.827-1.893-1.24-3.12-1.24-1.44 0-2.6.453-3.48 1.36-.88.88-1.44 2.12-1.68 3.72h9.92ZM163.139 9.6V38h-5.04V9.6h5.04Zm8.322 7.2.24 5.88-.64-.36c.32-2.053 1.094-3.56 2.32-4.52 1.254-.987 2.787-1.48 4.6-1.48 2.32 0 4.107.733 5.36 2.2 1.254 1.44 1.88 3.387 1.88 5.84V38h-4.96V25.92c0-1.253-.12-2.28-.36-3.08-.24-.8-.64-1.413-1.2-1.84-.533-.427-1.253-.64-2.16-.64-1.44 0-2.573.48-3.4 1.44-.8.933-1.2 2.307-1.2 4.12V38h-4.96V16.8h4.48Zm30.003 7.72c-.186-1.307-.706-2.32-1.56-3.04-.853-.72-1.866-1.08-3.04-1.08-1.68 0-2.986.613-3.92 1.84-.906 1.227-1.36 2.947-1.36 5.16s.454 3.933 1.36 5.16c.934 1.227 2.24 1.84 3.92 1.84 1.254 0 2.307-.373 3.16-1.12.854-.773 1.387-1.867 1.6-3.28l5.12.24c-.186 1.68-.733 3.147-1.64 4.4-.906 1.227-2.08 2.173-3.52 2.84-1.413.667-2.986 1-4.72 1-2.08 0-3.906-.453-5.48-1.36-1.546-.907-2.76-2.2-3.64-3.88-.853-1.68-1.28-3.627-1.28-5.84 0-2.24.427-4.187 1.28-5.84.88-1.68 2.094-2.973 3.64-3.88 1.574-.907 3.4-1.36 5.48-1.36 1.68 0 3.227.32 4.64.96 1.414.64 2.56 1.56 3.44 2.76.907 1.2 1.454 2.6 1.64 4.2l-5.12.28Zm11.443 8.16V38h-5.6v-5.32h5.6Z"/><path fill="#171717" fill-rule="evenodd" d="m7.839 40.783 16.03-28.054L20 6 0 40.783h7.839Zm8.214 0H40L27.99 19.894l-4.02 7.032 3.976 6.914H20.02l-3.967 6.943Z" clip-rule="evenodd"/></svg>

--------------------------------------------------------------------------------
FILE: public/placeholder-user.jpg
--------------------------------------------------------------------------------
[Could not read file: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte]

--------------------------------------------------------------------------------
FILE: public/placeholder.jpg
--------------------------------------------------------------------------------
[Could not read file: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte]

--------------------------------------------------------------------------------
FILE: public/placeholder.svg
--------------------------------------------------------------------------------
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="1200" fill="none"><rect width="1200" height="1200" fill="#EAEAEA" rx="3"/><g opacity=".5"><g opacity=".5"><path fill="#FAFAFA" d="M600.709 736.5c-75.454 0-136.621-61.167-136.621-136.62 0-75.454 61.167-136.621 136.621-136.621 75.453 0 136.62 61.167 136.62 136.621 0 75.453-61.167 136.62-136.62 136.62Z"/><path stroke="#C9C9C9" stroke-width="2.418" d="M600.709 736.5c-75.454 0-136.621-61.167-136.621-136.62 0-75.454 61.167-136.621 136.621-136.621 75.453 0 136.62 61.167 136.62 136.621 0 75.453-61.167 136.62-136.62 136.62Z"/></g><path stroke="url(#a)" stroke-width="2.418" d="M0-1.209h553.581" transform="scale(1 -1) rotate(45 1163.11 91.165)"/><path stroke="url(#b)" stroke-width="2.418" d="M404.846 598.671h391.726"/><path stroke="url(#c)" stroke-width="2.418" d="M599.5 795.742V404.017"/><path stroke="url(#d)" stroke-width="2.418" d="m795.717 796.597-391.441-391.44"/><path fill="#fff" d="M600.709 656.704c-31.384 0-56.825-25.441-56.825-56.824 0-31.384 25.441-56.825 56.825-56.825 31.383 0 56.824 25.441 56.824 56.825 0 31.383-25.441 56.824-56.824 56.824Z"/><g clip-path="url(#e)"><path fill="#666" fill-rule="evenodd" d="M616.426 586.58h-31.434v16.176l3.553-3.554.531-.531h9.068l.074-.074 8.463-8.463h2.565l7.18 7.181V586.58Zm-15.715 14.654 3.698 3.699 1.283 1.282-2.565 2.565-1.282-1.283-5.2-5.199h-6.066l-5.514 5.514-.073.073v2.876a2.418 2.418 0 0 0 2.418 2.418h26.598a2.418 2.418 0 0 0 2.418-2.418v-8.317l-8.463-8.463-7.181 7.181-.071.072Zm-19.347 5.442v4.085a6.045 6.045 0 0 0 6.046 6.045h26.598a6.044 6.044 0 0 0 6.045-6.045v-7.108l1.356-1.355-1.282-1.283-.074-.073v-17.989h-38.689v23.43l-.146.146.146.147Z" clip-rule="evenodd"/></g><path stroke="#C9C9C9" stroke-width="2.418" d="M600.709 656.704c-31.384 0-56.825-25.441-56.825-56.824 0-31.384 25.441-56.825 56.825-56.825 31.383 0 56.824 25.441 56.824 56.825 0 31.383-25.441 56.824-56.824 56.824Z"/></g><defs><linearGradient id="a" x1="554.061" x2="-.48" y1=".083" y2=".087" gradientUnits="userSpaceOnUse"><stop stop-color="#C9C9C9" stop-opacity="0"/><stop offset=".208" stop-color="#C9C9C9"/><stop offset=".792" stop-color="#C9C9C9"/><stop offset="1" stop-color="#C9C9C9" stop-opacity="0"/></linearGradient><linearGradient id="b" x1="796.912" x2="404.507" y1="599.963" y2="599.965" gradientUnits="userSpaceOnUse"><stop stop-color="#C9C9C9" stop-opacity="0"/><stop offset=".208" stop-color="#C9C9C9"/><stop offset=".792" stop-color="#C9C9C9"/><stop offset="1" stop-color="#C9C9C9" stop-opacity="0"/></linearGradient><linearGradient id="c" x1="600.792" x2="600.794" y1="403.677" y2="796.082" gradientUnits="userSpaceOnUse"><stop stop-color="#C9C9C9" stop-opacity="0"/><stop offset=".208" stop-color="#C9C9C9"/><stop offset=".792" stop-color="#C9C9C9"/><stop offset="1" stop-color="#C9C9C9" stop-opacity="0"/></linearGradient><linearGradient id="d" x1="404.85" x2="796.972" y1="403.903" y2="796.02" gradientUnits="userSpaceOnUse"><stop stop-color="#C9C9C9" stop-opacity="0"/><stop offset=".208" stop-color="#C9C9C9"/><stop offset=".792" stop-color="#C9C9C9"/><stop offset="1" stop-color="#C9C9C9" stop-opacity="0"/></linearGradient><clipPath id="e"><path fill="#fff" d="M581.364 580.535h38.689v38.689h-38.689z"/></clipPath></defs></svg>

################################################################################
DIRECTORY: styles
################################################################################

--------------------------------------------------------------------------------
FILE: styles/globals.css
--------------------------------------------------------------------------------
@tailwind base;
@tailwind components;
@tailwind utilities;

body {
  font-family: Arial, Helvetica, sans-serif;
}

@layer utilities {
  .text-balance {
    text-wrap: balance;
  }
}

@layer base {
  :root {
    --background: 0 0% 100%;
    --foreground: 0 0% 3.9%;
    --card: 0 0% 100%;
    --card-foreground: 0 0% 3.9%;
    --popover: 0 0% 100%;
    --popover-foreground: 0 0% 3.9%;
    --primary: 0 0% 9%;
    --primary-foreground: 0 0% 98%;
    --secondary: 0 0% 96.1%;
    --secondary-foreground: 0 0% 9%;
    --muted: 0 0% 96.1%;
    --muted-foreground: 0 0% 45.1%;
    --accent: 0 0% 96.1%;
    --accent-foreground: 0 0% 9%;
    --destructive: 0 84.2% 60.2%;
    --destructive-foreground: 0 0% 98%;
    --border: 0 0% 89.8%;
    --input: 0 0% 89.8%;
    --ring: 0 0% 3.9%;
    --chart-1: 12 76% 61%;
    --chart-2: 173 58% 39%;
    --chart-3: 197 37% 24%;
    --chart-4: 43 74% 66%;
    --chart-5: 27 87% 67%;
    --radius: 0.5rem;
    --sidebar-background: 0 0% 98%;
    --sidebar-foreground: 240 5.3% 26.1%;
    --sidebar-primary: 240 5.9% 10%;
    --sidebar-primary-foreground: 0 0% 98%;
    --sidebar-accent: 240 4.8% 95.9%;
    --sidebar-accent-foreground: 240 5.9% 10%;
    --sidebar-border: 220 13% 91%;
    --sidebar-ring: 217.2 91.2% 59.8%;
  }

  .dark {
    --background: 0 0% 3.9%;
    --foreground: 0 0% 98%;
    --card: 0 0% 3.9%;
    --card-foreground: 0 0% 98%;
    --popover: 0 0% 3.9%;
    --popover-foreground: 0 0% 98%;
    --primary: 0 0% 98%;
    --primary-foreground: 0 0% 9%;
    --secondary: 0 0% 14.9%;
    --secondary-foreground: 0 0% 98%;
    --muted: 0 0% 14.9%;
    --muted-foreground: 0 0% 63.9%;
    --accent: 0 0% 14.9%;
    --accent-foreground: 0 0% 98%;
    --destructive: 0 62.8% 30.6%;
    --destructive-foreground: 0 0% 98%;
    --border: 0 0% 14.9%;
    --input: 0 0% 14.9%;
    --ring: 0 0% 83.1%;
    --chart-1: 220 70% 50%;
    --chart-2: 160 60% 45%;
    --chart-3: 30 80% 55%;
    --chart-4: 280 65% 60%;
    --chart-5: 340 75% 55%;
    --sidebar-background: 240 5.9% 10%;
    --sidebar-foreground: 240 4.8% 95.9%;
    --sidebar-primary: 224.3 76.3% 48%;
    --sidebar-primary-foreground: 0 0% 100%;
    --sidebar-accent: 240 3.7% 15.9%;
    --sidebar-accent-foreground: 240 4.8% 95.9%;
    --sidebar-border: 240 3.7% 15.9%;
    --sidebar-ring: 217.2 91.2% 59.8%;
  }
}

@layer base {
  * {
    @apply border-border;
  }
  body {
    @apply bg-background text-foreground;
  }
}


################################################################################
DIRECTORY: scripts
################################################################################

--------------------------------------------------------------------------------
FILE: scripts/get-stripe-prices.js
--------------------------------------------------------------------------------
// Script to help you get the actual price IDs from Stripe
// Run this to get your price IDs: node scripts/get-stripe-prices.js

const Stripe = require("stripe")

// Replace with your secret key
const stripe = new Stripe(
  "sk_test_51RXwLjRrbGbUFaw4MDYMoqHLl462VEln3gzif78xmex3uSEgaYAxWIpzS1ppT8Xd1pPp5yMJy9K2s1kYBJq2T5l9002nlkBizv",
  {
    apiVersion: "2024-06-20",
  },
)

async function getPriceIds() {
  try {
    console.log("Fetching prices from Stripe...\n")

    const prices = await stripe.prices.list({
      limit: 100,
      expand: ["data.product"],
    })

    const productIds = {
      starter: "prod_SSsFu4AsGI7SNy",
      pro: "prod_SSsCk4SnLK47w5",
      growth: "prod_SSsGm02p67BVi8",
    }

    console.log("Your Price IDs:")
    console.log("================")

    for (const [tier, productId] of Object.entries(productIds)) {
      const price = prices.data.find((p) => p.product.id === productId)
      if (price) {
        console.log(`${tier}: "${price.id}",`)
      } else {
        console.log(`${tier}: "No price found for product ${productId}",`)
      }
    }

    console.log("\nCopy these price IDs to your STRIPE_PRICES object in lib/stripe.ts")
  } catch (error) {
    console.error("Error fetching prices:", error.message)
  }
}

getPriceIds()

