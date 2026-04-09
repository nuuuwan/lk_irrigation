# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--09_13:16:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **120,410 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-09 13:16:12 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | -0.009 |  |
| 2026-04-09 13:14:47 | Nawalapitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.008 |  |
| 2026-04-09 13:11:53 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-09 13:11:08 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-04-09 13:10:45 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-04-09 13:09:47 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-09 13:09:27 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | -0.054 |  |
| 2026-04-09 13:07:46 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | -0.009 |  |
| 2026-04-09 13:07:23 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.018 |  |
| 2026-04-09 13:06:26 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-04-09 13:06:11 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | -0.009 |  |
| 2026-04-09 13:05:23 | Rathnapura (Kalu Ganga) | 0.57 | 🟢 Normal | -0.011 |  |
| 2026-04-09 13:05:18 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-09 13:05:05 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | -0.005 |  |
| 2026-04-09 13:04:51 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | -0.010 |  |
| 2026-04-09 13:03:58 | Thanamalwila (Kirindi Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-09 13:03:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-04-09 13:03:10 | Hanwella (Kelani Ganga) | 0.53 | 🟢 Normal | -0.020 |  |
| 2026-04-09 13:03:04 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-04-09 13:02:55 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-09 13:02:39 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.052 |  |
| 2026-04-09 13:02:37 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-04-09 13:02:35 | Putupaula (Kalu Ganga) | 0.33 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-09 13:02:26 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-09 13:02:15 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-09 13:02:13 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-04-09 13:02:00 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-09 13:02:00 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-04-09 13:01:53 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-04-09 13:01:49 | Pitabeddara (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-09 13:01:47 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.040 |  |
| 2026-04-09 13:01:43 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-09 13:01:35 | Weraganthota (Mahaweli Ganga) | -2.68 | 🟢 Normal | -0.210 |  |
| 2026-04-09 13:01:34 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-04-09 13:01:22 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-09 13:01:15 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-09 13:00:07 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-09 13:11:08 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-04-09 13:02:37 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-04-09 13:03:04 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-04-09 13:02:35 | Putupaula (Kalu Ganga) | 0.33 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-09 13:05:18 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-09 13:01:22 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-09 13:02:15 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-09 13:01:43 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-09 13:00:07 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-09 13:09:47 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-09 13:02:26 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-09 13:11:53 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-09 13:01:49 | Pitabeddara (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-09 13:01:15 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-09 13:02:00 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-04-09 13:02:55 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-09 13:02:00 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-09 12:05:34 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-09 13:02:13 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-04-09 13:01:53 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-04-09 13:01:34 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-04-09 13:10:45 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-04-09 13:03:58 | Thanamalwila (Kirindi Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-09 13:03:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-04-09 13:05:05 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | -0.005 |  |
| 2026-04-09 13:14:47 | Nawalapitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.008 |  |
| 2026-04-09 13:16:12 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | -0.009 |  |
| 2026-04-09 13:07:46 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | -0.009 |  |
| 2026-04-09 13:06:11 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | -0.009 |  |
| 2026-04-09 12:05:14 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-04-09 13:06:26 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-04-09 13:04:51 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | -0.010 |  |
| 2026-04-09 13:05:23 | Rathnapura (Kalu Ganga) | 0.57 | 🟢 Normal | -0.011 |  |
| 2026-04-09 13:07:23 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.018 |  |
| 2026-04-09 13:03:10 | Hanwella (Kelani Ganga) | 0.53 | 🟢 Normal | -0.020 |  |
| 2026-04-09 13:01:47 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.040 |  |
| 2026-04-09 13:02:39 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.052 |  |
| 2026-04-09 13:09:27 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | -0.054 |  |
| 2026-04-09 13:01:35 | Weraganthota (Mahaweli Ganga) | -2.68 | 🟢 Normal | -0.210 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)