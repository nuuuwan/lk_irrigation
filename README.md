# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--07_05:07:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **281,067 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-07 05:07:12 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-07 05:06:42 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.032 |  |
| 2026-10-07 05:06:15 | Rathnapura (Kalu Ganga) | 1.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-07 05:06:04 | Badalgama (Maha Oya) | 2.72 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-10-07 05:04:57 | Magura (Kalu Ganga) | 2.61 | 🟢 Normal | -0.550 |  |
| 2026-10-07 05:04:41 | Dunamale (Aththanagalu Oya) | 2.22 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-07 05:04:32 | Moraketiya (Walawe Ganga) | 1.28 | 🟢 Normal | 0.301 | 🔺 Rising |
| 2026-10-07 05:04:12 | Holombuwa (Kelani Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-10-07 05:04:10 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-10-07 05:03:58 | Baddegama (Gin Ganga) | 2.29 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-10-07 05:03:48 | Glencourse (Kelani Ganga) | 10.95 | 🟢 Normal | -0.028 |  |
| 2026-10-07 05:03:43 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-10-07 05:03:39 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | -0.030 |  |
| 2026-10-07 05:03:07 | Giriulla (Maha Oya) | 1.86 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-07 05:03:00 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | -0.020 |  |
| 2026-10-07 05:02:45 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-10-07 05:02:35 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-07 05:02:32 | Ellagawa (Kalu Ganga) | 5.59 | 🟢 Normal | 0.000 |  |
| 2026-10-07 05:01:57 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-07 05:01:52 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-10-07 05:01:46 | Peradeniya (Mahaweli Ganga) | 2.86 | 🟢 Normal | -0.042 |  |
| 2026-10-07 05:01:29 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-07 05:01:28 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | -0.050 |  |
| 2026-10-07 05:01:18 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-10-07 05:01:10 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-07 05:01:08 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-07 05:00:29 | Thalgahagoda (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-10-07 04:46:24 | Magura (Kalu Ganga) | 2.78 | 🟢 Normal | -0.550 |  |
| 2026-10-07 04:39:42 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-07 04:38:49 | Magura (Kalu Ganga) | 2.58 | 🟢 Normal | -0.550 |  |
| 2026-10-07 04:31:06 | Pitabeddara (Nilwala Ganga) | 3.20 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-10-07 04:27:52 | Thalgahagoda (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-10-07 04:21:44 | Panadugama (Nilwala Ganga) | 5.63 | 🟡 Alert | 0.087 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-07 04:21:44 | Panadugama (Nilwala Ganga) | 5.63 | 🟡 Alert | 0.087 | 🔺 Rising |
| 2026-10-07 05:04:32 | Moraketiya (Walawe Ganga) | 1.28 | 🟢 Normal | 0.301 | 🔺 Rising |
| 2026-10-07 05:00:29 | Thalgahagoda (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-10-07 04:31:06 | Pitabeddara (Nilwala Ganga) | 3.20 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-10-07 05:03:58 | Baddegama (Gin Ganga) | 2.29 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-10-07 05:03:07 | Giriulla (Maha Oya) | 1.86 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-07 05:06:04 | Badalgama (Maha Oya) | 2.72 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-10-07 05:04:41 | Dunamale (Aththanagalu Oya) | 2.22 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-07 05:01:08 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-07 05:07:12 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-07 05:06:15 | Rathnapura (Kalu Ganga) | 1.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-07 05:01:10 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-07 05:02:45 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-10-07 05:01:57 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-07 05:01:52 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-10-06 18:03:52 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-07 05:02:32 | Ellagawa (Kalu Ganga) | 5.59 | 🟢 Normal | 0.000 |  |
| 2026-10-07 05:01:29 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-07 05:02:35 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-06 18:01:28 | Thanthirimale (Malwathu Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-10-07 04:15:48 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.009 |  |
| 2026-10-07 05:04:12 | Holombuwa (Kelani Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-10-07 05:03:43 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-10-07 04:04:48 | Hanwella (Kelani Ganga) | 2.76 | 🟢 Normal | -0.010 |  |
| 2026-10-07 05:01:18 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-10-07 04:01:47 | Siyambalanduwa (Heda Oya) | 0.25 | 🟢 Normal | -0.011 |  |
| 2026-10-06 18:01:43 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.011 |  |
| 2026-10-07 05:03:00 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | -0.020 |  |
| 2026-10-07 05:04:10 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-10-07 05:03:48 | Glencourse (Kelani Ganga) | 10.95 | 🟢 Normal | -0.028 |  |
| 2026-10-07 05:03:39 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | -0.030 |  |
| 2026-10-07 05:06:42 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.032 |  |
| 2026-10-07 05:01:46 | Peradeniya (Mahaweli Ganga) | 2.86 | 🟢 Normal | -0.042 |  |
| 2026-10-07 03:00:58 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.042 |  |
| 2026-10-07 05:01:28 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | -0.050 |  |
| 2026-10-07 04:01:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.15 | 🟢 Normal | -0.051 |  |
| 2026-10-07 04:19:28 | Deraniyagala (Kelani Ganga) | 0.86 | 🟢 Normal | -0.062 |  |
| 2026-10-07 05:04:57 | Magura (Kalu Ganga) | 2.61 | 🟢 Normal | -0.550 |  |
| 2026-10-07 03:56:43 | Thawalama (Gin Ganga) | 2.46 | 🟢 Normal | -3.214 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)