# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--24_11:07:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **106,003 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-24 11:07:55 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | -0.011 |  |
| 2026-03-24 11:07:40 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | -0.010 |  |
| 2026-03-24 11:07:15 | Ellagawa (Kalu Ganga) | 3.94 | 🟢 Normal | -0.010 |  |
| 2026-03-24 11:07:11 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.078 |  |
| 2026-03-24 11:05:12 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-24 11:05:05 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | -0.010 |  |
| 2026-03-24 11:04:47 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-24 11:04:28 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-24 11:04:01 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-24 11:03:58 | Putupaula (Kalu Ganga) | 0.15 | 🟢 Normal | -0.060 |  |
| 2026-03-24 11:03:58 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-03-24 11:03:54 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-03-24 11:03:08 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-24 11:03:07 | Nawalapitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-24 11:03:04 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-24 11:02:52 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-24 11:02:47 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.020 |  |
| 2026-03-24 11:02:44 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-24 11:02:43 | Padiyathalawa (Maduru Oya) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-03-24 11:02:27 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-24 11:02:25 | Pitabeddara (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-03-24 11:02:20 | Baddegama (Gin Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-03-24 11:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.49 | 🟢 Normal | -0.040 |  |
| 2026-03-24 11:01:48 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-24 11:01:46 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-24 11:01:41 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.193 | 🔺 Rising |
| 2026-03-24 11:01:32 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-24 11:01:28 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.102 |  |
| 2026-03-24 11:01:26 | Thanamalwila (Kirindi Oya) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-03-24 11:01:11 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-03-24 11:01:10 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-03-24 11:01:02 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.051 |  |
| 2026-03-24 11:00:57 | Horowpothana (Yan Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-03-24 11:00:42 | Weraganthota (Mahaweli Ganga) | -2.24 | 🟢 Normal | -0.144 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-24 11:01:41 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.193 | 🔺 Rising |
| 2026-03-24 11:02:52 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-24 11:02:44 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-24 11:03:04 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-24 11:04:47 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-24 10:01:11 | Moragaswewa (Deduru Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-24 11:03:07 | Nawalapitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-24 11:01:46 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-24 11:01:48 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-24 11:04:28 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-24 11:02:27 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-24 11:02:25 | Pitabeddara (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-03-24 11:03:08 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-24 11:02:20 | Baddegama (Gin Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-03-24 10:03:22 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-03-24 11:05:12 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-24 11:04:01 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-24 10:07:17 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-24 11:01:11 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-03-24 11:03:54 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-03-24 11:01:32 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-24 11:07:15 | Ellagawa (Kalu Ganga) | 3.94 | 🟢 Normal | -0.010 |  |
| 2026-03-24 11:02:43 | Padiyathalawa (Maduru Oya) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-03-24 11:01:26 | Thanamalwila (Kirindi Oya) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-03-24 11:03:58 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-03-24 11:05:05 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | -0.010 |  |
| 2026-03-24 11:01:10 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-03-24 11:07:40 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | -0.010 |  |
| 2026-03-24 11:00:57 | Horowpothana (Yan Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-03-24 11:07:55 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | -0.011 |  |
| 2026-03-24 11:02:47 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.020 |  |
| 2026-03-24 10:05:05 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | -0.030 |  |
| 2026-03-24 11:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.49 | 🟢 Normal | -0.040 |  |
| 2026-03-24 10:14:14 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.046 |  |
| 2026-03-24 11:01:02 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.051 |  |
| 2026-03-24 11:03:58 | Putupaula (Kalu Ganga) | 0.15 | 🟢 Normal | -0.060 |  |
| 2026-03-24 11:07:11 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.078 |  |
| 2026-03-24 11:01:28 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.102 |  |
| 2026-03-24 11:00:42 | Weraganthota (Mahaweli Ganga) | -2.24 | 🟢 Normal | -0.144 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)