# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--30_02:12:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **111,051 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-30 02:12:47 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-30 02:08:47 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-03-30 02:07:52 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.018 |  |
| 2026-03-30 02:05:59 | Kithulgala (Kelani Ganga) | 1.29 | 🟢 Normal | -0.272 |  |
| 2026-03-30 02:05:33 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-30 02:05:26 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | -0.005 |  |
| 2026-03-30 02:05:26 | Hanwella (Kelani Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-03-30 02:05:04 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-30 02:04:25 | Nawalapitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | -1.333 |  |
| 2026-03-30 02:04:08 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-30 02:04:04 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-30 02:04:02 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-30 02:03:58 | Nawalapitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | -1.333 |  |
| 2026-03-30 02:03:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.20 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-30 02:03:13 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-30 02:02:42 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-03-30 02:02:26 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-30 02:02:20 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-30 02:02:20 | Rathnapura (Kalu Ganga) | 0.48 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-03-30 02:02:08 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-30 02:02:07 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-30 02:02:01 | Glencourse (Kelani Ganga) | 8.26 | 🟢 Normal | 0.000 |  |
| 2026-03-30 02:01:45 | Badalgama (Maha Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-03-30 02:01:16 | Ellagawa (Kalu Ganga) | 3.66 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-03-30 02:01:15 | Ellagawa (Kalu Ganga) | 3.65 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-03-30 02:01:14 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-30 02:00:53 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-03-30 02:00:42 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-30 02:00:31 | Peradeniya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.279 |  |
| 2026-03-30 01:41:54 | Horowpothana (Yan Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-30 01:32:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.18 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-30 01:32:06 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-30 01:22:21 | Magura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-03-30 01:19:55 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | 0.037 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-30 02:01:16 | Ellagawa (Kalu Ganga) | 3.66 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-03-30 02:03:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.20 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-30 02:08:47 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-03-30 02:02:20 | Rathnapura (Kalu Ganga) | 0.48 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-03-30 01:22:21 | Magura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-03-30 02:01:14 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-30 01:01:16 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-30 02:04:04 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-30 02:02:26 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-30 02:02:20 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-30 02:02:07 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-30 01:41:54 | Horowpothana (Yan Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-29 18:03:02 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-30 01:01:06 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-30 02:05:33 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-29 23:23:26 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-03-30 00:02:38 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-30 01:10:12 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-30 02:02:01 | Glencourse (Kelani Ganga) | 8.26 | 🟢 Normal | 0.000 |  |
| 2026-03-30 02:00:53 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-03-30 02:02:08 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-30 01:02:37 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-30 01:00:47 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-30 02:02:42 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-03-30 02:01:45 | Badalgama (Maha Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-03-30 02:03:13 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-29 18:01:38 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-03-30 02:12:47 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-30 02:00:42 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-30 02:04:08 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-30 02:05:26 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | -0.005 |  |
| 2026-03-30 02:05:26 | Hanwella (Kelani Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-03-30 02:07:52 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.018 |  |
| 2026-03-30 01:03:56 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | -0.020 |  |
| 2026-03-30 00:06:21 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.031 |  |
| 2026-03-29 18:00:53 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | -0.229 |  |
| 2026-03-30 02:05:59 | Kithulgala (Kelani Ganga) | 1.29 | 🟢 Normal | -0.272 |  |
| 2026-03-30 02:00:31 | Peradeniya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.279 |  |
| 2026-03-30 02:04:25 | Nawalapitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | -1.333 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)