# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--24_19:04:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **296,912 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **25** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-24 19:04:07 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-24 19:03:54 | Glencourse (Kelani Ganga) | 10.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-24 19:03:54 | Dunamale (Aththanagalu Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-10-24 19:03:52 | Badalgama (Maha Oya) | 2.82 | 🟢 Normal | -0.010 |  |
| 2026-10-24 19:03:50 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-24 19:03:48 | Baddegama (Gin Ganga) | 2.04 | 🟢 Normal | -0.020 |  |
| 2026-10-24 19:03:08 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-10-24 19:03:06 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-24 19:02:46 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-24 19:02:39 | Urawa (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-10-24 19:02:33 | Deraniyagala (Kelani Ganga) | 0.94 | 🟢 Normal | -0.101 |  |
| 2026-10-24 19:02:23 | Giriulla (Maha Oya) | 1.49 | 🟢 Normal | -0.020 |  |
| 2026-10-24 19:02:18 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-10-24 19:02:12 | Panadugama (Nilwala Ganga) | 3.87 | 🟢 Normal | -0.033 |  |
| 2026-10-24 19:02:07 | Thanamalwila (Kirindi Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-10-24 19:02:04 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.068 |  |
| 2026-10-24 19:01:58 | Ellagawa (Kalu Ganga) | 5.98 | 🟢 Normal | -0.055 |  |
| 2026-10-24 19:01:16 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-10-24 19:01:08 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-24 19:01:05 | Horowpothana (Yan Oya) | 2.35 | 🟢 Normal | -0.010 |  |
| 2026-10-24 19:00:57 | Rathnapura (Kalu Ganga) | 2.10 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-24 19:00:50 | Moragaswewa (Deduru Oya) | 1.40 | 🟢 Normal | -0.080 |  |
| 2026-10-24 19:00:11 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-24 19:00:09 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-24 18:24:45 | Thalgahagoda (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-24 18:04:03 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-10-24 19:03:50 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-24 18:02:19 | Kithulgala (Kelani Ganga) | 2.22 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-24 19:00:57 | Rathnapura (Kalu Ganga) | 2.10 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-24 19:01:08 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-24 19:00:11 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-24 19:03:06 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-24 19:03:54 | Glencourse (Kelani Ganga) | 10.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-24 19:01:16 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-10-24 18:01:00 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-24 19:02:46 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-24 17:12:14 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-10-24 19:00:09 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-24 19:03:54 | Dunamale (Aththanagalu Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-10-24 19:04:07 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-24 18:02:52 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-10-24 19:02:39 | Urawa (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-10-24 18:24:45 | Thalgahagoda (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-24 19:03:08 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-10-24 19:01:05 | Horowpothana (Yan Oya) | 2.35 | 🟢 Normal | -0.010 |  |
| 2026-10-24 19:02:07 | Thanamalwila (Kirindi Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-10-24 19:03:52 | Badalgama (Maha Oya) | 2.82 | 🟢 Normal | -0.010 |  |
| 2026-10-24 19:02:18 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-10-24 18:02:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.78 | 🟢 Normal | -0.020 |  |
| 2026-10-24 19:02:23 | Giriulla (Maha Oya) | 1.49 | 🟢 Normal | -0.020 |  |
| 2026-10-24 18:00:25 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.020 |  |
| 2026-10-24 19:03:48 | Baddegama (Gin Ganga) | 2.04 | 🟢 Normal | -0.020 |  |
| 2026-10-24 18:09:14 | Pitabeddara (Nilwala Ganga) | 1.35 | 🟢 Normal | -0.022 |  |
| 2026-10-24 18:07:07 | Magura (Kalu Ganga) | 1.72 | 🟢 Normal | -0.028 |  |
| 2026-10-24 18:02:58 | Thanthirimale (Malwathu Oya) | 1.65 | 🟢 Normal | -0.030 |  |
| 2026-10-24 18:01:50 | Galgamuwa (Mee Oya) | 1.12 | 🟢 Normal | -0.030 |  |
| 2026-10-24 19:02:12 | Panadugama (Nilwala Ganga) | 3.87 | 🟢 Normal | -0.033 |  |
| 2026-10-24 18:02:34 | Hanwella (Kelani Ganga) | 3.16 | 🟢 Normal | -0.041 |  |
| 2026-10-24 18:02:11 | Thawalama (Gin Ganga) | 2.06 | 🟢 Normal | -0.045 |  |
| 2026-10-24 19:01:58 | Ellagawa (Kalu Ganga) | 5.98 | 🟢 Normal | -0.055 |  |
| 2026-10-24 19:02:04 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.068 |  |
| 2026-10-24 18:01:30 | Putupaula (Kalu Ganga) | 1.20 | 🟢 Normal | -0.075 |  |
| 2026-10-24 19:00:50 | Moragaswewa (Deduru Oya) | 1.40 | 🟢 Normal | -0.080 |  |
| 2026-10-24 19:02:33 | Deraniyagala (Kelani Ganga) | 0.94 | 🟢 Normal | -0.101 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)