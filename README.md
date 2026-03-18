# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--18_08:06:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **100,514 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-18 08:06:02 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-18 08:06:00 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-18 08:05:57 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-18 08:05:52 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-18 08:05:22 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-18 08:05:16 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-18 08:05:05 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-18 08:05:01 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-18 08:05:01 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.011 |  |
| 2026-03-18 08:04:43 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-03-18 08:04:36 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | -0.031 |  |
| 2026-03-18 08:04:33 | Rathnapura (Kalu Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-18 08:04:26 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-18 08:04:20 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.153 |  |
| 2026-03-18 08:04:09 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-18 08:04:00 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-03-18 08:04:00 | Putupaula (Kalu Ganga) | 0.22 | 🟢 Normal | -0.160 |  |
| 2026-03-18 08:03:57 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-18 08:03:52 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-18 08:03:48 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-18 08:03:44 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-18 08:03:10 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-18 08:02:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | -0.050 |  |
| 2026-03-18 08:02:41 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-18 08:02:01 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-18 08:01:37 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | -0.011 |  |
| 2026-03-18 08:01:28 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-18 08:01:05 | Ellagawa (Kalu Ganga) | 3.78 | 🟢 Normal | 0.000 |  |
| 2026-03-18 08:00:59 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | -0.011 |  |
| 2026-03-18 08:00:47 | Manampitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.040 |  |
| 2026-03-18 08:00:36 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-18 08:00:31 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-18 07:19:42 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-03-18 07:12:46 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-18 07:12:38 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-18 07:11:32 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.014 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-18 08:04:00 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-03-18 08:05:05 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-18 08:06:00 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-18 07:11:32 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-03-18 08:05:22 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-18 08:06:02 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-18 08:02:41 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-18 08:05:16 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-18 08:05:52 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-18 08:03:48 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-18 08:01:28 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-18 08:00:36 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-18 08:05:57 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-18 07:05:41 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-18 08:03:52 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-18 08:01:05 | Ellagawa (Kalu Ganga) | 3.78 | 🟢 Normal | 0.000 |  |
| 2026-03-18 07:19:42 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-03-18 08:04:26 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-18 08:03:44 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-18 08:03:10 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-18 08:04:09 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-18 08:03:57 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-18 08:04:43 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-03-18 07:03:13 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-18 08:04:33 | Rathnapura (Kalu Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-18 08:02:01 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-18 08:05:01 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-18 08:00:31 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-18 07:02:08 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.005 |  |
| 2026-03-18 08:01:37 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | -0.011 |  |
| 2026-03-18 08:00:59 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | -0.011 |  |
| 2026-03-18 08:05:01 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.011 |  |
| 2026-03-18 08:04:36 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | -0.031 |  |
| 2026-03-18 08:00:47 | Manampitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.040 |  |
| 2026-03-18 08:02:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | -0.050 |  |
| 2026-03-18 07:01:09 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.053 |  |
| 2026-03-18 07:05:28 | Weraganthota (Mahaweli Ganga) | -2.33 | 🟢 Normal | -0.139 |  |
| 2026-03-18 08:04:20 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.153 |  |
| 2026-03-18 08:04:00 | Putupaula (Kalu Ganga) | 0.22 | 🟢 Normal | -0.160 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)