# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--23_05:42:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **268,463 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Thalgahagoda — Alert; 🟡 Magura — Alert; 🟡 Baddegama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-23 05:42:06 | Baddegama (Gin Ganga) | 3.92 | 🟡 Alert | -0.527 |  |
| 2026-09-23 05:39:47 | Panadugama (Nilwala Ganga) | 4.50 | 🟢 Normal | -0.031 |  |
| 2026-09-23 05:37:33 | Baddegama (Gin Ganga) | 3.96 | 🟡 Alert | -0.527 |  |
| 2026-09-23 05:27:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.02 | 🟠 Minor Flood | -0.014 |  |
| 2026-09-23 05:11:16 | Ellagawa (Kalu Ganga) | 8.32 | 🟢 Normal | -0.044 |  |
| 2026-09-23 05:10:28 | Badalgama (Maha Oya) | 2.83 | 🟢 Normal | -0.037 |  |
| 2026-09-23 05:10:23 | Nawalapitiya (Mahaweli Ganga) | 2.26 | 🟢 Normal | -0.072 |  |
| 2026-09-23 05:10:16 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-23 05:09:11 | Rathnapura (Kalu Ganga) | 3.95 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-09-23 05:07:42 | Thawalama (Gin Ganga) | 2.53 | 🟢 Normal | -0.053 |  |
| 2026-09-23 05:07:31 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-09-23 05:07:27 | Holombuwa (Kelani Ganga) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-09-23 05:06:46 | Putupaula (Kalu Ganga) | 2.92 | 🟢 Normal | 0.000 |  |
| 2026-09-23 05:05:57 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-23 05:05:43 | Hanwella (Kelani Ganga) | 4.76 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-23 05:05:31 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-09-23 05:05:23 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-23 05:04:47 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-23 05:04:25 | Peradeniya (Mahaweli Ganga) | 3.48 | 🟢 Normal | -0.172 |  |
| 2026-09-23 05:04:00 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-09-23 05:03:10 | Dunamale (Aththanagalu Oya) | 2.70 | 🟢 Normal | -0.020 |  |
| 2026-09-23 05:02:20 | Glencourse (Kelani Ganga) | 12.91 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-23 05:01:59 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-09-23 05:01:59 | Giriulla (Maha Oya) | 1.51 | 🟢 Normal | -0.030 |  |
| 2026-09-23 05:01:57 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-23 05:01:38 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-23 05:01:35 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-23 05:01:28 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-09-23 05:01:17 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-09-23 05:01:09 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-23 05:00:35 | Magura (Kalu Ganga) | 4.15 | 🟡 Alert | -0.060 |  |
| 2026-09-23 05:00:26 | Thalgahagoda (Nilwala Ganga) | 1.45 | 🟡 Alert | -0.022 |  |
| 2026-09-23 05:00:20 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-09-23 05:00:07 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-23 05:27:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.02 | 🟠 Minor Flood | -0.014 |  |
| 2026-09-23 05:00:26 | Thalgahagoda (Nilwala Ganga) | 1.45 | 🟡 Alert | -0.022 |  |
| 2026-09-23 05:00:35 | Magura (Kalu Ganga) | 4.15 | 🟡 Alert | -0.060 |  |
| 2026-09-23 05:42:06 | Baddegama (Gin Ganga) | 3.92 | 🟡 Alert | -0.527 |  |
| 2026-09-23 05:09:11 | Rathnapura (Kalu Ganga) | 3.95 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-09-23 04:44:17 | Kithulgala (Kelani Ganga) | 2.55 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-09-23 05:05:43 | Hanwella (Kelani Ganga) | 4.76 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-23 05:02:20 | Glencourse (Kelani Ganga) | 12.91 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-22 18:00:33 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | 0.000 |  |
| 2026-09-23 05:00:20 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-09-23 05:04:47 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-23 05:01:35 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-23 05:01:57 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-23 05:04:00 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-09-22 18:04:56 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-23 05:05:23 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-23 05:01:09 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-23 05:05:57 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-23 05:10:16 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-23 05:01:38 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-23 05:06:46 | Putupaula (Kalu Ganga) | 2.92 | 🟢 Normal | 0.000 |  |
| 2026-09-23 05:01:59 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-09-23 05:07:31 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-09-23 05:00:07 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-09-23 03:10:26 | Pitabeddara (Nilwala Ganga) | 1.16 | 🟢 Normal | -0.009 |  |
| 2026-09-23 05:05:31 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-09-22 18:02:46 | Thanthirimale (Malwathu Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-09-23 05:01:28 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-09-23 05:07:27 | Holombuwa (Kelani Ganga) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-09-23 05:03:10 | Dunamale (Aththanagalu Oya) | 2.70 | 🟢 Normal | -0.020 |  |
| 2026-09-23 05:01:59 | Giriulla (Maha Oya) | 1.51 | 🟢 Normal | -0.030 |  |
| 2026-09-23 05:39:47 | Panadugama (Nilwala Ganga) | 4.50 | 🟢 Normal | -0.031 |  |
| 2026-09-23 05:10:28 | Badalgama (Maha Oya) | 2.83 | 🟢 Normal | -0.037 |  |
| 2026-09-23 05:11:16 | Ellagawa (Kalu Ganga) | 8.32 | 🟢 Normal | -0.044 |  |
| 2026-09-23 05:07:42 | Thawalama (Gin Ganga) | 2.53 | 🟢 Normal | -0.053 |  |
| 2026-09-23 04:14:44 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.067 |  |
| 2026-09-23 05:10:23 | Nawalapitiya (Mahaweli Ganga) | 2.26 | 🟢 Normal | -0.072 |  |
| 2026-09-23 04:03:03 | Deraniyagala (Kelani Ganga) | 2.06 | 🟢 Normal | -0.090 |  |
| 2026-09-23 05:04:25 | Peradeniya (Mahaweli Ganga) | 3.48 | 🟢 Normal | -0.172 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)