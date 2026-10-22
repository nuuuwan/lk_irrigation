# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--22_18:12:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **295,105 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **1** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-22 18:12:53 | Padiyathalawa (Maduru Oya) | 0.95 | 🟢 Normal | 0.689 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-22 18:12:53 | Padiyathalawa (Maduru Oya) | 0.95 | 🟢 Normal | 0.689 | 🔺 Rising |
| 2026-10-22 18:02:46 | Holombuwa (Kelani Ganga) | 2.51 | 🟢 Normal | 0.258 | 🔺 Rising |
| 2026-10-22 18:00:17 | Moragaswewa (Deduru Oya) | 4.73 | 🟢 Normal | 0.182 | 🔺 Rising |
| 2026-10-22 18:01:16 | Kithulgala (Kelani Ganga) | 2.19 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-10-22 18:04:46 | Thawalama (Gin Ganga) | 2.46 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-10-22 18:09:50 | Pitabeddara (Nilwala Ganga) | 1.72 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-10-22 18:02:00 | Hanwella (Kelani Ganga) | 4.48 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-10-22 18:06:30 | Dunamale (Aththanagalu Oya) | 2.42 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-22 18:07:15 | Panadugama (Nilwala Ganga) | 4.36 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-10-22 18:03:42 | Deraniyagala (Kelani Ganga) | 1.29 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-22 18:02:01 | Ellagawa (Kalu Ganga) | 7.73 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-10-22 18:01:42 | Magura (Kalu Ganga) | 2.07 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-10-22 18:00:09 | Putupaula (Kalu Ganga) | 1.76 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-10-22 18:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.69 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-22 18:03:38 | Rathnapura (Kalu Ganga) | 4.20 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-22 18:02:27 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-22 18:01:15 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-22 18:02:23 | Thanthirimale (Malwathu Oya) | 2.18 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-22 18:03:43 | Giriulla (Maha Oya) | 2.29 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-22 18:03:27 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-22 18:02:35 | Galgamuwa (Mee Oya) | 2.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-22 18:02:41 | Glencourse (Kelani Ganga) | 12.49 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-22 18:07:03 | Baddegama (Gin Ganga) | 2.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-22 18:03:45 | Wellawaya (Kirindi Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-10-22 18:01:34 | Yaka Wewa (Ma Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-10-22 18:06:54 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-22 18:03:40 | Manampitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-22 18:02:00 | Thalgahagoda (Nilwala Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-10-22 18:01:55 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-10-22 18:00:08 | Horowpothana (Yan Oya) | 3.04 | 🟢 Normal | -0.006 |  |
| 2026-10-22 18:06:20 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-10-22 18:03:06 | Thanamalwila (Kirindi Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-10-22 18:02:32 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | -0.012 |  |
| 2026-10-22 18:01:36 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.021 |  |
| 2026-10-22 18:03:11 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | -0.029 |  |
| 2026-10-22 18:04:45 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.031 |  |
| 2026-10-22 18:07:10 | Urawa (Nilwala Ganga) | 1.34 | 🟢 Normal | -0.060 |  |
| 2026-10-22 18:01:15 | Weraganthota (Mahaweli Ganga) | -2.10 | 🟢 Normal | -0.070 |  |
| 2026-10-22 18:01:27 | Badalgama (Maha Oya) | 3.50 | 🟢 Normal | -0.077 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)