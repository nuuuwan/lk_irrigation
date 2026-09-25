# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--25_09:07:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **270,437 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Thawalama — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-25 09:07:49 | Rathnapura (Kalu Ganga) | 6.35 | 🟡 Alert | -0.054 |  |
| 2026-09-25 09:07:39 | Holombuwa (Kelani Ganga) | 1.41 | 🟢 Normal | -0.095 |  |
| 2026-09-25 09:07:22 | Giriulla (Maha Oya) | 2.09 | 🟢 Normal | -0.080 |  |
| 2026-09-25 09:06:36 | Baddegama (Gin Ganga) | 4.67 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-25 09:06:30 | Glencourse (Kelani Ganga) | 14.35 | 🟢 Normal | -0.048 |  |
| 2026-09-25 09:06:17 | Dunamale (Aththanagalu Oya) | 3.10 | 🟢 Normal | -0.019 |  |
| 2026-09-25 09:06:11 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-25 09:06:04 | Thawalama (Gin Ganga) | 4.33 | 🟡 Alert | 0.105 | 🔺 Rising |
| 2026-09-25 09:05:58 | Magura (Kalu Ganga) | 4.83 | 🟡 Alert | -0.022 |  |
| 2026-09-25 09:05:05 | Moraketiya (Walawe Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-09-25 09:04:36 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.272 | 🔺 Rising |
| 2026-09-25 09:04:36 | Ellagawa (Kalu Ganga) | 8.72 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-25 09:04:34 | Hanwella (Kelani Ganga) | 6.28 | 🟢 Normal | -0.030 |  |
| 2026-09-25 09:04:28 | Urawa (Nilwala Ganga) | 1.53 | 🟢 Normal | -0.032 |  |
| 2026-09-25 09:04:19 | Badalgama (Maha Oya) | 3.36 | 🟢 Normal | -0.020 |  |
| 2026-09-25 09:04:18 | Putupaula (Kalu Ganga) | 2.75 | 🟢 Normal | 0.000 |  |
| 2026-09-25 09:04:18 | Moragaswewa (Deduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-25 09:04:16 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.042 |  |
| 2026-09-25 09:04:12 | Nawalapitiya (Mahaweli Ganga) | 2.89 | 🟢 Normal | -0.126 |  |
| 2026-09-25 09:04:08 | Panadugama (Nilwala Ganga) | 6.52 | 🟠 Minor Flood | -0.019 |  |
| 2026-09-25 09:03:51 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-25 09:03:50 | Kithulgala (Kelani Ganga) | 2.92 | 🟢 Normal | -0.032 |  |
| 2026-09-25 09:03:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.98 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-25 09:03:25 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-25 09:03:19 | Thanthirimale (Malwathu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-25 09:02:48 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-25 09:02:32 | Norwood (Kelani Ganga) | 1.61 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-09-25 09:02:24 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | -0.100 |  |
| 2026-09-25 09:02:22 | Deraniyagala (Kelani Ganga) | 2.17 | 🟢 Normal | -0.182 |  |
| 2026-09-25 09:02:18 | Manampitiya (Mahaweli Ganga) | -0.29 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-25 09:02:16 | Thalgahagoda (Nilwala Ganga) | 1.90 | 🟠 Minor Flood | 0.031 | 🔺 Rising |
| 2026-09-25 09:02:08 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-25 09:01:48 | Peradeniya (Mahaweli Ganga) | 4.38 | 🟢 Normal | 0.185 | 🔺 Rising |
| 2026-09-25 09:01:29 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-09-25 09:00:42 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-09-25 09:00:27 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-25 09:00:24 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-25 09:02:16 | Thalgahagoda (Nilwala Ganga) | 1.90 | 🟠 Minor Flood | 0.031 | 🔺 Rising |
| 2026-09-25 09:03:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.98 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-25 09:06:36 | Baddegama (Gin Ganga) | 4.67 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-25 09:04:08 | Panadugama (Nilwala Ganga) | 6.52 | 🟠 Minor Flood | -0.019 |  |
| 2026-09-25 09:06:04 | Thawalama (Gin Ganga) | 4.33 | 🟡 Alert | 0.105 | 🔺 Rising |
| 2026-09-25 09:02:32 | Norwood (Kelani Ganga) | 1.61 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-09-25 09:05:58 | Magura (Kalu Ganga) | 4.83 | 🟡 Alert | -0.022 |  |
| 2026-09-25 09:07:49 | Rathnapura (Kalu Ganga) | 6.35 | 🟡 Alert | -0.054 |  |
| 2026-09-25 09:04:36 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.272 | 🔺 Rising |
| 2026-09-25 09:01:48 | Peradeniya (Mahaweli Ganga) | 4.38 | 🟢 Normal | 0.185 | 🔺 Rising |
| 2026-09-25 08:17:05 | Pitabeddara (Nilwala Ganga) | 2.45 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-09-25 09:04:36 | Ellagawa (Kalu Ganga) | 8.72 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-25 09:02:18 | Manampitiya (Mahaweli Ganga) | -0.29 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-25 09:00:27 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-25 09:03:51 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-25 09:04:18 | Moragaswewa (Deduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-25 08:01:45 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-25 09:03:25 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-25 09:06:11 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-25 09:00:42 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-09-25 09:05:05 | Moraketiya (Walawe Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-09-25 09:02:48 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-25 09:04:18 | Putupaula (Kalu Ganga) | 2.75 | 🟢 Normal | 0.000 |  |
| 2026-09-25 09:03:19 | Thanthirimale (Malwathu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-25 09:00:24 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-25 09:02:08 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-25 09:01:29 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-09-25 09:06:17 | Dunamale (Aththanagalu Oya) | 3.10 | 🟢 Normal | -0.019 |  |
| 2026-09-25 09:04:19 | Badalgama (Maha Oya) | 3.36 | 🟢 Normal | -0.020 |  |
| 2026-09-25 09:04:34 | Hanwella (Kelani Ganga) | 6.28 | 🟢 Normal | -0.030 |  |
| 2026-09-25 09:03:50 | Kithulgala (Kelani Ganga) | 2.92 | 🟢 Normal | -0.032 |  |
| 2026-09-25 09:04:28 | Urawa (Nilwala Ganga) | 1.53 | 🟢 Normal | -0.032 |  |
| 2026-09-25 09:04:16 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.042 |  |
| 2026-09-25 09:06:30 | Glencourse (Kelani Ganga) | 14.35 | 🟢 Normal | -0.048 |  |
| 2026-09-25 09:07:22 | Giriulla (Maha Oya) | 2.09 | 🟢 Normal | -0.080 |  |
| 2026-09-25 09:07:39 | Holombuwa (Kelani Ganga) | 1.41 | 🟢 Normal | -0.095 |  |
| 2026-09-25 09:02:24 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | -0.100 |  |
| 2026-09-25 09:04:12 | Nawalapitiya (Mahaweli Ganga) | 2.89 | 🟢 Normal | -0.126 |  |
| 2026-09-25 09:02:22 | Deraniyagala (Kelani Ganga) | 2.17 | 🟢 Normal | -0.182 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)