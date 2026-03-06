# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--06_06:13:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **90,490 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-06 06:13:52 | Panadugama (Nilwala Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-03-06 06:13:34 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-06 06:13:02 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-06 06:11:19 | Manampitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.834 | 🔺 Rising |
| 2026-03-06 06:10:27 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | -0.003 |  |
| 2026-03-06 06:09:24 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-06 06:08:41 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-03-06 06:08:40 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-03-06 06:08:38 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-03-06 06:08:37 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.145 |  |
| 2026-03-06 06:08:21 | Ellagawa (Kalu Ganga) | 3.80 | 🟢 Normal | 0.000 |  |
| 2026-03-06 06:05:45 | Thanamalwila (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-06 06:04:54 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-03-06 06:04:17 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.011 |  |
| 2026-03-06 06:04:13 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-06 06:04:00 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.028 |  |
| 2026-03-06 06:03:42 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-03-06 06:03:41 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-03-06 06:03:37 | Wellawaya (Kirindi Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-03-06 06:03:22 | Padiyathalawa (Maduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-06 06:02:54 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-06 06:02:50 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-06 06:02:47 | Thawalama (Gin Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-06 06:02:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.68 | 🟢 Normal | -0.112 |  |
| 2026-03-06 06:02:38 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-06 06:02:36 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | -0.011 |  |
| 2026-03-06 06:02:36 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-06 06:02:28 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-06 06:02:28 | Norwood (Kelani Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-03-06 06:02:25 | Pitabeddara (Nilwala Ganga) | 0.13 | 🟢 Normal | -0.019 |  |
| 2026-03-06 06:02:21 | Hanwella (Kelani Ganga) | 0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-06 06:02:17 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-03-06 06:02:01 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-06 06:01:27 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.144 |  |
| 2026-03-06 06:01:25 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-06 06:01:16 | Weraganthota (Mahaweli Ganga) | -1.70 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-03-06 06:01:09 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-03-06 05:49:45 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-03-06 05:47:05 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-06 05:31:36 | Pitabeddara (Nilwala Ganga) | 0.14 | 🟢 Normal | -0.019 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-06 06:11:19 | Manampitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.834 | 🔺 Rising |
| 2026-03-06 06:02:17 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-03-06 06:04:54 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-03-06 06:03:42 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-03-06 05:49:45 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-03-06 06:03:41 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-03-06 06:02:21 | Hanwella (Kelani Ganga) | 0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-06 06:02:28 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-06 06:01:16 | Weraganthota (Mahaweli Ganga) | -1.70 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-03-06 06:03:37 | Wellawaya (Kirindi Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-03-06 06:13:02 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-06 06:02:38 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-05 18:01:17 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-06 06:04:13 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-06 06:08:21 | Ellagawa (Kalu Ganga) | 3.80 | 🟢 Normal | 0.000 |  |
| 2026-03-06 06:08:41 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-03-06 06:13:52 | Panadugama (Nilwala Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-03-06 06:03:22 | Padiyathalawa (Maduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-06 06:02:01 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-06 06:09:24 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-06 06:13:34 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-06 06:02:50 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-06 06:02:36 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-06 06:02:54 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-05 18:00:43 | Thanthirimale (Malwathu Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-06 06:02:47 | Thawalama (Gin Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-06 05:01:59 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-06 06:01:25 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-06 06:05:45 | Thanamalwila (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-06 06:10:27 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | -0.003 |  |
| 2026-03-06 06:02:28 | Norwood (Kelani Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-03-06 06:01:09 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-03-06 06:04:17 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.011 |  |
| 2026-03-06 06:02:36 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | -0.011 |  |
| 2026-03-06 06:02:25 | Pitabeddara (Nilwala Ganga) | 0.13 | 🟢 Normal | -0.019 |  |
| 2026-03-06 06:04:00 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.028 |  |
| 2026-03-06 06:02:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.68 | 🟢 Normal | -0.112 |  |
| 2026-03-06 06:01:27 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.144 |  |
| 2026-03-06 06:08:37 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.145 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)