# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--04_23:11:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **89,342 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-04 23:11:33 | Badalgama (Maha Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-03-04 23:11:10 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.080 |  |
| 2026-03-04 23:09:12 | Thawalama (Gin Ganga) | 0.94 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-04 23:07:40 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-04 23:06:39 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-04 23:05:54 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | -0.013 |  |
| 2026-03-04 23:05:19 | Hanwella (Kelani Ganga) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-03-04 23:05:12 | Rathnapura (Kalu Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-03-04 23:05:05 | Glencourse (Kelani Ganga) | 8.22 | 🟢 Normal | -0.031 |  |
| 2026-03-04 23:04:49 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-04 23:04:08 | Padiyathalawa (Maduru Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-04 23:04:08 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-04 23:03:57 | Badalgama (Maha Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-03-04 23:03:49 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-04 23:03:44 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-03-04 23:03:19 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-04 23:03:18 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-04 23:02:54 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-04 23:02:46 | Panadugama (Nilwala Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-03-04 23:02:34 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.150 |  |
| 2026-03-04 23:02:27 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-04 23:01:54 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-03-04 23:01:37 | Peradeniya (Mahaweli Ganga) | 1.91 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-03-04 23:01:26 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-04 23:01:13 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-04 23:01:04 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-03-04 23:00:42 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-04 23:00:23 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-04 23:00:19 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-04 22:27:00 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.007 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-04 23:01:37 | Peradeniya (Mahaweli Ganga) | 1.91 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-03-04 18:01:40 | Weraganthota (Mahaweli Ganga) | -1.87 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-03-04 23:03:49 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-04 23:09:12 | Thawalama (Gin Ganga) | 0.94 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-04 23:03:19 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-04 23:00:23 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-04 23:03:44 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-03-04 22:02:02 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-04 18:01:42 | Thanthirimale (Malwathu Oya) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-04 22:27:00 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-03-04 23:03:18 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-04 23:00:19 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-04 23:01:26 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-04 23:07:40 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-04 23:00:42 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-04 18:02:59 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-04 22:06:31 | Pitabeddara (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-04 21:02:34 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-04 23:01:04 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-03-04 23:01:54 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-03-04 23:02:46 | Panadugama (Nilwala Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-03-04 23:04:08 | Padiyathalawa (Maduru Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-04 22:05:02 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-04 23:02:54 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-04 23:04:08 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-04 23:04:49 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-04 23:11:33 | Badalgama (Maha Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-03-04 23:01:13 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-04 23:06:39 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-04 22:04:23 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-04 23:02:27 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-04 21:03:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-03-04 23:05:19 | Hanwella (Kelani Ganga) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-03-04 23:05:12 | Rathnapura (Kalu Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-03-04 23:05:54 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | -0.013 |  |
| 2026-03-04 23:05:05 | Glencourse (Kelani Ganga) | 8.22 | 🟢 Normal | -0.031 |  |
| 2026-03-04 23:11:10 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.080 |  |
| 2026-03-04 22:08:23 | Putupaula (Kalu Ganga) | 0.20 | 🟢 Normal | -0.101 |  |
| 2026-03-04 23:02:34 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.150 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)