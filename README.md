# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--17_15:19:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **318,382 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-17 15:19:28 | Pitabeddara (Nilwala Ganga) | 1.19 | 🟢 Normal | -0.012 |  |
| 2026-11-17 15:13:53 | Padiyathalawa (Maduru Oya) | 0.38 | 🟢 Normal | -0.005 |  |
| 2026-11-17 15:10:26 | Panadugama (Nilwala Ganga) | 3.74 | 🟢 Normal | -0.020 |  |
| 2026-11-17 15:09:41 | Baddegama (Gin Ganga) | 1.64 | 🟢 Normal | -0.009 |  |
| 2026-11-17 15:09:08 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | -0.019 |  |
| 2026-11-17 15:08:43 | Urawa (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-11-17 15:08:30 | Rathnapura (Kalu Ganga) | 1.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-17 15:07:16 | Glencourse (Kelani Ganga) | 10.18 | 🟢 Normal | -0.039 |  |
| 2026-11-17 15:07:06 | Magura (Kalu Ganga) | 1.60 | 🟢 Normal | -0.011 |  |
| 2026-11-17 15:07:02 | Holombuwa (Kelani Ganga) | 0.67 | 🟢 Normal | -0.015 |  |
| 2026-11-17 15:06:15 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-17 15:05:56 | Thalgahagoda (Nilwala Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-11-17 15:05:50 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-11-17 15:05:25 | Ellagawa (Kalu Ganga) | 5.07 | 🟢 Normal | -0.010 |  |
| 2026-11-17 15:05:12 | Peradeniya (Mahaweli Ganga) | 2.67 | 🟢 Normal | -0.020 |  |
| 2026-11-17 15:04:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-17 15:04:06 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-11-17 15:03:42 | Kuda Oya (Kirindi Oya) | 1.56 | 🟢 Normal | -0.010 |  |
| 2026-11-17 15:03:30 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-11-17 15:03:28 | Horowpothana (Yan Oya) | 1.89 | 🟢 Normal | -0.012 |  |
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

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-17 15:00:32 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-11-17 15:01:12 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-11-17 15:01:40 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-17 15:08:30 | Rathnapura (Kalu Ganga) | 1.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-17 15:06:15 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-17 15:04:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-17 15:03:30 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-11-17 15:02:46 | Moragaswewa (Deduru Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-11-17 15:02:43 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-11-17 15:02:08 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-17 15:02:44 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-17 15:05:50 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-11-17 15:00:09 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-17 15:02:50 | Dunamale (Aththanagalu Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-11-17 15:02:45 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-17 14:02:46 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-17 15:03:07 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | 0.000 |  |
| 2026-11-17 15:02:18 | Manampitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-11-17 15:08:43 | Urawa (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-11-17 15:13:53 | Padiyathalawa (Maduru Oya) | 0.38 | 🟢 Normal | -0.005 |  |
| 2026-11-17 15:09:41 | Baddegama (Gin Ganga) | 1.64 | 🟢 Normal | -0.009 |  |
| 2026-11-17 15:05:25 | Ellagawa (Kalu Ganga) | 5.07 | 🟢 Normal | -0.010 |  |
| 2026-11-17 15:02:14 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-11-17 15:03:42 | Kuda Oya (Kirindi Oya) | 1.56 | 🟢 Normal | -0.010 |  |
| 2026-11-17 15:04:06 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-11-17 15:02:53 | Hanwella (Kelani Ganga) | 1.97 | 🟢 Normal | -0.010 |  |
| 2026-11-17 15:01:10 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-11-17 15:01:45 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-11-17 15:05:56 | Thalgahagoda (Nilwala Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-11-17 15:02:45 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | -0.011 |  |
| 2026-11-17 15:07:06 | Magura (Kalu Ganga) | 1.60 | 🟢 Normal | -0.011 |  |
| 2026-11-17 15:03:28 | Horowpothana (Yan Oya) | 1.89 | 🟢 Normal | -0.012 |  |
| 2026-11-17 15:19:28 | Pitabeddara (Nilwala Ganga) | 1.19 | 🟢 Normal | -0.012 |  |
| 2026-11-17 15:07:02 | Holombuwa (Kelani Ganga) | 0.67 | 🟢 Normal | -0.015 |  |
| 2026-11-17 15:09:08 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | -0.019 |  |
| 2026-11-17 15:10:26 | Panadugama (Nilwala Ganga) | 3.74 | 🟢 Normal | -0.020 |  |
| 2026-11-17 15:05:12 | Peradeniya (Mahaweli Ganga) | 2.67 | 🟢 Normal | -0.020 |  |
| 2026-11-17 15:02:31 | Wellawaya (Kirindi Oya) | 1.27 | 🟢 Normal | -0.029 |  |
| 2026-11-17 15:07:16 | Glencourse (Kelani Ganga) | 10.18 | 🟢 Normal | -0.039 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)