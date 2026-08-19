# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--19_08:16:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **237,521 measurements** from **39** stations.
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
| 2026-08-19 08:16:06 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.016 |  |
| 2026-08-19 08:14:27 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | -0.008 |  |
| 2026-08-19 08:11:59 | Magura (Kalu Ganga) | 1.31 | 🟢 Normal | -0.009 |  |
| 2026-08-19 08:09:12 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-19 08:09:05 | Rathnapura (Kalu Ganga) | 1.45 | 🟢 Normal | -0.018 |  |
| 2026-08-19 08:08:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.29 | 🟢 Normal | -0.099 |  |
| 2026-08-19 08:08:22 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-19 08:07:06 | Panadugama (Nilwala Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-08-19 08:07:06 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-19 08:07:01 | Peradeniya (Mahaweli Ganga) | 2.54 | 🟢 Normal | -0.059 |  |
| 2026-08-19 08:05:34 | Glencourse (Kelani Ganga) | 9.69 | 🟢 Normal | -0.010 |  |
| 2026-08-19 08:05:22 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-08-19 08:04:57 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-19 08:04:40 | Putupaula (Kalu Ganga) | 0.83 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-19 08:04:23 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-19 08:03:48 | Hanwella (Kelani Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-08-19 08:03:38 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-08-19 08:03:34 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-19 08:03:10 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-19 08:02:51 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-19 08:02:51 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-19 08:02:44 | Moragaswewa (Deduru Oya) | -0.08 | 🟢 Normal | -0.010 |  |
| 2026-08-19 08:02:43 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.088 |  |
| 2026-08-19 08:02:43 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-08-19 08:02:42 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | -0.050 |  |
| 2026-08-19 08:02:41 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-19 08:02:31 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-19 08:02:25 | Ellagawa (Kalu Ganga) | 5.19 | 🟢 Normal | -0.010 |  |
| 2026-08-19 08:02:17 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-19 08:02:15 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-08-19 08:01:51 | Thanthirimale (Malwathu Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-08-19 08:01:49 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-19 08:01:21 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-19 08:01:19 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | -0.010 |  |
| 2026-08-19 08:01:16 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.063 |  |
| 2026-08-19 08:01:09 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-08-19 08:00:32 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-08-19 08:00:14 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-19 08:04:40 | Putupaula (Kalu Ganga) | 0.83 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-19 08:02:51 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-19 08:02:15 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-08-19 08:02:41 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-19 08:03:10 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-19 08:04:57 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-19 08:01:09 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-08-19 08:01:49 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-19 08:00:14 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-19 08:01:21 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-19 08:02:51 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-19 08:03:48 | Hanwella (Kelani Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-08-19 08:07:06 | Panadugama (Nilwala Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-08-19 08:04:23 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-19 08:08:22 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-19 08:07:06 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-19 08:02:17 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-19 08:03:34 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-19 08:03:38 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-08-19 08:09:12 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-19 08:01:51 | Thanthirimale (Malwathu Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-08-19 08:05:22 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-08-19 07:03:20 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-19 08:02:31 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-19 08:14:27 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | -0.008 |  |
| 2026-08-19 08:11:59 | Magura (Kalu Ganga) | 1.31 | 🟢 Normal | -0.009 |  |
| 2026-08-19 08:02:44 | Moragaswewa (Deduru Oya) | -0.08 | 🟢 Normal | -0.010 |  |
| 2026-08-19 08:02:25 | Ellagawa (Kalu Ganga) | 5.19 | 🟢 Normal | -0.010 |  |
| 2026-08-19 08:01:19 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | -0.010 |  |
| 2026-08-19 08:05:34 | Glencourse (Kelani Ganga) | 9.69 | 🟢 Normal | -0.010 |  |
| 2026-08-19 08:02:43 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-08-19 08:00:32 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-08-19 08:16:06 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.016 |  |
| 2026-08-19 08:09:05 | Rathnapura (Kalu Ganga) | 1.45 | 🟢 Normal | -0.018 |  |
| 2026-08-19 08:02:42 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | -0.050 |  |
| 2026-08-19 08:07:01 | Peradeniya (Mahaweli Ganga) | 2.54 | 🟢 Normal | -0.059 |  |
| 2026-08-19 08:01:16 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.063 |  |
| 2026-08-19 08:02:43 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.088 |  |
| 2026-08-19 08:08:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.29 | 🟢 Normal | -0.099 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)