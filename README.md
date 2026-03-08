# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--09_01:17:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **93,007 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-09 01:17:42 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-09 01:11:31 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-03-09 01:09:21 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-03-09 01:08:30 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.009 |  |
| 2026-03-09 01:07:30 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-09 01:06:23 | Rathnapura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-09 01:06:14 | Norwood (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-09 01:05:34 | Hanwella (Kelani Ganga) | 0.25 | 🟢 Normal | -0.030 |  |
| 2026-03-09 01:05:22 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-09 01:05:14 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-03-09 01:04:45 | Ellagawa (Kalu Ganga) | 3.90 | 🟢 Normal | 0.000 |  |
| 2026-03-09 01:03:41 | Giriulla (Maha Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-09 01:02:59 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-03-09 01:02:52 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-09 01:02:50 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-09 01:02:43 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-09 01:02:21 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.062 |  |
| 2026-03-09 01:02:11 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-09 01:02:05 | Moraketiya (Walawe Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-03-09 01:02:05 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-09 01:01:57 | Dunamale (Aththanagalu Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-09 01:01:35 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-09 01:01:30 | Glencourse (Kelani Ganga) | 8.25 | 🟢 Normal | -0.020 |  |
| 2026-03-09 01:01:17 | Manampitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-03-09 01:01:14 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-09 01:01:06 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.031 |  |
| 2026-03-09 01:00:59 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-09 01:00:40 | Manampitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-03-09 01:00:25 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-09 00:05:39 | Putupaula (Kalu Ganga) | 0.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-08 18:00:14 | Weraganthota (Mahaweli Ganga) | -1.76 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-09 01:01:14 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-09 01:06:23 | Rathnapura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-09 01:02:11 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-09 01:05:22 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-09 01:02:43 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-09 01:00:25 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-09 01:01:35 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-09 01:00:59 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-09 00:01:04 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-09 01:02:05 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-09 01:03:41 | Giriulla (Maha Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-08 18:31:40 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-08 23:06:42 | Magura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-08 23:39:28 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-09 01:06:14 | Norwood (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-09 01:02:59 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-03-09 01:04:45 | Ellagawa (Kalu Ganga) | 3.90 | 🟢 Normal | 0.000 |  |
| 2026-03-09 01:11:31 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-03-09 01:05:14 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-03-09 01:02:52 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-09 00:10:17 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-09 01:02:05 | Moraketiya (Walawe Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-03-09 01:02:50 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-09 01:01:57 | Dunamale (Aththanagalu Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-09 00:01:38 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-03-09 00:06:52 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-09 01:01:17 | Manampitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-03-08 18:03:18 | Thanthirimale (Malwathu Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-09 01:17:42 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-09 01:07:30 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-09 00:15:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-03-09 01:08:30 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.009 |  |
| 2026-03-09 01:09:21 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-03-09 01:01:30 | Glencourse (Kelani Ganga) | 8.25 | 🟢 Normal | -0.020 |  |
| 2026-03-09 01:05:34 | Hanwella (Kelani Ganga) | 0.25 | 🟢 Normal | -0.030 |  |
| 2026-03-09 01:01:06 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.031 |  |
| 2026-03-09 01:02:21 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.062 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

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

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)