#pragma once

#ifndef __CC_PLATFORM_H__
#define __CC_PLATFORM_H__

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

template< class T >
inline void cc_sprintf(char* const buffer, char const* const _format, const T& value, size_t iBufSize = 2048)
{
#ifdef __linux__
	sprintf(buffer, _format, value);
#elif _WIN32
	sprintf_s(buffer, iBufSize, _format, value);
#endif
}

template< class T >
inline int cc_sscanf(char const* const _Buffer, char const* const _Format, T* pValue)
{
#ifdef __linux__
	return sscanf(_Buffer, _Format, pValue);
#elif _WIN32
	return sscanf_s(_Buffer, _Format, pValue);
#endif
}

inline int cc_strcmp(char const* _String1, char const* _String2)
{
#ifdef __linux__
	return strcmp(_String1, _String2);
#elif _WIN32
	return strcmp(_String1, _String2);
#endif
}

inline void cc_strcpy(char* _String1, char const* _String2, size_t iSize)
{
#ifdef __linux__
	strcpy(_String1, _String2);
#elif _WIN32
	strcpy_s(_String1, iSize, _String2);
#endif
}

inline void cc_fopen(FILE **fp, char const* _FileName, char const* _Mode)
{
#ifdef __linux__
	*fp = fopen(_FileName, _Mode);
#elif _WIN32
	fopen_s(fp, _FileName, _Mode);
#endif
}

#endif // !__CC_PLATFORM_H__

