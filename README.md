# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--10_00:21:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **229,191 measurements** from **39** stations.
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
| 2026-08-10 00:21:38 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-10 00:17:11 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-10 00:15:45 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-08-10 00:15:43 | Hanwella (Kelani Ganga) | 2.18 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-08-10 00:15:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.80 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-08-10 00:13:32 | Magura (Kalu Ganga) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-08-10 00:12:31 | Rathnapura (Kalu Ganga) | 3.27 | 🟢 Normal | -0.030 |  |
| 2026-08-10 00:07:29 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-10 00:07:12 | Glencourse (Kelani Ganga) | 10.75 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-08-10 00:07:02 | Pitabeddara (Nilwala Ganga) | 1.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-10 00:06:32 | Peradeniya (Mahaweli Ganga) | 3.83 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-10 00:06:16 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-10 00:05:14 | Deraniyagala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.086 |  |
| 2026-08-10 00:04:33 | Kithulgala (Kelani Ganga) | 2.53 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-08-10 00:04:31 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | -0.010 |  |
| 2026-08-10 00:04:04 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | -0.019 |  |
| 2026-08-10 00:03:59 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | -0.005 |  |
| 2026-08-10 00:03:56 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-10 00:03:55 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-10 00:03:38 | Panadugama (Nilwala Ganga) | 3.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-10 00:03:36 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | -0.006 |  |
| 2026-08-10 00:03:22 | Ellagawa (Kalu Ganga) | 6.03 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-08-10 00:03:19 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-10 00:03:17 | Baddegama (Gin Ganga) | 2.26 | 🟢 Normal | -0.010 |  |
| 2026-08-10 00:03:06 | Thanamalwila (Kirindi Oya) | 0.45 | 🟢 Normal | -0.011 |  |
| 2026-08-10 00:03:00 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-08-10 00:02:34 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-08-10 00:02:21 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-10 00:02:01 | Nawalapitiya (Mahaweli Ganga) | 2.11 | 🟢 Normal | -0.020 |  |
| 2026-08-10 00:01:57 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-10 00:01:43 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-10 00:01:15 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-10 00:01:09 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-10 00:01:08 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-10 00:00:52 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-10 00:00:29 | Thalgahagoda (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-08-10 00:00:12 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 23:58:05 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-10 00:03:22 | Ellagawa (Kalu Ganga) | 6.03 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-08-10 00:15:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.80 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-08-10 00:04:33 | Kithulgala (Kelani Ganga) | 2.53 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-08-10 00:07:29 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-10 00:02:21 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-10 00:07:12 | Glencourse (Kelani Ganga) | 10.75 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-08-10 00:07:02 | Pitabeddara (Nilwala Ganga) | 1.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-10 00:00:52 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 18:01:36 | Thanthirimale (Malwathu Oya) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-10 00:00:12 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-10 00:03:38 | Panadugama (Nilwala Ganga) | 3.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-10 00:06:32 | Peradeniya (Mahaweli Ganga) | 3.83 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-10 00:15:43 | Hanwella (Kelani Ganga) | 2.18 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-08-10 00:06:16 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-10 00:01:08 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-10 00:01:57 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-10 00:02:34 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-08-10 00:17:11 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-09 18:03:43 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-10 00:01:43 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-10 00:01:09 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-10 00:03:56 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-10 00:03:00 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-08-10 00:21:38 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-10 00:03:19 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-10 00:00:29 | Thalgahagoda (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-08-10 00:01:15 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-10 00:03:59 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | -0.005 |  |
| 2026-08-10 00:03:36 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | -0.006 |  |
| 2026-08-10 00:15:45 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-08-10 00:13:32 | Magura (Kalu Ganga) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-08-10 00:04:31 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | -0.010 |  |
| 2026-08-10 00:03:17 | Baddegama (Gin Ganga) | 2.26 | 🟢 Normal | -0.010 |  |
| 2026-08-10 00:03:06 | Thanamalwila (Kirindi Oya) | 0.45 | 🟢 Normal | -0.011 |  |
| 2026-08-10 00:04:04 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | -0.019 |  |
| 2026-08-10 00:02:01 | Nawalapitiya (Mahaweli Ganga) | 2.11 | 🟢 Normal | -0.020 |  |
| 2026-08-10 00:12:31 | Rathnapura (Kalu Ganga) | 3.27 | 🟢 Normal | -0.030 |  |
| 2026-08-09 18:02:25 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.040 |  |
| 2026-08-10 00:05:14 | Deraniyagala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.086 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)