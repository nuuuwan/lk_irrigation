# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--15_02:29:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **97,611 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-15 02:29:42 | Dunamale (Aththanagalu Oya) | 1.21 | 🟢 Normal | -0.029 |  |
| 2026-03-15 02:23:38 | Thanamalwila (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-15 02:23:36 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.191 | 🔺 Rising |
| 2026-03-15 02:20:06 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-15 02:12:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | -1.756 |  |
| 2026-03-15 02:11:52 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-15 02:11:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.62 | 🟢 Normal | -1.756 |  |
| 2026-03-15 02:10:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | -1.756 |  |
| 2026-03-15 02:10:14 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-03-15 02:06:27 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | -0.011 |  |
| 2026-03-15 02:05:50 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | -0.009 |  |
| 2026-03-15 02:05:46 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | -0.019 |  |
| 2026-03-15 02:05:37 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-15 02:04:39 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-03-15 02:02:43 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | -0.020 |  |
| 2026-03-15 02:02:40 | Moragaswewa (Deduru Oya) | 0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-15 02:02:30 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-15 02:02:21 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | -0.005 |  |
| 2026-03-15 02:02:21 | Deraniyagala (Kelani Ganga) | 0.34 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-03-15 02:02:14 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.031 |  |
| 2026-03-15 02:02:00 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-03-15 02:01:53 | Manampitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.030 |  |
| 2026-03-15 02:01:51 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-15 02:01:41 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-15 02:00:51 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-03-15 02:00:20 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-03-15 01:40:58 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-15 01:40:29 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-15 02:23:36 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.191 | 🔺 Rising |
| 2026-03-15 01:03:22 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-03-15 02:00:20 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-03-15 02:02:21 | Deraniyagala (Kelani Ganga) | 0.34 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-03-15 01:01:06 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-15 02:10:14 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-03-15 01:04:49 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-03-15 01:16:37 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-03-15 02:05:37 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-14 23:06:16 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-15 02:01:51 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-15 02:02:40 | Moragaswewa (Deduru Oya) | 0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-15 02:02:00 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-03-15 01:04:42 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-15 02:02:30 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-15 02:01:41 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-14 18:03:23 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-15 00:06:18 | Magura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-15 02:20:06 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-15 01:01:14 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-15 01:21:31 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-15 02:11:52 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-14 18:01:03 | Thanthirimale (Malwathu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-15 01:40:58 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-15 02:23:38 | Thanamalwila (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-15 02:02:21 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | -0.005 |  |
| 2026-03-15 02:05:50 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | -0.009 |  |
| 2026-03-15 01:08:19 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-03-15 02:04:39 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-03-15 02:00:51 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-03-15 02:06:27 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | -0.011 |  |
| 2026-03-15 02:05:46 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | -0.019 |  |
| 2026-03-15 02:02:43 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | -0.020 |  |
| 2026-03-15 02:29:42 | Dunamale (Aththanagalu Oya) | 1.21 | 🟢 Normal | -0.029 |  |
| 2026-03-15 02:01:53 | Manampitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.030 |  |
| 2026-03-15 02:02:14 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.031 |  |
| 2026-03-15 01:00:59 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.080 |  |
| 2026-03-14 18:01:50 | Weraganthota (Mahaweli Ganga) | -2.87 | 🟢 Normal | -0.100 |  |
| 2026-03-15 02:12:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | -1.756 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)