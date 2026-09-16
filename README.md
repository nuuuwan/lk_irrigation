# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--16_17:05:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **262,621 measurements** from **39** stations.
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
| 2026-09-16 17:05:23 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-16 17:05:08 | Magura (Kalu Ganga) | 2.76 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-09-16 17:04:55 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-09-16 17:04:51 | Ellagawa (Kalu Ganga) | 5.40 | 🟢 Normal | -0.059 |  |
| 2026-09-16 17:04:49 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2026-09-16 17:04:40 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-16 17:04:29 | Hanwella (Kelani Ganga) | 1.45 | 🟢 Normal | -0.059 |  |
| 2026-09-16 17:04:07 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-16 17:04:02 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-09-16 17:03:35 | Wellawaya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-09-16 17:03:18 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-09-16 17:03:14 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-16 17:03:04 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-09-16 17:02:53 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-16 17:02:47 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-16 17:02:45 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | -0.021 |  |
| 2026-09-16 17:02:36 | Dunamale (Aththanagalu Oya) | 1.86 | 🟢 Normal | -0.021 |  |
| 2026-09-16 17:02:19 | Pitabeddara (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-16 17:02:19 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-16 17:02:18 | Glencourse (Kelani Ganga) | 9.48 | 🟢 Normal | -0.031 |  |
| 2026-09-16 17:02:16 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-09-16 17:02:08 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-09-16 17:01:50 | Horowpothana (Yan Oya) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-09-16 17:01:39 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-16 17:01:16 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-16 17:01:09 | Thanthirimale (Malwathu Oya) | 0.49 | 🟢 Normal | -0.020 |  |
| 2026-09-16 17:00:59 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-09-16 17:00:35 | Rathnapura (Kalu Ganga) | 1.38 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-16 17:00:31 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-16 16:23:04 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.086 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-16 17:04:49 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2026-09-16 17:03:18 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-09-16 17:04:55 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-09-16 17:05:08 | Magura (Kalu Ganga) | 2.76 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-09-16 17:00:35 | Rathnapura (Kalu Ganga) | 1.38 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-16 17:03:14 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-16 16:18:45 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-09-16 16:08:23 | Kithulgala (Kelani Ganga) | 1.76 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-16 17:02:19 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-16 16:03:52 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-16 17:02:16 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-09-16 16:06:22 | Baddegama (Gin Ganga) | 3.06 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-16 17:02:19 | Pitabeddara (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-16 17:04:07 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-16 17:02:47 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-16 17:01:39 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-16 17:04:40 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-16 17:02:53 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-16 17:00:31 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-16 17:01:16 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-16 16:03:10 | Putupaula (Kalu Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-16 17:05:23 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-16 17:02:08 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-09-16 16:12:01 | Panadugama (Nilwala Ganga) | 2.55 | 🟢 Normal | -0.010 |  |
| 2026-09-16 16:02:02 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | -0.010 |  |
| 2026-09-16 17:01:50 | Horowpothana (Yan Oya) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-09-16 17:03:04 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-09-16 17:03:35 | Wellawaya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-09-16 17:00:59 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-09-16 17:04:02 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-09-16 16:06:24 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | -0.020 |  |
| 2026-09-16 16:02:35 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.020 |  |
| 2026-09-16 17:01:09 | Thanthirimale (Malwathu Oya) | 0.49 | 🟢 Normal | -0.020 |  |
| 2026-09-16 17:02:45 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | -0.021 |  |
| 2026-09-16 17:02:36 | Dunamale (Aththanagalu Oya) | 1.86 | 🟢 Normal | -0.021 |  |
| 2026-09-16 17:02:18 | Glencourse (Kelani Ganga) | 9.48 | 🟢 Normal | -0.031 |  |
| 2026-09-16 16:10:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.75 | 🟢 Normal | -0.045 |  |
| 2026-09-16 17:04:29 | Hanwella (Kelani Ganga) | 1.45 | 🟢 Normal | -0.059 |  |
| 2026-09-16 17:04:51 | Ellagawa (Kalu Ganga) | 5.40 | 🟢 Normal | -0.059 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)