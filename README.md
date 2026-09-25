# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--25_16:16:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **270,718 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-25 16:16:22 | Urawa (Nilwala Ganga) | 1.35 | 🟢 Normal | -0.028 |  |
| 2026-09-25 16:15:59 | Giriulla (Maha Oya) | 1.98 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-09-25 16:11:04 | Thalgahagoda (Nilwala Ganga) | 1.90 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-25 16:10:05 | Glencourse (Kelani Ganga) | 13.73 | 🟢 Normal | -0.095 |  |
| 2026-09-25 16:10:03 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | -0.010 |  |
| 2026-09-25 16:09:52 | Thawalama (Gin Ganga) | 3.69 | 🟢 Normal | -0.047 |  |
| 2026-09-25 16:08:15 | Badalgama (Maha Oya) | 3.08 | 🟢 Normal | -0.028 |  |
| 2026-09-25 16:08:04 | Peradeniya (Mahaweli Ganga) | 3.95 | 🟢 Normal | 0.000 |  |
| 2026-09-25 16:06:52 | Panadugama (Nilwala Ganga) | 6.42 | 🟠 Minor Flood | -0.019 |  |
| 2026-09-25 16:05:36 | Hanwella (Kelani Ganga) | 6.10 | 🟢 Normal | -0.041 |  |
| 2026-09-25 16:05:30 | Kithulgala (Kelani Ganga) | 3.05 | 🟡 Alert | 0.100 | 🔺 Rising |
| 2026-09-25 16:05:23 | Nawalapitiya (Mahaweli Ganga) | 2.59 | 🟢 Normal | -0.010 |  |
| 2026-09-25 16:05:08 | Holombuwa (Kelani Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-09-25 16:04:59 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-25 16:04:50 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-25 16:04:41 | Putupaula (Kalu Ganga) | 2.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-25 16:04:40 | Magura (Kalu Ganga) | 4.80 | 🟡 Alert | 0.000 |  |
| 2026-09-25 16:04:33 | Ellagawa (Kalu Ganga) | 8.84 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-25 16:04:33 | Baddegama (Gin Ganga) | 4.73 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-25 16:04:06 | Rathnapura (Kalu Ganga) | 6.08 | 🟡 Alert | -0.021 |  |
| 2026-09-25 16:03:30 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-25 16:03:26 | Kuda Oya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-25 16:03:10 | Deraniyagala (Kelani Ganga) | 2.32 | 🟢 Normal | 0.335 | 🔺 Rising |
| 2026-09-25 16:02:38 | Pitabeddara (Nilwala Ganga) | 2.44 | 🟢 Normal | -0.021 |  |
| 2026-09-25 16:02:30 | Thanthirimale (Malwathu Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-25 16:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.03 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-25 16:02:13 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-09-25 16:02:02 | Norwood (Kelani Ganga) | 1.40 | 🟢 Normal | -0.030 |  |
| 2026-09-25 16:01:56 | Moraketiya (Walawe Ganga) | 1.30 | 🟢 Normal | -0.031 |  |
| 2026-09-25 16:01:50 | Nagalagam Street (Kelani Ganga) | 1.10 | 🟢 Normal | -0.046 |  |
| 2026-09-25 16:01:47 | Weraganthota (Mahaweli Ganga) | -2.78 | 🟢 Normal | -0.041 |  |
| 2026-09-25 16:01:27 | Dunamale (Aththanagalu Oya) | 2.82 | 🟢 Normal | -0.044 |  |
| 2026-09-25 16:01:26 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-25 16:01:25 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-25 16:01:22 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | -0.011 |  |
| 2026-09-25 16:01:21 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-25 16:00:49 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-09-25 16:00:09 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-25 16:04:33 | Baddegama (Gin Ganga) | 4.73 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-25 16:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.03 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-25 16:11:04 | Thalgahagoda (Nilwala Ganga) | 1.90 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-25 16:06:52 | Panadugama (Nilwala Ganga) | 6.42 | 🟠 Minor Flood | -0.019 |  |
| 2026-09-25 16:05:30 | Kithulgala (Kelani Ganga) | 3.05 | 🟡 Alert | 0.100 | 🔺 Rising |
| 2026-09-25 16:04:40 | Magura (Kalu Ganga) | 4.80 | 🟡 Alert | 0.000 |  |
| 2026-09-25 16:04:06 | Rathnapura (Kalu Ganga) | 6.08 | 🟡 Alert | -0.021 |  |
| 2026-09-25 16:03:10 | Deraniyagala (Kelani Ganga) | 2.32 | 🟢 Normal | 0.335 | 🔺 Rising |
| 2026-09-25 16:04:33 | Ellagawa (Kalu Ganga) | 8.84 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-25 16:15:59 | Giriulla (Maha Oya) | 1.98 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-09-25 16:04:41 | Putupaula (Kalu Ganga) | 2.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-25 16:01:25 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-25 16:01:21 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-25 16:03:30 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-25 16:04:50 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-25 15:04:17 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-25 16:00:09 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-25 16:04:59 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-25 16:01:26 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-25 16:02:30 | Thanthirimale (Malwathu Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-25 16:08:04 | Peradeniya (Mahaweli Ganga) | 3.95 | 🟢 Normal | 0.000 |  |
| 2026-09-25 16:03:26 | Kuda Oya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-25 16:05:23 | Nawalapitiya (Mahaweli Ganga) | 2.59 | 🟢 Normal | -0.010 |  |
| 2026-09-25 16:10:03 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | -0.010 |  |
| 2026-09-25 16:00:49 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-09-25 16:02:13 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-09-25 16:05:08 | Holombuwa (Kelani Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-09-25 16:01:22 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | -0.011 |  |
| 2026-09-25 16:02:38 | Pitabeddara (Nilwala Ganga) | 2.44 | 🟢 Normal | -0.021 |  |
| 2026-09-25 16:16:22 | Urawa (Nilwala Ganga) | 1.35 | 🟢 Normal | -0.028 |  |
| 2026-09-25 16:08:15 | Badalgama (Maha Oya) | 3.08 | 🟢 Normal | -0.028 |  |
| 2026-09-25 16:02:02 | Norwood (Kelani Ganga) | 1.40 | 🟢 Normal | -0.030 |  |
| 2026-09-25 16:01:56 | Moraketiya (Walawe Ganga) | 1.30 | 🟢 Normal | -0.031 |  |
| 2026-09-25 16:05:36 | Hanwella (Kelani Ganga) | 6.10 | 🟢 Normal | -0.041 |  |
| 2026-09-25 16:01:47 | Weraganthota (Mahaweli Ganga) | -2.78 | 🟢 Normal | -0.041 |  |
| 2026-09-25 16:01:27 | Dunamale (Aththanagalu Oya) | 2.82 | 🟢 Normal | -0.044 |  |
| 2026-09-25 16:01:50 | Nagalagam Street (Kelani Ganga) | 1.10 | 🟢 Normal | -0.046 |  |
| 2026-09-25 16:09:52 | Thawalama (Gin Ganga) | 3.69 | 🟢 Normal | -0.047 |  |
| 2026-09-25 16:10:05 | Glencourse (Kelani Ganga) | 13.73 | 🟢 Normal | -0.095 |  |

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)