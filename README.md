# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--04_17:13:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **89,125 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-04 17:13:37 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-04 17:11:04 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-04 17:10:17 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-04 17:08:48 | Magura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-04 17:08:17 | Rathnapura (Kalu Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-04 17:07:53 | Badalgama (Maha Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-03-04 17:06:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-03-04 17:06:47 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-04 17:06:44 | Glencourse (Kelani Ganga) | 8.20 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-03-04 17:06:09 | Ellagawa (Kalu Ganga) | 3.82 | 🟢 Normal | -0.010 |  |
| 2026-03-04 17:06:03 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.125 |  |
| 2026-03-04 17:05:51 | Dunamale (Aththanagalu Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-03-04 17:05:04 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-04 17:05:02 | Thawalama (Gin Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-03-04 17:04:53 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-04 17:04:53 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-04 17:04:37 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-04 17:04:26 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-04 17:03:56 | Padiyathalawa (Maduru Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-04 17:03:33 | Moraketiya (Walawe Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-03-04 17:03:23 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-03-04 17:03:20 | Pitabeddara (Nilwala Ganga) | 0.18 | 🟢 Normal | -8.710 |  |
| 2026-03-04 17:03:01 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-04 17:02:57 | Panadugama (Nilwala Ganga) | 1.87 | 🟢 Normal | -0.011 |  |
| 2026-03-04 17:02:51 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-04 17:02:35 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-04 17:02:25 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-04 17:01:57 | Putupaula (Kalu Ganga) | 0.83 | 🟢 Normal | -0.121 |  |
| 2026-03-04 17:01:49 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-04 17:01:36 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-03-04 17:01:28 | Weraganthota (Mahaweli Ganga) | -1.93 | 🟢 Normal | -0.080 |  |
| 2026-03-04 17:01:27 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-04 17:01:10 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-04 17:01:03 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-04 17:00:48 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-04 17:00:45 | Thanthirimale (Malwathu Oya) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-04 17:00:39 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-03-04 17:00:17 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-04 17:06:44 | Glencourse (Kelani Ganga) | 8.20 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-03-04 17:01:27 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-04 17:01:10 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-04 17:03:01 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-04 17:00:45 | Thanthirimale (Malwathu Oya) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-04 17:08:17 | Rathnapura (Kalu Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-04 17:10:17 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-04 17:00:17 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-04 17:01:03 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-04 17:00:48 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-04 17:01:49 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-04 17:05:04 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-04 17:06:47 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-04 17:08:48 | Magura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-04 17:02:51 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-04 17:04:26 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-04 17:03:56 | Padiyathalawa (Maduru Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-04 17:02:25 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-04 17:04:37 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-04 17:07:53 | Badalgama (Maha Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-03-04 17:02:35 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-04 16:11:15 | Manampitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-04 17:04:53 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-04 17:11:04 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-04 17:04:53 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-04 17:13:37 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-04 17:06:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-03-04 17:06:09 | Ellagawa (Kalu Ganga) | 3.82 | 🟢 Normal | -0.010 |  |
| 2026-03-04 17:03:33 | Moraketiya (Walawe Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-03-04 17:05:02 | Thawalama (Gin Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-03-04 17:03:23 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-03-04 17:01:36 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-03-04 17:00:39 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-03-04 17:05:51 | Dunamale (Aththanagalu Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-03-04 17:02:57 | Panadugama (Nilwala Ganga) | 1.87 | 🟢 Normal | -0.011 |  |
| 2026-03-04 17:01:28 | Weraganthota (Mahaweli Ganga) | -1.93 | 🟢 Normal | -0.080 |  |
| 2026-03-04 17:01:57 | Putupaula (Kalu Ganga) | 0.83 | 🟢 Normal | -0.121 |  |
| 2026-03-04 17:06:03 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.125 |  |
| 2026-03-04 17:03:20 | Pitabeddara (Nilwala Ganga) | 0.18 | 🟢 Normal | -8.710 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)