# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--25_21:11:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **270,908 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Magura — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-25 21:11:16 | Thawalama (Gin Ganga) | 3.52 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-25 21:10:12 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-25 21:09:03 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-25 21:08:43 | Holombuwa (Kelani Ganga) | 1.28 | 🟢 Normal | -0.019 |  |
| 2026-09-25 21:07:12 | Thalgahagoda (Nilwala Ganga) | 1.91 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-25 21:07:07 | Baddegama (Gin Ganga) | 4.75 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-25 21:07:03 | Moraketiya (Walawe Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-09-25 21:06:42 | Magura (Kalu Ganga) | 4.78 | 🟡 Alert | -0.010 |  |
| 2026-09-25 21:06:41 | Putupaula (Kalu Ganga) | 2.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-25 21:06:16 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-25 21:05:50 | Urawa (Nilwala Ganga) | 1.19 | 🟢 Normal | -0.037 |  |
| 2026-09-25 21:05:43 | Glencourse (Kelani Ganga) | 13.75 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-09-25 21:05:35 | Kithulgala (Kelani Ganga) | 3.07 | 🟡 Alert | -0.083 |  |
| 2026-09-25 21:05:32 | Rathnapura (Kalu Ganga) | 5.88 | 🟡 Alert | -0.071 |  |
| 2026-09-25 21:04:33 | Nawalapitiya (Mahaweli Ganga) | 2.75 | 🟢 Normal | -0.102 |  |
| 2026-09-25 21:04:27 | Panadugama (Nilwala Ganga) | 6.30 | 🟠 Minor Flood | -0.030 |  |
| 2026-09-25 21:03:52 | Ellagawa (Kalu Ganga) | 8.95 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-25 21:03:39 | Hanwella (Kelani Ganga) | 5.86 | 🟢 Normal | -0.031 |  |
| 2026-09-25 21:03:09 | Giriulla (Maha Oya) | 1.94 | 🟢 Normal | -0.020 |  |
| 2026-09-25 21:03:06 | Deraniyagala (Kelani Ganga) | 2.60 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-09-25 21:02:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.07 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-25 21:02:49 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-25 21:02:45 | Badalgama (Maha Oya) | 3.10 | 🟢 Normal | 0.000 |  |
| 2026-09-25 21:02:29 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-25 21:02:26 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-25 21:02:22 | Dunamale (Aththanagalu Oya) | 2.74 | 🟢 Normal | -0.041 |  |
| 2026-09-25 21:02:19 | Nagalagam Street (Kelani Ganga) | 0.84 | 🟢 Normal | -0.015 |  |
| 2026-09-25 21:02:15 | Norwood (Kelani Ganga) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-09-25 21:01:57 | Peradeniya (Mahaweli Ganga) | 4.02 | 🟢 Normal | 0.000 |  |
| 2026-09-25 21:01:53 | Pitabeddara (Nilwala Ganga) | 2.36 | 🟢 Normal | -1.264 |  |
| 2026-09-25 21:01:49 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.020 |  |
| 2026-09-25 21:01:36 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-25 21:01:29 | Kuda Oya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-25 21:01:25 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-25 21:01:01 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-25 21:00:24 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-25 21:02:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.07 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-25 21:07:07 | Baddegama (Gin Ganga) | 4.75 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-25 21:07:12 | Thalgahagoda (Nilwala Ganga) | 1.91 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-25 21:04:27 | Panadugama (Nilwala Ganga) | 6.30 | 🟠 Minor Flood | -0.030 |  |
| 2026-09-25 21:06:42 | Magura (Kalu Ganga) | 4.78 | 🟡 Alert | -0.010 |  |
| 2026-09-25 21:05:32 | Rathnapura (Kalu Ganga) | 5.88 | 🟡 Alert | -0.071 |  |
| 2026-09-25 21:05:35 | Kithulgala (Kelani Ganga) | 3.07 | 🟡 Alert | -0.083 |  |
| 2026-09-25 21:03:06 | Deraniyagala (Kelani Ganga) | 2.60 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-09-25 21:05:43 | Glencourse (Kelani Ganga) | 13.75 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-09-25 21:02:49 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-25 21:03:52 | Ellagawa (Kalu Ganga) | 8.95 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-25 21:00:24 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-25 21:06:41 | Putupaula (Kalu Ganga) | 2.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-25 21:11:16 | Thawalama (Gin Ganga) | 3.52 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-25 21:01:36 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-25 21:06:16 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-25 21:01:25 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-25 21:02:29 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-25 18:01:13 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-25 21:10:12 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-25 21:01:01 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-25 21:09:03 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-25 21:02:45 | Badalgama (Maha Oya) | 3.10 | 🟢 Normal | 0.000 |  |
| 2026-09-25 18:01:42 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-25 21:01:57 | Peradeniya (Mahaweli Ganga) | 4.02 | 🟢 Normal | 0.000 |  |
| 2026-09-25 21:01:29 | Kuda Oya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-25 21:02:26 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-25 21:02:15 | Norwood (Kelani Ganga) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-09-25 21:07:03 | Moraketiya (Walawe Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-09-25 21:02:19 | Nagalagam Street (Kelani Ganga) | 0.84 | 🟢 Normal | -0.015 |  |
| 2026-09-25 21:08:43 | Holombuwa (Kelani Ganga) | 1.28 | 🟢 Normal | -0.019 |  |
| 2026-09-25 18:02:19 | Weraganthota (Mahaweli Ganga) | -2.82 | 🟢 Normal | -0.020 |  |
| 2026-09-25 21:01:49 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.020 |  |
| 2026-09-25 21:03:09 | Giriulla (Maha Oya) | 1.94 | 🟢 Normal | -0.020 |  |
| 2026-09-25 21:03:39 | Hanwella (Kelani Ganga) | 5.86 | 🟢 Normal | -0.031 |  |
| 2026-09-25 21:05:50 | Urawa (Nilwala Ganga) | 1.19 | 🟢 Normal | -0.037 |  |
| 2026-09-25 21:02:22 | Dunamale (Aththanagalu Oya) | 2.74 | 🟢 Normal | -0.041 |  |
| 2026-09-25 21:04:33 | Nawalapitiya (Mahaweli Ganga) | 2.75 | 🟢 Normal | -0.102 |  |
| 2026-09-25 21:01:53 | Pitabeddara (Nilwala Ganga) | 2.36 | 🟢 Normal | -1.264 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)