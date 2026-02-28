# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--28_23:16:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **85,756 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-28 23:16:21 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-02-28 23:10:43 | Ellagawa (Kalu Ganga) | 3.99 | 🟢 Normal | 0.000 |  |
| 2026-02-28 23:10:10 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-28 23:09:40 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | -0.009 |  |
| 2026-02-28 23:09:18 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-02-28 23:08:10 | Dunamale (Aththanagalu Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-28 23:08:02 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-28 23:07:05 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-28 23:07:02 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-28 23:06:43 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-28 23:06:42 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-28 23:06:40 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-28 23:06:23 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-28 23:06:12 | Dunamale (Aththanagalu Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-28 23:05:58 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.016 |  |
| 2026-02-28 23:05:22 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-28 23:05:11 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-28 23:04:20 | Hanwella (Kelani Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-02-28 23:04:08 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-28 23:03:27 | Peradeniya (Mahaweli Ganga) | 1.73 | 🟢 Normal | 0.329 | 🔺 Rising |
| 2026-02-28 23:03:18 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-02-28 23:03:10 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-28 23:03:04 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-02-28 23:02:40 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-02-28 23:02:12 | Glencourse (Kelani Ganga) | 8.30 | 🟢 Normal | -0.020 |  |
| 2026-02-28 23:02:10 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-02-28 23:01:56 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-28 23:01:45 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-28 23:01:34 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-02-28 23:01:28 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-02-28 23:00:48 | Manampitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-02-28 23:00:17 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-28 23:00:10 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-28 22:59:46 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-28 22:28:41 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.016 |  |
| 2026-02-28 22:27:48 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-28 22:26:26 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-28 23:03:27 | Peradeniya (Mahaweli Ganga) | 1.73 | 🟢 Normal | 0.329 | 🔺 Rising |
| 2026-02-28 23:01:34 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-02-28 22:08:29 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-02-28 18:00:50 | Weraganthota (Mahaweli Ganga) | -1.93 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-02-28 21:06:36 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-28 23:08:02 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-28 23:16:21 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-02-28 23:06:42 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-28 23:03:04 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-02-28 23:00:10 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-28 23:01:56 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-28 23:01:45 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-28 23:05:11 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-28 23:03:10 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-28 23:00:17 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-28 18:04:16 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-28 23:05:22 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-28 23:10:43 | Ellagawa (Kalu Ganga) | 3.99 | 🟢 Normal | 0.000 |  |
| 2026-02-28 22:27:48 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-28 23:02:10 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-02-28 23:06:40 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-28 23:04:08 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-28 23:08:10 | Dunamale (Aththanagalu Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-28 23:07:05 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-28 23:09:18 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-02-28 23:06:43 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-28 23:00:48 | Manampitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-02-28 18:17:10 | Thanthirimale (Malwathu Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-02-28 22:59:46 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-28 23:10:10 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-28 23:02:40 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-02-28 23:06:23 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-28 23:09:40 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | -0.009 |  |
| 2026-02-28 23:04:20 | Hanwella (Kelani Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-02-28 23:03:18 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-02-28 23:01:28 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-02-28 23:05:58 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.016 |  |
| 2026-02-28 23:02:12 | Glencourse (Kelani Ganga) | 8.30 | 🟢 Normal | -0.020 |  |
| 2026-02-28 20:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | -0.028 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)