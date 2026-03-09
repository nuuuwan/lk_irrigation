# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--09_05:26:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **93,149 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-09 05:26:10 | Dunamale (Aththanagalu Oya) | 0.34 | 🟢 Normal | -0.007 |  |
| 2026-03-09 05:24:03 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.030 |  |
| 2026-03-09 05:12:31 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-09 05:11:48 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-09 05:10:45 | Moraketiya (Walawe Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-09 05:09:43 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.018 |  |
| 2026-03-09 05:09:22 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-03-09 05:06:54 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-09 05:06:15 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-09 05:06:15 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.009 |  |
| 2026-03-09 05:05:53 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-09 05:05:53 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-03-09 05:05:45 | Hanwella (Kelani Ganga) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-03-09 05:05:23 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-03-09 05:05:03 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-09 05:04:38 | Rathnapura (Kalu Ganga) | 0.97 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-03-09 05:04:31 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-03-09 05:04:27 | Badalgama (Maha Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-03-09 05:03:48 | Giriulla (Maha Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-09 05:03:23 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | -0.020 |  |
| 2026-03-09 05:03:21 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-09 05:02:43 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-03-09 05:02:36 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-09 05:01:41 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-09 05:01:31 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-09 05:01:25 | Manampitiya (Mahaweli Ganga) | 0.89 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-09 05:01:23 | Ellagawa (Kalu Ganga) | 3.85 | 🟢 Normal | -0.014 |  |
| 2026-03-09 05:01:01 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-09 05:00:54 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-03-09 05:00:51 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.121 |  |
| 2026-03-09 05:00:41 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-03-09 05:00:22 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-09 04:46:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.42 | 🟢 Normal | 0.014 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-09 05:04:38 | Rathnapura (Kalu Ganga) | 0.97 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-03-09 05:00:41 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-03-08 18:00:14 | Weraganthota (Mahaweli Ganga) | -1.76 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-09 05:01:25 | Manampitiya (Mahaweli Ganga) | 0.89 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-09 04:46:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.42 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-03-09 05:03:21 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-09 05:00:22 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-09 05:04:31 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-03-09 05:09:22 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-03-09 05:01:31 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-09 05:01:01 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-09 05:01:41 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-09 05:03:48 | Giriulla (Maha Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-09 05:02:43 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-03-08 18:31:40 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-09 04:22:45 | Magura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-09 05:06:15 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-09 05:05:53 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-03-09 05:05:23 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-03-09 03:01:59 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-09 05:06:54 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-09 05:10:45 | Moraketiya (Walawe Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-09 04:01:54 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-09 05:05:53 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-09 05:04:27 | Badalgama (Maha Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-03-09 05:11:48 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-08 18:03:18 | Thanthirimale (Malwathu Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-09 05:02:36 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-09 05:05:03 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-09 05:12:31 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-09 05:26:10 | Dunamale (Aththanagalu Oya) | 0.34 | 🟢 Normal | -0.007 |  |
| 2026-03-09 05:06:15 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.009 |  |
| 2026-03-09 05:00:54 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-03-09 05:05:45 | Hanwella (Kelani Ganga) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-03-09 05:01:23 | Ellagawa (Kalu Ganga) | 3.85 | 🟢 Normal | -0.014 |  |
| 2026-03-09 05:09:43 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.018 |  |
| 2026-03-09 05:03:23 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | -0.020 |  |
| 2026-03-09 05:24:03 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.030 |  |
| 2026-03-09 05:00:51 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.121 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)