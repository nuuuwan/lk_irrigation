# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--10_17:44:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **229,833 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **26** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-10 17:44:35 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.011 |  |
| 2026-08-10 17:42:25 | Thanthirimale (Malwathu Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-10 17:24:44 | Thawalama (Gin Ganga) | 1.84 | 🟢 Normal | 90.000 | 🔺 Rising |
| 2026-08-10 17:24:16 | Thawalama (Gin Ganga) | 1.14 | 🟢 Normal | 90.000 | 🔺 Rising |
| 2026-08-10 17:24:14 | Thawalama (Gin Ganga) | 1.87 | 🟢 Normal | 90.000 | 🔺 Rising |
| 2026-08-10 17:20:41 | Magura (Kalu Ganga) | 1.82 | 🟢 Normal | -0.018 |  |
| 2026-08-10 17:18:46 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.016 |  |
| 2026-08-10 17:15:13 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | -0.008 |  |
| 2026-08-10 17:13:54 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-10 17:12:15 | Panadugama (Nilwala Ganga) | 3.10 | 🟢 Normal | -0.525 |  |
| 2026-08-10 17:10:28 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-08-10 17:08:13 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-10 17:08:00 | Nawalapitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | -0.009 |  |
| 2026-08-10 17:07:23 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-10 17:07:15 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-10 17:06:13 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-08-10 17:05:56 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-08-10 17:05:48 | Glencourse (Kelani Ganga) | 10.34 | 🟢 Normal | -0.010 |  |
| 2026-08-10 17:05:21 | Rathnapura (Kalu Ganga) | 2.26 | 🟢 Normal | -0.030 |  |
| 2026-08-10 17:05:12 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-10 17:05:07 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.029 |  |
| 2026-08-10 17:04:46 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-10 17:04:10 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-10 17:03:47 | Deraniyagala (Kelani Ganga) | 1.13 | 🟢 Normal | -0.049 |  |
| 2026-08-10 17:03:31 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | -0.023 |  |
| 2026-08-10 17:03:19 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-10 17:24:44 | Thawalama (Gin Ganga) | 1.84 | 🟢 Normal | 90.000 | 🔺 Rising |
| 2026-08-10 17:00:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.14 | 🟢 Normal | 0.239 | 🔺 Rising |
| 2026-08-10 17:00:32 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | 0.000 |  |
| 2026-08-10 17:02:28 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-08-10 17:00:36 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-10 17:04:46 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-10 17:13:54 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-10 17:02:17 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-10 17:07:23 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-10 17:08:13 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-10 17:10:28 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-08-10 17:07:15 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-10 17:00:47 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-08-10 17:06:13 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-08-10 17:04:10 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-10 17:42:25 | Thanthirimale (Malwathu Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-10 17:05:12 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-10 17:03:11 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-10 17:15:13 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | -0.008 |  |
| 2026-08-10 17:08:00 | Nawalapitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | -0.009 |  |
| 2026-08-10 17:05:48 | Glencourse (Kelani Ganga) | 10.34 | 🟢 Normal | -0.010 |  |
| 2026-08-10 17:05:56 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-08-10 17:01:06 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-08-10 17:00:38 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | -0.010 |  |
| 2026-08-10 17:03:19 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-08-10 17:00:49 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-08-10 17:01:40 | Peradeniya (Mahaweli Ganga) | 3.58 | 🟢 Normal | -0.011 |  |
| 2026-08-10 17:44:35 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.011 |  |
| 2026-08-10 17:18:46 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.016 |  |
| 2026-08-10 17:20:41 | Magura (Kalu Ganga) | 1.82 | 🟢 Normal | -0.018 |  |
| 2026-08-10 17:01:11 | Baddegama (Gin Ganga) | 2.29 | 🟢 Normal | -0.021 |  |
| 2026-08-10 17:03:31 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | -0.023 |  |
| 2026-08-10 17:05:07 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.029 |  |
| 2026-08-10 17:05:21 | Rathnapura (Kalu Ganga) | 2.26 | 🟢 Normal | -0.030 |  |
| 2026-08-10 17:01:44 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.030 |  |
| 2026-08-10 17:03:47 | Deraniyagala (Kelani Ganga) | 1.13 | 🟢 Normal | -0.049 |  |
| 2026-08-10 17:03:06 | Ellagawa (Kalu Ganga) | 6.05 | 🟢 Normal | -0.051 |  |
| 2026-08-10 17:02:21 | Hanwella (Kelani Ganga) | 2.09 | 🟢 Normal | -0.071 |  |
| 2026-08-10 17:12:15 | Panadugama (Nilwala Ganga) | 3.10 | 🟢 Normal | -0.525 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)