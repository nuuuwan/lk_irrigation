# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--24_09:19:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **105,930 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-24 09:19:42 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-03-24 09:15:37 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-24 09:11:41 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-24 09:11:13 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-03-24 09:09:32 | Ellagawa (Kalu Ganga) | 3.96 | 🟢 Normal | -0.010 |  |
| 2026-03-24 09:09:02 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.047 |  |
| 2026-03-24 09:07:21 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.046 |  |
| 2026-03-24 09:06:45 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-24 09:06:15 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | -0.010 |  |
| 2026-03-24 09:06:05 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-24 09:05:22 | Horowpothana (Yan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-03-24 09:05:10 | Thanamalwila (Kirindi Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-24 09:05:08 | Pitabeddara (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-03-24 09:04:59 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-03-24 09:04:52 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.020 |  |
| 2026-03-24 09:04:40 | Hanwella (Kelani Ganga) | 0.24 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-24 09:04:33 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.379 | 🔺 Rising |
| 2026-03-24 09:04:26 | Moragaswewa (Deduru Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-24 09:04:18 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | -0.029 |  |
| 2026-03-24 09:04:10 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-24 09:04:08 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.029 |  |
| 2026-03-24 09:03:58 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.123 |  |
| 2026-03-24 09:03:51 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-24 09:03:43 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-24 09:03:37 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-24 09:03:32 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-03-24 09:03:27 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-24 09:03:24 | Putupaula (Kalu Ganga) | 0.33 | 🟢 Normal | -0.150 |  |
| 2026-03-24 09:03:08 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-24 09:03:04 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-24 09:03:00 | Baddegama (Gin Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-03-24 09:02:49 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.040 |  |
| 2026-03-24 09:02:48 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-24 09:04:33 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.379 | 🔺 Rising |
| 2026-03-24 09:02:12 | Weraganthota (Mahaweli Ganga) | -2.31 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-03-24 09:04:40 | Hanwella (Kelani Ganga) | 0.24 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-24 09:04:10 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-24 09:03:51 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-24 09:06:05 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-24 09:00:43 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-24 09:03:04 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-24 09:04:26 | Moragaswewa (Deduru Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-24 09:00:29 | Nawalapitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-24 09:01:15 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-24 09:02:48 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-24 09:05:22 | Horowpothana (Yan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-03-24 09:03:08 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-24 09:01:39 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-24 09:19:42 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-03-24 09:11:41 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-24 09:03:27 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-24 09:06:45 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-24 09:01:13 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-03-24 09:15:37 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-24 09:01:18 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-24 09:05:10 | Thanamalwila (Kirindi Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-24 09:04:59 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-03-24 09:09:32 | Ellagawa (Kalu Ganga) | 3.96 | 🟢 Normal | -0.010 |  |
| 2026-03-24 09:05:08 | Pitabeddara (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-03-24 09:03:32 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-03-24 09:01:23 | Magura (Kalu Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-03-24 09:03:00 | Baddegama (Gin Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-03-24 09:06:15 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | -0.010 |  |
| 2026-03-24 09:04:52 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.020 |  |
| 2026-03-24 09:04:18 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | -0.029 |  |
| 2026-03-24 09:04:08 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.029 |  |
| 2026-03-24 09:02:49 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.040 |  |
| 2026-03-24 09:07:21 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.046 |  |
| 2026-03-24 09:09:02 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.047 |  |
| 2026-03-24 09:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.59 | 🟢 Normal | -0.070 |  |
| 2026-03-24 09:03:58 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.123 |  |
| 2026-03-24 09:03:24 | Putupaula (Kalu Ganga) | 0.33 | 🟢 Normal | -0.150 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)