# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--12_11:16:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **313,744 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert; 🟡 Moraketiya — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-12 11:16:54 | Thaldena (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.025 |  |
| 2026-11-12 11:16:26 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 11:14:07 | Horowpothana (Yan Oya) | 2.46 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-12 11:09:45 | Urawa (Nilwala Ganga) | 1.72 | 🟢 Normal | -0.100 |  |
| 2026-11-12 11:09:31 | Thawalama (Gin Ganga) | 3.27 | 🟢 Normal | -0.380 |  |
| 2026-11-12 11:09:29 | Baddegama (Gin Ganga) | 4.10 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 11:09:01 | Padiyathalawa (Maduru Oya) | 0.93 | 🟢 Normal | -0.021 |  |
| 2026-11-12 11:07:49 | Peradeniya (Mahaweli Ganga) | 4.85 | 🟢 Normal | -0.086 |  |
| 2026-11-12 11:07:27 | Magura (Kalu Ganga) | 5.40 | 🟡 Alert | -0.040 |  |
| 2026-11-12 11:07:25 | Badalgama (Maha Oya) | 4.38 | 🟢 Normal | -0.050 |  |
| 2026-11-12 11:06:23 | Putupaula (Kalu Ganga) | 2.54 | 🟢 Normal | -0.010 |  |
| 2026-11-12 11:06:09 | Thanamalwila (Kirindi Oya) | 2.48 | 🟢 Normal | -0.073 |  |
| 2026-11-12 11:05:59 | Glencourse (Kelani Ganga) | 13.05 | 🟢 Normal | -0.155 |  |
| 2026-11-12 11:05:27 | Giriulla (Maha Oya) | 2.95 | 🟢 Normal | -0.124 |  |
| 2026-11-12 11:05:08 | Holombuwa (Kelani Ganga) | 1.71 | 🟢 Normal | -0.051 |  |
| 2026-11-12 11:04:49 | Pitabeddara (Nilwala Ganga) | 2.52 | 🟢 Normal | -0.077 |  |
| 2026-11-12 11:04:40 | Ellagawa (Kalu Ganga) | 8.33 | 🟢 Normal | 0.000 |  |
| 2026-11-12 11:04:28 | Katharagama (Menik Ganga) | 0.58 | 🟢 Normal | -0.029 |  |
| 2026-11-12 11:04:18 | Galgamuwa (Mee Oya) | 0.73 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-12 11:03:55 | Weraganthota (Mahaweli Ganga) | -1.69 | 🟢 Normal | -0.155 |  |
| 2026-11-12 11:03:32 | Manampitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-11-12 11:03:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.34 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-11-12 11:03:11 | Rathnapura (Kalu Ganga) | 5.23 | 🟡 Alert | -0.077 |  |
| 2026-11-12 11:03:10 | Siyambalanduwa (Heda Oya) | 1.14 | 🟢 Normal | -0.096 |  |
| 2026-11-12 11:02:54 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-12 11:02:49 | Nawalapitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.020 |  |
| 2026-11-12 11:02:45 | Kuda Oya (Kirindi Oya) | 2.67 | 🟢 Normal | -0.033 |  |
| 2026-11-12 11:02:41 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | -0.020 |  |
| 2026-11-12 11:02:36 | Deraniyagala (Kelani Ganga) | 1.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-12 11:02:32 | Kithulgala (Kelani Ganga) | 2.11 | 🟢 Normal | -0.159 |  |
| 2026-11-12 11:02:22 | Panadugama (Nilwala Ganga) | 5.95 | 🟡 Alert | -0.023 |  |
| 2026-11-12 11:02:17 | Hanwella (Kelani Ganga) | 5.57 | 🟢 Normal | -0.031 |  |
| 2026-11-12 11:02:02 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-11-12 11:01:39 | Moraketiya (Walawe Ganga) | 3.90 | 🟡 Alert | -0.021 |  |
| 2026-11-12 11:01:38 | Nakkala (Kumbukkan Oya) | 1.60 | 🟢 Normal | -0.039 |  |
| 2026-11-12 11:01:37 | Moragaswewa (Deduru Oya) | 3.32 | 🟢 Normal | -0.159 |  |
| 2026-11-12 11:00:54 | Wellawaya (Kirindi Oya) | 1.77 | 🟢 Normal | -0.027 |  |
| 2026-11-12 11:00:49 | Dunamale (Aththanagalu Oya) | 4.25 | 🟡 Alert | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-12 11:09:29 | Baddegama (Gin Ganga) | 4.10 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 11:16:26 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 11:03:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.34 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-11-12 11:00:49 | Dunamale (Aththanagalu Oya) | 4.25 | 🟡 Alert | 0.000 |  |
| 2026-11-12 11:01:39 | Moraketiya (Walawe Ganga) | 3.90 | 🟡 Alert | -0.021 |  |
| 2026-11-12 11:02:22 | Panadugama (Nilwala Ganga) | 5.95 | 🟡 Alert | -0.023 |  |
| 2026-11-12 11:07:27 | Magura (Kalu Ganga) | 5.40 | 🟡 Alert | -0.040 |  |
| 2026-11-12 11:03:11 | Rathnapura (Kalu Ganga) | 5.23 | 🟡 Alert | -0.077 |  |
| 2026-11-12 11:03:32 | Manampitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-11-12 11:02:54 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-12 11:04:18 | Galgamuwa (Mee Oya) | 0.73 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-12 11:14:07 | Horowpothana (Yan Oya) | 2.46 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-12 11:02:36 | Deraniyagala (Kelani Ganga) | 1.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-12 11:04:40 | Ellagawa (Kalu Ganga) | 8.33 | 🟢 Normal | 0.000 |  |
| 2026-11-12 11:02:02 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-11-12 11:06:23 | Putupaula (Kalu Ganga) | 2.54 | 🟢 Normal | -0.010 |  |
| 2026-11-12 11:02:49 | Nawalapitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.020 |  |
| 2026-11-12 11:02:41 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | -0.020 |  |
| 2026-11-12 11:09:01 | Padiyathalawa (Maduru Oya) | 0.93 | 🟢 Normal | -0.021 |  |
| 2026-11-12 11:16:54 | Thaldena (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.025 |  |
| 2026-11-12 11:00:54 | Wellawaya (Kirindi Oya) | 1.77 | 🟢 Normal | -0.027 |  |
| 2026-11-12 11:04:28 | Katharagama (Menik Ganga) | 0.58 | 🟢 Normal | -0.029 |  |
| 2026-11-12 11:02:17 | Hanwella (Kelani Ganga) | 5.57 | 🟢 Normal | -0.031 |  |
| 2026-11-12 11:02:45 | Kuda Oya (Kirindi Oya) | 2.67 | 🟢 Normal | -0.033 |  |
| 2026-11-12 11:01:38 | Nakkala (Kumbukkan Oya) | 1.60 | 🟢 Normal | -0.039 |  |
| 2026-11-12 10:02:27 | Norwood (Kelani Ganga) | 1.42 | 🟢 Normal | -0.041 |  |
| 2026-11-12 11:07:25 | Badalgama (Maha Oya) | 4.38 | 🟢 Normal | -0.050 |  |
| 2026-11-12 11:05:08 | Holombuwa (Kelani Ganga) | 1.71 | 🟢 Normal | -0.051 |  |
| 2026-11-12 11:06:09 | Thanamalwila (Kirindi Oya) | 2.48 | 🟢 Normal | -0.073 |  |
| 2026-11-12 11:04:49 | Pitabeddara (Nilwala Ganga) | 2.52 | 🟢 Normal | -0.077 |  |
| 2026-11-12 11:07:49 | Peradeniya (Mahaweli Ganga) | 4.85 | 🟢 Normal | -0.086 |  |
| 2026-11-12 11:03:10 | Siyambalanduwa (Heda Oya) | 1.14 | 🟢 Normal | -0.096 |  |
| 2026-11-12 11:09:45 | Urawa (Nilwala Ganga) | 1.72 | 🟢 Normal | -0.100 |  |
| 2026-11-12 11:05:27 | Giriulla (Maha Oya) | 2.95 | 🟢 Normal | -0.124 |  |
| 2026-11-12 11:03:55 | Weraganthota (Mahaweli Ganga) | -1.69 | 🟢 Normal | -0.155 |  |
| 2026-11-12 11:05:59 | Glencourse (Kelani Ganga) | 13.05 | 🟢 Normal | -0.155 |  |
| 2026-11-12 11:02:32 | Kithulgala (Kelani Ganga) | 2.11 | 🟢 Normal | -0.159 |  |
| 2026-11-12 11:01:37 | Moragaswewa (Deduru Oya) | 3.32 | 🟢 Normal | -0.159 |  |
| 2026-11-12 11:09:31 | Thawalama (Gin Ganga) | 3.27 | 🟢 Normal | -0.380 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)