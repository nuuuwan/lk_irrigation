# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--17_18:10:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **318,501 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **44** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-17 18:10:21 | Panadugama (Nilwala Ganga) | 3.71 | 🟢 Normal | 0.000 |  |
| 2026-11-17 18:08:54 | Kithulgala (Kelani Ganga) | 2.09 | 🟢 Normal | -0.047 |  |
| 2026-11-17 18:06:18 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-11-17 18:06:15 | Moraketiya (Walawe Ganga) | 1.08 | 🟢 Normal | -0.009 |  |
| 2026-11-17 18:05:50 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-11-17 18:05:32 | Horowpothana (Yan Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-11-17 18:05:29 | Glencourse (Kelani Ganga) | 10.13 | 🟢 Normal | -0.019 |  |
| 2026-11-17 18:04:43 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | -0.009 |  |
| 2026-11-17 18:04:39 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.030 |  |
| 2026-11-17 18:03:49 | Weraganthota (Mahaweli Ganga) | -2.19 | 🟢 Normal | 0.000 |  |
| 2026-11-17 18:03:48 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-17 18:03:44 | Magura (Kalu Ganga) | 1.58 | 🟢 Normal | -0.011 |  |
| 2026-11-17 18:03:41 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-11-17 18:03:39 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | -122.400 |  |
| 2026-11-17 18:03:25 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.023 |  |
| 2026-11-17 18:03:24 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-11-17 18:03:23 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-11-17 18:03:22 | Thawalama (Gin Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-11-17 18:03:18 | Hanwella (Kelani Ganga) | 1.92 | 🟢 Normal | -0.023 |  |
| 2026-11-17 18:03:10 | Ellagawa (Kalu Ganga) | 5.04 | 🟢 Normal | -0.010 |  |
| 2026-11-17 18:03:08 | Manampitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-17 18:03:02 | Peradeniya (Mahaweli Ganga) | 2.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-17 18:02:59 | Katharagama (Menik Ganga) | 1.30 | 🟢 Normal | -122.400 |  |
| 2026-11-17 18:02:55 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | -0.030 |  |
| 2026-11-17 18:02:46 | Badalgama (Maha Oya) | 2.59 | 🟢 Normal | 0.000 |  |
| 2026-11-17 18:02:32 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-17 18:02:20 | Rathnapura (Kalu Ganga) | 1.54 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-17 18:02:17 | Kuda Oya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-11-17 18:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-17 18:02:11 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | -0.012 |  |
| 2026-11-17 18:02:10 | Pitabeddara (Nilwala Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-11-17 18:02:00 | Urawa (Nilwala Ganga) | 0.92 | 🟢 Normal | -0.012 |  |
| 2026-11-17 18:01:47 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-17 18:01:44 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-17 18:01:44 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-11-17 18:01:42 | Weraganthota (Mahaweli Ganga) | -2.19 | 🟢 Normal | 0.000 |  |
| 2026-11-17 18:01:40 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-11-17 18:01:03 | Dunamale (Aththanagalu Oya) | 1.67 | 🟢 Normal | -0.021 |  |
| 2026-11-17 18:00:55 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-11-17 18:00:35 | Baddegama (Gin Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-11-17 18:00:28 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-11-17 18:00:24 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-17 18:00:12 | Wellawaya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-17 17:46:15 | Baddegama (Gin Ganga) | 1.63 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-17 18:05:50 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-11-17 18:03:08 | Manampitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-17 18:02:20 | Rathnapura (Kalu Ganga) | 1.54 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-17 18:00:12 | Wellawaya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-17 18:01:47 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-17 18:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-17 18:03:02 | Peradeniya (Mahaweli Ganga) | 2.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-17 18:03:48 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-17 18:03:49 | Weraganthota (Mahaweli Ganga) | -2.19 | 🟢 Normal | 0.000 |  |
| 2026-11-17 18:00:55 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-11-17 18:01:44 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-11-17 18:01:40 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-11-17 18:02:32 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-17 18:05:32 | Horowpothana (Yan Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-11-17 18:03:41 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-11-17 18:02:10 | Pitabeddara (Nilwala Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-11-17 18:06:18 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-11-17 18:00:35 | Baddegama (Gin Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-11-17 18:10:21 | Panadugama (Nilwala Ganga) | 3.71 | 🟢 Normal | 0.000 |  |
| 2026-11-17 18:00:28 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-11-17 18:00:24 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-17 18:02:46 | Badalgama (Maha Oya) | 2.59 | 🟢 Normal | 0.000 |  |
| 2026-11-17 18:01:44 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-17 18:03:24 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-11-17 18:02:17 | Kuda Oya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-11-17 18:06:15 | Moraketiya (Walawe Ganga) | 1.08 | 🟢 Normal | -0.009 |  |
| 2026-11-17 18:04:43 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | -0.009 |  |
| 2026-11-17 18:03:10 | Ellagawa (Kalu Ganga) | 5.04 | 🟢 Normal | -0.010 |  |
| 2026-11-17 18:03:44 | Magura (Kalu Ganga) | 1.58 | 🟢 Normal | -0.011 |  |
| 2026-11-17 18:02:00 | Urawa (Nilwala Ganga) | 0.92 | 🟢 Normal | -0.012 |  |
| 2026-11-17 18:02:11 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | -0.012 |  |
| 2026-11-17 18:05:29 | Glencourse (Kelani Ganga) | 10.13 | 🟢 Normal | -0.019 |  |
| 2026-11-17 18:01:03 | Dunamale (Aththanagalu Oya) | 1.67 | 🟢 Normal | -0.021 |  |
| 2026-11-17 18:03:18 | Hanwella (Kelani Ganga) | 1.92 | 🟢 Normal | -0.023 |  |
| 2026-11-17 18:03:25 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.023 |  |
| 2026-11-17 18:02:55 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | -0.030 |  |
| 2026-11-17 18:04:39 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.030 |  |
| 2026-11-17 18:08:54 | Kithulgala (Kelani Ganga) | 2.09 | 🟢 Normal | -0.047 |  |
| 2026-11-17 18:03:39 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | -122.400 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)