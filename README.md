# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--25_20:07:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **270,866 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Panadugama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Magura — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-25 20:07:25 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-25 20:06:47 | Magura (Kalu Ganga) | 4.79 | 🟡 Alert | 0.000 |  |
| 2026-09-25 20:06:29 | Baddegama (Gin Ganga) | 4.75 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-25 20:06:28 | Rathnapura (Kalu Ganga) | 5.95 | 🟡 Alert | -0.065 |  |
| 2026-09-25 20:05:44 | Badalgama (Maha Oya) | 3.10 | 🟢 Normal | 0.000 |  |
| 2026-09-25 20:05:43 | Holombuwa (Kelani Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-09-25 20:05:30 | Moraketiya (Walawe Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-09-25 20:05:30 | Nawalapitiya (Mahaweli Ganga) | 2.85 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-09-25 20:05:09 | Putupaula (Kalu Ganga) | 2.82 | 🟢 Normal | 0.000 |  |
| 2026-09-25 20:04:56 | Hanwella (Kelani Ganga) | 5.89 | 🟢 Normal | -0.050 |  |
| 2026-09-25 20:04:23 | Glencourse (Kelani Ganga) | 13.69 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-09-25 20:03:54 | Panadugama (Nilwala Ganga) | 6.33 | 🟠 Minor Flood | -0.020 |  |
| 2026-09-25 20:03:54 | Ellagawa (Kalu Ganga) | 8.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-25 20:03:50 | Giriulla (Maha Oya) | 1.96 | 🟢 Normal | -0.020 |  |
| 2026-09-25 20:03:39 | Thawalama (Gin Ganga) | 3.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-25 20:03:22 | Dunamale (Aththanagalu Oya) | 2.78 | 🟢 Normal | -0.021 |  |
| 2026-09-25 20:03:15 | Peradeniya (Mahaweli Ganga) | 4.02 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-25 20:02:39 | Deraniyagala (Kelani Ganga) | 2.50 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-25 20:02:34 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-25 20:02:33 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | -0.062 |  |
| 2026-09-25 20:02:13 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-25 20:02:04 | Norwood (Kelani Ganga) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-09-25 20:02:00 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-09-25 20:01:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.06 | 🟠 Minor Flood | -0.913 |  |
| 2026-09-25 20:01:51 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-25 20:01:45 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-25 20:01:42 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-25 20:01:13 | Kuda Oya (Kirindi Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-09-25 20:01:11 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-25 20:00:48 | Urawa (Nilwala Ganga) | 1.23 | 🟢 Normal | -0.025 |  |
| 2026-09-25 20:00:17 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-25 19:58:58 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-25 19:36:06 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-25 19:26:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.60 | 🟠 Minor Flood | -0.913 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-25 19:15:08 | Thalgahagoda (Nilwala Ganga) | 1.91 | 🟠 Minor Flood | 0.008 | 🔺 Rising |
| 2026-09-25 20:06:29 | Baddegama (Gin Ganga) | 4.75 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-25 20:03:54 | Panadugama (Nilwala Ganga) | 6.33 | 🟠 Minor Flood | -0.020 |  |
| 2026-09-25 20:01:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.06 | 🟠 Minor Flood | -0.913 |  |
| 2026-09-25 20:06:47 | Magura (Kalu Ganga) | 4.79 | 🟡 Alert | 0.000 |  |
| 2026-09-25 20:06:28 | Rathnapura (Kalu Ganga) | 5.95 | 🟡 Alert | -0.065 |  |
| 2026-09-25 20:05:30 | Nawalapitiya (Mahaweli Ganga) | 2.85 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-09-25 20:04:23 | Glencourse (Kelani Ganga) | 13.69 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-09-25 20:02:00 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-09-25 20:02:39 | Deraniyagala (Kelani Ganga) | 2.50 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-25 20:02:34 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-25 20:03:15 | Peradeniya (Mahaweli Ganga) | 4.02 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-25 20:03:54 | Ellagawa (Kalu Ganga) | 8.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-25 20:03:39 | Thawalama (Gin Ganga) | 3.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-25 20:00:17 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-25 20:01:11 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-25 19:36:06 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-25 20:01:42 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-25 20:01:51 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-25 18:01:13 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-25 19:04:45 | Pitabeddara (Nilwala Ganga) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-09-25 19:58:58 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-25 20:01:45 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-25 20:07:25 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-25 20:05:09 | Putupaula (Kalu Ganga) | 2.82 | 🟢 Normal | 0.000 |  |
| 2026-09-25 20:05:44 | Badalgama (Maha Oya) | 3.10 | 🟢 Normal | 0.000 |  |
| 2026-09-25 20:05:43 | Holombuwa (Kelani Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-09-25 18:01:42 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-25 20:02:13 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-25 20:05:30 | Moraketiya (Walawe Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-09-25 20:01:13 | Kuda Oya (Kirindi Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-09-25 20:02:04 | Norwood (Kelani Ganga) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-09-25 20:03:50 | Giriulla (Maha Oya) | 1.96 | 🟢 Normal | -0.020 |  |
| 2026-09-25 18:02:19 | Weraganthota (Mahaweli Ganga) | -2.82 | 🟢 Normal | -0.020 |  |
| 2026-09-25 20:03:22 | Dunamale (Aththanagalu Oya) | 2.78 | 🟢 Normal | -0.021 |  |
| 2026-09-25 20:00:48 | Urawa (Nilwala Ganga) | 1.23 | 🟢 Normal | -0.025 |  |
| 2026-09-25 20:04:56 | Hanwella (Kelani Ganga) | 5.89 | 🟢 Normal | -0.050 |  |
| 2026-09-25 20:02:33 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | -0.062 |  |
| 2026-09-25 19:10:14 | Kithulgala (Kelani Ganga) | 2.97 | 🟢 Normal | -0.069 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)