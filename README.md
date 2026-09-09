# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--10_00:06:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **256,603 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-10 00:06:59 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.009 |  |
| 2026-09-10 00:06:25 | Rathnapura (Kalu Ganga) | 1.09 | 🟢 Normal | -0.020 |  |
| 2026-09-10 00:05:59 | Thanamalwila (Kirindi Oya) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-09-10 00:05:51 | Kuda Oya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-10 00:05:17 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-09-10 00:04:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.84 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-09-10 00:04:26 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-09-10 00:04:26 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-09-10 00:04:18 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-10 00:03:56 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-09-10 00:03:54 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-10 00:03:40 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-10 00:03:36 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-10 00:03:17 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-09-10 00:02:41 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-10 00:02:36 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-09-10 00:02:28 | Magura (Kalu Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-10 00:02:15 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | -0.020 |  |
| 2026-09-10 00:02:09 | Glencourse (Kelani Ganga) | 9.30 | 🟢 Normal | -0.053 |  |
| 2026-09-10 00:02:05 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-10 00:01:47 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-10 00:01:27 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-10 00:01:26 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-09-10 00:01:16 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-10 00:01:03 | Moragaswewa (Deduru Oya) | -0.28 | 🟢 Normal | -0.253 |  |
| 2026-09-10 00:00:35 | Moraketiya (Walawe Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-10 00:00:12 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-09-09 23:34:08 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-09 23:01:14 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 4.364 | 🔺 Rising |
| 2026-09-10 00:01:26 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-09-10 00:04:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.84 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-09-09 18:02:14 | Thanthirimale (Malwathu Oya) | 0.55 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-09 23:07:35 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-09-09 23:11:10 | Thalgahagoda (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-09-10 00:03:17 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-09-10 00:00:12 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-09-10 00:01:27 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-10 00:03:36 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-10 00:03:56 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-09-10 00:01:47 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-09 18:00:54 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-10 00:02:28 | Magura (Kalu Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-10 00:01:16 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-09 23:06:26 | Hanwella (Kelani Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-09 23:04:07 | Baddegama (Gin Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-09-10 00:04:26 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-09-10 00:04:18 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-10 00:00:35 | Moraketiya (Walawe Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-10 00:02:05 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-10 00:02:41 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-09 23:10:28 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-10 00:03:40 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-10 00:05:17 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-09-09 23:01:52 | Manampitiya (Mahaweli Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-10 00:04:26 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-09-10 00:03:54 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-10 00:05:51 | Kuda Oya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-10 00:06:59 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.009 |  |
| 2026-09-09 23:08:02 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-09-10 00:05:59 | Thanamalwila (Kirindi Oya) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-09-10 00:02:36 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-09-10 00:02:15 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | -0.020 |  |
| 2026-09-10 00:06:25 | Rathnapura (Kalu Ganga) | 1.09 | 🟢 Normal | -0.020 |  |
| 2026-09-09 23:05:01 | Ellagawa (Kalu Ganga) | 4.70 | 🟢 Normal | -0.030 |  |
| 2026-09-10 00:02:09 | Glencourse (Kelani Ganga) | 9.30 | 🟢 Normal | -0.053 |  |
| 2026-09-09 18:06:33 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.121 |  |
| 2026-09-10 00:01:03 | Moragaswewa (Deduru Oya) | -0.28 | 🟢 Normal | -0.253 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)