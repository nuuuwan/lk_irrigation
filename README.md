# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--01_21:06:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **86,582 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-01 21:06:38 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | -0.052 |  |
| 2026-03-01 21:05:49 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-01 21:05:44 | Thawalama (Gin Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-03-01 21:05:12 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | -0.010 |  |
| 2026-03-01 21:04:52 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-03-01 21:04:49 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-03-01 21:04:36 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-01 21:04:31 | Hanwella (Kelani Ganga) | 0.25 | 🟢 Normal | -0.020 |  |
| 2026-03-01 21:04:29 | Padiyathalawa (Maduru Oya) | 0.69 | 🟢 Normal | -0.009 |  |
| 2026-03-01 21:04:20 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-03-01 21:04:04 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-01 21:03:47 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-01 21:03:41 | Dunamale (Aththanagalu Oya) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-01 21:03:23 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-01 21:02:51 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | -0.020 |  |
| 2026-03-01 21:02:49 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-01 21:02:36 | Glencourse (Kelani Ganga) | 8.20 | 🟢 Normal | 0.000 |  |
| 2026-03-01 21:02:26 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-01 21:02:18 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-01 21:02:12 | Manampitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-03-01 21:02:09 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-01 21:01:43 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-01 21:01:37 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-01 21:01:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | -0.011 |  |
| 2026-03-01 21:01:19 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-01 21:01:15 | Rathnapura (Kalu Ganga) | 0.49 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-03-01 21:00:38 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-03-01 21:00:28 | Wellawaya (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-01 20:59:25 | Horowpothana (Yan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-03-01 20:27:31 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-01 20:19:11 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-01 20:17:53 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-01 20:16:08 | Horowpothana (Yan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-03-01 20:10:44 | Rathnapura (Kalu Ganga) | 0.46 | 🟢 Normal | 0.036 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-01 21:04:20 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-03-01 18:01:43 | Weraganthota (Mahaweli Ganga) | -2.45 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-03-01 21:01:15 | Rathnapura (Kalu Ganga) | 0.49 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-03-01 20:03:41 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-01 21:03:41 | Dunamale (Aththanagalu Oya) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-01 21:00:28 | Wellawaya (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-01 20:04:18 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-03-01 21:02:26 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-01 21:01:19 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-01 21:02:18 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-01 21:02:09 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-01 20:59:25 | Horowpothana (Yan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-03-01 18:01:07 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-01 20:05:30 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-03-01 21:03:23 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-01 21:04:49 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-03-01 20:17:53 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-01 20:03:25 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-03-01 21:02:36 | Glencourse (Kelani Ganga) | 8.20 | 🟢 Normal | 0.000 |  |
| 2026-03-01 21:01:37 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-01 21:00:38 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-03-01 21:04:04 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-01 21:04:36 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-01 21:02:12 | Manampitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-03-01 21:05:49 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-01 21:01:43 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-01 21:02:49 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-01 21:04:29 | Padiyathalawa (Maduru Oya) | 0.69 | 🟢 Normal | -0.009 |  |
| 2026-03-01 21:05:44 | Thawalama (Gin Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-03-01 21:05:12 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | -0.010 |  |
| 2026-03-01 18:00:31 | Thanthirimale (Malwathu Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-03-01 21:01:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | -0.011 |  |
| 2026-03-01 21:04:31 | Hanwella (Kelani Ganga) | 0.25 | 🟢 Normal | -0.020 |  |
| 2026-03-01 21:02:51 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | -0.020 |  |
| 2026-03-01 21:04:52 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-03-01 21:06:38 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | -0.052 |  |
| 2026-03-01 20:02:59 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.060 |  |
| 2026-03-01 20:00:21 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.073 |  |
| 2026-03-01 20:06:27 | Putupaula (Kalu Ganga) | 0.24 | 🟢 Normal | -0.107 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)