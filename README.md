# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--14_07:21:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **45,136 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-14 07:21:26 | Panadugama (Nilwala Ganga) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-01-14 07:20:17 | Rathnapura (Kalu Ganga) | 0.86 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-01-14 07:18:30 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-01-14 07:12:44 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-14 07:12:26 | Horowpothana (Yan Oya) | 3.39 | 🟢 Normal | -0.060 |  |
| 2026-01-14 07:10:06 | Glencourse (Kelani Ganga) | 8.88 | 🟢 Normal | -0.027 |  |
| 2026-01-14 07:09:29 | Dunamale (Aththanagalu Oya) | 1.26 | 🟢 Normal | -0.035 |  |
| 2026-01-14 07:09:16 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-14 07:08:47 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | -0.009 |  |
| 2026-01-14 07:08:30 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-14 07:07:32 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | -0.028 |  |
| 2026-01-14 07:07:05 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-01-14 07:06:59 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-14 07:06:59 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-14 07:06:43 | Padiyathalawa (Maduru Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-01-14 07:06:11 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-14 07:05:40 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-01-14 07:05:35 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-01-14 07:05:12 | Thanthirimale (Malwathu Oya) | 2.43 | 🟢 Normal | -0.012 |  |
| 2026-01-14 07:05:12 | Badalgama (Maha Oya) | 2.11 | 🟢 Normal | -0.010 |  |
| 2026-01-14 07:05:09 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-14 07:05:04 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.032 |  |
| 2026-01-14 07:04:19 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.140 |  |
| 2026-01-14 07:04:18 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-01-14 07:04:11 | Hanwella (Kelani Ganga) | 1.01 | 🟢 Normal | -0.020 |  |
| 2026-01-14 07:03:52 | Manampitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | -0.040 |  |
| 2026-01-14 07:03:49 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.137 |  |
| 2026-01-14 07:03:40 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-14 07:02:56 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-14 07:02:36 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-14 07:02:25 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.020 |  |
| 2026-01-14 07:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.81 | 🟢 Normal | -0.072 |  |
| 2026-01-14 07:02:16 | Magura (Kalu Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-01-14 07:02:15 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.005 |  |
| 2026-01-14 07:01:55 | Yaka Wewa (Ma Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-01-14 07:01:49 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-01-14 07:01:32 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-14 07:01:22 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-14 07:00:23 | Weraganthota (Mahaweli Ganga) | -1.46 | 🟢 Normal | -0.010 |  |
| 2026-01-14 06:33:05 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-14 07:02:56 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-14 07:02:36 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-14 07:06:11 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-14 07:20:17 | Rathnapura (Kalu Ganga) | 0.86 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-01-14 07:03:40 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-14 07:01:22 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-14 07:12:44 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-14 07:07:05 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-01-14 07:08:30 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-14 07:21:26 | Panadugama (Nilwala Ganga) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-01-14 07:05:09 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-14 07:06:59 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-14 07:06:59 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-14 07:18:30 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-01-14 07:05:35 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-01-14 07:09:16 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-14 07:02:15 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.005 |  |
| 2026-01-14 07:08:47 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | -0.009 |  |
| 2026-01-14 07:05:40 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-01-14 07:02:16 | Magura (Kalu Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-01-14 07:04:18 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-01-14 07:00:23 | Weraganthota (Mahaweli Ganga) | -1.46 | 🟢 Normal | -0.010 |  |
| 2026-01-14 07:05:12 | Badalgama (Maha Oya) | 2.11 | 🟢 Normal | -0.010 |  |
| 2026-01-14 07:06:43 | Padiyathalawa (Maduru Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-01-14 07:01:55 | Yaka Wewa (Ma Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-01-14 07:01:49 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-01-14 07:05:12 | Thanthirimale (Malwathu Oya) | 2.43 | 🟢 Normal | -0.012 |  |
| 2026-01-14 07:04:11 | Hanwella (Kelani Ganga) | 1.01 | 🟢 Normal | -0.020 |  |
| 2026-01-14 07:02:25 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.020 |  |
| 2026-01-14 07:10:06 | Glencourse (Kelani Ganga) | 8.88 | 🟢 Normal | -0.027 |  |
| 2026-01-14 07:07:32 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | -0.028 |  |
| 2026-01-14 07:05:04 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.032 |  |
| 2026-01-14 07:09:29 | Dunamale (Aththanagalu Oya) | 1.26 | 🟢 Normal | -0.035 |  |
| 2026-01-14 07:03:52 | Manampitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | -0.040 |  |
| 2026-01-14 07:12:26 | Horowpothana (Yan Oya) | 3.39 | 🟢 Normal | -0.060 |  |
| 2026-01-14 07:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.81 | 🟢 Normal | -0.072 |  |
| 2026-01-14 06:10:15 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.136 |  |
| 2026-01-14 07:03:49 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.137 |  |
| 2026-01-14 07:04:19 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.140 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)