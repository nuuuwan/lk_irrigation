# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--08_13:23:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **119,528 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-08 13:23:10 | Urawa (Nilwala Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-08 13:16:06 | Panadugama (Nilwala Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-04-08 13:11:53 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-08 13:09:31 | Pitabeddara (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-08 13:08:58 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-04-08 13:06:49 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-08 13:06:16 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-08 13:06:00 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | -0.020 |  |
| 2026-04-08 13:05:58 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | -18.000 |  |
| 2026-04-08 13:05:56 | Ellagawa (Kalu Ganga) | 3.89 | 🟢 Normal | -18.000 |  |
| 2026-04-08 13:05:02 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-04-08 13:04:29 | Urawa (Nilwala Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-08 13:04:28 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-08 13:04:09 | Rathnapura (Kalu Ganga) | 0.76 | 🟢 Normal | -0.039 |  |
| 2026-04-08 13:03:44 | Peradeniya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-08 13:03:33 | Glencourse (Kelani Ganga) | 8.52 | 🟢 Normal | -0.030 |  |
| 2026-04-08 13:03:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.30 | 🟢 Normal | -0.042 |  |
| 2026-04-08 13:03:15 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-08 13:02:52 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-04-08 13:02:47 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | -0.020 |  |
| 2026-04-08 13:02:42 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-04-08 13:02:38 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-08 13:02:29 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-04-08 13:02:27 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-04-08 13:02:20 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-08 13:02:18 | Nawalapitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-08 13:01:54 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-08 13:01:49 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-08 13:01:33 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-08 13:01:31 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.080 |  |
| 2026-04-08 13:01:16 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-08 13:01:16 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-08 13:01:12 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-08 13:01:07 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-08 13:01:07 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-08 13:00:43 | Manampitiya (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.030 |  |
| 2026-04-08 13:00:43 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-08 13:00:21 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-04-08 13:00:18 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-08 13:00:12 | Weraganthota (Mahaweli Ganga) | -2.64 | 🟢 Normal | -0.360 |  |
| 2026-04-08 12:57:03 | Pitabeddara (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-08 13:08:58 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-04-08 13:05:02 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-04-08 12:08:49 | Putupaula (Kalu Ganga) | 0.27 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-08 13:01:54 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-08 13:02:18 | Nawalapitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-08 13:01:12 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-08 13:06:49 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-08 13:01:16 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-08 13:01:16 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-08 13:00:18 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-08 13:01:49 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-08 13:02:42 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-04-08 13:02:29 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-04-08 13:11:53 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-08 12:07:04 | Magura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-08 13:09:31 | Pitabeddara (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-08 13:03:15 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-08 13:02:20 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-08 13:16:06 | Panadugama (Nilwala Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-04-08 13:01:33 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-08 13:01:07 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-08 13:02:38 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-08 13:02:27 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-04-08 13:02:52 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-04-08 13:01:07 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-08 13:03:44 | Peradeniya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-08 13:23:10 | Urawa (Nilwala Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-08 13:06:16 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-08 13:00:43 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-08 13:00:21 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-04-08 13:06:00 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | -0.020 |  |
| 2026-04-08 13:02:47 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | -0.020 |  |
| 2026-04-08 13:00:43 | Manampitiya (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.030 |  |
| 2026-04-08 13:03:33 | Glencourse (Kelani Ganga) | 8.52 | 🟢 Normal | -0.030 |  |
| 2026-04-08 13:04:09 | Rathnapura (Kalu Ganga) | 0.76 | 🟢 Normal | -0.039 |  |
| 2026-04-08 13:03:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.30 | 🟢 Normal | -0.042 |  |
| 2026-04-08 13:01:31 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.080 |  |
| 2026-04-08 13:00:12 | Weraganthota (Mahaweli Ganga) | -2.64 | 🟢 Normal | -0.360 |  |
| 2026-04-08 13:05:58 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)