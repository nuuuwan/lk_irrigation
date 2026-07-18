# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--19_04:19:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **210,124 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-19 04:19:04 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-19 04:18:44 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-19 04:15:14 | Rathnapura (Kalu Ganga) | 0.65 | 🟢 Normal | -0.008 |  |
| 2026-07-19 04:11:23 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-19 04:07:35 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-07-19 04:06:37 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-07-19 04:06:34 | Nawalapitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | -0.009 |  |
| 2026-07-19 04:06:34 | Glencourse (Kelani Ganga) | 9.18 | 🟢 Normal | 0.000 |  |
| 2026-07-19 04:06:20 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-07-19 04:06:00 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-19 04:05:52 | Glencourse (Kelani Ganga) | 9.18 | 🟢 Normal | 0.000 |  |
| 2026-07-19 04:05:22 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-07-19 04:04:24 | Hanwella (Kelani Ganga) | 0.61 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-19 04:04:21 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-19 04:04:15 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-19 04:03:47 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-07-19 04:03:17 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-07-19 04:03:09 | Siyambalanduwa (Heda Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-19 04:02:46 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-19 04:02:30 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-19 04:02:29 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-19 04:02:12 | Thalgahagoda (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-07-19 04:02:02 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-19 04:01:58 | Peradeniya (Mahaweli Ganga) | 1.72 | 🟢 Normal | -0.063 |  |
| 2026-07-19 04:01:58 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-19 04:01:54 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-19 04:01:42 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-19 04:01:28 | Ellagawa (Kalu Ganga) | 4.11 | 🟢 Normal | 0.000 |  |
| 2026-07-19 04:01:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-07-19 04:00:52 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-19 04:00:24 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-19 04:06:37 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-07-19 04:07:35 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-07-19 04:03:47 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-07-19 04:02:12 | Thalgahagoda (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-07-19 04:01:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-07-19 04:04:24 | Hanwella (Kelani Ganga) | 0.61 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-18 18:01:57 | Thanthirimale (Malwathu Oya) | 1.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-19 04:00:24 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-19 04:02:29 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-19 03:02:21 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-19 02:36:08 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-19 04:00:52 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-19 04:01:42 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-19 04:05:22 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-07-19 04:02:02 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-18 18:02:55 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-19 04:02:46 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-19 02:38:10 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-07-19 04:02:30 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-19 04:01:28 | Ellagawa (Kalu Ganga) | 4.11 | 🟢 Normal | 0.000 |  |
| 2026-07-19 04:06:20 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-07-19 04:19:04 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-19 04:06:34 | Glencourse (Kelani Ganga) | 9.18 | 🟢 Normal | 0.000 |  |
| 2026-07-19 03:11:28 | Moraketiya (Walawe Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-07-19 04:03:09 | Siyambalanduwa (Heda Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-19 03:07:16 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-07-19 04:01:54 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-19 04:04:21 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-19 04:03:17 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-07-19 04:11:23 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-19 04:18:44 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-19 04:06:00 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-19 04:04:15 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-19 03:02:09 | Thanamalwila (Kirindi Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-19 04:15:14 | Rathnapura (Kalu Ganga) | 0.65 | 🟢 Normal | -0.008 |  |
| 2026-07-19 04:06:34 | Nawalapitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | -0.009 |  |
| 2026-07-18 18:00:36 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.047 |  |
| 2026-07-19 03:12:35 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | -0.056 |  |
| 2026-07-19 04:01:58 | Peradeniya (Mahaweli Ganga) | 1.72 | 🟢 Normal | -0.063 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)