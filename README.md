# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--07_07:42:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **281,156 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **13** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-07 07:42:00 | Siyambalanduwa (Heda Oya) | 0.28 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-10-07 07:28:59 | Thalgahagoda (Nilwala Ganga) | 1.08 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-10-07 07:26:15 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-10-07 07:26:14 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-10-07 07:23:48 | Moraketiya (Walawe Ganga) | 1.40 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-07 07:21:21 | Thanthirimale (Malwathu Oya) | 0.81 | 🟢 Normal | -0.006 |  |
| 2026-10-07 07:19:46 | Panadugama (Nilwala Ganga) | 5.73 | 🟡 Alert | 0.015 | 🔺 Rising |
| 2026-10-07 07:11:05 | Badalgama (Maha Oya) | 2.87 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-10-07 07:09:03 | Baddegama (Gin Ganga) | 2.40 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-10-07 07:08:12 | Magura (Kalu Ganga) | 2.43 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-10-07 07:07:58 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | -0.048 |  |
| 2026-10-07 07:07:18 | Glencourse (Kelani Ganga) | 10.91 | 🟢 Normal | -0.028 |  |
| 2026-10-07 07:06:20 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | -0.099 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-07 07:19:46 | Panadugama (Nilwala Ganga) | 5.73 | 🟡 Alert | 0.015 | 🔺 Rising |
| 2026-10-07 07:00:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.36 | 🟢 Normal | 0.260 | 🔺 Rising |
| 2026-10-07 07:03:36 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-10-07 07:00:41 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-10-07 07:11:05 | Badalgama (Maha Oya) | 2.87 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-10-07 07:28:59 | Thalgahagoda (Nilwala Ganga) | 1.08 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-10-07 07:06:01 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-10-07 07:09:03 | Baddegama (Gin Ganga) | 2.40 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-10-07 07:03:45 | Ellagawa (Kalu Ganga) | 5.62 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-07 07:01:56 | Rathnapura (Kalu Ganga) | 1.78 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-07 07:08:12 | Magura (Kalu Ganga) | 2.43 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-10-07 07:23:48 | Moraketiya (Walawe Ganga) | 1.40 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-07 07:42:00 | Siyambalanduwa (Heda Oya) | 0.28 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-10-07 07:04:30 | Urawa (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-07 07:04:12 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-07 07:02:12 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-10-07 07:00:10 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-07 07:01:22 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-07 07:00:46 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-10-07 07:26:15 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-10-07 07:03:44 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-10-07 07:02:31 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-10-07 07:02:29 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-07 07:04:09 | Dunamale (Aththanagalu Oya) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-10-07 07:00:56 | Manampitiya (Mahaweli Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-10-07 07:21:21 | Thanthirimale (Malwathu Oya) | 0.81 | 🟢 Normal | -0.006 |  |
| 2026-10-07 07:02:44 | Giriulla (Maha Oya) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-10-07 07:02:23 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | -0.010 |  |
| 2026-10-07 07:02:48 | Nagalagam Street (Kelani Ganga) | 0.41 | 🟢 Normal | -0.017 |  |
| 2026-10-07 07:04:27 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.019 |  |
| 2026-10-07 07:05:37 | Hanwella (Kelani Ganga) | 2.73 | 🟢 Normal | -0.021 |  |
| 2026-10-07 07:07:18 | Glencourse (Kelani Ganga) | 10.91 | 🟢 Normal | -0.028 |  |
| 2026-10-07 07:04:59 | Thawalama (Gin Ganga) | 2.76 | 🟢 Normal | -0.032 |  |
| 2026-10-07 07:07:58 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | -0.048 |  |
| 2026-10-07 07:01:23 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.072 |  |
| 2026-10-07 07:01:57 | Nakkala (Kumbukkan Oya) | 0.91 | 🟢 Normal | -0.081 |  |
| 2026-10-07 07:06:20 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | -0.099 |  |
| 2026-10-07 07:05:30 | Peradeniya (Mahaweli Ganga) | 2.72 | 🟢 Normal | -0.101 |  |
| 2026-10-07 07:01:10 | Pitabeddara (Nilwala Ganga) | 1.60 | 🟢 Normal | -0.490 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)