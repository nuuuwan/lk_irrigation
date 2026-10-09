# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--10_00:11:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **283,592 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-10 00:11:48 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-10 00:10:30 | Baddegama (Gin Ganga) | 2.55 | 🟢 Normal | 0.000 |  |
| 2026-10-10 00:07:54 | Panadugama (Nilwala Ganga) | 4.38 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-10-10 00:07:18 | Urawa (Nilwala Ganga) | 1.32 | 🟢 Normal | -0.134 |  |
| 2026-10-10 00:07:18 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-10 00:05:55 | Hanwella (Kelani Ganga) | 4.07 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-10-10 00:05:45 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | -0.041 |  |
| 2026-10-10 00:05:27 | Peradeniya (Mahaweli Ganga) | 4.11 | 🟢 Normal | -0.182 |  |
| 2026-10-10 00:05:13 | Holombuwa (Kelani Ganga) | 1.70 | 🟢 Normal | -0.106 |  |
| 2026-10-10 00:04:46 | Pitabeddara (Nilwala Ganga) | 2.18 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-10 00:04:39 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-10 00:04:22 | Rathnapura (Kalu Ganga) | 3.89 | 🟢 Normal | -0.030 |  |
| 2026-10-10 00:04:01 | Norwood (Kelani Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-10-10 00:03:54 | Ellagawa (Kalu Ganga) | 6.68 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-10-10 00:03:50 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-10 00:03:41 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.030 |  |
| 2026-10-10 00:03:32 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-10 00:03:27 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.021 |  |
| 2026-10-10 00:03:27 | Dunamale (Aththanagalu Oya) | 2.87 | 🟢 Normal | 0.220 | 🔺 Rising |
| 2026-10-10 00:03:18 | Giriulla (Maha Oya) | 3.68 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-10-10 00:03:13 | Moragaswewa (Deduru Oya) | 2.18 | 🟢 Normal | 0.225 | 🔺 Rising |
| 2026-10-10 00:03:00 | Manampitiya (Mahaweli Ganga) | -0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-10 00:02:50 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.021 |  |
| 2026-10-10 00:02:48 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-10-10 00:02:23 | Thanamalwila (Kirindi Oya) | 0.96 | 🟢 Normal | -0.029 |  |
| 2026-10-10 00:02:22 | Badalgama (Maha Oya) | 4.12 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-10-10 00:01:59 | Magura (Kalu Ganga) | 2.19 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-10-10 00:01:56 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-10 00:01:53 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-10-10 00:01:40 | Glencourse (Kelani Ganga) | 12.25 | 🟢 Normal | -0.232 |  |
| 2026-10-10 00:01:32 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | -0.198 |  |
| 2026-10-10 00:01:10 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | -0.031 |  |
| 2026-10-10 00:00:50 | Thawalama (Gin Ganga) | 2.13 | 🟢 Normal | -0.020 |  |
| 2026-10-10 00:00:43 | Moraketiya (Walawe Ganga) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-10 00:00:25 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-10 00:03:13 | Moragaswewa (Deduru Oya) | 2.18 | 🟢 Normal | 0.225 | 🔺 Rising |
| 2026-10-10 00:03:27 | Dunamale (Aththanagalu Oya) | 2.87 | 🟢 Normal | 0.220 | 🔺 Rising |
| 2026-10-10 00:03:54 | Ellagawa (Kalu Ganga) | 6.68 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-10-10 00:07:54 | Panadugama (Nilwala Ganga) | 4.38 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-10-10 00:02:22 | Badalgama (Maha Oya) | 4.12 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-10-10 00:03:18 | Giriulla (Maha Oya) | 3.68 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-10-10 00:05:55 | Hanwella (Kelani Ganga) | 4.07 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-10-10 00:07:18 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-10 00:01:59 | Magura (Kalu Ganga) | 2.19 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-10-10 00:04:46 | Pitabeddara (Nilwala Ganga) | 2.18 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-09 18:10:37 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-10 00:00:43 | Moraketiya (Walawe Ganga) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-10 00:03:32 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-09 18:01:41 | Weraganthota (Mahaweli Ganga) | -3.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-10 00:02:48 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-10-10 00:11:48 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-10 00:00:25 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-10 00:01:56 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-10 00:10:30 | Baddegama (Gin Ganga) | 2.55 | 🟢 Normal | 0.000 |  |
| 2026-10-10 00:04:39 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-10 00:03:50 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-10 00:03:00 | Manampitiya (Mahaweli Ganga) | -0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-09 18:01:04 | Thanthirimale (Malwathu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-10 00:01:53 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-10-10 00:04:01 | Norwood (Kelani Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-10-10 00:00:50 | Thawalama (Gin Ganga) | 2.13 | 🟢 Normal | -0.020 |  |
| 2026-10-10 00:02:50 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.021 |  |
| 2026-10-10 00:03:27 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.021 |  |
| 2026-10-10 00:02:23 | Thanamalwila (Kirindi Oya) | 0.96 | 🟢 Normal | -0.029 |  |
| 2026-10-10 00:04:22 | Rathnapura (Kalu Ganga) | 3.89 | 🟢 Normal | -0.030 |  |
| 2026-10-10 00:03:41 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.030 |  |
| 2026-10-10 00:01:10 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | -0.031 |  |
| 2026-10-09 23:12:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.27 | 🟢 Normal | -0.039 |  |
| 2026-10-10 00:05:45 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | -0.041 |  |
| 2026-10-10 00:05:13 | Holombuwa (Kelani Ganga) | 1.70 | 🟢 Normal | -0.106 |  |
| 2026-10-10 00:07:18 | Urawa (Nilwala Ganga) | 1.32 | 🟢 Normal | -0.134 |  |
| 2026-10-10 00:05:27 | Peradeniya (Mahaweli Ganga) | 4.11 | 🟢 Normal | -0.182 |  |
| 2026-10-10 00:01:32 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | -0.198 |  |
| 2026-10-10 00:01:40 | Glencourse (Kelani Ganga) | 12.25 | 🟢 Normal | -0.232 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)