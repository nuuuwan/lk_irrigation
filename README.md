# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--25_17:05:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **270,747 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-25 17:05:55 | Glencourse (Kelani Ganga) | 13.65 | 🟢 Normal | -0.086 |  |
| 2026-09-25 17:05:52 | Badalgama (Maha Oya) | 3.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-25 17:05:34 | Magura (Kalu Ganga) | 4.80 | 🟡 Alert | 0.000 |  |
| 2026-09-25 17:04:50 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-25 17:04:27 | Putupaula (Kalu Ganga) | 2.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-25 17:04:23 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-25 17:04:08 | Kithulgala (Kelani Ganga) | 3.09 | 🟡 Alert | 0.041 | 🔺 Rising |
| 2026-09-25 17:03:53 | Ellagawa (Kalu Ganga) | 8.86 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-25 17:03:45 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-09-25 17:03:24 | Panadugama (Nilwala Ganga) | 6.39 | 🟠 Minor Flood | -0.032 |  |
| 2026-09-25 17:03:12 | Hanwella (Kelani Ganga) | 6.05 | 🟢 Normal | -0.052 |  |
| 2026-09-25 17:02:59 | Deraniyagala (Kelani Ganga) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-09-25 17:02:52 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-25 17:02:44 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-25 17:02:37 | Nawalapitiya (Mahaweli Ganga) | 2.65 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-09-25 17:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.04 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-25 17:02:34 | Rathnapura (Kalu Ganga) | 6.07 | 🟡 Alert | -0.010 |  |
| 2026-09-25 17:02:30 | Norwood (Kelani Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-09-25 17:02:14 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-25 17:02:04 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-25 17:02:03 | Weraganthota (Mahaweli Ganga) | -2.80 | 🟢 Normal | -0.020 |  |
| 2026-09-25 17:01:58 | Nagalagam Street (Kelani Ganga) | 1.01 | 🟢 Normal | -0.091 |  |
| 2026-09-25 17:01:52 | Peradeniya (Mahaweli Ganga) | 3.98 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-09-25 17:01:41 | Baddegama (Gin Ganga) | 4.74 | 🟠 Minor Flood | 0.011 | 🔺 Rising |
| 2026-09-25 17:01:26 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-25 17:01:18 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-25 17:01:16 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-25 17:00:53 | Pitabeddara (Nilwala Ganga) | 2.43 | 🟢 Normal | -0.010 |  |
| 2026-09-25 17:00:44 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-25 17:01:41 | Baddegama (Gin Ganga) | 4.74 | 🟠 Minor Flood | 0.011 | 🔺 Rising |
| 2026-09-25 17:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.04 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-25 16:11:04 | Thalgahagoda (Nilwala Ganga) | 1.90 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-25 17:03:24 | Panadugama (Nilwala Ganga) | 6.39 | 🟠 Minor Flood | -0.032 |  |
| 2026-09-25 17:04:08 | Kithulgala (Kelani Ganga) | 3.09 | 🟡 Alert | 0.041 | 🔺 Rising |
| 2026-09-25 17:05:34 | Magura (Kalu Ganga) | 4.80 | 🟡 Alert | 0.000 |  |
| 2026-09-25 17:02:34 | Rathnapura (Kalu Ganga) | 6.07 | 🟡 Alert | -0.010 |  |
| 2026-09-25 17:02:37 | Nawalapitiya (Mahaweli Ganga) | 2.65 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-09-25 17:01:52 | Peradeniya (Mahaweli Ganga) | 3.98 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-09-25 17:03:53 | Ellagawa (Kalu Ganga) | 8.86 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-25 16:15:59 | Giriulla (Maha Oya) | 1.98 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-09-25 17:05:52 | Badalgama (Maha Oya) | 3.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-25 17:04:27 | Putupaula (Kalu Ganga) | 2.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-25 17:02:14 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-25 17:01:18 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-25 17:02:52 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-25 16:01:25 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-25 17:02:04 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-25 17:01:26 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-25 17:02:44 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-25 17:02:59 | Deraniyagala (Kelani Ganga) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-09-25 15:04:17 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-25 17:00:44 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-25 17:04:23 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-25 17:04:50 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-25 17:01:16 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-25 16:03:26 | Kuda Oya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-25 17:03:45 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-09-25 17:02:30 | Norwood (Kelani Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-09-25 16:05:08 | Holombuwa (Kelani Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-09-25 17:00:53 | Pitabeddara (Nilwala Ganga) | 2.43 | 🟢 Normal | -0.010 |  |
| 2026-09-25 17:02:03 | Weraganthota (Mahaweli Ganga) | -2.80 | 🟢 Normal | -0.020 |  |
| 2026-09-25 16:16:22 | Urawa (Nilwala Ganga) | 1.35 | 🟢 Normal | -0.028 |  |
| 2026-09-25 16:01:56 | Moraketiya (Walawe Ganga) | 1.30 | 🟢 Normal | -0.031 |  |
| 2026-09-25 16:01:27 | Dunamale (Aththanagalu Oya) | 2.82 | 🟢 Normal | -0.044 |  |
| 2026-09-25 16:09:52 | Thawalama (Gin Ganga) | 3.69 | 🟢 Normal | -0.047 |  |
| 2026-09-25 17:03:12 | Hanwella (Kelani Ganga) | 6.05 | 🟢 Normal | -0.052 |  |
| 2026-09-25 17:05:55 | Glencourse (Kelani Ganga) | 13.65 | 🟢 Normal | -0.086 |  |
| 2026-09-25 17:01:58 | Nagalagam Street (Kelani Ganga) | 1.01 | 🟢 Normal | -0.091 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)