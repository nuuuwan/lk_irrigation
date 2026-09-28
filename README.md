# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--28_06:12:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **273,008 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **17** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-28 06:12:20 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.138 |  |
| 2026-09-28 06:08:43 | Urawa (Nilwala Ganga) | 0.67 | 🟢 Normal | -0.144 |  |
| 2026-09-28 06:06:32 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | -0.019 |  |
| 2026-09-28 06:06:22 | Hanwella (Kelani Ganga) | 3.39 | 🟢 Normal | -0.019 |  |
| 2026-09-28 06:05:59 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-28 06:05:49 | Pitabeddara (Nilwala Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-09-28 06:05:47 | Pitabeddara (Nilwala Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-09-28 06:05:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.57 | 🟡 Alert | -0.282 |  |
| 2026-09-28 06:05:06 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.009 |  |
| 2026-09-28 06:04:46 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-28 06:04:43 | Thawalama (Gin Ganga) | 2.31 | 🟢 Normal | -0.010 |  |
| 2026-09-28 06:04:27 | Putupaula (Kalu Ganga) | 2.37 | 🟢 Normal | -0.151 |  |
| 2026-09-28 06:04:06 | Peradeniya (Mahaweli Ganga) | 3.20 | 🟢 Normal | -0.117 |  |
| 2026-09-28 06:04:01 | Baddegama (Gin Ganga) | 4.27 | 🟠 Minor Flood | -0.030 |  |
| 2026-09-28 06:03:34 | Dunamale (Aththanagalu Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-09-28 06:03:25 | Deraniyagala (Kelani Ganga) | 1.16 | 🟢 Normal | -0.020 |  |
| 2026-09-28 06:02:51 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-28 06:01:20 | Thalgahagoda (Nilwala Ganga) | 1.78 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-28 06:04:01 | Baddegama (Gin Ganga) | 4.27 | 🟠 Minor Flood | -0.030 |  |
| 2026-09-28 06:05:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.57 | 🟡 Alert | -0.282 |  |
| 2026-09-28 06:02:49 | Weraganthota (Mahaweli Ganga) | -3.13 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-09-28 06:00:15 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-09-28 06:02:37 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-28 06:01:22 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-28 06:05:59 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-28 06:02:51 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-09-28 06:02:04 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-28 06:05:49 | Pitabeddara (Nilwala Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-09-28 06:02:44 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-09-28 06:04:46 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-28 06:00:32 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-28 06:03:34 | Dunamale (Aththanagalu Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-09-28 06:02:34 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-27 18:02:06 | Thanthirimale (Malwathu Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-28 06:02:28 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-09-28 06:05:06 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.009 |  |
| 2026-09-28 06:04:43 | Thawalama (Gin Ganga) | 2.31 | 🟢 Normal | -0.010 |  |
| 2026-09-28 06:02:38 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-09-28 06:00:40 | Nawalapitiya (Mahaweli Ganga) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-09-28 06:01:08 | Kithulgala (Kelani Ganga) | 2.34 | 🟢 Normal | -0.010 |  |
| 2026-09-28 06:00:11 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | -0.011 |  |
| 2026-09-28 06:01:27 | Magura (Kalu Ganga) | 2.30 | 🟢 Normal | -0.012 |  |
| 2026-09-28 06:06:32 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | -0.019 |  |
| 2026-09-28 06:06:22 | Hanwella (Kelani Ganga) | 3.39 | 🟢 Normal | -0.019 |  |
| 2026-09-28 06:01:36 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | -0.020 |  |
| 2026-09-28 06:03:25 | Deraniyagala (Kelani Ganga) | 1.16 | 🟢 Normal | -0.020 |  |
| 2026-09-28 06:02:26 | Glencourse (Kelani Ganga) | 11.33 | 🟢 Normal | -0.020 |  |
| 2026-09-28 06:02:33 | Badalgama (Maha Oya) | 2.41 | 🟢 Normal | -0.032 |  |
| 2026-09-28 06:02:09 | Panadugama (Nilwala Ganga) | 4.71 | 🟢 Normal | -0.042 |  |
| 2026-09-28 06:01:17 | Rathnapura (Kalu Ganga) | 2.35 | 🟢 Normal | -0.061 |  |
| 2026-09-28 06:04:06 | Peradeniya (Mahaweli Ganga) | 3.20 | 🟢 Normal | -0.117 |  |
| 2026-09-28 06:02:16 | Ellagawa (Kalu Ganga) | 6.87 | 🟢 Normal | -0.129 |  |
| 2026-09-28 06:12:20 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.138 |  |
| 2026-09-28 06:08:43 | Urawa (Nilwala Ganga) | 0.67 | 🟢 Normal | -0.144 |  |
| 2026-09-28 06:04:27 | Putupaula (Kalu Ganga) | 2.37 | 🟢 Normal | -0.151 |  |
| 2026-09-27 18:01:49 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)