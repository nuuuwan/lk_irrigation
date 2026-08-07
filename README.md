# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--07_19:23:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **227,206 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-07 19:23:34 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-08-07 19:16:34 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-07 19:16:20 | Rathnapura (Kalu Ganga) | 1.87 | 🟢 Normal | -0.008 |  |
| 2026-08-07 19:15:31 | Peradeniya (Mahaweli Ganga) | 3.96 | 🟢 Normal | -0.008 |  |
| 2026-08-07 19:13:36 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-07 19:11:37 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | -0.017 |  |
| 2026-08-07 19:11:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.85 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-08-07 19:09:33 | Magura (Kalu Ganga) | 1.67 | 🟢 Normal | -0.026 |  |
| 2026-08-07 19:09:21 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-08-07 19:07:36 | Glencourse (Kelani Ganga) | 11.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-07 19:07:13 | Badalgama (Maha Oya) | 2.20 | 🟢 Normal | -0.009 |  |
| 2026-08-07 19:06:30 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-07 19:06:27 | Ellagawa (Kalu Ganga) | 5.62 | 🟢 Normal | -0.037 |  |
| 2026-08-07 19:06:14 | Deraniyagala (Kelani Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-08-07 19:05:44 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-07 19:05:10 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | -108.000 |  |
| 2026-08-07 19:05:09 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | -108.000 |  |
| 2026-08-07 19:04:53 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-07 19:04:28 | Hanwella (Kelani Ganga) | 2.69 | 🟢 Normal | -0.039 |  |
| 2026-08-07 19:04:26 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-08-07 19:03:52 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | -0.010 |  |
| 2026-08-07 19:03:30 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-08-07 19:03:21 | Kithulgala (Kelani Ganga) | 2.35 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-08-07 19:03:00 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-07 19:02:44 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-08-07 19:02:37 | Norwood (Kelani Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-08-07 19:02:25 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-07 19:02:24 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-07 19:02:19 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-07 19:02:07 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-08-07 19:02:03 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.030 |  |
| 2026-08-07 19:01:38 | Panadugama (Nilwala Ganga) | 2.49 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-08-07 19:01:32 | Nawalapitiya (Mahaweli Ganga) | 2.16 | 🟢 Normal | -0.020 |  |
| 2026-08-07 19:01:31 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | -0.011 |  |
| 2026-08-07 19:01:25 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-07 19:00:49 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-07 19:00:10 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-07 19:03:21 | Kithulgala (Kelani Ganga) | 2.35 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-08-07 19:11:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.85 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-08-07 19:01:38 | Panadugama (Nilwala Ganga) | 2.49 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-08-07 19:07:36 | Glencourse (Kelani Ganga) | 11.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-07 19:06:30 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-07 18:07:07 | Thanamalwila (Kirindi Oya) | 0.56 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-08-07 19:09:21 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-08-07 19:00:49 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-07 18:00:27 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | 0.000 |  |
| 2026-08-07 19:00:10 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-07 19:16:34 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-07 19:02:24 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-07 19:04:26 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-08-07 19:23:34 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-08-07 18:10:22 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-07 19:05:44 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-07 19:06:14 | Deraniyagala (Kelani Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-08-07 19:04:53 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-07 19:02:19 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-07 19:02:25 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-07 18:01:27 | Thanthirimale (Malwathu Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-08-07 19:13:36 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-07 19:02:07 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-08-07 19:01:25 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-07 19:16:20 | Rathnapura (Kalu Ganga) | 1.87 | 🟢 Normal | -0.008 |  |
| 2026-08-07 19:15:31 | Peradeniya (Mahaweli Ganga) | 3.96 | 🟢 Normal | -0.008 |  |
| 2026-08-07 19:07:13 | Badalgama (Maha Oya) | 2.20 | 🟢 Normal | -0.009 |  |
| 2026-08-07 19:03:30 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-08-07 19:03:52 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | -0.010 |  |
| 2026-08-07 19:02:37 | Norwood (Kelani Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-08-07 19:02:44 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-08-07 19:01:31 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | -0.011 |  |
| 2026-08-07 19:11:37 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | -0.017 |  |
| 2026-08-07 19:01:32 | Nawalapitiya (Mahaweli Ganga) | 2.16 | 🟢 Normal | -0.020 |  |
| 2026-08-07 19:09:33 | Magura (Kalu Ganga) | 1.67 | 🟢 Normal | -0.026 |  |
| 2026-08-07 19:02:03 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.030 |  |
| 2026-08-07 19:06:27 | Ellagawa (Kalu Ganga) | 5.62 | 🟢 Normal | -0.037 |  |
| 2026-08-07 19:04:28 | Hanwella (Kelani Ganga) | 2.69 | 🟢 Normal | -0.039 |  |
| 2026-08-07 19:05:10 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | -108.000 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)