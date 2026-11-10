# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--11_02:26:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **312,489 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Dunamale — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-11 02:26:56 | Badalgama (Maha Oya) | 3.25 | 🟢 Normal | -0.024 |  |
| 2026-11-11 02:26:30 | Urawa (Nilwala Ganga) | 1.40 | 🟢 Normal | -0.007 |  |
| 2026-11-11 02:19:49 | Siyambalanduwa (Heda Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-11-11 02:18:12 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | -0.009 |  |
| 2026-11-11 02:15:21 | Panadugama (Nilwala Ganga) | 6.10 | 🟠 Minor Flood | -0.009 |  |
| 2026-11-11 02:10:32 | Holombuwa (Kelani Ganga) | 1.66 | 🟢 Normal | -0.135 |  |
| 2026-11-11 02:10:31 | Dunamale (Aththanagalu Oya) | 4.35 | 🟡 Alert | -0.027 |  |
| 2026-11-11 02:08:11 | Baddegama (Gin Ganga) | 4.27 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-11 02:08:10 | Deraniyagala (Kelani Ganga) | 1.34 | 🟢 Normal | -0.019 |  |
| 2026-11-11 02:07:49 | Magura (Kalu Ganga) | 4.08 | 🟡 Alert | -108.000 |  |
| 2026-11-11 02:07:48 | Magura (Kalu Ganga) | 4.11 | 🟡 Alert | -108.000 |  |
| 2026-11-11 02:07:32 | Nagalagam Street (Kelani Ganga) | 1.01 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-11-11 02:07:16 | Rathnapura (Kalu Ganga) | 5.34 | 🟡 Alert | -0.103 |  |
| 2026-11-11 02:06:49 | Moraketiya (Walawe Ganga) | 2.34 | 🟢 Normal | -0.047 |  |
| 2026-11-11 02:05:25 | Giriulla (Maha Oya) | 4.00 | 🟢 Normal | 0.452 | 🔺 Rising |
| 2026-11-11 02:05:13 | Pitabeddara (Nilwala Ganga) | 2.50 | 🟢 Normal | -0.066 |  |
| 2026-11-11 02:05:12 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-11 02:04:13 | Katharagama (Menik Ganga) | 0.15 | 🟢 Normal | -0.050 |  |
| 2026-11-11 02:04:13 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.098 |  |
| 2026-11-11 02:04:13 | Hanwella (Kelani Ganga) | 4.89 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-11-11 02:04:03 | Peradeniya (Mahaweli Ganga) | 4.90 | 🟢 Normal | -0.200 |  |
| 2026-11-11 02:03:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.67 | 🟠 Minor Flood | -0.545 |  |
| 2026-11-11 02:03:45 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.048 |  |
| 2026-11-11 02:03:45 | Siyambalanduwa (Heda Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-11-11 02:02:50 | Manampitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.020 |  |
| 2026-11-11 02:02:47 | Kuda Oya (Kirindi Oya) | 1.95 | 🟢 Normal | -0.039 |  |
| 2026-11-11 02:02:45 | Norwood (Kelani Ganga) | 1.35 | 🟢 Normal | -108.000 |  |
| 2026-11-11 02:02:44 | Norwood (Kelani Ganga) | 1.38 | 🟢 Normal | -108.000 |  |
| 2026-11-11 02:02:42 | Glencourse (Kelani Ganga) | 13.18 | 🟢 Normal | -0.010 |  |
| 2026-11-11 02:02:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.68 | 🟠 Minor Flood | -0.545 |  |
| 2026-11-11 02:02:29 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | -126.000 |  |
| 2026-11-11 02:02:27 | Nakkala (Kumbukkan Oya) | 1.25 | 🟢 Normal | -126.000 |  |
| 2026-11-11 02:02:11 | Thanamalwila (Kirindi Oya) | 2.00 | 🟢 Normal | -0.041 |  |
| 2026-11-11 02:01:48 | Thawalama (Gin Ganga) | 4.21 | 🟡 Alert | -0.246 |  |
| 2026-11-11 02:01:37 | Wellawaya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-11-11 02:01:21 | Ellagawa (Kalu Ganga) | 8.55 | 🟢 Normal | -0.010 |  |
| 2026-11-11 02:01:19 | Moragaswewa (Deduru Oya) | 3.21 | 🟢 Normal | -0.070 |  |
| 2026-11-11 02:01:10 | Wellawaya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-11 02:08:11 | Baddegama (Gin Ganga) | 4.27 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-11 01:07:33 | Thalgahagoda (Nilwala Ganga) | 1.72 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-11 02:15:21 | Panadugama (Nilwala Ganga) | 6.10 | 🟠 Minor Flood | -0.009 |  |
| 2026-11-11 02:03:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.67 | 🟠 Minor Flood | -0.545 |  |
| 2026-11-11 02:10:31 | Dunamale (Aththanagalu Oya) | 4.35 | 🟡 Alert | -0.027 |  |
| 2026-11-11 02:07:16 | Rathnapura (Kalu Ganga) | 5.34 | 🟡 Alert | -0.103 |  |
| 2026-11-11 02:01:48 | Thawalama (Gin Ganga) | 4.21 | 🟡 Alert | -0.246 |  |
| 2026-11-11 02:07:49 | Magura (Kalu Ganga) | 4.08 | 🟡 Alert | -108.000 |  |
| 2026-11-11 02:05:25 | Giriulla (Maha Oya) | 4.00 | 🟢 Normal | 0.452 | 🔺 Rising |
| 2026-11-11 02:04:13 | Hanwella (Kelani Ganga) | 4.89 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-11-11 02:07:32 | Nagalagam Street (Kelani Ganga) | 1.01 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-11-10 18:00:51 | Weraganthota (Mahaweli Ganga) | -2.63 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-11-10 22:02:07 | Padiyathalawa (Maduru Oya) | 0.51 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-11-11 02:05:12 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-11 02:01:37 | Wellawaya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-11-11 00:22:08 | Horowpothana (Yan Oya) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-11-11 02:19:49 | Siyambalanduwa (Heda Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-11-11 00:12:57 | Putupaula (Kalu Ganga) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-11-10 18:04:35 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-11-11 02:26:30 | Urawa (Nilwala Ganga) | 1.40 | 🟢 Normal | -0.007 |  |
| 2026-11-11 02:18:12 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | -0.009 |  |
| 2026-11-10 18:10:04 | Galgamuwa (Mee Oya) | 0.76 | 🟢 Normal | -0.009 |  |
| 2026-11-11 02:02:42 | Glencourse (Kelani Ganga) | 13.18 | 🟢 Normal | -0.010 |  |
| 2026-11-11 02:01:21 | Ellagawa (Kalu Ganga) | 8.55 | 🟢 Normal | -0.010 |  |
| 2026-11-11 02:08:10 | Deraniyagala (Kelani Ganga) | 1.34 | 🟢 Normal | -0.019 |  |
| 2026-11-11 02:02:50 | Manampitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.020 |  |
| 2026-11-11 02:26:56 | Badalgama (Maha Oya) | 3.25 | 🟢 Normal | -0.024 |  |
| 2026-11-11 02:02:47 | Kuda Oya (Kirindi Oya) | 1.95 | 🟢 Normal | -0.039 |  |
| 2026-11-11 02:02:11 | Thanamalwila (Kirindi Oya) | 2.00 | 🟢 Normal | -0.041 |  |
| 2026-11-11 02:06:49 | Moraketiya (Walawe Ganga) | 2.34 | 🟢 Normal | -0.047 |  |
| 2026-11-11 02:03:45 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.048 |  |
| 2026-11-11 02:04:13 | Katharagama (Menik Ganga) | 0.15 | 🟢 Normal | -0.050 |  |
| 2026-11-11 02:05:13 | Pitabeddara (Nilwala Ganga) | 2.50 | 🟢 Normal | -0.066 |  |
| 2026-11-11 02:01:19 | Moragaswewa (Deduru Oya) | 3.21 | 🟢 Normal | -0.070 |  |
| 2026-11-11 02:04:13 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.098 |  |
| 2026-11-11 02:10:32 | Holombuwa (Kelani Ganga) | 1.66 | 🟢 Normal | -0.135 |  |
| 2026-11-11 02:04:03 | Peradeniya (Mahaweli Ganga) | 4.90 | 🟢 Normal | -0.200 |  |
| 2026-11-11 02:02:45 | Norwood (Kelani Ganga) | 1.35 | 🟢 Normal | -108.000 |  |
| 2026-11-11 02:02:29 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | -126.000 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)