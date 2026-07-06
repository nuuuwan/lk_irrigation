# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--07_05:06:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **199,420 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-07 05:06:43 | Baddegama (Gin Ganga) | 0.88 | 🟢 Normal | -0.020 |  |
| 2026-07-07 05:06:15 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-07 05:06:08 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | -0.150 |  |
| 2026-07-07 05:05:21 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-07 05:04:39 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-07 05:04:14 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-07 05:03:57 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-07-07 05:03:06 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-07 05:03:05 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-07 05:03:02 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-07-07 05:02:56 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.058 |  |
| 2026-07-07 05:02:41 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-07 05:02:30 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-07-07 05:02:27 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-07 05:02:21 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.050 |  |
| 2026-07-07 05:02:09 | Hanwella (Kelani Ganga) | 1.58 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-07 05:01:57 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-07-07 05:01:51 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-07-07 05:01:41 | Dunamale (Aththanagalu Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-07-07 05:01:33 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-07 05:00:58 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-07-07 05:00:53 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | -122.000 |  |
| 2026-07-07 05:00:47 | Moragaswewa (Deduru Oya) | 0.15 | 🟢 Normal | -0.011 |  |
| 2026-07-07 05:00:35 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | -122.000 |  |
| 2026-07-07 04:43:42 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | -0.006 |  |
| 2026-07-07 04:42:47 | Deraniyagala (Kelani Ganga) | 0.74 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-07-07 04:39:04 | Badalgama (Maha Oya) | 2.29 | 🟢 Normal | -0.006 |  |
| 2026-07-07 04:20:51 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-07-07 04:20:49 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-07-07 04:18:00 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | 0.057 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-07 04:07:09 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 1.636 | 🔺 Rising |
| 2026-07-07 03:00:45 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-07-07 05:01:51 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-07-07 05:03:57 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-07-07 05:02:30 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-07-07 03:06:50 | Glencourse (Kelani Ganga) | 9.96 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-07 05:01:57 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-07-07 05:02:09 | Hanwella (Kelani Ganga) | 1.58 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-07 05:02:27 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-07 04:00:52 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-07 05:00:58 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-07-07 05:04:14 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-07 05:03:05 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-07 04:12:15 | Magura (Kalu Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-07 05:03:06 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-07 05:04:39 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-07 05:02:41 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-07 05:05:21 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-07 04:02:22 | Rathnapura (Kalu Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-06 18:00:56 | Thanthirimale (Malwathu Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-07 05:06:15 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-07 04:01:10 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-07 05:01:33 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-07 04:43:42 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | -0.006 |  |
| 2026-07-07 04:39:04 | Badalgama (Maha Oya) | 2.29 | 🟢 Normal | -0.006 |  |
| 2026-07-07 03:06:11 | Ellagawa (Kalu Ganga) | 4.77 | 🟢 Normal | -0.009 |  |
| 2026-07-07 04:09:24 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.009 |  |
| 2026-07-06 18:02:06 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.010 |  |
| 2026-07-06 18:06:11 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-07-07 05:03:02 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-07-07 05:01:41 | Dunamale (Aththanagalu Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-07-07 05:00:47 | Moragaswewa (Deduru Oya) | 0.15 | 🟢 Normal | -0.011 |  |
| 2026-07-07 02:01:26 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | -0.011 |  |
| 2026-07-07 05:06:43 | Baddegama (Gin Ganga) | 0.88 | 🟢 Normal | -0.020 |  |
| 2026-07-07 05:02:21 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.050 |  |
| 2026-07-07 05:02:56 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.058 |  |
| 2026-07-07 04:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.060 |  |
| 2026-07-07 05:06:08 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | -0.150 |  |
| 2026-07-07 05:00:53 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | -122.000 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)