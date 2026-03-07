# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--07_09:17:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **91,504 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-07 09:17:48 | Magura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-07 09:13:05 | Panadugama (Nilwala Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-03-07 09:08:59 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-03-07 09:08:18 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 09:07:58 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-03-07 09:07:33 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 09:06:35 | Rathnapura (Kalu Ganga) | 0.47 | 🟢 Normal | -0.011 |  |
| 2026-03-07 09:06:18 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-03-07 09:06:12 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-07 09:06:02 | Padiyathalawa (Maduru Oya) | 0.59 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-07 09:05:55 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-07 09:05:50 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.060 |  |
| 2026-03-07 09:05:24 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-07 09:05:11 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-03-07 09:05:03 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-07 09:04:17 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.191 | 🔺 Rising |
| 2026-03-07 09:04:03 | Thawalama (Gin Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-03-07 09:03:48 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-07 09:03:36 | Hanwella (Kelani Ganga) | 0.25 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-07 09:03:29 | Horowpothana (Yan Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-07 09:03:18 | Thanamalwila (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-03-07 09:03:10 | Putupaula (Kalu Ganga) | 0.31 | 🟢 Normal | -0.087 |  |
| 2026-03-07 09:03:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.41 | 🟢 Normal | -0.050 |  |
| 2026-03-07 09:02:52 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-07 09:02:19 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | -0.051 |  |
| 2026-03-07 09:02:16 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-03-07 09:02:09 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-07 09:02:07 | Nawalapitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-03-07 09:01:49 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-07 09:01:44 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | -0.011 |  |
| 2026-03-07 09:01:19 | Ellagawa (Kalu Ganga) | 3.89 | 🟢 Normal | -0.010 |  |
| 2026-03-07 09:01:17 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-07 09:01:16 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-07 09:01:15 | Pitabeddara (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-03-07 09:01:11 | Manampitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-03-07 09:01:07 | Thanthirimale (Malwathu Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-03-07 09:00:59 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-07 09:00:45 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-07 09:00:32 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.079 |  |
| 2026-03-07 09:00:23 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-07 09:00:15 | Weraganthota (Mahaweli Ganga) | -1.73 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-07 09:04:17 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.191 | 🔺 Rising |
| 2026-03-07 09:03:36 | Hanwella (Kelani Ganga) | 0.25 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-07 09:02:52 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-07 09:00:45 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-07 09:05:24 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-07 09:06:02 | Padiyathalawa (Maduru Oya) | 0.59 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-07 09:08:59 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-03-07 09:00:15 | Weraganthota (Mahaweli Ganga) | -1.73 | 🟢 Normal | 0.000 |  |
| 2026-03-07 09:01:49 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-07 08:00:37 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 09:02:07 | Nawalapitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-03-07 09:01:16 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-07 09:02:09 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-07 09:03:29 | Horowpothana (Yan Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-07 09:07:33 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 09:17:48 | Magura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-07 09:01:15 | Pitabeddara (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-03-07 09:07:58 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-03-07 09:13:05 | Panadugama (Nilwala Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-03-07 09:00:59 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-07 09:00:23 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-07 09:03:48 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-07 09:06:12 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-07 09:05:03 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-07 09:01:07 | Thanthirimale (Malwathu Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-03-07 09:04:03 | Thawalama (Gin Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-03-07 09:08:18 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 09:05:55 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-07 09:03:18 | Thanamalwila (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-03-07 09:05:11 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-03-07 09:01:19 | Ellagawa (Kalu Ganga) | 3.89 | 🟢 Normal | -0.010 |  |
| 2026-03-07 09:01:11 | Manampitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-03-07 09:06:35 | Rathnapura (Kalu Ganga) | 0.47 | 🟢 Normal | -0.011 |  |
| 2026-03-07 09:01:44 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | -0.011 |  |
| 2026-03-07 09:03:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.41 | 🟢 Normal | -0.050 |  |
| 2026-03-07 09:02:19 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | -0.051 |  |
| 2026-03-07 09:05:50 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.060 |  |
| 2026-03-07 09:00:32 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.079 |  |
| 2026-03-07 09:03:10 | Putupaula (Kalu Ganga) | 0.31 | 🟢 Normal | -0.087 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)