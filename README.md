# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--04_19:33:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **197,288 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **6** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-04 19:33:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.44 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-07-04 19:14:25 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-04 19:13:44 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | -0.016 |  |
| 2026-07-04 19:11:54 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-07-04 19:10:22 | Holombuwa (Kelani Ganga) | 1.68 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-07-04 19:10:03 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-04 19:01:23 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | 0.202 | 🔺 Rising |
| 2026-07-04 19:11:54 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-07-04 19:04:45 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-07-04 19:04:34 | Hanwella (Kelani Ganga) | 2.90 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-07-04 19:10:22 | Holombuwa (Kelani Ganga) | 1.68 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-07-04 19:03:27 | Dunamale (Aththanagalu Oya) | 1.79 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-07-04 19:06:16 | Glencourse (Kelani Ganga) | 11.40 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-04 19:02:26 | Nawalapitiya (Mahaweli Ganga) | 1.95 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-04 19:33:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.44 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-07-04 19:00:37 | Magura (Kalu Ganga) | 1.32 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-04 19:05:27 | Badalgama (Maha Oya) | 2.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 19:06:47 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 19:02:59 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 18:00:43 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | 0.000 |  |
| 2026-07-04 19:00:06 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-04 19:00:10 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-04 19:01:19 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-04 19:10:03 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-04 19:00:49 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-07-04 18:04:06 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-07-04 19:14:25 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-04 19:03:13 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-07-04 19:05:24 | Panadugama (Nilwala Ganga) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-07-04 19:05:29 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-04 19:08:32 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-04 19:01:02 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-07-04 19:05:53 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-04 19:02:39 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-04 18:00:35 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-04 19:02:39 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-04 19:05:05 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-07-04 19:01:49 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-04 19:08:32 | Thanamalwila (Kirindi Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-07-04 19:03:56 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-07-04 19:13:44 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | -0.016 |  |
| 2026-07-04 19:02:30 | Deraniyagala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.030 |  |
| 2026-07-04 19:07:14 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.031 |  |
| 2026-07-04 19:03:55 | Rathnapura (Kalu Ganga) | 2.04 | 🟢 Normal | -0.050 |  |
| 2026-07-04 19:01:54 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.062 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)