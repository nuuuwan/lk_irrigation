# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--05_04:08:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **89,508 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-05 04:08:26 | Glencourse (Kelani Ganga) | 8.22 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-03-05 04:07:48 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-05 04:05:53 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-05 04:05:50 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-03-05 04:05:10 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-03-05 04:05:03 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-05 04:05:01 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-05 04:04:33 | Rathnapura (Kalu Ganga) | 0.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-05 04:03:59 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-03-05 04:03:25 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-05 04:03:21 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-05 04:03:20 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.203 |  |
| 2026-03-05 04:03:01 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-05 04:02:29 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | -0.079 |  |
| 2026-03-05 04:02:12 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-05 04:02:00 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-05 04:01:28 | Hanwella (Kelani Ganga) | 0.22 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-03-05 04:01:26 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-05 04:01:14 | Ellagawa (Kalu Ganga) | 3.83 | 🟢 Normal | -0.010 |  |
| 2026-03-05 04:01:10 | Padiyathalawa (Maduru Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-05 04:01:09 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-03-05 04:00:39 | Moraketiya (Walawe Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-05 04:00:27 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-05 04:00:13 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-03-05 03:35:01 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-05 03:34:16 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-03-05 03:28:52 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-05 03:28:24 | Manampitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-03-05 03:25:08 | Thawalama (Gin Ganga) | 1.01 | 🟢 Normal | 4.909 | 🔺 Rising |
| 2026-03-05 03:24:46 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | 4.909 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-05 03:25:08 | Thawalama (Gin Ganga) | 1.01 | 🟢 Normal | 4.909 | 🔺 Rising |
| 2026-03-05 04:00:13 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-03-05 03:34:16 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-03-04 18:01:40 | Weraganthota (Mahaweli Ganga) | -1.87 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-03-05 04:08:26 | Glencourse (Kelani Ganga) | 8.22 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-03-05 03:14:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.68 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-03-05 03:28:24 | Manampitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-03-05 03:01:50 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-05 04:05:03 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-05 04:01:28 | Hanwella (Kelani Ganga) | 0.22 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-03-05 04:00:27 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-05 04:04:33 | Rathnapura (Kalu Ganga) | 0.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-04 18:01:42 | Thanthirimale (Malwathu Oya) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-05 04:07:48 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-05 04:01:26 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-05 04:02:12 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-05 02:21:13 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-04 18:02:59 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-05 04:03:21 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-05 04:05:53 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-05 04:01:10 | Padiyathalawa (Maduru Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-05 04:00:39 | Moraketiya (Walawe Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-05 03:01:51 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-05 04:03:01 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-05 04:03:25 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-05 03:09:46 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-05 03:28:52 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-05 04:05:01 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-05 04:02:00 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-05 03:01:47 | Panadugama (Nilwala Ganga) | 1.86 | 🟢 Normal | -0.006 |  |
| 2026-03-05 04:03:59 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-03-05 04:05:10 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-03-05 04:01:14 | Ellagawa (Kalu Ganga) | 3.83 | 🟢 Normal | -0.010 |  |
| 2026-03-05 03:03:47 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-03-05 04:01:09 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-03-05 04:05:50 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-03-05 04:02:29 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | -0.079 |  |
| 2026-03-05 04:03:20 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.203 |  |
| 2026-03-05 03:12:51 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -1.424 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)