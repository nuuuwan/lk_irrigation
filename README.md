# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--10_15:13:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **41,891 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-10 15:13:08 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.021 |  |
| 2026-01-10 15:11:56 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-10 15:11:14 | Nakkala (Kumbukkan Oya) | 1.12 | 🟢 Normal | -0.009 |  |
| 2026-01-10 15:09:11 | Magura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-10 15:07:18 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-01-10 15:07:09 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | -0.009 |  |
| 2026-01-10 15:06:42 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-10 15:06:16 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-10 15:06:10 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 15:06:06 | Padiyathalawa (Maduru Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-01-10 15:05:51 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | 0.000 |  |
| 2026-01-10 15:05:49 | Panadugama (Nilwala Ganga) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-01-10 15:05:46 | Manampitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-01-10 15:05:43 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-10 15:05:42 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-01-10 15:05:36 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-10 15:05:07 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-10 15:04:58 | Moragaswewa (Deduru Oya) | 0.75 | 🟢 Normal | -0.028 |  |
| 2026-01-10 15:04:52 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-10 15:04:28 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-01-10 15:04:05 | Katharagama (Menik Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-10 15:03:44 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-01-10 15:03:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-01-10 15:02:57 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-10 15:02:53 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-10 15:02:41 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-01-10 15:02:36 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-01-10 15:02:14 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 15:01:58 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.035 |  |
| 2026-01-10 15:01:53 | Manampitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-01-10 15:01:51 | Ellagawa (Kalu Ganga) | 4.06 | 🟢 Normal | 0.000 |  |
| 2026-01-10 15:01:44 | Baddegama (Gin Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-01-10 15:01:36 | Horowpothana (Yan Oya) | 2.73 | 🟢 Normal | 0.000 |  |
| 2026-01-10 15:01:23 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-01-10 15:01:22 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-10 15:01:21 | Yaka Wewa (Ma Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-10 15:01:03 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-01-10 15:00:24 | Siyambalanduwa (Heda Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-01-10 15:00:20 | Weraganthota (Mahaweli Ganga) | -1.30 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-10 15:05:42 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-01-10 15:01:23 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-01-10 15:03:44 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-01-10 15:01:22 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-10 15:01:03 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-01-10 15:02:14 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 15:06:10 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 15:00:20 | Weraganthota (Mahaweli Ganga) | -1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-10 15:02:41 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-01-10 15:11:56 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-10 15:01:21 | Yaka Wewa (Ma Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-10 15:02:53 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-10 15:01:36 | Horowpothana (Yan Oya) | 2.73 | 🟢 Normal | 0.000 |  |
| 2026-01-10 15:06:42 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-10 15:09:11 | Magura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-10 15:05:36 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-10 15:04:52 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-10 15:01:51 | Ellagawa (Kalu Ganga) | 4.06 | 🟢 Normal | 0.000 |  |
| 2026-01-10 15:05:49 | Panadugama (Nilwala Ganga) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-01-10 15:06:06 | Padiyathalawa (Maduru Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-01-10 15:05:51 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | 0.000 |  |
| 2026-01-10 15:02:57 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-10 15:00:24 | Siyambalanduwa (Heda Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-01-10 15:05:43 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-10 15:04:05 | Katharagama (Menik Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-10 15:05:07 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-10 15:06:16 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-10 15:05:46 | Manampitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-01-10 14:17:14 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-01-10 15:07:18 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-01-10 15:04:28 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-01-10 15:11:14 | Nakkala (Kumbukkan Oya) | 1.12 | 🟢 Normal | -0.009 |  |
| 2026-01-10 15:07:09 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | -0.009 |  |
| 2026-01-10 15:03:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-01-10 15:01:44 | Baddegama (Gin Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-01-10 15:02:36 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-01-10 15:13:08 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.021 |  |
| 2026-01-10 15:04:58 | Moragaswewa (Deduru Oya) | 0.75 | 🟢 Normal | -0.028 |  |
| 2026-01-10 15:01:58 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.035 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)