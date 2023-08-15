#include "gtest/gtest.h"

extern "C"
{
#include "testy/func.h"
}

TEST(func_ok, ok)
{
    ASSERT_EQ(func_ok(1, 1), 1);
}

TEST(func_ok, not_ok)
{
    ASSERT_EQ(func_ok(2, 2), 0);
}

TEST(testy, not_ok)
{
    ASSERT_EQ(func_ok(-1, -1), 0);
}

TEST(testy, ok)
{
    ASSERT_EQ(func_ok(2, 0), 1);
}