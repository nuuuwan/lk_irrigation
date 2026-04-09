# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--09_14:13:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **120,446 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-09 14:13:17 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-09 14:12:29 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-04-09 14:09:43 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-09 14:08:18 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-09 14:07:41 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-04-09 14:07:34 | Peradeniya (Mahaweli Ganga) | 1.06 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-09 14:07:13 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-09 14:07:06 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-09 14:07:05 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | -0.031 |  |
| 2026-04-09 14:05:29 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-09 14:04:55 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-09 14:03:56 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | 0.000 |  |
| 2026-04-09 14:03:25 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-09 14:03:08 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-09 14:03:08 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | -0.030 |  |
| 2026-04-09 14:03:05 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-09 14:02:57 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.020 |  |
| 2026-04-09 14:02:56 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-04-09 14:02:55 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-09 14:02:47 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | -0.020 |  |
| 2026-04-09 14:02:45 | Rathnapura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-09 14:02:44 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | -0.040 |  |
| 2026-04-09 14:02:39 | Putupaula (Kalu Ganga) | 0.36 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-09 14:02:29 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.011 |  |
| 2026-04-09 14:02:23 | Pitabeddara (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-09 14:02:21 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-04-09 14:02:20 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-04-09 14:02:18 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | -0.011 |  |
| 2026-04-09 14:02:15 | Weraganthota (Mahaweli Ganga) | -2.85 | 🟢 Normal | -0.168 |  |
| 2026-04-09 14:02:10 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-09 14:01:54 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-04-09 14:01:49 | Thanthirimale (Malwathu Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-04-09 14:01:49 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | -0.011 |  |
| 2026-04-09 14:01:39 | Manampitiya (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.030 |  |
| 2026-04-09 14:00:21 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-09 13:36:00 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-09 14:07:41 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-04-09 14:02:39 | Putupaula (Kalu Ganga) | 0.36 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-09 14:01:54 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-04-09 14:04:55 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-09 14:07:34 | Peradeniya (Mahaweli Ganga) | 1.06 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-09 14:03:08 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-09 14:08:18 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-09 14:02:10 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-09 14:02:55 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-09 14:02:23 | Pitabeddara (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-09 14:03:25 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-09 14:03:56 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | 0.000 |  |
| 2026-04-09 13:02:00 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-04-09 14:07:06 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-09 13:02:55 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-09 14:03:05 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-09 14:05:29 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-09 14:02:20 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-04-09 14:12:29 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-04-09 14:09:43 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-09 14:02:45 | Rathnapura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-09 14:13:17 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-09 14:07:13 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-09 13:03:58 | Thanamalwila (Kirindi Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-09 13:03:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-04-09 13:16:12 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | -0.009 |  |
| 2026-04-09 12:05:14 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-04-09 14:01:49 | Thanthirimale (Malwathu Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-04-09 14:02:56 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-04-09 14:01:49 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | -0.011 |  |
| 2026-04-09 14:02:29 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.011 |  |
| 2026-04-09 14:02:18 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | -0.011 |  |
| 2026-04-09 14:02:47 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | -0.020 |  |
| 2026-04-09 14:02:57 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.020 |  |
| 2026-04-09 14:03:08 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | -0.030 |  |
| 2026-04-09 14:01:39 | Manampitiya (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.030 |  |
| 2026-04-09 14:07:05 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | -0.031 |  |
| 2026-04-09 14:02:44 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | -0.040 |  |
| 2026-04-09 14:02:15 | Weraganthota (Mahaweli Ganga) | -2.85 | 🟢 Normal | -0.168 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)