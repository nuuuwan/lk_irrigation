# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--04_20:38:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **142,941 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **26** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-04 20:38:17 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-05-04 20:19:14 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | -0.019 |  |
| 2026-05-04 20:15:31 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-05-04 20:14:14 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-04 20:14:10 | Rathnapura (Kalu Ganga) | 1.92 | 🟢 Normal | 0.692 | 🔺 Rising |
| 2026-05-04 20:13:37 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-05-04 20:12:48 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.076 |  |
| 2026-05-04 20:11:53 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.117 |  |
| 2026-05-04 20:10:02 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-04 20:09:36 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-05-04 20:09:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | -0.024 |  |
| 2026-05-04 20:07:40 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-05-04 20:07:01 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-04 20:06:39 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | 0.000 |  |
| 2026-05-04 20:06:36 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | -0.032 |  |
| 2026-05-04 20:06:18 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-04 20:05:35 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-05-04 20:05:34 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-05-04 20:05:13 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-05-04 20:05:13 | Peradeniya (Mahaweli Ganga) | 1.07 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-05-04 20:05:06 | Thanamalwila (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-04 20:04:28 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-05-04 20:03:58 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-05-04 20:03:56 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-05-04 20:03:51 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-05-04 20:03:42 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-04 20:14:10 | Rathnapura (Kalu Ganga) | 1.92 | 🟢 Normal | 0.692 | 🔺 Rising |
| 2026-05-04 20:03:51 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-05-04 20:02:16 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-05-04 20:09:36 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-05-04 20:05:13 | Peradeniya (Mahaweli Ganga) | 1.07 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-05-04 20:02:09 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-04 20:02:53 | Manampitiya (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-04 20:02:21 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-04 20:06:18 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-04 20:02:48 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-04 20:03:42 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-04 20:02:22 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-04 18:02:41 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.000 |  |
| 2026-05-04 20:00:47 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-04 20:13:37 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-05-04 20:01:39 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-04 20:04:28 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-05-04 20:38:17 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-05-04 18:01:37 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-04 20:14:14 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-04 20:03:58 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-05-04 20:15:31 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-05-04 20:01:38 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-04 20:06:39 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | 0.000 |  |
| 2026-05-04 20:07:40 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-05-04 18:03:48 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-05-04 20:07:01 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-04 20:02:58 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-04 20:05:06 | Thanamalwila (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-04 20:05:35 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-05-04 20:05:34 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-05-04 20:01:43 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-05-04 20:19:14 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | -0.019 |  |
| 2026-05-04 20:00:48 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.021 |  |
| 2026-05-04 20:09:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | -0.024 |  |
| 2026-05-04 20:06:36 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | -0.032 |  |
| 2026-05-04 20:02:17 | Norwood (Kelani Ganga) | 1.26 | 🟢 Normal | -0.050 |  |
| 2026-05-04 20:12:48 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.076 |  |
| 2026-05-04 20:11:53 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.117 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)