# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--05_23:03:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **307,894 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **14** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-05 23:03:21 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-05 23:03:09 | Giriulla (Maha Oya) | 2.10 | 🟢 Normal | -0.010 |  |
| 2026-11-05 23:02:43 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-11-05 23:02:40 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-11-05 23:02:36 | Pitabeddara (Nilwala Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-11-05 23:02:15 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-11-05 23:01:56 | Moragaswewa (Deduru Oya) | 3.21 | 🟢 Normal | -0.050 |  |
| 2026-11-05 23:01:44 | Yaka Wewa (Ma Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-11-05 23:01:42 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-05 23:01:21 | Moraketiya (Walawe Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-11-05 23:01:16 | Kuda Oya (Kirindi Oya) | 2.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-05 23:01:02 | Thalgahagoda (Nilwala Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-11-05 23:00:20 | Glencourse (Kelani Ganga) | 10.55 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-11-05 23:00:11 | Wellawaya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-05 22:07:25 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-11-05 22:11:12 | Rathnapura (Kalu Ganga) | 2.82 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-11-05 22:03:14 | Ellagawa (Kalu Ganga) | 6.57 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-11-05 23:00:20 | Glencourse (Kelani Ganga) | 10.55 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-11-05 23:01:42 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-05 22:02:30 | Dunamale (Aththanagalu Oya) | 2.52 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-05 22:05:03 | Hanwella (Kelani Ganga) | 2.33 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-05 22:13:14 | Magura (Kalu Ganga) | 2.76 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-05 22:02:08 | Peradeniya (Mahaweli Ganga) | 2.74 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-05 23:01:16 | Kuda Oya (Kirindi Oya) | 2.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-05 22:04:23 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-05 23:03:21 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-05 23:00:11 | Wellawaya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-11-05 23:01:44 | Yaka Wewa (Ma Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-11-05 23:02:15 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-11-05 18:03:39 | Galgamuwa (Mee Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-11-05 23:02:36 | Pitabeddara (Nilwala Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-11-05 23:01:21 | Moraketiya (Walawe Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-11-05 22:07:24 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-05 22:03:42 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-11-05 23:02:43 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-11-05 22:21:28 | Urawa (Nilwala Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-11-05 23:01:02 | Thalgahagoda (Nilwala Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-11-05 22:07:40 | Thanamalwila (Kirindi Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-11-05 22:05:57 | Panadugama (Nilwala Ganga) | 4.25 | 🟢 Normal | -0.009 |  |
| 2026-11-05 23:02:40 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-11-05 23:03:09 | Giriulla (Maha Oya) | 2.10 | 🟢 Normal | -0.010 |  |
| 2026-11-05 22:05:11 | Putupaula (Kalu Ganga) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-11-05 22:03:46 | Badalgama (Maha Oya) | 3.21 | 🟢 Normal | -0.011 |  |
| 2026-11-05 18:01:46 | Thanthirimale (Malwathu Oya) | 1.84 | 🟢 Normal | -0.012 |  |
| 2026-11-05 22:16:24 | Baddegama (Gin Ganga) | 1.90 | 🟢 Normal | -0.018 |  |
| 2026-11-05 22:04:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.78 | 🟢 Normal | -0.020 |  |
| 2026-11-05 22:03:18 | Padiyathalawa (Maduru Oya) | 0.35 | 🟢 Normal | -0.022 |  |
| 2026-11-05 22:05:22 | Thawalama (Gin Ganga) | 2.07 | 🟢 Normal | -0.025 |  |
| 2026-11-05 22:02:52 | Manampitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | -0.040 |  |
| 2026-11-05 18:01:57 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | -0.049 |  |
| 2026-11-05 23:01:56 | Moragaswewa (Deduru Oya) | 3.21 | 🟢 Normal | -0.050 |  |
| 2026-11-05 22:07:26 | Holombuwa (Kelani Ganga) | 1.12 | 🟢 Normal | -0.059 |  |
| 2026-11-05 22:08:48 | Kithulgala (Kelani Ganga) | 1.67 | 🟢 Normal | -0.175 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)