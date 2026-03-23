# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--24_00:32:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **105,603 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-24 00:32:33 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-03-24 00:16:52 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-24 00:11:56 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-24 00:09:49 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.028 |  |
| 2026-03-24 00:06:51 | Putupaula (Kalu Ganga) | 0.23 | 🟢 Normal | -0.068 |  |
| 2026-03-24 00:06:09 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-03-24 00:05:56 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.019 |  |
| 2026-03-24 00:05:15 | Glencourse (Kelani Ganga) | 8.21 | 🟢 Normal | 0.000 |  |
| 2026-03-24 00:04:40 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -1.500 |  |
| 2026-03-24 00:04:24 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-03-24 00:04:16 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -1.500 |  |
| 2026-03-24 00:04:14 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -1.500 |  |
| 2026-03-24 00:03:42 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | -0.012 |  |
| 2026-03-24 00:03:41 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-24 00:03:24 | Pitabeddara (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-24 00:03:22 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-24 00:03:20 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-24 00:03:06 | Baddegama (Gin Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-03-24 00:03:05 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-03-24 00:03:04 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-24 00:02:55 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | -0.031 |  |
| 2026-03-24 00:02:50 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-24 00:02:45 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-03-24 00:02:41 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-24 00:02:25 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | -0.020 |  |
| 2026-03-24 00:02:22 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-24 00:02:19 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-24 00:02:17 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-03-24 00:02:06 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.305 | 🔺 Rising |
| 2026-03-24 00:02:00 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-03-24 00:01:13 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-24 00:00:38 | Manampitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-24 00:00:20 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-24 00:02:06 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.305 | 🔺 Rising |
| 2026-03-23 22:01:56 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-24 00:02:17 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-03-24 00:11:56 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-24 00:02:19 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-23 23:01:02 | Moragaswewa (Deduru Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-24 00:00:20 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-23 21:01:22 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-24 00:16:52 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-23 18:00:14 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-23 23:05:47 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-24 00:03:24 | Pitabeddara (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-24 00:02:50 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-24 00:03:06 | Baddegama (Gin Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-03-23 22:11:18 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-03-24 00:03:04 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-24 00:02:41 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-24 00:05:15 | Glencourse (Kelani Ganga) | 8.21 | 🟢 Normal | 0.000 |  |
| 2026-03-24 00:01:13 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-24 00:02:22 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-24 00:04:24 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-03-24 00:00:38 | Manampitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-24 00:03:20 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-24 00:32:33 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-03-24 00:03:41 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-24 00:03:05 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-03-24 00:02:00 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-03-24 00:06:09 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-03-23 18:02:17 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-03-24 00:02:45 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-03-24 00:03:42 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | -0.012 |  |
| 2026-03-24 00:05:56 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.019 |  |
| 2026-03-24 00:02:25 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | -0.020 |  |
| 2026-03-23 21:05:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.48 | 🟢 Normal | -0.021 |  |
| 2026-03-24 00:09:49 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.028 |  |
| 2026-03-24 00:02:55 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | -0.031 |  |
| 2026-03-24 00:06:51 | Putupaula (Kalu Ganga) | 0.23 | 🟢 Normal | -0.068 |  |
| 2026-03-23 18:00:42 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | -0.101 |  |
| 2026-03-24 00:04:40 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -1.500 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)