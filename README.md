# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--30_20:46:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **111,743 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-30 20:46:15 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.006 |  |
| 2026-03-30 20:30:13 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-30 20:25:58 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | -0.037 |  |
| 2026-03-30 20:25:57 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-30 20:13:42 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-30 20:11:32 | Putupaula (Kalu Ganga) | 0.36 | 🟢 Normal | -0.037 |  |
| 2026-03-30 20:10:57 | Peradeniya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-03-30 20:09:10 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | -0.009 |  |
| 2026-03-30 20:09:08 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | -0.011 |  |
| 2026-03-30 20:07:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.18 | 🟢 Normal | -0.014 |  |
| 2026-03-30 20:07:48 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-30 20:07:31 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-03-30 20:06:06 | Rathnapura (Kalu Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-03-30 20:06:02 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-30 20:06:01 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-30 20:05:44 | Magura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-03-30 20:05:21 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | -0.009 |  |
| 2026-03-30 20:05:00 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-30 20:04:44 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-03-30 20:04:38 | Deraniyagala (Kelani Ganga) | 0.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-30 20:04:27 | Hanwella (Kelani Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-03-30 20:04:01 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-30 20:03:50 | Glencourse (Kelani Ganga) | 8.28 | 🟢 Normal | -0.041 |  |
| 2026-03-30 20:03:44 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.049 |  |
| 2026-03-30 20:03:40 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-30 20:03:23 | Badalgama (Maha Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-03-30 20:02:52 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-30 20:02:21 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-30 20:02:20 | Ellagawa (Kalu Ganga) | 3.68 | 🟢 Normal | 0.000 |  |
| 2026-03-30 20:02:14 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-30 20:01:56 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-03-30 20:01:41 | Manampitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-30 20:01:34 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-30 20:01:03 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-30 20:00:57 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-30 20:00:17 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-30 20:00:08 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-30 20:01:41 | Manampitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-30 20:07:31 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-03-30 20:10:57 | Peradeniya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-03-30 20:03:40 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-30 20:05:44 | Magura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-03-30 20:04:38 | Deraniyagala (Kelani Ganga) | 0.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-30 18:07:18 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-30 20:13:42 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-30 20:05:00 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-30 20:00:57 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-30 20:07:48 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-30 20:00:17 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-30 20:01:34 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-30 20:02:52 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-30 20:30:13 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-30 20:06:01 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-30 20:02:20 | Ellagawa (Kalu Ganga) | 3.68 | 🟢 Normal | 0.000 |  |
| 2026-03-30 20:00:08 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-03-30 20:04:01 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-30 20:02:21 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-30 20:04:44 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-03-30 20:03:23 | Badalgama (Maha Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-03-30 20:06:02 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-30 18:00:31 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-03-30 20:25:57 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-30 20:01:03 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-30 20:46:15 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.006 |  |
| 2026-03-30 20:05:21 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | -0.009 |  |
| 2026-03-30 20:09:10 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | -0.009 |  |
| 2026-03-30 20:04:27 | Hanwella (Kelani Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-03-30 20:06:06 | Rathnapura (Kalu Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-03-30 20:01:56 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-03-30 20:09:08 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | -0.011 |  |
| 2026-03-30 20:07:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.18 | 🟢 Normal | -0.014 |  |
| 2026-03-30 20:11:32 | Putupaula (Kalu Ganga) | 0.36 | 🟢 Normal | -0.037 |  |
| 2026-03-30 20:25:58 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | -0.037 |  |
| 2026-03-30 20:03:50 | Glencourse (Kelani Ganga) | 8.28 | 🟢 Normal | -0.041 |  |
| 2026-03-30 18:03:12 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | -0.049 |  |
| 2026-03-30 20:03:44 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.049 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)