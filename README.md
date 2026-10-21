# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--21_17:08:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **294,164 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-21 17:08:20 | Peradeniya (Mahaweli Ganga) | 3.50 | 🟢 Normal | 0.640 | 🔺 Rising |
| 2026-10-21 17:07:11 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.046 |  |
| 2026-10-21 17:06:56 | Thanthirimale (Malwathu Oya) | 1.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 17:05:52 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-21 17:05:41 | Badalgama (Maha Oya) | 2.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-21 17:05:41 | Holombuwa (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-10-21 17:05:16 | Pitabeddara (Nilwala Ganga) | 1.57 | 🟢 Normal | 0.266 | 🔺 Rising |
| 2026-10-21 17:05:11 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-21 17:05:07 | Hanwella (Kelani Ganga) | 2.31 | 🟢 Normal | -0.029 |  |
| 2026-10-21 17:04:39 | Moraketiya (Walawe Ganga) | 1.29 | 🟢 Normal | -0.114 |  |
| 2026-10-21 17:04:37 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | 0.193 | 🔺 Rising |
| 2026-10-21 17:04:24 | Manampitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-21 17:03:31 | Rathnapura (Kalu Ganga) | 1.83 | 🟢 Normal | -0.012 |  |
| 2026-10-21 17:03:30 | Horowpothana (Yan Oya) | 2.43 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-21 17:03:12 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-21 17:03:06 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-10-21 17:03:05 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-10-21 17:03:01 | Nawalapitiya (Mahaweli Ganga) | 1.76 | 🟢 Normal | 0.495 | 🔺 Rising |
| 2026-10-21 17:03:00 | Moragaswewa (Deduru Oya) | 1.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 17:02:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.58 | 🟢 Normal | -0.090 |  |
| 2026-10-21 17:02:26 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-10-21 17:02:25 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-21 17:02:20 | Nakkala (Kumbukkan Oya) | 1.90 | 🟢 Normal | 0.825 | 🔺 Rising |
| 2026-10-21 17:02:14 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | -0.010 |  |
| 2026-10-21 17:02:13 | Dunamale (Aththanagalu Oya) | 1.65 | 🟢 Normal | -0.049 |  |
| 2026-10-21 17:01:55 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.031 |  |
| 2026-10-21 17:01:34 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-21 17:01:34 | Glencourse (Kelani Ganga) | 10.50 | 🟢 Normal | 0.000 |  |
| 2026-10-21 17:01:25 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-10-21 17:01:21 | Thanamalwila (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-10-21 17:01:19 | Thaldena (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.237 |  |
| 2026-10-21 17:01:09 | Wellawaya (Kirindi Oya) | 3.33 | 🟢 Normal | 1.937 | 🔺 Rising |
| 2026-10-21 17:00:45 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | -0.031 |  |
| 2026-10-21 17:00:07 | Magura (Kalu Ganga) | 1.61 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-21 17:01:09 | Wellawaya (Kirindi Oya) | 3.33 | 🟢 Normal | 1.937 | 🔺 Rising |
| 2026-10-21 17:02:20 | Nakkala (Kumbukkan Oya) | 1.90 | 🟢 Normal | 0.825 | 🔺 Rising |
| 2026-10-21 17:08:20 | Peradeniya (Mahaweli Ganga) | 3.50 | 🟢 Normal | 0.640 | 🔺 Rising |
| 2026-10-21 17:03:01 | Nawalapitiya (Mahaweli Ganga) | 1.76 | 🟢 Normal | 0.495 | 🔺 Rising |
| 2026-10-21 17:05:16 | Pitabeddara (Nilwala Ganga) | 1.57 | 🟢 Normal | 0.266 | 🔺 Rising |
| 2026-10-21 17:04:37 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | 0.193 | 🔺 Rising |
| 2026-10-21 17:03:05 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-10-21 17:04:24 | Manampitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-21 17:03:30 | Horowpothana (Yan Oya) | 2.43 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-21 17:02:25 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-21 17:05:52 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-21 16:01:10 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-21 17:01:25 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-10-21 17:05:41 | Badalgama (Maha Oya) | 2.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-21 17:03:12 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-21 17:03:00 | Moragaswewa (Deduru Oya) | 1.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 17:06:56 | Thanthirimale (Malwathu Oya) | 1.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 17:01:34 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-21 17:00:07 | Magura (Kalu Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-21 17:03:06 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-10-21 17:01:34 | Glencourse (Kelani Ganga) | 10.50 | 🟢 Normal | 0.000 |  |
| 2026-10-21 17:05:41 | Holombuwa (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-10-21 16:07:44 | Urawa (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-21 17:05:11 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-21 17:02:26 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-10-21 17:01:21 | Thanamalwila (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-10-21 16:12:32 | Galgamuwa (Mee Oya) | 1.53 | 🟢 Normal | -0.009 |  |
| 2026-10-21 16:05:34 | Ellagawa (Kalu Ganga) | 5.55 | 🟢 Normal | -0.009 |  |
| 2026-10-21 17:02:14 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | -0.010 |  |
| 2026-10-21 17:03:31 | Rathnapura (Kalu Ganga) | 1.83 | 🟢 Normal | -0.012 |  |
| 2026-10-21 16:07:22 | Panadugama (Nilwala Ganga) | 3.95 | 🟢 Normal | -0.021 |  |
| 2026-10-21 17:05:07 | Hanwella (Kelani Ganga) | 2.31 | 🟢 Normal | -0.029 |  |
| 2026-10-21 17:00:45 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | -0.031 |  |
| 2026-10-21 17:01:55 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.031 |  |
| 2026-10-21 17:07:11 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.046 |  |
| 2026-10-21 17:02:13 | Dunamale (Aththanagalu Oya) | 1.65 | 🟢 Normal | -0.049 |  |
| 2026-10-21 17:02:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.58 | 🟢 Normal | -0.090 |  |
| 2026-10-21 17:04:39 | Moraketiya (Walawe Ganga) | 1.29 | 🟢 Normal | -0.114 |  |
| 2026-10-21 17:01:19 | Thaldena (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.237 |  |

## River Water Level Charts by Station

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)