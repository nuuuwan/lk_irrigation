# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--08_02:14:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **281,866 measurements** from **39** stations.
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
| 2026-10-08 02:14:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.18 | 🟢 Normal | -0.052 |  |
| 2026-10-08 02:11:10 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-08 02:09:38 | Thalgahagoda (Nilwala Ganga) | 1.03 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-08 02:08:11 | Panadugama (Nilwala Ganga) | 4.58 | 🟢 Normal | -0.033 |  |
| 2026-10-08 02:07:51 | Magura (Kalu Ganga) | 3.34 | 🟢 Normal | -648.000 |  |
| 2026-10-08 02:07:50 | Magura (Kalu Ganga) | 3.52 | 🟢 Normal | -648.000 |  |
| 2026-10-08 02:06:52 | Holombuwa (Kelani Ganga) | 1.82 | 🟢 Normal | -1.002 |  |
| 2026-10-08 02:06:48 | Ellagawa (Kalu Ganga) | 5.53 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-08 02:05:03 | Pitabeddara (Nilwala Ganga) | 1.12 | 🟢 Normal | -0.031 |  |
| 2026-10-08 02:04:56 | Glencourse (Kelani Ganga) | 11.73 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-08 02:04:40 | Baddegama (Gin Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-10-08 02:04:25 | Hanwella (Kelani Ganga) | 3.22 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2026-10-08 02:04:24 | Giriulla (Maha Oya) | 2.20 | 🟢 Normal | 0.705 | 🔺 Rising |
| 2026-10-08 02:04:05 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-08 02:04:03 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-10-08 02:03:52 | Badalgama (Maha Oya) | 2.73 | 🟢 Normal | -0.010 |  |
| 2026-10-08 02:03:24 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.643 | 🔺 Rising |
| 2026-10-08 02:02:44 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-10-08 02:02:42 | Kithulgala (Kelani Ganga) | 2.14 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-10-08 02:02:39 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-08 02:02:27 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-08 02:02:21 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-08 02:01:50 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-10-08 02:01:35 | Siyambalanduwa (Heda Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-08 02:01:34 | Peradeniya (Mahaweli Ganga) | 3.38 | 🟢 Normal | -0.081 |  |
| 2026-10-08 02:01:20 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-08 02:01:00 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-08 02:00:57 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-08 02:00:42 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-08 01:58:32 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-08 02:04:24 | Giriulla (Maha Oya) | 2.20 | 🟢 Normal | 0.705 | 🔺 Rising |
| 2026-10-08 02:03:24 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.643 | 🔺 Rising |
| 2026-10-08 02:04:25 | Hanwella (Kelani Ganga) | 3.22 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2026-10-08 02:02:42 | Kithulgala (Kelani Ganga) | 2.14 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-10-08 01:03:36 | Dunamale (Aththanagalu Oya) | 2.70 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-10-08 01:14:11 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-10-08 02:09:38 | Thalgahagoda (Nilwala Ganga) | 1.03 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-08 02:02:27 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-08 02:04:56 | Glencourse (Kelani Ganga) | 11.73 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-08 02:04:05 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-07 18:03:09 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-08 02:01:00 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-08 02:06:48 | Ellagawa (Kalu Ganga) | 5.53 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-08 02:00:57 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-07 23:05:45 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-08 02:02:44 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-10-07 18:03:15 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-10-08 02:02:39 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-08 02:04:40 | Baddegama (Gin Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-10-08 01:01:07 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-08 02:01:35 | Siyambalanduwa (Heda Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-08 02:00:42 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-08 02:02:21 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-08 02:11:10 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-07 18:09:53 | Thanthirimale (Malwathu Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-10-08 02:01:20 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-08 02:01:50 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-10-08 00:03:50 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.005 |  |
| 2026-10-08 02:03:52 | Badalgama (Maha Oya) | 2.73 | 🟢 Normal | -0.010 |  |
| 2026-10-08 02:04:03 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-10-08 01:02:21 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | -0.011 |  |
| 2026-10-08 00:11:02 | Rathnapura (Kalu Ganga) | 1.99 | 🟢 Normal | -0.018 |  |
| 2026-10-08 02:05:03 | Pitabeddara (Nilwala Ganga) | 1.12 | 🟢 Normal | -0.031 |  |
| 2026-10-08 02:08:11 | Panadugama (Nilwala Ganga) | 4.58 | 🟢 Normal | -0.033 |  |
| 2026-10-08 01:03:23 | Thawalama (Gin Ganga) | 2.40 | 🟢 Normal | -0.050 |  |
| 2026-10-08 02:14:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.18 | 🟢 Normal | -0.052 |  |
| 2026-10-08 02:01:34 | Peradeniya (Mahaweli Ganga) | 3.38 | 🟢 Normal | -0.081 |  |
| 2026-10-08 02:06:52 | Holombuwa (Kelani Ganga) | 1.82 | 🟢 Normal | -1.002 |  |
| 2026-10-08 02:07:51 | Magura (Kalu Ganga) | 3.34 | 🟢 Normal | -648.000 |  |

## River Water Level Charts by Station

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)