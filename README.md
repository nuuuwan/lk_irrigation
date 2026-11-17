# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--17_15:03:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **318,362 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **21** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-17 15:03:07 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | 0.000 |  |
| 2026-11-17 15:02:53 | Hanwella (Kelani Ganga) | 1.97 | 🟢 Normal | -0.010 |  |
| 2026-11-17 15:02:50 | Dunamale (Aththanagalu Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-11-17 15:02:46 | Moragaswewa (Deduru Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-11-17 15:02:45 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | -0.011 |  |
| 2026-11-17 15:02:45 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-17 15:02:44 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-17 15:02:43 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-11-17 15:02:31 | Wellawaya (Kirindi Oya) | 1.27 | 🟢 Normal | -0.029 |  |
| 2026-11-17 15:02:18 | Manampitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-11-17 15:02:14 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-11-17 15:02:08 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-17 15:01:45 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-11-17 15:01:40 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-17 15:01:12 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-11-17 15:01:10 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-11-17 15:00:32 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-11-17 15:00:09 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-17 14:30:50 | Pitabeddara (Nilwala Ganga) | 1.20 | 🟢 Normal | -0.007 |  |
| 2026-11-17 14:12:29 | Magura (Kalu Ganga) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-11-17 14:12:16 | Horowpothana (Yan Oya) | 1.90 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-17 14:02:53 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-11-17 15:00:32 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-11-17 15:01:12 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-11-17 15:01:40 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-17 14:02:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.46 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-17 14:09:22 | Rathnapura (Kalu Ganga) | 1.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-17 14:06:26 | Peradeniya (Mahaweli Ganga) | 2.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-17 15:02:46 | Moragaswewa (Deduru Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-11-17 15:02:43 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-11-17 15:02:08 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-17 15:02:44 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-17 14:12:16 | Horowpothana (Yan Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-11-17 14:02:50 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-11-17 14:04:39 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-11-17 13:07:40 | Padiyathalawa (Maduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-11-17 14:05:11 | Glencourse (Kelani Ganga) | 10.22 | 🟢 Normal | 0.000 |  |
| 2026-11-17 15:00:09 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-17 15:02:50 | Dunamale (Aththanagalu Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-11-17 15:02:45 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-17 14:02:46 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-17 15:03:07 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | 0.000 |  |
| 2026-11-17 15:02:18 | Manampitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-11-17 14:05:29 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-11-17 14:09:59 | Urawa (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-11-17 14:07:01 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-17 14:30:50 | Pitabeddara (Nilwala Ganga) | 1.20 | 🟢 Normal | -0.007 |  |
| 2026-11-17 15:02:14 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-11-17 14:12:29 | Magura (Kalu Ganga) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-11-17 14:03:09 | Ellagawa (Kalu Ganga) | 5.08 | 🟢 Normal | -0.010 |  |
| 2026-11-17 15:02:53 | Hanwella (Kelani Ganga) | 1.97 | 🟢 Normal | -0.010 |  |
| 2026-11-17 15:01:10 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-11-17 15:01:45 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-11-17 13:04:03 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-11-17 15:02:45 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | -0.011 |  |
| 2026-11-17 14:02:08 | Kuda Oya (Kirindi Oya) | 1.57 | 🟢 Normal | -0.011 |  |
| 2026-11-17 14:09:10 | Panadugama (Nilwala Ganga) | 3.76 | 🟢 Normal | -0.019 |  |
| 2026-11-17 14:04:41 | Baddegama (Gin Ganga) | 1.65 | 🟢 Normal | -0.021 |  |
| 2026-11-17 15:02:31 | Wellawaya (Kirindi Oya) | 1.27 | 🟢 Normal | -0.029 |  |
| 2026-11-17 14:06:46 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | -0.093 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)