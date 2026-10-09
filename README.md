# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--09_08:00:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **282,954 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **2** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-09 08:00:15 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | -0.030 |  |
| 2026-10-09 07:26:58 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.014 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-09 07:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.89 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-10-09 07:09:20 | Baddegama (Gin Ganga) | 2.78 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-10-09 07:01:42 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-09 07:01:37 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-09 07:03:42 | Ellagawa (Kalu Ganga) | 6.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-09 07:03:23 | Kithulgala (Kelani Ganga) | 2.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-09 07:08:31 | Thanthirimale (Malwathu Oya) | 0.81 | 🟢 Normal | 0.002 |  |
| 2026-10-09 07:00:13 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-09 07:02:20 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-09 07:03:54 | Galgamuwa (Mee Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-09 07:03:38 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-09 07:08:40 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-09 07:02:44 | Siyambalanduwa (Heda Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-10-09 07:12:19 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-09 07:03:32 | Thalgahagoda (Nilwala Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-10-09 07:14:26 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.008 |  |
| 2026-10-09 07:02:21 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | -0.010 |  |
| 2026-10-09 07:02:24 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-10-09 07:03:02 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-10-09 07:03:53 | Dunamale (Aththanagalu Oya) | 2.95 | 🟢 Normal | -0.010 |  |
| 2026-10-09 07:00:42 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | -0.011 |  |
| 2026-10-09 07:26:58 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.014 |  |
| 2026-10-09 07:07:03 | Badalgama (Maha Oya) | 4.93 | 🟢 Normal | -0.019 |  |
| 2026-10-09 07:04:42 | Hanwella (Kelani Ganga) | 4.01 | 🟢 Normal | -0.020 |  |
| 2026-10-09 07:01:46 | Weraganthota (Mahaweli Ganga) | -3.13 | 🟢 Normal | -0.030 |  |
| 2026-10-09 08:00:15 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | -0.030 |  |
| 2026-10-09 07:01:09 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.035 |  |
| 2026-10-09 07:05:29 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | -0.037 |  |
| 2026-10-09 07:04:42 | Putupaula (Kalu Ganga) | 1.21 | 🟢 Normal | -0.038 |  |
| 2026-10-09 07:11:11 | Holombuwa (Kelani Ganga) | 1.65 | 🟢 Normal | -0.047 |  |
| 2026-10-09 07:17:02 | Magura (Kalu Ganga) | 2.56 | 🟢 Normal | -0.051 |  |
| 2026-10-09 07:00:47 | Pitabeddara (Nilwala Ganga) | 1.24 | 🟢 Normal | -0.053 |  |
| 2026-10-09 07:08:40 | Panadugama (Nilwala Ganga) | 4.45 | 🟢 Normal | -0.066 |  |
| 2026-10-09 07:05:25 | Rathnapura (Kalu Ganga) | 3.26 | 🟢 Normal | -0.082 |  |
| 2026-10-09 07:03:40 | Moragaswewa (Deduru Oya) | 1.92 | 🟢 Normal | -0.125 |  |
| 2026-10-09 07:08:43 | Glencourse (Kelani Ganga) | 12.05 | 🟢 Normal | -0.137 |  |
| 2026-10-09 07:01:32 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | -0.159 |  |
| 2026-10-09 07:02:21 | Giriulla (Maha Oya) | 3.74 | 🟢 Normal | -0.180 |  |
| 2026-10-09 07:11:24 | Thawalama (Gin Ganga) | 2.71 | 🟢 Normal | -0.234 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)