# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--12_21:13:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **204,552 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-12 21:13:44 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-12 21:11:13 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-12 21:09:55 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-07-12 21:09:53 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-07-12 21:06:59 | Thalgahagoda (Nilwala Ganga) | 0.09 | 🟢 Normal | -0.048 |  |
| 2026-07-12 21:06:56 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-12 21:06:02 | Glencourse (Kelani Ganga) | 9.07 | 🟢 Normal | 0.000 |  |
| 2026-07-12 21:05:40 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-12 21:05:11 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-07-12 21:05:05 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-12 21:05:04 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-12 21:04:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | -0.019 |  |
| 2026-07-12 21:04:17 | Rathnapura (Kalu Ganga) | 0.94 | 🟢 Normal | -0.035 |  |
| 2026-07-12 21:04:17 | Dunamale (Aththanagalu Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-12 21:03:52 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-12 21:03:46 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-12 21:03:29 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-07-12 21:03:27 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-12 21:03:24 | Magura (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-12 21:03:03 | Peradeniya (Mahaweli Ganga) | 1.99 | 🟢 Normal | 0.375 | 🔺 Rising |
| 2026-07-12 21:02:53 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-07-12 21:02:51 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-12 21:02:49 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-12 21:02:39 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | -0.020 |  |
| 2026-07-12 21:02:31 | Hanwella (Kelani Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-07-12 21:02:25 | Thanamalwila (Kirindi Oya) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-07-12 21:02:22 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | -0.010 |  |
| 2026-07-12 21:02:17 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-12 21:02:16 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | -0.005 |  |
| 2026-07-12 21:02:08 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-07-12 21:01:47 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-12 21:01:30 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | 0.000 |  |
| 2026-07-12 21:01:27 | Putupaula (Kalu Ganga) | 0.17 | 🟢 Normal | -0.036 |  |
| 2026-07-12 21:01:26 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-12 21:01:09 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-12 21:01:00 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-07-12 21:00:21 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.156 |  |
| 2026-07-12 20:34:24 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-12 21:03:03 | Peradeniya (Mahaweli Ganga) | 1.99 | 🟢 Normal | 0.375 | 🔺 Rising |
| 2026-07-12 21:05:05 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-12 21:01:26 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-12 18:00:50 | Weraganthota (Mahaweli Ganga) | -3.39 | 🟢 Normal | 0.000 |  |
| 2026-07-12 21:01:47 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-12 21:03:52 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-12 21:05:40 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-12 21:11:13 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-12 21:13:44 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-12 18:02:26 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-12 21:03:24 | Magura (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-12 21:01:09 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-12 21:02:51 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-12 21:01:30 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | 0.000 |  |
| 2026-07-12 21:09:55 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-07-12 21:02:53 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-07-12 21:06:56 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-12 21:06:02 | Glencourse (Kelani Ganga) | 9.07 | 🟢 Normal | 0.000 |  |
| 2026-07-12 21:03:46 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-12 21:02:17 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-12 21:04:17 | Dunamale (Aththanagalu Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-12 21:03:27 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-12 21:05:04 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-12 18:01:22 | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-12 21:05:11 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-07-12 21:02:49 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-12 21:02:16 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | -0.005 |  |
| 2026-07-12 21:02:08 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-07-12 21:02:25 | Thanamalwila (Kirindi Oya) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-07-12 21:01:00 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-07-12 21:03:29 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-07-12 21:02:31 | Hanwella (Kelani Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-07-12 21:02:22 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | -0.010 |  |
| 2026-07-12 21:04:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | -0.019 |  |
| 2026-07-12 21:02:39 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | -0.020 |  |
| 2026-07-12 21:04:17 | Rathnapura (Kalu Ganga) | 0.94 | 🟢 Normal | -0.035 |  |
| 2026-07-12 21:01:27 | Putupaula (Kalu Ganga) | 0.17 | 🟢 Normal | -0.036 |  |
| 2026-07-12 21:06:59 | Thalgahagoda (Nilwala Ganga) | 0.09 | 🟢 Normal | -0.048 |  |
| 2026-07-12 21:00:21 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.156 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)