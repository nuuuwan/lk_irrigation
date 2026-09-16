# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--17_02:05:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **262,946 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **22** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-17 02:05:51 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-09-17 02:05:43 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-09-17 02:04:54 | Horowpothana (Yan Oya) | 1.87 | 🟢 Normal | -0.005 |  |
| 2026-09-17 02:04:45 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-09-17 02:04:40 | Hanwella (Kelani Ganga) | 1.53 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-09-17 02:04:03 | Ellagawa (Kalu Ganga) | 5.02 | 🟢 Normal | -0.020 |  |
| 2026-09-17 02:03:52 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-17 02:03:41 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-09-17 02:03:18 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-17 02:02:54 | Glencourse (Kelani Ganga) | 9.99 | 🟢 Normal | -0.061 |  |
| 2026-09-17 02:02:49 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-17 02:02:40 | Peradeniya (Mahaweli Ganga) | 2.34 | 🟢 Normal | -0.187 |  |
| 2026-09-17 02:02:39 | Dunamale (Aththanagalu Oya) | 2.36 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-09-17 02:02:36 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.051 |  |
| 2026-09-17 02:02:01 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | -0.010 |  |
| 2026-09-17 02:01:37 | Thawalama (Gin Ganga) | 2.06 | 🟢 Normal | -0.199 |  |
| 2026-09-17 02:01:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-17 02:01:10 | Rathnapura (Kalu Ganga) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-09-17 02:00:20 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-17 01:59:55 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-17 01:34:01 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-09-17 01:28:31 | Thawalama (Gin Ganga) | 2.17 | 🟢 Normal | -0.199 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-17 01:05:47 | Panadugama (Nilwala Ganga) | 2.51 | 🟢 Normal | 328.909 | 🔺 Rising |
| 2026-09-17 02:02:39 | Dunamale (Aththanagalu Oya) | 2.36 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-09-17 02:05:43 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-09-17 02:04:40 | Hanwella (Kelani Ganga) | 1.53 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-09-17 01:05:04 | Baddegama (Gin Ganga) | 3.15 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-09-17 01:04:43 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-17 01:01:06 | Magura (Kalu Ganga) | 3.28 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-17 02:02:49 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-17 01:59:55 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-17 00:03:52 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-17 02:01:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-16 18:02:49 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.000 |  |
| 2026-09-17 02:05:51 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-09-17 01:00:45 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-17 02:03:18 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-17 02:04:45 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-09-16 18:01:06 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-17 01:02:40 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-09-17 01:34:01 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-09-17 02:00:20 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-17 02:03:52 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-17 01:05:29 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-17 02:03:41 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-09-17 01:07:41 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-17 01:02:18 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-09-17 02:04:54 | Horowpothana (Yan Oya) | 1.87 | 🟢 Normal | -0.005 |  |
| 2026-09-17 01:05:56 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-09-17 02:02:01 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | -0.010 |  |
| 2026-09-16 18:00:42 | Thanthirimale (Malwathu Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-09-17 01:14:45 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.014 |  |
| 2026-09-17 02:04:03 | Ellagawa (Kalu Ganga) | 5.02 | 🟢 Normal | -0.020 |  |
| 2026-09-17 02:01:10 | Rathnapura (Kalu Ganga) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-09-17 01:00:36 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.030 |  |
| 2026-09-17 01:02:02 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | -0.030 |  |
| 2026-09-17 02:02:36 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.051 |  |
| 2026-09-17 02:02:54 | Glencourse (Kelani Ganga) | 9.99 | 🟢 Normal | -0.061 |  |
| 2026-09-17 00:08:01 | Putupaula (Kalu Ganga) | 1.05 | 🟢 Normal | -0.131 |  |
| 2026-09-17 02:02:40 | Peradeniya (Mahaweli Ganga) | 2.34 | 🟢 Normal | -0.187 |  |
| 2026-09-17 02:01:37 | Thawalama (Gin Ganga) | 2.06 | 🟢 Normal | -0.199 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)