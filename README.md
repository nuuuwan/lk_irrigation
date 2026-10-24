# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--24_15:07:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **296,763 measurements** from **39** stations.
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
| 2026-10-24 15:07:06 | Glencourse (Kelani Ganga) | 10.93 | 🟢 Normal | -0.037 |  |
| 2026-10-24 15:06:30 | Pitabeddara (Nilwala Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-10-24 15:06:30 | Rathnapura (Kalu Ganga) | 2.10 | 🟢 Normal | -0.029 |  |
| 2026-10-24 15:06:26 | Holombuwa (Kelani Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-10-24 15:06:18 | Dunamale (Aththanagalu Oya) | 1.82 | 🟢 Normal | -0.077 |  |
| 2026-10-24 15:05:25 | Deraniyagala (Kelani Ganga) | 0.96 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-24 15:05:18 | Putupaula (Kalu Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-10-24 15:04:38 | Badalgama (Maha Oya) | 2.87 | 🟢 Normal | -0.020 |  |
| 2026-10-24 15:04:38 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-10-24 15:04:17 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-10-24 15:04:11 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.089 |  |
| 2026-10-24 15:04:06 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-24 15:03:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.85 | 🟢 Normal | -0.019 |  |
| 2026-10-24 15:03:40 | Magura (Kalu Ganga) | 1.81 | 🟢 Normal | -0.027 |  |
| 2026-10-24 15:03:35 | Urawa (Nilwala Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-10-24 15:03:35 | Thawalama (Gin Ganga) | 2.08 | 🟢 Normal | -0.010 |  |
| 2026-10-24 15:03:17 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-10-24 15:03:07 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.012 |  |
| 2026-10-24 15:02:55 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-10-24 15:02:40 | Manampitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-10-24 15:02:39 | Hanwella (Kelani Ganga) | 3.30 | 🟢 Normal | -0.050 |  |
| 2026-10-24 15:02:38 | Giriulla (Maha Oya) | 1.56 | 🟢 Normal | -0.010 |  |
| 2026-10-24 15:02:24 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-10-24 15:02:11 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-10-24 15:01:52 | Moragaswewa (Deduru Oya) | 1.68 | 🟢 Normal | -0.429 |  |
| 2026-10-24 15:01:47 | Thanthirimale (Malwathu Oya) | 1.74 | 🟢 Normal | -0.031 |  |
| 2026-10-24 15:01:27 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-24 15:01:25 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.218 |  |
| 2026-10-24 15:01:24 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-24 15:01:10 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-24 15:01:09 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-10-24 15:00:43 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | -0.020 |  |
| 2026-10-24 15:00:39 | Horowpothana (Yan Oya) | 2.32 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-24 15:00:32 | Galgamuwa (Mee Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-10-24 15:00:12 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.154 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-24 15:00:39 | Horowpothana (Yan Oya) | 2.32 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-24 15:05:25 | Deraniyagala (Kelani Ganga) | 0.96 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-24 15:02:55 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-10-24 15:01:24 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-24 15:01:10 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-24 15:00:32 | Galgamuwa (Mee Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-10-24 15:06:30 | Pitabeddara (Nilwala Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-10-24 15:03:17 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-10-24 14:07:20 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-10-24 15:04:38 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-10-24 15:01:27 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-24 15:04:06 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-24 15:06:26 | Holombuwa (Kelani Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-10-24 15:02:40 | Manampitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-10-24 14:04:00 | Thalgahagoda (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-24 15:02:11 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-10-24 15:03:35 | Thawalama (Gin Ganga) | 2.08 | 🟢 Normal | -0.010 |  |
| 2026-10-24 15:04:17 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-10-24 15:01:09 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-10-24 15:05:18 | Putupaula (Kalu Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-10-24 15:02:24 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-10-24 15:02:38 | Giriulla (Maha Oya) | 1.56 | 🟢 Normal | -0.010 |  |
| 2026-10-24 15:03:35 | Urawa (Nilwala Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-10-24 15:03:07 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.012 |  |
| 2026-10-24 14:08:32 | Panadugama (Nilwala Ganga) | 3.98 | 🟢 Normal | -0.019 |  |
| 2026-10-24 15:03:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.85 | 🟢 Normal | -0.019 |  |
| 2026-10-24 15:00:43 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | -0.020 |  |
| 2026-10-24 15:04:38 | Badalgama (Maha Oya) | 2.87 | 🟢 Normal | -0.020 |  |
| 2026-10-24 15:03:40 | Magura (Kalu Ganga) | 1.81 | 🟢 Normal | -0.027 |  |
| 2026-10-24 15:06:30 | Rathnapura (Kalu Ganga) | 2.10 | 🟢 Normal | -0.029 |  |
| 2026-10-24 15:01:47 | Thanthirimale (Malwathu Oya) | 1.74 | 🟢 Normal | -0.031 |  |
| 2026-10-24 14:09:11 | Ellagawa (Kalu Ganga) | 6.21 | 🟢 Normal | -0.035 |  |
| 2026-10-24 15:07:06 | Glencourse (Kelani Ganga) | 10.93 | 🟢 Normal | -0.037 |  |
| 2026-10-24 15:02:39 | Hanwella (Kelani Ganga) | 3.30 | 🟢 Normal | -0.050 |  |
| 2026-10-24 15:06:18 | Dunamale (Aththanagalu Oya) | 1.82 | 🟢 Normal | -0.077 |  |
| 2026-10-24 15:04:11 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.089 |  |
| 2026-10-24 15:00:12 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.154 |  |
| 2026-10-24 15:01:25 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.218 |  |
| 2026-10-24 15:01:52 | Moragaswewa (Deduru Oya) | 1.68 | 🟢 Normal | -0.429 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)