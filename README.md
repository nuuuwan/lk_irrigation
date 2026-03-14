# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--14_19:33:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **97,378 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-14 19:33:47 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-14 19:20:24 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-03-14 19:17:34 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-03-14 19:13:50 | Magura (Kalu Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-14 19:11:59 | Panadugama (Nilwala Ganga) | 2.14 | 🟢 Normal | -0.018 |  |
| 2026-03-14 19:11:00 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.044 |  |
| 2026-03-14 19:09:29 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-14 19:07:56 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-03-14 19:07:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | -0.029 |  |
| 2026-03-14 19:06:47 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-14 19:06:37 | Kithulgala (Kelani Ganga) | 2.02 | 🟢 Normal | 0.653 | 🔺 Rising |
| 2026-03-14 19:06:03 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | -0.148 |  |
| 2026-03-14 19:05:58 | Hanwella (Kelani Ganga) | 0.65 | 🟢 Normal | -0.038 |  |
| 2026-03-14 19:05:09 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 19:04:44 | Dunamale (Aththanagalu Oya) | 1.15 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2026-03-14 19:04:35 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-03-14 19:04:31 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-14 19:04:25 | Putupaula (Kalu Ganga) | 0.46 | 🟢 Normal | -0.038 |  |
| 2026-03-14 19:04:05 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | -0.010 |  |
| 2026-03-14 19:03:32 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.060 |  |
| 2026-03-14 19:03:31 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-14 19:03:09 | Rathnapura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.037 |  |
| 2026-03-14 19:03:08 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 19:02:53 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-14 19:02:26 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-14 19:02:21 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-14 19:02:10 | Glencourse (Kelani Ganga) | 8.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 19:01:55 | Manampitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | -0.020 |  |
| 2026-03-14 19:01:44 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-14 19:01:30 | Padiyathalawa (Maduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-14 19:01:26 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-03-14 19:01:16 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-14 19:01:12 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-14 19:01:11 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-14 19:00:18 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-14 19:00:17 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-14 19:06:37 | Kithulgala (Kelani Ganga) | 2.02 | 🟢 Normal | 0.653 | 🔺 Rising |
| 2026-03-14 19:04:44 | Dunamale (Aththanagalu Oya) | 1.15 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2026-03-14 19:07:56 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-03-14 19:20:24 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-03-14 19:02:21 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-14 19:03:08 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 19:02:10 | Glencourse (Kelani Ganga) | 8.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 19:05:09 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 19:00:17 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-03-14 19:00:18 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-14 19:02:53 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-14 19:01:44 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-14 19:04:35 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-03-14 19:33:47 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-14 18:03:23 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-14 19:13:50 | Magura (Kalu Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-14 19:09:29 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-14 19:17:34 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-03-14 19:01:30 | Padiyathalawa (Maduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-14 19:01:16 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-14 19:06:47 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-14 19:04:31 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-14 19:01:12 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-14 19:03:31 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-14 18:01:03 | Thanthirimale (Malwathu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-14 19:02:26 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-14 19:01:11 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-14 19:04:05 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | -0.010 |  |
| 2026-03-14 19:11:59 | Panadugama (Nilwala Ganga) | 2.14 | 🟢 Normal | -0.018 |  |
| 2026-03-14 19:01:55 | Manampitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | -0.020 |  |
| 2026-03-14 19:01:26 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-03-14 19:07:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | -0.029 |  |
| 2026-03-14 19:03:09 | Rathnapura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.037 |  |
| 2026-03-14 19:05:58 | Hanwella (Kelani Ganga) | 0.65 | 🟢 Normal | -0.038 |  |
| 2026-03-14 19:04:25 | Putupaula (Kalu Ganga) | 0.46 | 🟢 Normal | -0.038 |  |
| 2026-03-14 19:11:00 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.044 |  |
| 2026-03-14 19:03:32 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.060 |  |
| 2026-03-14 18:01:50 | Weraganthota (Mahaweli Ganga) | -2.87 | 🟢 Normal | -0.100 |  |
| 2026-03-14 19:06:03 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | -0.148 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)