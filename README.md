# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--04_21:22:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **89,279 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-04 21:22:22 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.040 |  |
| 2026-03-04 21:15:09 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-04 21:15:06 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-04 21:12:48 | Magura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-04 21:12:43 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-03-04 21:10:02 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.054 |  |
| 2026-03-04 21:08:48 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.091 |  |
| 2026-03-04 21:08:29 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-04 21:08:11 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-04 21:06:49 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-04 21:05:53 | Panadugama (Nilwala Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-03-04 21:05:30 | Pitabeddara (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-04 21:05:28 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-04 21:05:24 | Glencourse (Kelani Ganga) | 8.27 | 🟢 Normal | -0.029 |  |
| 2026-03-04 21:05:18 | Padiyathalawa (Maduru Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-04 21:05:14 | Peradeniya (Mahaweli Ganga) | 1.51 | 🟢 Normal | 0.403 | 🔺 Rising |
| 2026-03-04 21:05:06 | Panadugama (Nilwala Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-03-04 21:05:01 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-03-04 21:04:23 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-04 21:04:16 | Rathnapura (Kalu Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-04 21:04:08 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-04 21:03:58 | Thawalama (Gin Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-03-04 21:03:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-03-04 21:03:26 | Badalgama (Maha Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-03-04 21:03:19 | Ellagawa (Kalu Ganga) | 3.83 | 🟢 Normal | 0.000 |  |
| 2026-03-04 21:03:17 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-04 21:03:07 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-04 21:02:57 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-04 21:02:37 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-04 21:02:34 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-04 21:02:30 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-04 21:02:18 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-03-04 21:02:15 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-04 21:02:12 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-04 21:02:07 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-04 21:02:06 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-04 21:01:52 | Hanwella (Kelani Ganga) | 0.20 | 🟢 Normal | -0.031 |  |
| 2026-03-04 21:01:30 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-04 21:00:49 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-04 21:00:12 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-04 21:05:14 | Peradeniya (Mahaweli Ganga) | 1.51 | 🟢 Normal | 0.403 | 🔺 Rising |
| 2026-03-04 18:01:40 | Weraganthota (Mahaweli Ganga) | -1.87 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-03-04 21:03:07 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-04 21:02:06 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-04 21:02:15 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-04 21:03:17 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-04 18:01:42 | Thanthirimale (Malwathu Oya) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-04 21:02:18 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-03-04 21:12:43 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-03-04 21:15:09 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-04 21:00:49 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-04 21:01:30 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-04 21:02:37 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-04 21:08:29 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-04 18:02:59 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-04 21:12:48 | Magura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-04 21:05:30 | Pitabeddara (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-04 21:02:34 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-04 21:03:19 | Ellagawa (Kalu Ganga) | 3.83 | 🟢 Normal | 0.000 |  |
| 2026-03-04 21:05:53 | Panadugama (Nilwala Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-03-04 21:05:18 | Padiyathalawa (Maduru Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-04 21:15:06 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-04 21:02:07 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-04 21:04:08 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-04 21:02:12 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-04 21:03:26 | Badalgama (Maha Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-03-04 21:06:49 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-04 21:04:16 | Rathnapura (Kalu Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-04 21:03:58 | Thawalama (Gin Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-03-04 21:04:23 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-04 21:05:28 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-04 21:08:11 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-04 21:03:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-03-04 21:05:01 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-03-04 21:05:24 | Glencourse (Kelani Ganga) | 8.27 | 🟢 Normal | -0.029 |  |
| 2026-03-04 21:01:52 | Hanwella (Kelani Ganga) | 0.20 | 🟢 Normal | -0.031 |  |
| 2026-03-04 21:22:22 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.040 |  |
| 2026-03-04 21:10:02 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.054 |  |
| 2026-03-04 21:08:48 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.091 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)