# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--30_09:13:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **193,324 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-30 09:13:33 | Baddegama (Gin Ganga) | 2.82 | 🟢 Normal | 0.000 |  |
| 2026-06-30 09:10:16 | Thawalama (Gin Ganga) | 1.81 | 🟢 Normal | -0.101 |  |
| 2026-06-30 09:09:55 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-06-30 09:09:16 | Thalgahagoda (Nilwala Ganga) | 0.89 | 🟢 Normal | -0.033 |  |
| 2026-06-30 09:09:08 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-30 09:08:56 | Rathnapura (Kalu Ganga) | 3.95 | 🟢 Normal | -0.164 |  |
| 2026-06-30 09:07:54 | Kithulgala (Kelani Ganga) | 1.32 | 🟢 Normal | -0.305 |  |
| 2026-06-30 09:07:08 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-30 09:06:52 | Panadugama (Nilwala Ganga) | 3.62 | 🟢 Normal | -0.097 |  |
| 2026-06-30 09:06:27 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-06-30 09:06:00 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-30 09:05:47 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-30 09:05:43 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-30 09:05:35 | Pitabeddara (Nilwala Ganga) | 1.02 | 🟢 Normal | -0.141 |  |
| 2026-06-30 09:05:10 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-30 09:04:20 | Putupaula (Kalu Ganga) | 1.67 | 🟢 Normal | -0.010 |  |
| 2026-06-30 09:04:17 | Glencourse (Kelani Ganga) | 10.74 | 🟢 Normal | -0.081 |  |
| 2026-06-30 09:04:09 | Hanwella (Kelani Ganga) | 3.11 | 🟢 Normal | -0.090 |  |
| 2026-06-30 09:04:05 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | -0.025 |  |
| 2026-06-30 09:03:25 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.028 |  |
| 2026-06-30 09:03:21 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-06-30 09:02:58 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-06-30 09:02:57 | Baddegama (Gin Ganga) | 2.82 | 🟢 Normal | 0.000 |  |
| 2026-06-30 09:02:43 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-30 09:02:42 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-06-30 09:02:40 | Badalgama (Maha Oya) | 2.58 | 🟢 Normal | -0.010 |  |
| 2026-06-30 09:02:35 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-06-30 09:02:35 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-06-30 09:02:31 | Magura (Kalu Ganga) | 1.97 | 🟢 Normal | -0.044 |  |
| 2026-06-30 09:02:29 | Nawalapitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.020 |  |
| 2026-06-30 09:02:25 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-06-30 09:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.62 | 🟢 Normal | -0.060 |  |
| 2026-06-30 09:02:15 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-30 09:02:03 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-30 09:01:30 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-30 09:01:24 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-06-30 09:01:22 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-30 09:01:08 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-30 09:00:38 | Thanthirimale (Malwathu Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-06-30 08:55:47 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-30 09:01:24 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-06-30 09:05:43 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-30 09:01:08 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-30 09:02:03 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-30 09:03:21 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-06-30 09:01:30 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-30 09:05:47 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-30 09:09:55 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-06-30 09:02:58 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-06-30 09:13:33 | Baddegama (Gin Ganga) | 2.82 | 🟢 Normal | 0.000 |  |
| 2026-06-30 09:09:08 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-30 09:02:35 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-06-30 09:02:15 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-30 08:04:18 | Dunamale (Aththanagalu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-06-30 09:02:43 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-30 09:06:00 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-30 09:02:25 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-06-30 09:00:38 | Thanthirimale (Malwathu Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-06-30 09:01:22 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-30 09:07:08 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-30 08:15:39 | Ellagawa (Kalu Ganga) | 7.96 | 🟢 Normal | -0.008 |  |
| 2026-06-30 09:04:20 | Putupaula (Kalu Ganga) | 1.67 | 🟢 Normal | -0.010 |  |
| 2026-06-30 09:02:35 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-06-30 09:02:42 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-06-30 09:02:40 | Badalgama (Maha Oya) | 2.58 | 🟢 Normal | -0.010 |  |
| 2026-06-30 09:06:27 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-06-30 09:02:29 | Nawalapitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.020 |  |
| 2026-06-30 09:04:05 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | -0.025 |  |
| 2026-06-30 09:03:25 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.028 |  |
| 2026-06-30 09:09:16 | Thalgahagoda (Nilwala Ganga) | 0.89 | 🟢 Normal | -0.033 |  |
| 2026-06-30 09:02:31 | Magura (Kalu Ganga) | 1.97 | 🟢 Normal | -0.044 |  |
| 2026-06-30 09:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.62 | 🟢 Normal | -0.060 |  |
| 2026-06-30 09:04:17 | Glencourse (Kelani Ganga) | 10.74 | 🟢 Normal | -0.081 |  |
| 2026-06-30 09:04:09 | Hanwella (Kelani Ganga) | 3.11 | 🟢 Normal | -0.090 |  |
| 2026-06-30 09:06:52 | Panadugama (Nilwala Ganga) | 3.62 | 🟢 Normal | -0.097 |  |
| 2026-06-30 09:10:16 | Thawalama (Gin Ganga) | 1.81 | 🟢 Normal | -0.101 |  |
| 2026-06-30 09:05:35 | Pitabeddara (Nilwala Ganga) | 1.02 | 🟢 Normal | -0.141 |  |
| 2026-06-30 09:08:56 | Rathnapura (Kalu Ganga) | 3.95 | 🟢 Normal | -0.164 |  |
| 2026-06-30 09:07:54 | Kithulgala (Kelani Ganga) | 1.32 | 🟢 Normal | -0.305 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)