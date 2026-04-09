# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--09_09:12:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **120,254 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-09 09:12:58 | Panadugama (Nilwala Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-04-09 09:12:11 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.009 |  |
| 2026-04-09 09:10:27 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | -0.039 |  |
| 2026-04-09 09:06:52 | Pitabeddara (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-09 09:06:31 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-04-09 09:05:32 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.009 |  |
| 2026-04-09 09:05:22 | Dunamale (Aththanagalu Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-09 09:04:50 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-04-09 09:04:40 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | -0.020 |  |
| 2026-04-09 09:04:36 | Ellagawa (Kalu Ganga) | 3.97 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-09 09:04:27 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.097 |  |
| 2026-04-09 09:04:22 | Thanamalwila (Kirindi Oya) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-04-09 09:04:08 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | -0.011 |  |
| 2026-04-09 09:04:03 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-09 09:04:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.43 | 🟢 Normal | -0.046 |  |
| 2026-04-09 09:03:35 | Weraganthota (Mahaweli Ganga) | -2.16 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-04-09 09:03:34 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-09 09:03:23 | Glencourse (Kelani Ganga) | 8.77 | 🟢 Normal | -0.030 |  |
| 2026-04-09 09:03:21 | Hanwella (Kelani Ganga) | 0.55 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-09 09:03:18 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.094 |  |
| 2026-04-09 09:03:01 | Magura (Kalu Ganga) | 1.01 | 🟢 Normal | -0.034 |  |
| 2026-04-09 09:02:44 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-09 09:02:41 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-04-09 09:02:24 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-09 09:02:23 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-04-09 09:02:22 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-09 09:02:20 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-04-09 09:02:18 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | -0.051 |  |
| 2026-04-09 09:02:15 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.101 |  |
| 2026-04-09 09:01:33 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.080 |  |
| 2026-04-09 09:01:23 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-04-09 09:01:07 | Thanthirimale (Malwathu Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-04-09 09:01:07 | Manampitiya (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.030 |  |
| 2026-04-09 09:00:49 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-09 09:00:25 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-09 09:00:13 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-09 09:00:06 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-09 09:03:35 | Weraganthota (Mahaweli Ganga) | -2.16 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-04-09 09:03:21 | Hanwella (Kelani Ganga) | 0.55 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-09 09:04:36 | Ellagawa (Kalu Ganga) | 3.97 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-09 09:04:03 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-09 08:21:12 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-04-09 09:00:49 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-09 09:00:06 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-09 09:02:22 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-09 09:06:52 | Pitabeddara (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-09 09:12:58 | Panadugama (Nilwala Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-04-09 09:02:24 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-09 09:03:34 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-09 09:05:22 | Dunamale (Aththanagalu Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-09 09:00:25 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-09 09:02:44 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-09 09:06:31 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-04-09 08:19:23 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-09 09:00:13 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-09 09:12:11 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.009 |  |
| 2026-04-09 09:05:32 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.009 |  |
| 2026-04-09 09:04:50 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-04-09 09:02:20 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-04-09 09:04:22 | Thanamalwila (Kirindi Oya) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-04-09 09:01:07 | Thanthirimale (Malwathu Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-04-09 09:02:41 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-04-09 09:02:23 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-04-09 09:01:23 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-04-09 09:04:08 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | -0.011 |  |
| 2026-04-09 09:04:40 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | -0.020 |  |
| 2026-04-09 09:01:07 | Manampitiya (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.030 |  |
| 2026-04-09 09:03:23 | Glencourse (Kelani Ganga) | 8.77 | 🟢 Normal | -0.030 |  |
| 2026-04-09 09:03:01 | Magura (Kalu Ganga) | 1.01 | 🟢 Normal | -0.034 |  |
| 2026-04-09 09:10:27 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | -0.039 |  |
| 2026-04-09 09:04:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.43 | 🟢 Normal | -0.046 |  |
| 2026-04-09 09:02:18 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | -0.051 |  |
| 2026-04-09 09:01:33 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.080 |  |
| 2026-04-09 09:03:18 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.094 |  |
| 2026-04-09 09:04:27 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.097 |  |
| 2026-04-09 09:02:15 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.101 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

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

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)