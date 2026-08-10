# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--10_23:26:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **230,050 measurements** from **39** stations.
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
| 2026-08-10 23:26:02 | Panadugama (Nilwala Ganga) | 3.49 | 🟢 Normal | -0.022 |  |
| 2026-08-10 23:17:48 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-10 23:14:49 | Thalgahagoda (Nilwala Ganga) | 0.82 | 🟢 Normal | -0.037 |  |
| 2026-08-10 23:13:58 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | -0.008 |  |
| 2026-08-10 23:10:20 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-08-10 23:08:21 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-10 23:05:54 | Baddegama (Gin Ganga) | 2.20 | 🟢 Normal | -0.019 |  |
| 2026-08-10 23:05:10 | Peradeniya (Mahaweli Ganga) | 3.53 | 🟢 Normal | -0.010 |  |
| 2026-08-10 23:04:53 | Thawalama (Gin Ganga) | 1.82 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-10 23:04:29 | Nawalapitiya (Mahaweli Ganga) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-08-10 23:04:08 | Rathnapura (Kalu Ganga) | 2.12 | 🟢 Normal | -0.020 |  |
| 2026-08-10 23:04:02 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-08-10 23:03:38 | Siyambalanduwa (Heda Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-10 23:03:35 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | -0.010 |  |
| 2026-08-10 23:03:28 | Hanwella (Kelani Ganga) | 1.85 | 🟢 Normal | -0.029 |  |
| 2026-08-10 23:03:01 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | -0.020 |  |
| 2026-08-10 23:03:00 | Kithulgala (Kelani Ganga) | 2.35 | 🟢 Normal | 0.273 | 🔺 Rising |
| 2026-08-10 23:02:49 | Glencourse (Kelani Ganga) | 10.35 | 🟢 Normal | -0.011 |  |
| 2026-08-10 23:02:48 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-08-10 23:02:40 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-08-10 23:02:22 | Thanamalwila (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-10 23:02:09 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-10 23:01:55 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-08-10 23:01:41 | Manampitiya (Mahaweli Ganga) | -0.01 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-10 23:01:39 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-10 23:01:29 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-10 23:01:21 | Ellagawa (Kalu Ganga) | 5.78 | 🟢 Normal | -0.050 |  |
| 2026-08-10 23:00:53 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-10 23:00:52 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | -0.010 |  |
| 2026-08-10 23:00:13 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-10 23:03:00 | Kithulgala (Kelani Ganga) | 2.35 | 🟢 Normal | 0.273 | 🔺 Rising |
| 2026-08-10 22:02:45 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-08-10 23:01:41 | Manampitiya (Mahaweli Ganga) | -0.01 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-10 23:04:53 | Thawalama (Gin Ganga) | 1.82 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-10 23:00:53 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-10 23:01:29 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-10 23:02:40 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-08-10 23:02:09 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-10 17:02:17 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-10 22:15:18 | Magura (Kalu Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-08-10 22:03:11 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-08-10 23:01:39 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-10 23:02:48 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-08-10 23:03:38 | Siyambalanduwa (Heda Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-10 23:01:55 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-08-10 23:08:21 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-10 23:10:20 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-08-10 17:42:25 | Thanthirimale (Malwathu Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-10 23:17:48 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-10 21:06:55 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-10 23:02:22 | Thanamalwila (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-10 23:13:58 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | -0.008 |  |
| 2026-08-10 23:04:29 | Nawalapitiya (Mahaweli Ganga) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-08-10 23:00:52 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | -0.010 |  |
| 2026-08-10 23:04:02 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-08-10 23:05:10 | Peradeniya (Mahaweli Ganga) | 3.53 | 🟢 Normal | -0.010 |  |
| 2026-08-10 23:03:35 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | -0.010 |  |
| 2026-08-10 23:02:49 | Glencourse (Kelani Ganga) | 10.35 | 🟢 Normal | -0.011 |  |
| 2026-08-10 23:00:13 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | -0.011 |  |
| 2026-08-10 23:05:54 | Baddegama (Gin Ganga) | 2.20 | 🟢 Normal | -0.019 |  |
| 2026-08-10 23:03:01 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | -0.020 |  |
| 2026-08-10 18:00:16 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.020 |  |
| 2026-08-10 23:04:08 | Rathnapura (Kalu Ganga) | 2.12 | 🟢 Normal | -0.020 |  |
| 2026-08-10 23:26:02 | Panadugama (Nilwala Ganga) | 3.49 | 🟢 Normal | -0.022 |  |
| 2026-08-10 22:02:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.10 | 🟢 Normal | -0.024 |  |
| 2026-08-10 23:03:28 | Hanwella (Kelani Ganga) | 1.85 | 🟢 Normal | -0.029 |  |
| 2026-08-10 23:14:49 | Thalgahagoda (Nilwala Ganga) | 0.82 | 🟢 Normal | -0.037 |  |
| 2026-08-10 23:01:21 | Ellagawa (Kalu Ganga) | 5.78 | 🟢 Normal | -0.050 |  |
| 2026-08-10 22:06:28 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.091 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)