# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--22_05:15:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **52,259 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-22 05:15:32 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-01-22 05:12:22 | Ellagawa (Kalu Ganga) | 3.85 | 🟢 Normal | 0.000 |  |
| 2026-01-22 05:11:38 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | -0.030 |  |
| 2026-01-22 05:09:45 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-01-22 05:09:06 | Ellagawa (Kalu Ganga) | 3.85 | 🟢 Normal | 0.000 |  |
| 2026-01-22 05:08:41 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-22 05:08:29 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-22 05:07:47 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-01-22 05:06:53 | Thanamalwila (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-22 05:06:23 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-22 05:06:17 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-22 05:05:35 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-22 05:05:34 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-01-22 05:05:27 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-22 05:04:47 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-22 05:04:43 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-22 05:04:18 | Dunamale (Aththanagalu Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-22 05:04:06 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-01-22 05:03:57 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-01-22 05:03:29 | Manampitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.019 |  |
| 2026-01-22 05:03:20 | Putupaula (Kalu Ganga) | 0.89 | 🟢 Normal | 0.189 | 🔺 Rising |
| 2026-01-22 05:03:18 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-01-22 05:03:10 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-22 05:02:53 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-22 05:02:46 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-22 05:02:39 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-22 05:02:11 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.185 |  |
| 2026-01-22 05:01:50 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-22 05:01:10 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-22 05:01:10 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-01-22 05:00:51 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-22 05:00:10 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | -0.182 |  |
| 2026-01-22 04:51:42 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.030 |  |
| 2026-01-22 04:42:35 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-01-22 04:40:11 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-22 04:34:44 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.189 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-22 05:03:20 | Putupaula (Kalu Ganga) | 0.89 | 🟢 Normal | 0.189 | 🔺 Rising |
| 2026-01-22 05:04:06 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-01-22 04:01:12 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-22 05:06:23 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-22 03:00:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-22 05:05:27 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-21 18:03:38 | Weraganthota (Mahaweli Ganga) | -1.86 | 🟢 Normal | 0.000 |  |
| 2026-01-22 04:00:55 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-22 05:03:10 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-22 05:06:17 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-22 05:02:46 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-22 05:01:50 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-22 05:02:53 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-22 05:03:18 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-01-21 18:02:52 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-22 05:08:29 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-22 05:01:10 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-22 05:02:39 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-22 05:12:22 | Ellagawa (Kalu Ganga) | 3.85 | 🟢 Normal | 0.000 |  |
| 2026-01-22 05:05:34 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-01-22 05:07:47 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-01-22 03:04:09 | Padiyathalawa (Maduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-22 05:05:35 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-22 05:00:51 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-22 05:08:41 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-22 05:04:18 | Dunamale (Aththanagalu Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-22 00:00:09 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-22 05:09:45 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-01-22 05:04:43 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-21 18:01:41 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-01-22 05:15:32 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-01-22 05:04:47 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-22 05:06:53 | Thanamalwila (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-22 05:03:57 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-01-22 05:01:10 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-01-22 05:03:29 | Manampitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.019 |  |
| 2026-01-22 05:11:38 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | -0.030 |  |
| 2026-01-22 05:00:10 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | -0.182 |  |
| 2026-01-22 05:02:11 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.185 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)