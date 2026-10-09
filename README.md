# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--09_22:07:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **283,519 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-09 22:07:02 | Thalgahagoda (Nilwala Ganga) | 0.92 | 🟢 Normal | -0.009 |  |
| 2026-10-09 22:06:48 | Rathnapura (Kalu Ganga) | 4.05 | 🟢 Normal | -0.097 |  |
| 2026-10-09 22:06:42 | Holombuwa (Kelani Ganga) | 1.92 | 🟢 Normal | -0.105 |  |
| 2026-10-09 22:06:38 | Baddegama (Gin Ganga) | 2.57 | 🟢 Normal | -0.009 |  |
| 2026-10-09 22:06:02 | Thawalama (Gin Ganga) | 2.16 | 🟢 Normal | -0.010 |  |
| 2026-10-09 22:05:56 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | -0.029 |  |
| 2026-10-09 22:05:40 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-09 22:05:17 | Badalgama (Maha Oya) | 3.95 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-09 22:05:14 | Giriulla (Maha Oya) | 3.54 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-10-09 22:04:04 | Pitabeddara (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.454 | 🔺 Rising |
| 2026-10-09 22:04:00 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-10-09 22:03:55 | Norwood (Kelani Ganga) | 1.47 | 🟢 Normal | -0.033 |  |
| 2026-10-09 22:03:44 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-09 22:03:35 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-10-09 22:03:28 | Dunamale (Aththanagalu Oya) | 2.37 | 🟢 Normal | 0.250 | 🔺 Rising |
| 2026-10-09 22:02:46 | Manampitiya (Mahaweli Ganga) | -0.37 | 🟢 Normal | -0.010 |  |
| 2026-10-09 22:02:44 | Urawa (Nilwala Ganga) | 1.62 | 🟢 Normal | -0.277 |  |
| 2026-10-09 22:02:41 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-09 22:02:40 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-10-09 22:02:29 | Moragaswewa (Deduru Oya) | 1.76 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-10-09 22:02:23 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | -0.020 |  |
| 2026-10-09 22:02:20 | Ellagawa (Kalu Ganga) | 6.44 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-10-09 22:02:15 | Hanwella (Kelani Ganga) | 3.91 | 🟢 Normal | 0.216 | 🔺 Rising |
| 2026-10-09 22:02:11 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-09 22:02:09 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-10-09 22:02:06 | Thanamalwila (Kirindi Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-10-09 22:01:49 | Peradeniya (Mahaweli Ganga) | 4.56 | 🟢 Normal | -0.020 |  |
| 2026-10-09 22:01:09 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-09 22:00:43 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | -0.032 |  |
| 2026-10-09 22:00:18 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-09 22:04:04 | Pitabeddara (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.454 | 🔺 Rising |
| 2026-10-09 22:03:28 | Dunamale (Aththanagalu Oya) | 2.37 | 🟢 Normal | 0.250 | 🔺 Rising |
| 2026-10-09 22:02:15 | Hanwella (Kelani Ganga) | 3.91 | 🟢 Normal | 0.216 | 🔺 Rising |
| 2026-10-09 22:02:29 | Moragaswewa (Deduru Oya) | 1.76 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-10-09 22:02:20 | Ellagawa (Kalu Ganga) | 6.44 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-10-09 22:05:14 | Giriulla (Maha Oya) | 3.54 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-10-09 21:10:04 | Magura (Kalu Ganga) | 2.03 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-09 22:05:17 | Badalgama (Maha Oya) | 3.95 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-09 21:11:14 | Panadugama (Nilwala Ganga) | 4.05 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-09 22:00:18 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-09 21:04:36 | Glencourse (Kelani Ganga) | 12.59 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-09 18:10:37 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-09 18:01:41 | Weraganthota (Mahaweli Ganga) | -3.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-09 22:04:00 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-10-09 22:02:11 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-09 22:01:09 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-09 22:03:44 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-09 22:03:35 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-10-09 22:02:41 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-09 21:02:15 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-10-09 22:05:40 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-09 18:01:04 | Thanthirimale (Malwathu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-09 22:02:40 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-10-09 22:06:38 | Baddegama (Gin Ganga) | 2.57 | 🟢 Normal | -0.009 |  |
| 2026-10-09 22:07:02 | Thalgahagoda (Nilwala Ganga) | 0.92 | 🟢 Normal | -0.009 |  |
| 2026-10-09 22:06:02 | Thawalama (Gin Ganga) | 2.16 | 🟢 Normal | -0.010 |  |
| 2026-10-09 22:02:06 | Thanamalwila (Kirindi Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-10-09 22:02:46 | Manampitiya (Mahaweli Ganga) | -0.37 | 🟢 Normal | -0.010 |  |
| 2026-10-09 22:02:09 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-10-09 22:01:49 | Peradeniya (Mahaweli Ganga) | 4.56 | 🟢 Normal | -0.020 |  |
| 2026-10-09 22:02:23 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | -0.020 |  |
| 2026-10-09 22:05:56 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | -0.029 |  |
| 2026-10-09 22:00:43 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | -0.032 |  |
| 2026-10-09 22:03:55 | Norwood (Kelani Ganga) | 1.47 | 🟢 Normal | -0.033 |  |
| 2026-10-09 21:13:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.35 | 🟢 Normal | -0.043 |  |
| 2026-10-09 21:07:11 | Putupaula (Kalu Ganga) | 1.26 | 🟢 Normal | -0.045 |  |
| 2026-10-09 22:06:48 | Rathnapura (Kalu Ganga) | 4.05 | 🟢 Normal | -0.097 |  |
| 2026-10-09 22:06:42 | Holombuwa (Kelani Ganga) | 1.92 | 🟢 Normal | -0.105 |  |
| 2026-10-09 22:02:44 | Urawa (Nilwala Ganga) | 1.62 | 🟢 Normal | -0.277 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)