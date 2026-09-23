# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--24_01:03:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **269,220 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Thawalama — Alert; 🟡 Baddegama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **23** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-24 01:03:48 | Badalgama (Maha Oya) | 2.58 | 🟢 Normal | -0.010 |  |
| 2026-09-24 01:03:46 | Kuda Oya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-24 01:03:38 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-24 01:03:33 | Thawalama (Gin Ganga) | 4.14 | 🟡 Alert | 0.110 | 🔺 Rising |
| 2026-09-24 01:03:25 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-09-24 01:03:15 | Thalgahagoda (Nilwala Ganga) | 1.34 | 🟢 Normal | -0.019 |  |
| 2026-09-24 01:03:06 | Deraniyagala (Kelani Ganga) | 1.87 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-24 01:02:53 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-09-24 01:02:50 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-24 01:02:41 | Glencourse (Kelani Ganga) | 12.74 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-24 01:02:36 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-24 01:02:08 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-09-24 01:02:08 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-24 01:01:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.83 | 🟠 Minor Flood | -0.034 |  |
| 2026-09-24 01:01:14 | Ellagawa (Kalu Ganga) | 7.82 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-24 01:00:35 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-24 01:00:18 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.031 |  |
| 2026-09-24 00:43:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.84 | 🟠 Minor Flood | -0.034 |  |
| 2026-09-24 00:36:11 | Rathnapura (Kalu Ganga) | 4.32 | 🟢 Normal | 0.000 |  |
| 2026-09-24 00:34:25 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-09-24 00:24:34 | Putupaula (Kalu Ganga) | 2.72 | 🟢 Normal | 0.000 |  |
| 2026-09-24 00:21:17 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-09-24 00:17:35 | Rathnapura (Kalu Ganga) | 4.32 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-24 01:01:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.83 | 🟠 Minor Flood | -0.034 |  |
| 2026-09-24 01:03:33 | Thawalama (Gin Ganga) | 4.14 | 🟡 Alert | 0.110 | 🔺 Rising |
| 2026-09-24 00:07:24 | Baddegama (Gin Ganga) | 3.65 | 🟡 Alert | 0.000 |  |
| 2026-09-24 00:07:24 | Urawa (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.318 | 🔺 Rising |
| 2026-09-24 00:05:33 | Pitabeddara (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-09-24 00:13:48 | Panadugama (Nilwala Ganga) | 4.61 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-09-24 00:07:01 | Peradeniya (Mahaweli Ganga) | 4.02 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-09-24 00:09:31 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-09-24 00:08:59 | Holombuwa (Kelani Ganga) | 1.76 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-24 01:02:41 | Glencourse (Kelani Ganga) | 12.74 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-24 01:03:25 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-09-24 00:01:04 | Kithulgala (Kelani Ganga) | 2.40 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-09-24 00:01:32 | Magura (Kalu Ganga) | 3.90 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-24 01:03:06 | Deraniyagala (Kelani Ganga) | 1.87 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-24 00:08:39 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-24 01:01:14 | Ellagawa (Kalu Ganga) | 7.82 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-24 01:02:08 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-24 01:02:08 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-09-24 01:00:35 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-24 01:02:36 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-24 00:01:22 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-24 01:02:53 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-09-24 00:21:17 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-09-24 00:05:18 | Hanwella (Kelani Ganga) | 4.57 | 🟢 Normal | 0.000 |  |
| 2026-09-24 01:02:50 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-24 01:03:38 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-24 00:03:09 | Dunamale (Aththanagalu Oya) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-09-24 00:02:32 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-24 00:24:34 | Putupaula (Kalu Ganga) | 2.72 | 🟢 Normal | 0.000 |  |
| 2026-09-24 00:02:36 | Manampitiya (Mahaweli Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-24 00:36:11 | Rathnapura (Kalu Ganga) | 4.32 | 🟢 Normal | 0.000 |  |
| 2026-09-23 18:03:31 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-24 01:03:46 | Kuda Oya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-23 18:10:48 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | -0.009 |  |
| 2026-09-24 01:03:48 | Badalgama (Maha Oya) | 2.58 | 🟢 Normal | -0.010 |  |
| 2026-09-24 00:04:45 | Nawalapitiya (Mahaweli Ganga) | 2.53 | 🟢 Normal | -0.010 |  |
| 2026-09-24 01:03:15 | Thalgahagoda (Nilwala Ganga) | 1.34 | 🟢 Normal | -0.019 |  |
| 2026-09-23 18:01:34 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | -0.020 |  |
| 2026-09-24 01:00:18 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.031 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)