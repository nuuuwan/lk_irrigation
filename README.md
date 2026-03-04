# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--05_01:28:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **89,409 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-05 01:28:09 | Panadugama (Nilwala Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-03-05 01:25:17 | Peradeniya (Mahaweli Ganga) | 1.81 | 🟢 Normal | -0.165 |  |
| 2026-03-05 01:24:58 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-03-05 01:15:59 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-05 01:14:19 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | -0.009 |  |
| 2026-03-05 01:09:46 | Pitabeddara (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-05 01:07:46 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-05 01:07:02 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | -0.009 |  |
| 2026-03-05 01:06:49 | Rathnapura (Kalu Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-03-05 01:06:23 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-03-05 01:06:12 | Glencourse (Kelani Ganga) | 8.20 | 🟢 Normal | -0.010 |  |
| 2026-03-05 01:06:03 | Hanwella (Kelani Ganga) | 0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-05 01:05:38 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-05 01:04:27 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -0.020 |  |
| 2026-03-05 01:03:45 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-05 01:03:28 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-03-05 01:03:14 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-03-05 01:02:48 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-05 01:02:44 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-03-05 01:02:35 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-03-05 01:02:23 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-05 01:02:16 | Manampitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-03-05 01:01:30 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-05 01:01:26 | Badalgama (Maha Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-03-05 01:01:11 | Padiyathalawa (Maduru Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-05 01:00:28 | Nawalapitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-03-05 00:52:25 | Pitabeddara (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-05 00:42:37 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-05 00:41:07 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-05 01:24:58 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-03-05 01:03:28 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-03-04 18:01:40 | Weraganthota (Mahaweli Ganga) | -1.87 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-03-05 00:06:19 | Thawalama (Gin Ganga) | 0.96 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-05 00:05:58 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-03-05 01:02:23 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-05 01:06:03 | Hanwella (Kelani Ganga) | 0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-04 18:01:42 | Thanthirimale (Malwathu Oya) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-05 01:02:44 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-03-05 00:03:09 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-05 00:01:38 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-05 01:02:48 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-05 00:41:07 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-04 18:02:59 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-05 00:06:12 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-05 01:09:46 | Pitabeddara (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-05 01:03:14 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-03-05 01:05:38 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-05 01:28:09 | Panadugama (Nilwala Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-03-05 01:01:11 | Padiyathalawa (Maduru Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-05 01:07:46 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-05 00:00:12 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-05 01:01:30 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-05 01:03:45 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-05 00:03:30 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-05 01:01:26 | Badalgama (Maha Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-03-05 01:15:59 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-05 00:32:49 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-05 01:02:35 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-03-04 21:03:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-03-05 01:14:19 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | -0.009 |  |
| 2026-03-05 01:07:02 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | -0.009 |  |
| 2026-03-05 01:06:12 | Glencourse (Kelani Ganga) | 8.20 | 🟢 Normal | -0.010 |  |
| 2026-03-05 01:06:49 | Rathnapura (Kalu Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-03-05 01:06:23 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-03-05 01:00:28 | Nawalapitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-03-05 01:02:16 | Manampitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-03-05 01:04:27 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -0.020 |  |
| 2026-03-05 01:25:17 | Peradeniya (Mahaweli Ganga) | 1.81 | 🟢 Normal | -0.165 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)