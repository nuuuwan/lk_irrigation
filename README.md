# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--12_03:51:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **94,991 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-12 03:51:32 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-03-12 03:33:13 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-03-12 03:14:42 | Thawalama (Gin Ganga) | 0.78 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-03-12 03:14:17 | Ellagawa (Kalu Ganga) | 3.76 | 🟢 Normal | 0.000 |  |
| 2026-03-12 03:12:30 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-12 03:12:26 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -35.426 |  |
| 2026-03-12 03:10:48 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | -0.009 |  |
| 2026-03-12 03:09:29 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-03-12 03:08:15 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-12 03:07:43 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-12 03:06:53 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-12 03:06:53 | Thanamalwila (Kirindi Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-12 03:06:14 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-12 03:05:28 | Rathnapura (Kalu Ganga) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-12 03:05:06 | Magura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-12 03:04:47 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-12 03:04:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.50 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-03-12 03:04:21 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-12 03:04:13 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-12 03:03:45 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-03-12 03:03:15 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-12 03:03:11 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-12 03:03:01 | Manampitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-12 03:02:23 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-12 03:02:19 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-03-12 03:02:08 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.298 |  |
| 2026-03-12 03:01:57 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-12 03:01:27 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-12 03:01:14 | Giriulla (Maha Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-12 03:01:09 | Panadugama (Nilwala Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-03-12 03:01:06 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-03-12 03:00:56 | Kithulgala (Kelani Ganga) | 8.39 | 🔴 Major Flood | -35.426 |  |
| 2026-03-12 03:00:55 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-12 03:00:39 | Moraketiya (Walawe Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-12 03:00:16 | Padiyathalawa (Maduru Oya) | 0.53 | 🟢 Normal | 0.011 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-12 03:51:32 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-03-12 03:04:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.50 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-03-12 03:01:06 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-03-12 03:03:45 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-03-12 03:08:15 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-12 03:14:42 | Thawalama (Gin Ganga) | 0.78 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-03-12 03:00:16 | Padiyathalawa (Maduru Oya) | 0.53 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-12 03:03:15 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-12 03:04:13 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-12 03:05:28 | Rathnapura (Kalu Ganga) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-12 03:00:55 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-12 02:01:01 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-12 03:02:23 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-12 03:12:30 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-12 03:01:14 | Giriulla (Maha Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-12 03:33:13 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-03-10 18:02:23⌛ | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-12 03:05:06 | Magura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-12 03:06:14 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-12 03:09:29 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-03-12 03:14:17 | Ellagawa (Kalu Ganga) | 3.76 | 🟢 Normal | 0.000 |  |
| 2026-03-12 03:01:09 | Panadugama (Nilwala Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-03-12 02:03:03 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | 0.000 |  |
| 2026-03-12 03:00:39 | Moraketiya (Walawe Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-12 03:01:57 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-12 03:04:47 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-12 03:03:11 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-12 03:04:21 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-12 03:01:27 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-12 03:07:43 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-12 03:03:01 | Manampitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-10 18:00:47⌛ | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-12 03:06:53 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-12 03:02:19 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-03-12 03:06:53 | Thanamalwila (Kirindi Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-12 03:10:48 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | -0.009 |  |
| 2026-03-10 18:02:53⌛ | Weraganthota (Mahaweli Ganga) | -2.89 | 🟢 Normal | -0.088 |  |
| 2026-03-12 03:02:08 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.298 |  |
| 2026-03-12 03:12:26 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -35.426 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)