# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--16_20:17:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **99,205 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-16 20:17:41 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.051 |  |
| 2026-03-16 20:17:12 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-16 20:13:07 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 20:12:22 | Glencourse (Kelani Ganga) | 8.42 | 🟢 Normal | -0.027 |  |
| 2026-03-16 20:12:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.34 | 🟢 Normal | -0.047 |  |
| 2026-03-16 20:08:28 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | 0.000 |  |
| 2026-03-16 20:08:24 | Peradeniya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-16 20:07:59 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-03-16 20:07:03 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.043 |  |
| 2026-03-16 20:06:37 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-16 20:06:14 | Rathnapura (Kalu Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-03-16 20:05:09 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-03-16 20:04:11 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-16 20:04:04 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-03-16 20:04:03 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.034 |  |
| 2026-03-16 20:03:58 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-03-16 20:03:57 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | -0.061 |  |
| 2026-03-16 20:03:51 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-16 20:03:39 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-16 20:03:27 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-16 20:03:04 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-16 20:02:52 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-16 20:02:37 | Thanamalwila (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-16 20:02:22 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-16 20:02:18 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | -0.011 |  |
| 2026-03-16 20:02:15 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 20:01:49 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.112 |  |
| 2026-03-16 20:01:42 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-03-16 20:01:37 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-03-16 20:01:23 | Manampitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-03-16 20:01:13 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-16 20:01:06 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | -0.012 |  |
| 2026-03-16 20:00:57 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-16 20:00:45 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-03-16 20:00:43 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-03-16 19:46:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.36 | 🟢 Normal | -0.047 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-16 20:05:09 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-03-16 20:04:11 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-16 20:04:04 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-03-16 20:06:37 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-16 20:08:24 | Peradeniya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-16 20:00:43 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-03-16 20:17:12 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-16 20:00:57 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-16 20:03:51 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-16 20:03:04 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-16 19:18:24 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 18:04:59 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-16 20:13:07 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 20:02:22 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-16 20:08:28 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | 0.000 |  |
| 2026-03-16 20:07:59 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-03-16 20:03:39 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-16 20:01:13 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-16 20:02:52 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-16 20:02:15 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 20:01:23 | Manampitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-03-16 18:01:58 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-16 19:12:08 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-16 20:01:37 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-03-16 20:02:37 | Thanamalwila (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-16 20:03:58 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-03-16 20:01:42 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-03-16 20:06:14 | Rathnapura (Kalu Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-03-16 20:00:45 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-03-16 20:02:18 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | -0.011 |  |
| 2026-03-16 20:01:06 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | -0.012 |  |
| 2026-03-16 20:12:22 | Glencourse (Kelani Ganga) | 8.42 | 🟢 Normal | -0.027 |  |
| 2026-03-16 20:04:03 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.034 |  |
| 2026-03-16 20:07:03 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.043 |  |
| 2026-03-16 20:12:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.34 | 🟢 Normal | -0.047 |  |
| 2026-03-16 20:17:41 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.051 |  |
| 2026-03-16 20:03:57 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | -0.061 |  |
| 2026-03-16 20:01:49 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.112 |  |
| 2026-03-16 18:00:13 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.210 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)