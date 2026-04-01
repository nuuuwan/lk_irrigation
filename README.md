# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--01_08:09:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **113,054 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-01 08:09:31 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-01 08:09:14 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.126 |  |
| 2026-04-01 08:07:45 | Magura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-01 08:07:21 | Panadugama (Nilwala Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-04-01 08:06:10 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-01 08:05:56 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-01 08:05:55 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-04-01 08:05:45 | Badalgama (Maha Oya) | 1.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-01 08:05:42 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-01 08:05:40 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-01 08:05:13 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-01 08:05:12 | Rathnapura (Kalu Ganga) | 0.45 | 🟢 Normal | -0.020 |  |
| 2026-04-01 08:04:57 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-01 08:04:45 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-01 08:04:42 | Hanwella (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-01 08:04:06 | Thanthirimale (Malwathu Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-04-01 08:03:35 | Pitabeddara (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-01 08:03:13 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-01 08:03:08 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-01 08:03:03 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-01 08:02:59 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.052 |  |
| 2026-04-01 08:02:57 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | -0.041 |  |
| 2026-04-01 08:02:55 | Thawalama (Gin Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-04-01 08:02:51 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.096 |  |
| 2026-04-01 08:02:47 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-01 08:02:41 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.359 |  |
| 2026-04-01 08:02:40 | Weraganthota (Mahaweli Ganga) | -1.84 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-04-01 08:02:17 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-01 08:02:12 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-01 08:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.38 | 🟢 Normal | -0.041 |  |
| 2026-04-01 08:02:01 | Ellagawa (Kalu Ganga) | 3.75 | 🟢 Normal | 0.000 |  |
| 2026-04-01 08:01:46 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.101 |  |
| 2026-04-01 08:01:45 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-01 08:01:39 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-01 08:01:24 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-01 08:01:22 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-04-01 08:00:21 | Nawalapitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-01 08:02:40 | Weraganthota (Mahaweli Ganga) | -1.84 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-04-01 08:05:56 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-01 08:05:45 | Badalgama (Maha Oya) | 1.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-01 08:03:03 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-01 08:02:47 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-01 08:01:24 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-01 08:09:31 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-01 08:01:39 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-01 08:01:45 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-01 08:05:13 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-01 08:07:45 | Magura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-01 08:03:35 | Pitabeddara (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-01 08:04:42 | Hanwella (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-01 08:02:01 | Ellagawa (Kalu Ganga) | 3.75 | 🟢 Normal | 0.000 |  |
| 2026-04-01 08:07:21 | Panadugama (Nilwala Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-04-01 08:03:08 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-01 08:02:17 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-01 08:02:12 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-01 08:03:13 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-01 08:06:10 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-01 08:05:42 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-01 08:04:06 | Thanthirimale (Malwathu Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-04-01 08:02:55 | Thawalama (Gin Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-04-01 08:05:40 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-01 08:04:45 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-01 08:01:22 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-04-01 08:04:57 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-01 08:05:55 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-04-01 08:00:21 | Nawalapitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-04-01 07:02:10 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-04-01 08:05:12 | Rathnapura (Kalu Ganga) | 0.45 | 🟢 Normal | -0.020 |  |
| 2026-04-01 08:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.38 | 🟢 Normal | -0.041 |  |
| 2026-04-01 08:02:57 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | -0.041 |  |
| 2026-04-01 08:02:59 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.052 |  |
| 2026-04-01 06:06:28 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.057 |  |
| 2026-04-01 08:02:51 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.096 |  |
| 2026-04-01 08:01:46 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.101 |  |
| 2026-04-01 08:09:14 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.126 |  |
| 2026-04-01 08:02:41 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.359 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)