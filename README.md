# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--07_00:40:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **91,173 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-07 00:40:50 | Putupaula (Kalu Ganga) | 0.20 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-03-07 00:16:59 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.032 |  |
| 2026-03-07 00:13:21 | Peradeniya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.539 | 🔺 Rising |
| 2026-03-07 00:11:35 | Moraketiya (Walawe Ganga) | 0.64 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-07 00:07:43 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-07 00:06:49 | Horowpothana (Yan Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-07 00:06:05 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-07 00:05:38 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-07 00:05:10 | Rathnapura (Kalu Ganga) | 0.55 | 🟢 Normal | -0.020 |  |
| 2026-03-07 00:04:51 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-03-07 00:04:38 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | 0.387 | 🔺 Rising |
| 2026-03-07 00:04:31 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-07 00:04:23 | Padiyathalawa (Maduru Oya) | 0.58 | 🟢 Normal | -0.020 |  |
| 2026-03-07 00:03:50 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-07 00:03:46 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | -0.020 |  |
| 2026-03-07 00:03:43 | Thawalama (Gin Ganga) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-07 00:03:37 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-07 00:03:08 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-07 00:03:05 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | 0.387 | 🔺 Rising |
| 2026-03-07 00:03:05 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-07 00:02:44 | Manampitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-07 00:02:43 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-07 00:02:38 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-07 00:02:38 | Glencourse (Kelani Ganga) | 8.15 | 🟢 Normal | -0.021 |  |
| 2026-03-07 00:02:12 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | -0.010 |  |
| 2026-03-07 00:02:09 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.189 |  |
| 2026-03-07 00:01:52 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | -0.010 |  |
| 2026-03-07 00:01:11 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-07 00:01:02 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-07 00:00:55 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-03-07 00:00:55 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-07 00:00:53 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-07 00:00:19 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-03-06 23:59:59 | Peradeniya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.539 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-07 00:13:21 | Peradeniya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.539 | 🔺 Rising |
| 2026-03-07 00:04:38 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | 0.387 | 🔺 Rising |
| 2026-03-07 00:04:51 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-03-07 00:40:50 | Putupaula (Kalu Ganga) | 0.20 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-03-07 00:04:31 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-07 00:03:43 | Thawalama (Gin Ganga) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-07 00:01:11 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-07 00:11:35 | Moraketiya (Walawe Ganga) | 0.64 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-07 00:05:38 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-07 00:00:19 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-03-07 00:00:55 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-07 00:02:38 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-07 00:03:08 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-07 00:06:49 | Horowpothana (Yan Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-06 18:01:33 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-06 23:13:01 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-06 23:06:10 | Pitabeddara (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-03-07 00:02:43 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-06 20:16:16 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-06 23:10:33 | Panadugama (Nilwala Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-03-07 00:03:37 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-07 00:03:05 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-07 00:06:05 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-07 00:03:50 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-07 00:07:43 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-07 00:02:44 | Manampitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-06 18:03:37 | Thanthirimale (Malwathu Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-03-07 00:01:02 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-06 21:11:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-03-07 00:01:52 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | -0.010 |  |
| 2026-03-07 00:00:55 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-03-07 00:02:12 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | -0.010 |  |
| 2026-03-07 00:04:23 | Padiyathalawa (Maduru Oya) | 0.58 | 🟢 Normal | -0.020 |  |
| 2026-03-07 00:03:46 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | -0.020 |  |
| 2026-03-07 00:05:10 | Rathnapura (Kalu Ganga) | 0.55 | 🟢 Normal | -0.020 |  |
| 2026-03-07 00:02:38 | Glencourse (Kelani Ganga) | 8.15 | 🟢 Normal | -0.021 |  |
| 2026-03-07 00:16:59 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.032 |  |
| 2026-03-06 18:03:18 | Weraganthota (Mahaweli Ganga) | -2.15 | 🟢 Normal | -0.051 |  |
| 2026-03-07 00:02:09 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.189 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)