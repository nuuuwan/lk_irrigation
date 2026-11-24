# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--24_19:03:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **324,682 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Moraketiya — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **13** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-24 19:03:32 | Thalgahagoda (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.056 |  |
| 2026-11-24 19:03:26 | Peradeniya (Mahaweli Ganga) | 4.10 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-11-24 19:03:20 | Moraketiya (Walawe Ganga) | 3.10 | 🟡 Alert | 0.224 | 🔺 Rising |
| 2026-11-24 19:02:45 | Moragaswewa (Deduru Oya) | 1.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-24 19:02:20 | Kuda Oya (Kirindi Oya) | 1.66 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-24 19:02:13 | Manampitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-24 19:02:02 | Pitabeddara (Nilwala Ganga) | 1.45 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-24 19:01:53 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-11-24 19:01:39 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-24 19:01:32 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-24 19:01:21 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-11-24 19:00:50 | Magura (Kalu Ganga) | 2.58 | 🟢 Normal | 0.300 | 🔺 Rising |
| 2026-11-24 18:20:25 | Thalgahagoda (Nilwala Ganga) | 0.92 | 🟢 Normal | -0.056 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-24 19:03:20 | Moraketiya (Walawe Ganga) | 3.10 | 🟡 Alert | 0.224 | 🔺 Rising |
| 2026-11-24 18:00:31 | Nawalapitiya (Mahaweli Ganga) | 2.45 | 🟢 Normal | 1.060 | 🔺 Rising |
| 2026-11-24 18:08:17 | Holombuwa (Kelani Ganga) | 1.61 | 🟢 Normal | 0.754 | 🔺 Rising |
| 2026-11-24 18:05:42 | Glencourse (Kelani Ganga) | 10.86 | 🟢 Normal | 0.507 | 🔺 Rising |
| 2026-11-24 18:07:08 | Dunamale (Aththanagalu Oya) | 2.36 | 🟢 Normal | 0.300 | 🔺 Rising |
| 2026-11-24 19:00:50 | Magura (Kalu Ganga) | 2.58 | 🟢 Normal | 0.300 | 🔺 Rising |
| 2026-11-24 19:03:26 | Peradeniya (Mahaweli Ganga) | 4.10 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-11-24 18:02:12 | Rathnapura (Kalu Ganga) | 1.82 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-11-24 18:06:45 | Baddegama (Gin Ganga) | 1.62 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-11-24 19:01:21 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-11-24 18:01:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.65 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-24 18:04:38 | Giriulla (Maha Oya) | 2.48 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-24 18:02:42 | Urawa (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-24 18:07:20 | Kithulgala (Kelani Ganga) | 2.11 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-11-24 18:00:10 | Horowpothana (Yan Oya) | 2.30 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-11-24 19:01:32 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-24 19:02:20 | Kuda Oya (Kirindi Oya) | 1.66 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-24 18:04:24 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-24 19:02:02 | Pitabeddara (Nilwala Ganga) | 1.45 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-24 19:02:45 | Moragaswewa (Deduru Oya) | 1.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-24 18:03:14 | Hanwella (Kelani Ganga) | 1.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-24 18:06:03 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-24 18:06:15 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-24 19:01:39 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-24 18:02:13 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-11-24 18:06:15 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-11-24 18:01:50 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-11-24 19:02:13 | Manampitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-24 18:01:28 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-24 19:01:53 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-11-24 18:04:24 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-11-24 18:04:37 | Weraganthota (Mahaweli Ganga) | -2.50 | 🟢 Normal | -0.019 |  |
| 2026-11-22 17:02:02⌛ | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-24 18:03:09 | Ellagawa (Kalu Ganga) | 5.27 | 🟢 Normal | -0.031 |  |
| 2026-11-24 18:04:14 | Thawalama (Gin Ganga) | 2.52 | 🟢 Normal | -0.032 |  |
| 2026-11-24 19:03:32 | Thalgahagoda (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.056 |  |
| 2026-11-24 18:05:07 | Badalgama (Maha Oya) | 3.66 | 🟢 Normal | -0.063 |  |
| 2026-11-24 18:08:04 | Panadugama (Nilwala Ganga) | 3.95 | 🟢 Normal | -0.068 |  |
| 2026-11-24 18:03:30 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.090 |  |

## River Water Level Charts by Station

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)