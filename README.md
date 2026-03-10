# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--10_16:14:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **94,490 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-10 16:14:03 | Dunamale (Aththanagalu Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-10 16:12:27 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-10 16:12:22 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-03-10 16:12:11 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-10 16:10:12 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-03-10 16:10:10 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-03-10 16:08:59 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-10 16:08:30 | Thawalama (Gin Ganga) | 0.95 | 🟢 Normal | -0.028 |  |
| 2026-03-10 16:06:14 | Thanamalwila (Kirindi Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-10 16:04:56 | Giriulla (Maha Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-10 16:04:53 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-03-10 16:04:36 | Rathnapura (Kalu Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-10 16:04:04 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-03-10 16:03:57 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-10 16:03:46 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-10 16:03:35 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-10 16:03:23 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-10 16:03:09 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-03-10 16:02:57 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-10 16:02:47 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-10 16:02:37 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-10 16:02:33 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-10 16:02:30 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-10 16:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.22 | 🟢 Normal | -0.020 |  |
| 2026-03-10 16:02:10 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-10 16:02:09 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-03-10 16:02:08 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-10 16:01:51 | Weraganthota (Mahaweli Ganga) | -2.71 | 🟢 Normal | -0.080 |  |
| 2026-03-10 16:01:47 | Manampitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-03-10 16:01:31 | Padiyathalawa (Maduru Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-10 16:01:15 | Moraketiya (Walawe Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-10 16:01:10 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-03-10 16:01:08 | Ellagawa (Kalu Ganga) | 3.90 | 🟢 Normal | -0.021 |  |
| 2026-03-10 16:01:07 | Moragaswewa (Deduru Oya) | -0.10 | 🟢 Normal | -0.011 |  |
| 2026-03-10 16:00:54 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-03-10 16:00:45 | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-03-10 16:00:18 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-03-10 16:00:10 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.011 |  |
| 2026-03-10 15:27:55 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-10 16:00:54 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-03-10 16:04:53 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-03-10 16:04:04 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-03-10 16:01:47 | Manampitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-03-10 16:12:22 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-03-10 16:03:46 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-10 16:01:15 | Moraketiya (Walawe Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-10 16:08:59 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-10 16:00:18 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-03-10 16:02:30 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-10 16:02:08 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-10 16:03:35 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-10 16:04:56 | Giriulla (Maha Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-10 16:10:12 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-03-10 16:03:57 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-10 16:12:11 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-10 16:02:33 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-10 16:02:37 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-10 16:02:57 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-10 16:02:47 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-10 15:05:20 | Panadugama (Nilwala Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-03-10 16:01:31 | Padiyathalawa (Maduru Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-10 15:27:55 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-10 16:14:03 | Dunamale (Aththanagalu Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-10 16:02:10 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-10 16:03:23 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-10 16:04:36 | Rathnapura (Kalu Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-10 16:01:10 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-03-10 16:12:27 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-10 16:02:09 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-03-10 16:06:14 | Thanamalwila (Kirindi Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-10 16:03:09 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-03-10 16:00:45 | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-03-10 16:00:10 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.011 |  |
| 2026-03-10 16:01:07 | Moragaswewa (Deduru Oya) | -0.10 | 🟢 Normal | -0.011 |  |
| 2026-03-10 16:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.22 | 🟢 Normal | -0.020 |  |
| 2026-03-10 16:01:08 | Ellagawa (Kalu Ganga) | 3.90 | 🟢 Normal | -0.021 |  |
| 2026-03-10 16:08:30 | Thawalama (Gin Ganga) | 0.95 | 🟢 Normal | -0.028 |  |
| 2026-03-10 16:01:51 | Weraganthota (Mahaweli Ganga) | -2.71 | 🟢 Normal | -0.080 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)