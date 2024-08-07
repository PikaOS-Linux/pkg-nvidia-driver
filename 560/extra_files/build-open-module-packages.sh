#!/bin/sh
set -e

# compilation will succeed, but the module may not be loadable due to mismatching symvers
#export IGNORE_CC_MISMATCH=1

test -x /usr/bin/module-assistant || apt-get install module-assistant

cd /usr/src

summary=
nl="
"

kernels=
slenrek=
failed=
kmin=3.10
for k in $(ls -dvr1 /lib/modules/*/build 2>/dev/null | cut -d/ -f4) ; do
	if dpkg --compare-versions "$k" lt "$kmin" ; then
		summary="${summary}SKIP $k (older than $kmin)${nl}"
		continue
	fi
	kconfig=/lib/modules/$k/build/.config
	if [ -f "$kconfig" ]; then
		if grep -q -E "^CONFIG_PREEMPT_RT=[ym]" $kconfig ; then
			summary="${summary}SKIP $k (CONFIG_PREEMPT_RT)${nl}"
			continue
		fi
		if grep -q -E "^CONFIG_PREEMPT_RT_FULL=[ym]" $kconfig ; then
			summary="${summary}SKIP $k (CONFIG_PREEMPT_RT_FULL)${nl}"
			continue
		fi
	fi
	kernels="$kernels $k"
	slenrek="$k $slenrek"
done

modules=nvidia-open-kernel

module-assistant clean $modules
for k in $kernels ; do
	ret=0
	module-assistant build --text-mode --force --kvers-list "$k" $modules || ret=$?
	if [ "$ret" = 0 ]; then
		summary="${summary}PASS $k${nl}"
	else
		failed="$failed $k"
		summary="${summary}FAIL $k ($ret)${nl}"
	fi
done

ls -l *.deb || true
for m in $modules ; do
	for k in $slenrek ; do
		echo "* ${m} ${k}:"
		ls -l ${m}-${k}_*.deb || true
	done
done

if [ -n "$summary" ]; then
	echo "Summary:"
	echo -n "$summary"
fi

for k in $failed ; do
	echo "$modules MODULE BUILD FAILED FOR $k"
done

test -z "$failed" || exit 1
