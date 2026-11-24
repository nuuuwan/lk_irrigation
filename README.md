# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--24_12:08:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **324,439 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-24 12:08:50 | Panadugama (Nilwala Ganga) | 4.04 | 🟢 Normal | 5.684 | 🔺 Rising |
| 2026-11-24 12:08:31 | Panadugama (Nilwala Ganga) | 4.01 | 🟢 Normal | 5.684 | 🔺 Rising |
| 2026-11-24 12:08:28 | Thalgahagoda (Nilwala Ganga) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-24 12:08:25 | Rathnapura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.064 |  |
| 2026-11-24 12:06:58 | Glencourse (Kelani Ganga) | 10.12 | 🟢 Normal | -0.157 |  |
| 2026-11-24 12:06:33 | Baddegama (Gin Ganga) | 1.59 | 🟢 Normal | -0.019 |  |
| 2026-11-24 12:06:15 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-11-24 12:06:03 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-24 12:05:35 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-11-24 12:05:31 | Pitabeddara (Nilwala Ganga) | 1.52 | 🟢 Normal | -0.019 |  |
| 2026-11-24 12:05:10 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | -0.070 |  |
| 2026-11-24 12:04:55 | Urawa (Nilwala Ganga) | 1.07 | 🟢 Normal | -0.031 |  |
| 2026-11-24 12:04:46 | Magura (Kalu Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-11-24 12:04:40 | Hanwella (Kelani Ganga) | 2.48 | 🟢 Normal | -0.127 |  |
| 2026-11-24 12:04:13 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-11-24 12:03:45 | Deraniyagala (Kelani Ganga) | 0.54 | 🟢 Normal | -0.039 |  |
| 2026-11-24 12:03:43 | Badalgama (Maha Oya) | 4.12 | 🟢 Normal | -0.238 |  |
| 2026-11-24 12:03:27 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-11-24 12:02:49 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-11-24 12:02:44 | Dunamale (Aththanagalu Oya) | 1.68 | 🟢 Normal | -0.010 |  |
| 2026-11-24 12:02:36 | Galgamuwa (Mee Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-11-24 12:02:36 | Thanamalwila (Kirindi Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-11-24 12:02:34 | Giriulla (Maha Oya) | 2.75 | 🟢 Normal | -0.137 |  |
| 2026-11-24 12:02:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.80 | 🟢 Normal | -0.071 |  |
| 2026-11-24 12:02:25 | Putupaula (Kalu Ganga) | 0.69 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-11-24 12:02:25 | Thawalama (Gin Ganga) | 1.83 | 🟢 Normal | -0.041 |  |
| 2026-11-24 12:02:17 | Kuda Oya (Kirindi Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-11-24 12:02:12 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-11-24 12:02:05 | Nagalagam Street (Kelani Ganga) | 0.59 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-11-24 12:01:41 | Ellagawa (Kalu Ganga) | 5.44 | 🟢 Normal | 0.000 |  |
| 2026-11-24 12:01:36 | Moragaswewa (Deduru Oya) | 0.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-24 12:01:34 | Moraketiya (Walawe Ganga) | 2.60 | 🟢 Normal | 0.000 |  |
| 2026-11-24 12:01:26 | Manampitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-24 12:01:24 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-11-24 12:01:20 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-24 12:01:14 | Peradeniya (Mahaweli Ganga) | 2.59 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-24 12:00:26 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-24 12:00:25 | Horowpothana (Yan Oya) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-11-24 12:00:11 | Weraganthota (Mahaweli Ganga) | -2.11 | 🟢 Normal | 0.920 | 🔺 Rising |
| 2026-11-24 11:20:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.85 | 🟢 Normal | -0.071 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-24 12:08:50 | Panadugama (Nilwala Ganga) | 4.04 | 🟢 Normal | 5.684 | 🔺 Rising |
| 2026-11-24 12:00:11 | Weraganthota (Mahaweli Ganga) | -2.11 | 🟢 Normal | 0.920 | 🔺 Rising |
| 2026-11-24 12:02:05 | Nagalagam Street (Kelani Ganga) | 0.59 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-11-24 12:02:25 | Putupaula (Kalu Ganga) | 0.69 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-11-24 12:01:26 | Manampitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-24 12:01:14 | Peradeniya (Mahaweli Ganga) | 2.59 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-24 12:01:36 | Moragaswewa (Deduru Oya) | 0.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-24 12:06:03 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-24 12:08:28 | Thalgahagoda (Nilwala Ganga) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-24 12:01:24 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-11-24 12:01:20 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-24 12:00:25 | Horowpothana (Yan Oya) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-11-24 12:02:36 | Galgamuwa (Mee Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-11-24 12:04:46 | Magura (Kalu Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-11-24 12:05:35 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-11-24 12:01:41 | Ellagawa (Kalu Ganga) | 5.44 | 🟢 Normal | 0.000 |  |
| 2026-11-24 12:01:34 | Moraketiya (Walawe Ganga) | 2.60 | 🟢 Normal | 0.000 |  |
| 2026-11-24 12:00:26 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-24 12:06:15 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-11-24 12:02:49 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-11-24 12:02:17 | Kuda Oya (Kirindi Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-11-24 12:04:13 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-11-24 12:03:27 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-11-24 12:02:36 | Thanamalwila (Kirindi Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-11-24 12:02:44 | Dunamale (Aththanagalu Oya) | 1.68 | 🟢 Normal | -0.010 |  |
| 2026-11-24 12:02:12 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-11-24 12:05:31 | Pitabeddara (Nilwala Ganga) | 1.52 | 🟢 Normal | -0.019 |  |
| 2026-11-24 12:06:33 | Baddegama (Gin Ganga) | 1.59 | 🟢 Normal | -0.019 |  |
| 2026-11-22 17:02:02⌛ | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-24 12:04:55 | Urawa (Nilwala Ganga) | 1.07 | 🟢 Normal | -0.031 |  |
| 2026-11-24 12:03:45 | Deraniyagala (Kelani Ganga) | 0.54 | 🟢 Normal | -0.039 |  |
| 2026-11-24 12:02:25 | Thawalama (Gin Ganga) | 1.83 | 🟢 Normal | -0.041 |  |
| 2026-11-24 12:08:25 | Rathnapura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.064 |  |
| 2026-11-24 12:05:10 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | -0.070 |  |
| 2026-11-24 12:02:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.80 | 🟢 Normal | -0.071 |  |
| 2026-11-24 12:04:40 | Hanwella (Kelani Ganga) | 2.48 | 🟢 Normal | -0.127 |  |
| 2026-11-24 12:02:34 | Giriulla (Maha Oya) | 2.75 | 🟢 Normal | -0.137 |  |
| 2026-11-24 12:06:58 | Glencourse (Kelani Ganga) | 10.12 | 🟢 Normal | -0.157 |  |
| 2026-11-24 12:03:43 | Badalgama (Maha Oya) | 4.12 | 🟢 Normal | -0.238 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)