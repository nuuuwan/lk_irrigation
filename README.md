# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--23_00:02:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **323,115 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **23** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-23 00:02:47 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-11-23 00:02:39 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-11-23 00:02:33 | Thanamalwila (Kirindi Oya) | 1.47 | 🟢 Normal | 2.400 | 🔺 Rising |
| 2026-11-23 00:02:30 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.021 |  |
| 2026-11-23 00:02:18 | Thanamalwila (Kirindi Oya) | 1.46 | 🟢 Normal | 2.400 | 🔺 Rising |
| 2026-11-23 00:02:04 | Giriulla (Maha Oya) | 1.46 | 🟢 Normal | -0.021 |  |
| 2026-11-23 00:02:01 | Kuda Oya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-11-23 00:01:47 | Dunamale (Aththanagalu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-23 00:01:41 | Glencourse (Kelani Ganga) | 9.00 | 🟢 Normal | 0.000 |  |
| 2026-11-23 00:01:37 | Moragaswewa (Deduru Oya) | 2.53 | 🟢 Normal | -0.249 |  |
| 2026-11-23 00:01:26 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-11-23 00:01:09 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-11-23 00:00:37 | Magura (Kalu Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-11-23 00:00:36 | Moraketiya (Walawe Ganga) | 2.75 | 🟢 Normal | -0.051 |  |
| 2026-11-23 00:00:18 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.011 |  |
| 2026-11-23 00:00:13 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-23 00:00:06 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-22 23:59:25 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-22 23:56:23 | Kuda Oya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-11-22 23:37:56 | Rathnapura (Kalu Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-11-22 23:37:26 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-11-22 23:35:04 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-11-22 23:35:01 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-23 00:02:33 | Thanamalwila (Kirindi Oya) | 1.47 | 🟢 Normal | 2.400 | 🔺 Rising |
| 2026-11-22 22:06:51 | Thawalama (Gin Ganga) | 3.15 | 🟢 Normal | 0.396 | 🔺 Rising |
| 2026-11-22 23:05:13 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-11-23 00:02:39 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-11-23 00:02:47 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-11-22 23:02:33 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-22 18:00:53 | Weraganthota (Mahaweli Ganga) | -2.45 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-22 23:00:21 | Horowpothana (Yan Oya) | 2.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-23 00:00:13 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-23 00:01:09 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-11-22 22:01:24 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-22 18:00:10 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-11-23 00:00:37 | Magura (Kalu Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-11-22 21:02:08 | Pitabeddara (Nilwala Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-22 23:35:04 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-11-22 23:04:56 | Ellagawa (Kalu Ganga) | 5.45 | 🟢 Normal | 0.000 |  |
| 2026-11-23 00:01:41 | Glencourse (Kelani Ganga) | 9.00 | 🟢 Normal | 0.000 |  |
| 2026-11-23 00:00:06 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-23 00:01:47 | Dunamale (Aththanagalu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-22 23:03:49 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-11-22 23:37:26 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-11-22 23:37:56 | Rathnapura (Kalu Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-11-22 18:02:00 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-11-23 00:02:01 | Kuda Oya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-11-22 23:08:03 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-11-22 23:03:50 | Panadugama (Nilwala Ganga) | 4.35 | 🟢 Normal | -0.010 |  |
| 2026-11-23 00:00:18 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.011 |  |
| 2026-11-22 23:15:30 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | -0.017 |  |
| 2026-11-23 00:01:26 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-11-22 23:05:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.12 | 🟢 Normal | -0.020 |  |
| 2026-11-23 00:02:04 | Giriulla (Maha Oya) | 1.46 | 🟢 Normal | -0.021 |  |
| 2026-11-23 00:02:30 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.021 |  |
| 2026-11-22 17:02:02 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-22 22:05:18 | Urawa (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.030 |  |
| 2026-11-22 23:04:42 | Badalgama (Maha Oya) | 2.80 | 🟢 Normal | -0.031 |  |
| 2026-11-22 22:02:12 | Hanwella (Kelani Ganga) | 1.08 | 🟢 Normal | -0.043 |  |
| 2026-11-23 00:00:36 | Moraketiya (Walawe Ganga) | 2.75 | 🟢 Normal | -0.051 |  |
| 2026-11-22 23:01:00 | Manampitiya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.208 |  |
| 2026-11-23 00:01:37 | Moragaswewa (Deduru Oya) | 2.53 | 🟢 Normal | -0.249 |  |

## River Water Level Charts by Station

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)