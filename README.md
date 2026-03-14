# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--14_22:17:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **97,486 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-14 22:17:10 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-14 22:14:22 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-03-14 22:14:03 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-03-14 22:10:17 | Baddegama (Gin Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-03-14 22:10:03 | Putupaula (Kalu Ganga) | 0.39 | 🟢 Normal | -0.009 |  |
| 2026-03-14 22:09:07 | Moraketiya (Walawe Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-14 22:08:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.68 | 🟢 Normal | -0.023 |  |
| 2026-03-14 22:07:58 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | -0.020 |  |
| 2026-03-14 22:05:59 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | -0.010 |  |
| 2026-03-14 22:05:42 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.063 |  |
| 2026-03-14 22:05:19 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | -0.010 |  |
| 2026-03-14 22:04:26 | Padiyathalawa (Maduru Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-03-14 22:04:15 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-14 22:04:11 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-14 22:03:46 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-03-14 22:03:39 | Hanwella (Kelani Ganga) | 0.57 | 🟢 Normal | -0.021 |  |
| 2026-03-14 22:03:30 | Manampitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.038 |  |
| 2026-03-14 22:03:29 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-03-14 22:03:14 | Peradeniya (Mahaweli Ganga) | 1.92 | 🟢 Normal | 0.227 | 🔺 Rising |
| 2026-03-14 22:03:11 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-03-14 22:03:07 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-03-14 22:02:59 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 22:02:42 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-14 22:02:28 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-14 22:02:21 | Thanamalwila (Kirindi Oya) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 22:02:15 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | 0.000 |  |
| 2026-03-14 22:02:07 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-14 22:01:54 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-14 22:01:17 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-14 22:01:16 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 22:00:52 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-14 22:00:36 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-03-14 22:00:34 | Magura (Kalu Ganga) | 0.74 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-14 22:03:14 | Peradeniya (Mahaweli Ganga) | 1.92 | 🟢 Normal | 0.227 | 🔺 Rising |
| 2026-03-14 22:03:11 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-03-14 21:01:45 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-14 22:14:03 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-03-14 22:03:29 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-03-14 22:01:17 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-14 22:14:22 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-03-14 22:01:16 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 21:02:56 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 22:02:21 | Thanamalwila (Kirindi Oya) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 22:02:59 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 22:00:36 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-03-14 22:00:52 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-14 22:02:07 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-14 22:02:28 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-14 22:17:10 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-14 18:03:23 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-14 22:00:34 | Magura (Kalu Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-14 22:02:15 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | 0.000 |  |
| 2026-03-14 22:01:54 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-14 22:09:07 | Moraketiya (Walawe Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-14 22:04:15 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-14 22:02:42 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-14 22:04:11 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-14 18:01:03 | Thanthirimale (Malwathu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-14 22:10:03 | Putupaula (Kalu Ganga) | 0.39 | 🟢 Normal | -0.009 |  |
| 2026-03-14 22:04:26 | Padiyathalawa (Maduru Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-03-14 22:05:59 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | -0.010 |  |
| 2026-03-14 22:10:17 | Baddegama (Gin Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-03-14 22:03:46 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-03-14 21:02:43 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-03-14 22:05:19 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | -0.010 |  |
| 2026-03-14 22:03:07 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-03-14 22:07:58 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | -0.020 |  |
| 2026-03-14 22:03:39 | Hanwella (Kelani Ganga) | 0.57 | 🟢 Normal | -0.021 |  |
| 2026-03-14 22:08:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.68 | 🟢 Normal | -0.023 |  |
| 2026-03-14 22:03:30 | Manampitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.038 |  |
| 2026-03-14 22:05:42 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.063 |  |
| 2026-03-14 18:01:50 | Weraganthota (Mahaweli Ganga) | -2.87 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)