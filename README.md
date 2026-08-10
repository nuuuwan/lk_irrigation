# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--10_15:26:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **229,753 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-10 15:26:05 | Panadugama (Nilwala Ganga) | 3.75 | 🟢 Normal | 0.000 |  |
| 2026-08-10 15:14:13 | Panadugama (Nilwala Ganga) | 3.75 | 🟢 Normal | 0.000 |  |
| 2026-08-10 15:11:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.88 | 🟢 Normal | 0.245 | 🔺 Rising |
| 2026-08-10 15:11:01 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | -0.041 |  |
| 2026-08-10 15:10:48 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-10 15:09:12 | Magura (Kalu Ganga) | 1.85 | 🟢 Normal | -0.018 |  |
| 2026-08-10 15:09:07 | Baddegama (Gin Ganga) | 2.31 | 🟢 Normal | 0.000 |  |
| 2026-08-10 15:06:46 | Rathnapura (Kalu Ganga) | 2.30 | 🟢 Normal | -0.088 |  |
| 2026-08-10 15:06:08 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-08-10 15:06:08 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-10 15:05:25 | Glencourse (Kelani Ganga) | 10.37 | 🟢 Normal | -0.088 |  |
| 2026-08-10 15:04:38 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-08-10 15:04:37 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-10 15:04:25 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-10 15:03:59 | Hanwella (Kelani Ganga) | 2.22 | 🟢 Normal | -0.058 |  |
| 2026-08-10 15:03:38 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.246 | 🔺 Rising |
| 2026-08-10 15:03:29 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-10 15:03:27 | Baddegama (Gin Ganga) | 2.31 | 🟢 Normal | 0.000 |  |
| 2026-08-10 15:03:19 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-10 15:03:15 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-08-10 15:03:06 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-08-10 15:03:02 | Ellagawa (Kalu Ganga) | 6.15 | 🟢 Normal | -0.049 |  |
| 2026-08-10 15:03:01 | Deraniyagala (Kelani Ganga) | 1.03 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-08-10 15:03:00 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-08-10 15:02:59 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-08-10 15:02:38 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-10 15:02:32 | Peradeniya (Mahaweli Ganga) | 3.58 | 🟢 Normal | -0.022 |  |
| 2026-08-10 15:02:29 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-08-10 15:02:23 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-10 15:02:18 | Thanthirimale (Malwathu Oya) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-10 15:02:12 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-10 15:02:10 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-10 15:01:49 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.041 |  |
| 2026-08-10 15:01:42 | Nagalagam Street (Kelani Ganga) | 0.53 | 🟢 Normal | -0.046 |  |
| 2026-08-10 15:01:08 | Nawalapitiya (Mahaweli Ganga) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-08-10 15:00:49 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-10 15:00:44 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-10 15:00:39 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-08-10 15:00:12 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.107 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-10 15:03:38 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.246 | 🔺 Rising |
| 2026-08-10 15:11:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.88 | 🟢 Normal | 0.245 | 🔺 Rising |
| 2026-08-10 15:03:01 | Deraniyagala (Kelani Ganga) | 1.03 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-08-10 15:02:18 | Thanthirimale (Malwathu Oya) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-10 15:00:39 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-08-10 15:03:19 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-10 15:02:23 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-10 15:03:00 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-08-10 15:00:49 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-10 14:10:58 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-10 15:06:08 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-10 15:09:07 | Baddegama (Gin Ganga) | 2.31 | 🟢 Normal | 0.000 |  |
| 2026-08-10 15:26:05 | Panadugama (Nilwala Ganga) | 3.75 | 🟢 Normal | 0.000 |  |
| 2026-08-10 15:04:37 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-10 15:02:10 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-10 14:04:13 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-08-10 15:02:12 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-10 15:02:59 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-08-10 15:06:08 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-08-10 15:03:29 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-10 15:02:38 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-10 15:04:38 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-08-10 15:10:48 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-10 15:00:44 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-10 15:04:25 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-10 15:03:15 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-08-10 15:03:06 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-08-10 15:02:29 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-08-10 15:01:08 | Nawalapitiya (Mahaweli Ganga) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-08-10 15:09:12 | Magura (Kalu Ganga) | 1.85 | 🟢 Normal | -0.018 |  |
| 2026-08-10 15:02:32 | Peradeniya (Mahaweli Ganga) | 3.58 | 🟢 Normal | -0.022 |  |
| 2026-08-10 15:11:01 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | -0.041 |  |
| 2026-08-10 15:01:49 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.041 |  |
| 2026-08-10 15:01:42 | Nagalagam Street (Kelani Ganga) | 0.53 | 🟢 Normal | -0.046 |  |
| 2026-08-10 15:03:02 | Ellagawa (Kalu Ganga) | 6.15 | 🟢 Normal | -0.049 |  |
| 2026-08-10 15:03:59 | Hanwella (Kelani Ganga) | 2.22 | 🟢 Normal | -0.058 |  |
| 2026-08-10 15:05:25 | Glencourse (Kelani Ganga) | 10.37 | 🟢 Normal | -0.088 |  |
| 2026-08-10 15:06:46 | Rathnapura (Kalu Ganga) | 2.30 | 🟢 Normal | -0.088 |  |
| 2026-08-10 15:00:12 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.107 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)