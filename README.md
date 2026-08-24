# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--25_02:32:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **242,672 measurements** from **39** stations.
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
| 2026-08-25 02:32:35 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-08-25 02:17:40 | Hanwella (Kelani Ganga) | 1.09 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-08-25 02:14:28 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-25 02:11:26 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-25 02:10:21 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-08-25 02:09:25 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-08-25 02:08:09 | Glencourse (Kelani Ganga) | 9.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-25 02:07:43 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-25 02:07:39 | Manampitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | 40.378 | 🔺 Rising |
| 2026-08-25 02:07:28 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-25 02:07:18 | Panadugama (Nilwala Ganga) | 2.37 | 🟢 Normal | 0.000 |  |
| 2026-08-25 02:06:25 | Manampitiya (Mahaweli Ganga) | -0.35 | 🟢 Normal | 40.378 | 🔺 Rising |
| 2026-08-25 02:04:56 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-25 02:04:02 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | -0.020 |  |
| 2026-08-25 02:03:45 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-08-25 02:03:29 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-25 02:03:12 | Horowpothana (Yan Oya) | 2.00 | 🟢 Normal | -0.020 |  |
| 2026-08-25 02:02:45 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-08-25 02:02:40 | Rathnapura (Kalu Ganga) | 1.29 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-08-25 02:02:37 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.030 |  |
| 2026-08-25 02:02:31 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-25 02:02:23 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-08-25 02:02:18 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-25 02:02:17 | Peradeniya (Mahaweli Ganga) | 2.96 | 🟢 Normal | -0.010 |  |
| 2026-08-25 02:02:13 | Ellagawa (Kalu Ganga) | 4.88 | 🟢 Normal | 0.000 |  |
| 2026-08-25 02:02:05 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-25 02:01:48 | Moragaswewa (Deduru Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-25 02:01:46 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-25 02:01:33 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-08-25 02:01:12 | Magura (Kalu Ganga) | 1.24 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-25 02:07:39 | Manampitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | 40.378 | 🔺 Rising |
| 2026-08-25 02:17:40 | Hanwella (Kelani Ganga) | 1.09 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-08-25 02:02:40 | Rathnapura (Kalu Ganga) | 1.29 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-08-25 00:19:46 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-08-25 01:43:08 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-08-25 02:08:09 | Glencourse (Kelani Ganga) | 9.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-25 00:18:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-25 02:32:35 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-08-25 02:14:28 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-25 01:02:43 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-08-25 01:00:41 | Wellawaya (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-25 02:01:46 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-25 02:01:48 | Moragaswewa (Deduru Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-25 02:01:33 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-08-25 02:11:26 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-25 02:03:45 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-08-24 18:02:21 | Galgamuwa (Mee Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-25 02:10:21 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-08-25 02:02:13 | Ellagawa (Kalu Ganga) | 4.88 | 🟢 Normal | 0.000 |  |
| 2026-08-25 02:02:45 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-08-25 02:07:18 | Panadugama (Nilwala Ganga) | 2.37 | 🟢 Normal | 0.000 |  |
| 2026-08-25 00:00:24 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-25 00:16:29 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-25 00:05:08 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-25 02:02:18 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-25 02:04:56 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-25 02:02:23 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-08-25 02:09:25 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-08-25 02:07:43 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-25 02:07:28 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-25 02:02:31 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-24 18:01:27 | Thanthirimale (Malwathu Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-08-25 02:02:17 | Peradeniya (Mahaweli Ganga) | 2.96 | 🟢 Normal | -0.010 |  |
| 2026-08-25 02:01:12 | Magura (Kalu Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-08-25 02:04:02 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | -0.020 |  |
| 2026-08-25 02:03:12 | Horowpothana (Yan Oya) | 2.00 | 🟢 Normal | -0.020 |  |
| 2026-08-25 02:02:37 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.030 |  |
| 2026-08-25 00:03:25 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | -0.031 |  |
| 2026-08-24 18:01:18 | Weraganthota (Mahaweli Ganga) | -3.03 | 🟢 Normal | -0.119 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)