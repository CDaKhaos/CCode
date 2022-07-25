#pragma once

#ifndef __CC_PLATFORM_H__
#define __CC_PLATFORM_H__


#define LINUX

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

template< class T >
inline void cc_sprintf(char* const buffer, char const* const _format, const T& value, size_t iBufSize = 2048)
{
#ifdef LINUX
	sprintf(buffer, _format, value);
#else
	sprintf_s(buffer, iBufSize, _format, value);
#endif
}

template< class T >
inline int cc_sscanf(char const* const _Buffer, char const* const _Format, T* pValue)
{
#ifdef LINUX
	return sscanf(_Buffer, _Format, pValue);
#else
	return sscanf_s(_Buffer, _Format, pValue);
#endif
}

inline int cc_strcmp(char const* _String1, char const* _String2)
{
#ifdef LINUX
	return strcmp(_String1, _String2);
#else
	return strcmp(_String1, _String2);
#endif
}

inline void cc_strcpy(char* _String1, char const* _String2, size_t iSize)
{
#ifdef LINUX
	strcpy(_String1, _String2);
#else
	strcpy_s(_String1, iSize, _String2);
#endif
}

inline void cc_fopen(FILE **fp, char const* _FileName, char const* _Mode)
{
#ifdef LINUX
	*fp = fopen(_FileName, _Mode);
#else
	fopen_s(fp, _FileName, _Mode);
#endif
}

#endif // !__CC_PLATFORM_H__

