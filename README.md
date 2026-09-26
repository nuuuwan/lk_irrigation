# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--26_18:08:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **271,702 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-26 18:08:49 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-26 18:08:00 | Thawalama (Gin Ganga) | 2.75 | 🟢 Normal | -0.021 |  |
| 2026-09-26 18:07:47 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.085 |  |
| 2026-09-26 18:07:37 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-26 18:06:31 | Holombuwa (Kelani Ganga) | 1.16 | 🟢 Normal | -0.060 |  |
| 2026-09-26 18:06:20 | Dunamale (Aththanagalu Oya) | 2.58 | 🟢 Normal | 0.000 |  |
| 2026-09-26 18:05:42 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-26 18:05:30 | Urawa (Nilwala Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-09-26 18:05:10 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-26 18:05:01 | Panadugama (Nilwala Ganga) | 5.86 | 🟡 Alert | -0.021 |  |
| 2026-09-26 18:04:57 | Badalgama (Maha Oya) | 2.90 | 🟢 Normal | -0.011 |  |
| 2026-09-26 18:04:48 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 1.143 | 🔺 Rising |
| 2026-09-26 18:04:37 | Deraniyagala (Kelani Ganga) | 1.77 | 🟢 Normal | -0.087 |  |
| 2026-09-26 18:03:45 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 1.143 | 🔺 Rising |
| 2026-09-26 18:03:42 | Thalgahagoda (Nilwala Ganga) | 1.95 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-26 18:03:42 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | 0.000 |  |
| 2026-09-26 18:03:34 | Ellagawa (Kalu Ganga) | 8.90 | 🟢 Normal | -0.030 |  |
| 2026-09-26 18:03:29 | Rathnapura (Kalu Ganga) | 4.89 | 🟢 Normal | -0.072 |  |
| 2026-09-26 18:03:23 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-09-26 18:03:14 | Hanwella (Kelani Ganga) | 5.29 | 🟢 Normal | -0.010 |  |
| 2026-09-26 18:03:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.91 | 🟠 Minor Flood | -0.020 |  |
| 2026-09-26 18:03:10 | Magura (Kalu Ganga) | 3.61 | 🟢 Normal | -0.046 |  |
| 2026-09-26 18:03:05 | Pitabeddara (Nilwala Ganga) | 1.59 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-09-26 18:02:41 | Giriulla (Maha Oya) | 1.68 | 🟢 Normal | -0.020 |  |
| 2026-09-26 18:02:32 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-26 18:02:26 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-26 18:02:24 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-09-26 18:02:21 | Thanthirimale (Malwathu Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-09-26 18:02:17 | Putupaula (Kalu Ganga) | 2.93 | 🟢 Normal | 0.000 |  |
| 2026-09-26 18:02:01 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-26 18:01:54 | Kithulgala (Kelani Ganga) | 2.55 | 🟢 Normal | -0.084 |  |
| 2026-09-26 18:01:47 | Baddegama (Gin Ganga) | 4.83 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-26 18:01:33 | Manampitiya (Mahaweli Ganga) | -0.01 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-26 18:01:22 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | -0.030 |  |
| 2026-09-26 18:01:19 | Nawalapitiya (Mahaweli Ganga) | 2.24 | 🟢 Normal | -0.021 |  |
| 2026-09-26 18:01:00 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-09-26 18:00:56 | Glencourse (Kelani Ganga) | 13.08 | 🟢 Normal | -0.020 |  |
| 2026-09-26 18:00:27 | Weraganthota (Mahaweli Ganga) | -3.23 | 🟢 Normal | -0.089 |  |
| 2026-09-26 18:00:14 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-26 17:30:11 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-26 18:01:47 | Baddegama (Gin Ganga) | 4.83 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-26 18:03:42 | Thalgahagoda (Nilwala Ganga) | 1.95 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-26 18:03:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.91 | 🟠 Minor Flood | -0.020 |  |
| 2026-09-26 18:05:01 | Panadugama (Nilwala Ganga) | 5.86 | 🟡 Alert | -0.021 |  |
| 2026-09-26 18:04:48 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 1.143 | 🔺 Rising |
| 2026-09-26 18:03:05 | Pitabeddara (Nilwala Ganga) | 1.59 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-09-26 18:01:33 | Manampitiya (Mahaweli Ganga) | -0.01 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-26 18:00:14 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-26 18:02:01 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-26 18:02:32 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-26 18:08:49 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-26 18:05:10 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-26 16:04:13 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-26 18:01:00 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-09-26 18:02:26 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-26 18:06:20 | Dunamale (Aththanagalu Oya) | 2.58 | 🟢 Normal | 0.000 |  |
| 2026-09-26 18:05:42 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-26 18:02:17 | Putupaula (Kalu Ganga) | 2.93 | 🟢 Normal | 0.000 |  |
| 2026-09-26 18:03:42 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | 0.000 |  |
| 2026-09-26 18:07:37 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-26 18:02:24 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-09-26 18:03:23 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-09-26 18:03:14 | Hanwella (Kelani Ganga) | 5.29 | 🟢 Normal | -0.010 |  |
| 2026-09-26 18:05:30 | Urawa (Nilwala Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-09-26 18:02:21 | Thanthirimale (Malwathu Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-09-26 18:04:57 | Badalgama (Maha Oya) | 2.90 | 🟢 Normal | -0.011 |  |
| 2026-09-26 18:02:41 | Giriulla (Maha Oya) | 1.68 | 🟢 Normal | -0.020 |  |
| 2026-09-26 18:00:56 | Glencourse (Kelani Ganga) | 13.08 | 🟢 Normal | -0.020 |  |
| 2026-09-26 18:01:19 | Nawalapitiya (Mahaweli Ganga) | 2.24 | 🟢 Normal | -0.021 |  |
| 2026-09-26 18:08:00 | Thawalama (Gin Ganga) | 2.75 | 🟢 Normal | -0.021 |  |
| 2026-09-26 18:03:34 | Ellagawa (Kalu Ganga) | 8.90 | 🟢 Normal | -0.030 |  |
| 2026-09-26 18:01:22 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | -0.030 |  |
| 2026-09-26 18:03:10 | Magura (Kalu Ganga) | 3.61 | 🟢 Normal | -0.046 |  |
| 2026-09-26 18:06:31 | Holombuwa (Kelani Ganga) | 1.16 | 🟢 Normal | -0.060 |  |
| 2026-09-26 18:03:29 | Rathnapura (Kalu Ganga) | 4.89 | 🟢 Normal | -0.072 |  |
| 2026-09-26 18:01:54 | Kithulgala (Kelani Ganga) | 2.55 | 🟢 Normal | -0.084 |  |
| 2026-09-26 18:07:47 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.085 |  |
| 2026-09-26 18:04:37 | Deraniyagala (Kelani Ganga) | 1.77 | 🟢 Normal | -0.087 |  |
| 2026-09-26 18:00:27 | Weraganthota (Mahaweli Ganga) | -3.23 | 🟢 Normal | -0.089 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)