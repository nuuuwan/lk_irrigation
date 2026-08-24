# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--25_03:08:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **242,694 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **23** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-25 03:08:25 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-08-25 03:06:09 | Ellagawa (Kalu Ganga) | 4.89 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-25 03:05:55 | Moragaswewa (Deduru Oya) | -0.11 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-25 03:04:57 | Panadugama (Nilwala Ganga) | 2.37 | 🟢 Normal | 0.000 |  |
| 2026-08-25 03:04:52 | Hanwella (Kelani Ganga) | 1.13 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-08-25 03:04:00 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-08-25 03:03:49 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-08-25 03:03:44 | Horowpothana (Yan Oya) | 1.98 | 🟢 Normal | -0.020 |  |
| 2026-08-25 03:03:30 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-25 03:03:27 | Glencourse (Kelani Ganga) | 9.61 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-08-25 03:03:21 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-25 03:03:16 | Rathnapura (Kalu Ganga) | 1.32 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-25 03:02:33 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-08-25 03:02:25 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-25 03:02:18 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-25 03:02:13 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.010 |  |
| 2026-08-25 03:01:56 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-25 03:01:42 | Manampitiya (Mahaweli Ganga) | -0.33 | 🟢 Normal | -0.899 |  |
| 2026-08-25 03:00:56 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-08-25 03:00:51 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-25 03:00:50 | Wellawaya (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-25 03:00:29 | Wellawaya (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-25 02:32:35 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.042 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-25 03:03:27 | Glencourse (Kelani Ganga) | 9.61 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-08-25 03:04:52 | Hanwella (Kelani Ganga) | 1.13 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-08-25 03:00:56 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-08-25 00:19:46 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-08-25 03:03:16 | Rathnapura (Kalu Ganga) | 1.32 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-25 03:02:33 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-08-25 00:18:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-25 03:06:09 | Ellagawa (Kalu Ganga) | 4.89 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-25 03:05:55 | Moragaswewa (Deduru Oya) | -0.11 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-25 01:02:43 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-08-25 03:00:50 | Wellawaya (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-25 02:01:46 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-25 02:01:33 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-08-25 02:11:26 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-25 03:04:00 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-08-24 18:02:21 | Galgamuwa (Mee Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-25 03:00:51 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-25 02:10:21 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-08-25 02:02:45 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-08-25 03:04:57 | Panadugama (Nilwala Ganga) | 2.37 | 🟢 Normal | 0.000 |  |
| 2026-08-25 00:00:24 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-25 00:16:29 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-25 03:03:21 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-25 03:02:18 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-25 03:01:56 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-25 03:03:30 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-25 03:03:49 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-08-25 02:07:43 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-25 02:07:28 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-25 03:02:25 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-24 18:01:27 | Thanthirimale (Malwathu Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-08-25 02:02:17 | Peradeniya (Mahaweli Ganga) | 2.96 | 🟢 Normal | -0.010 |  |
| 2026-08-25 03:02:13 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.010 |  |
| 2026-08-25 03:08:25 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-08-25 02:01:12 | Magura (Kalu Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-08-25 03:03:44 | Horowpothana (Yan Oya) | 1.98 | 🟢 Normal | -0.020 |  |
| 2026-08-25 00:03:25 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | -0.031 |  |
| 2026-08-24 18:01:18 | Weraganthota (Mahaweli Ganga) | -3.03 | 🟢 Normal | -0.119 |  |
| 2026-08-25 03:01:42 | Manampitiya (Mahaweli Ganga) | -0.33 | 🟢 Normal | -0.899 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)