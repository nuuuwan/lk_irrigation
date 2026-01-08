# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--09_03:05:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **40,508 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-09 03:05:49 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-09 03:05:43 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-09 03:05:37 | Thanamalwila (Kirindi Oya) | 0.92 | 🟢 Normal | -0.009 |  |
| 2026-01-09 03:05:08 | Panadugama (Nilwala Ganga) | 2.61 | 🟢 Normal | -0.019 |  |
| 2026-01-09 03:04:58 | Katharagama (Menik Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-09 03:04:55 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | -0.056 |  |
| 2026-01-09 03:04:25 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.021 |  |
| 2026-01-09 03:04:16 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.023 |  |
| 2026-01-09 03:03:50 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-09 03:03:44 | Nakkala (Kumbukkan Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-01-09 03:02:57 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-09 03:02:49 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-09 03:02:25 | Dunamale (Aththanagalu Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-09 03:02:16 | Moragaswewa (Deduru Oya) | 2.38 | 🟢 Normal | 0.654 | 🔺 Rising |
| 2026-01-09 03:02:11 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-09 03:02:09 | Siyambalanduwa (Heda Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-01-09 03:02:02 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | 0.000 |  |
| 2026-01-09 03:01:52 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-09 03:01:50 | Yaka Wewa (Ma Oya) | 0.75 | 🟢 Normal | -0.055 |  |
| 2026-01-09 03:01:49 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-01-09 03:01:45 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-01-09 03:01:21 | Padiyathalawa (Maduru Oya) | 1.27 | 🟢 Normal | -0.011 |  |
| 2026-01-09 03:01:18 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.195 |  |
| 2026-01-09 03:01:08 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-09 03:00:19 | Horowpothana (Yan Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-01-09 02:59:51 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-09 02:59:41 | Horowpothana (Yan Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-01-09 02:50:54 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | -0.055 |  |
| 2026-01-09 02:45:01 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-01-09 02:39:21 | Dunamale (Aththanagalu Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-09 02:33:34 | Peradeniya (Mahaweli Ganga) | 2.19 | 🟢 Normal | -0.195 |  |
| 2026-01-09 02:23:03 | Horowpothana (Yan Oya) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-01-09 02:16:24 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-09 02:16:23 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-09 02:12:19 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-09 02:12:07 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.023 |  |
| 2026-01-09 02:10:25 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-09 02:08:12 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-09 00:12:03 | Thaldena (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.783 | 🔺 Rising |
| 2026-01-09 03:02:16 | Moragaswewa (Deduru Oya) | 2.38 | 🟢 Normal | 0.654 | 🔺 Rising |
| 2026-01-09 02:03:35 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-01-09 00:15:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-01-09 02:45:01 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-01-09 02:07:07 | Glencourse (Kelani Ganga) | 8.69 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-01-08 18:00:51 | Weraganthota (Mahaweli Ganga) | -1.15 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-09 02:59:51 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-09 03:02:11 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-09 03:02:49 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-09 03:00:19 | Horowpothana (Yan Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-01-09 03:03:50 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-09 03:05:49 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-09 03:02:57 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-09 03:05:43 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-09 03:02:02 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | 0.000 |  |
| 2026-01-09 03:01:08 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-09 03:02:25 | Dunamale (Aththanagalu Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-09 03:04:58 | Katharagama (Menik Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-09 03:01:52 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-09 01:36:06 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-09 02:10:25 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-09 01:03:06 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-09 03:01:45 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-01-09 03:05:37 | Thanamalwila (Kirindi Oya) | 0.92 | 🟢 Normal | -0.009 |  |
| 2026-01-08 18:02:13 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-01-09 03:03:44 | Nakkala (Kumbukkan Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-01-09 03:02:09 | Siyambalanduwa (Heda Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-01-09 03:01:49 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-01-09 03:01:21 | Padiyathalawa (Maduru Oya) | 1.27 | 🟢 Normal | -0.011 |  |
| 2026-01-09 03:05:08 | Panadugama (Nilwala Ganga) | 2.61 | 🟢 Normal | -0.019 |  |
| 2026-01-09 03:04:25 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.021 |  |
| 2026-01-09 03:04:16 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.023 |  |
| 2026-01-08 18:07:05 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | -0.038 |  |
| 2026-01-09 01:01:31 | Manampitiya (Mahaweli Ganga) | 2.04 | 🟢 Normal | -0.049 |  |
| 2026-01-09 03:01:50 | Yaka Wewa (Ma Oya) | 0.75 | 🟢 Normal | -0.055 |  |
| 2026-01-09 03:04:55 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | -0.056 |  |
| 2026-01-09 03:01:18 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.195 |  |
| 2026-01-09 02:06:58 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | -1.846 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)