# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--08_07:26:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **92,332 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-08 07:26:38 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-08 07:26:25 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-03-08 07:15:23 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | -0.018 |  |
| 2026-03-08 07:13:56 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-08 07:12:47 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.031 |  |
| 2026-03-08 07:09:46 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | -0.163 |  |
| 2026-03-08 07:08:37 | Panadugama (Nilwala Ganga) | 1.87 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-03-08 07:08:12 | Moraketiya (Walawe Ganga) | 0.52 | 🟢 Normal | -0.009 |  |
| 2026-03-08 07:07:28 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-08 07:05:47 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-08 07:05:40 | Glencourse (Kelani Ganga) | 8.54 | 🟢 Normal | -0.010 |  |
| 2026-03-08 07:05:34 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-08 07:05:05 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-08 07:05:05 | Dunamale (Aththanagalu Oya) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-03-08 07:04:44 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-03-08 07:04:37 | Horowpothana (Yan Oya) | 1.18 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-08 07:04:32 | Thawalama (Gin Ganga) | 1.06 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-03-08 07:04:30 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-08 07:04:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.48 | 🟢 Normal | -0.058 |  |
| 2026-03-08 07:04:19 | Hanwella (Kelani Ganga) | 0.26 | 🟢 Normal | -0.048 |  |
| 2026-03-08 07:04:09 | Padiyathalawa (Maduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-08 07:03:53 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-08 07:03:47 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-08 07:03:29 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.100 |  |
| 2026-03-08 07:03:25 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-08 07:03:20 | Deraniyagala (Kelani Ganga) | 0.04 | 🟢 Normal | -0.010 |  |
| 2026-03-08 07:03:17 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-08 07:02:49 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-08 07:02:44 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-08 07:02:42 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-03-08 07:02:40 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-03-08 07:01:57 | Manampitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.020 |  |
| 2026-03-08 07:01:52 | Giriulla (Maha Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-08 07:01:50 | Weraganthota (Mahaweli Ganga) | -2.10 | 🟢 Normal | -0.403 |  |
| 2026-03-08 07:01:49 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | 4.500 | 🔺 Rising |
| 2026-03-08 07:01:28 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.041 |  |
| 2026-03-08 07:01:18 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-03-08 07:01:17 | Rathnapura (Kalu Ganga) | 0.64 | 🟢 Normal | 4.500 | 🔺 Rising |
| 2026-03-08 07:00:46 | Nawalapitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.021 |  |
| 2026-03-08 07:00:41 | Thanthirimale (Malwathu Oya) | 0.77 | 🟢 Normal | -0.002 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-08 07:01:49 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | 4.500 | 🔺 Rising |
| 2026-03-08 07:04:32 | Thawalama (Gin Ganga) | 1.06 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-03-08 07:08:37 | Panadugama (Nilwala Ganga) | 1.87 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-03-08 07:04:37 | Horowpothana (Yan Oya) | 1.18 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-08 07:03:25 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-08 07:05:47 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-08 07:07:28 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-08 07:26:25 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-03-08 07:02:40 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-03-08 07:05:34 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-08 07:02:42 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-03-08 07:02:44 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-08 07:03:53 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-08 07:01:52 | Giriulla (Maha Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-08 07:02:49 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-08 07:04:30 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-08 07:04:44 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-03-08 07:04:09 | Padiyathalawa (Maduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-08 07:13:56 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-08 07:05:05 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-08 07:26:38 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-08 07:03:17 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-08 07:03:47 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-08 07:00:41 | Thanthirimale (Malwathu Oya) | 0.77 | 🟢 Normal | -0.002 |  |
| 2026-03-08 07:08:12 | Moraketiya (Walawe Ganga) | 0.52 | 🟢 Normal | -0.009 |  |
| 2026-03-08 07:05:05 | Dunamale (Aththanagalu Oya) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-03-08 07:03:20 | Deraniyagala (Kelani Ganga) | 0.04 | 🟢 Normal | -0.010 |  |
| 2026-03-08 07:01:18 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-03-08 07:05:40 | Glencourse (Kelani Ganga) | 8.54 | 🟢 Normal | -0.010 |  |
| 2026-03-08 07:15:23 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | -0.018 |  |
| 2026-03-08 07:01:57 | Manampitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.020 |  |
| 2026-03-08 07:00:46 | Nawalapitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.021 |  |
| 2026-03-08 07:12:47 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.031 |  |
| 2026-03-08 07:01:28 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.041 |  |
| 2026-03-08 07:04:19 | Hanwella (Kelani Ganga) | 0.26 | 🟢 Normal | -0.048 |  |
| 2026-03-08 07:04:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.48 | 🟢 Normal | -0.058 |  |
| 2026-03-08 07:03:29 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.100 |  |
| 2026-03-08 07:09:46 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | -0.163 |  |
| 2026-03-08 07:01:50 | Weraganthota (Mahaweli Ganga) | -2.10 | 🟢 Normal | -0.403 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)