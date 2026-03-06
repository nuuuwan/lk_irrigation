# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--06_13:12:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **90,766 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-06 13:12:28 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.008 |  |
| 2026-03-06 13:07:37 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-06 13:07:20 | Thalgahagoda (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-06 13:06:45 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-06 13:06:24 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.009 |  |
| 2026-03-06 13:06:17 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.009 |  |
| 2026-03-06 13:06:14 | Weraganthota (Mahaweli Ganga) | -1.75 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-06 13:06:01 | Thawalama (Gin Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-03-06 13:05:43 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-03-06 13:05:38 | Glencourse (Kelani Ganga) | 8.47 | 🟢 Normal | -0.010 |  |
| 2026-03-06 13:04:51 | Badalgama (Maha Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-03-06 13:04:30 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-06 13:04:19 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-06 13:04:03 | Ellagawa (Kalu Ganga) | 3.78 | 🟢 Normal | 0.000 |  |
| 2026-03-06 13:03:59 | Panadugama (Nilwala Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-03-06 13:03:44 | Padiyathalawa (Maduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-06 13:03:42 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-03-06 13:03:40 | Horowpothana (Yan Oya) | 1.17 | 🟢 Normal | -0.021 |  |
| 2026-03-06 13:03:28 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-06 13:03:20 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-03-06 13:03:19 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-06 13:03:11 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.082 |  |
| 2026-03-06 13:03:10 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-06 13:02:59 | Pitabeddara (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-03-06 13:02:50 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-06 13:02:30 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-06 13:02:11 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-06 13:02:09 | Wellawaya (Kirindi Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-06 13:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-03-06 13:01:38 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-06 13:01:33 | Manampitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-06 13:01:33 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-03-06 13:01:25 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-03-06 13:01:21 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-06 13:01:07 | Thanthirimale (Malwathu Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-03-06 13:00:35 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-06 12:23:08 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.047 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-06 13:05:43 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-03-06 12:04:31 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-03-06 13:01:25 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-03-06 13:02:50 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-06 13:01:33 | Manampitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-06 13:07:37 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-06 13:06:14 | Weraganthota (Mahaweli Ganga) | -1.75 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-06 13:01:33 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-03-06 13:02:09 | Wellawaya (Kirindi Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-06 13:03:20 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-03-06 12:03:42 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-06 13:01:21 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-06 13:01:38 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-06 13:02:30 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-06 13:06:45 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-06 12:04:34 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-06 13:02:59 | Pitabeddara (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-03-06 13:03:19 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-06 13:03:10 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-06 13:04:03 | Ellagawa (Kalu Ganga) | 3.78 | 🟢 Normal | 0.000 |  |
| 2026-03-06 13:03:59 | Panadugama (Nilwala Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-03-06 13:03:44 | Padiyathalawa (Maduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-06 13:00:35 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-06 13:02:11 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-06 13:03:28 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-06 13:04:19 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-06 13:04:51 | Badalgama (Maha Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-03-06 13:04:30 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-06 13:01:07 | Thanthirimale (Malwathu Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-03-06 13:06:01 | Thawalama (Gin Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-03-06 13:07:20 | Thalgahagoda (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-06 13:12:28 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.008 |  |
| 2026-03-06 13:06:24 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.009 |  |
| 2026-03-06 13:06:17 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.009 |  |
| 2026-03-06 13:05:38 | Glencourse (Kelani Ganga) | 8.47 | 🟢 Normal | -0.010 |  |
| 2026-03-06 13:03:42 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-03-06 13:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-03-06 13:03:40 | Horowpothana (Yan Oya) | 1.17 | 🟢 Normal | -0.021 |  |
| 2026-03-06 13:03:11 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.082 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)