# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--30_09:11:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **220,172 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-30 09:11:16 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.026 |  |
| 2026-07-30 09:09:50 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-07-30 09:08:20 | Rathnapura (Kalu Ganga) | 0.96 | 🟢 Normal | -0.021 |  |
| 2026-07-30 09:07:45 | Glencourse (Kelani Ganga) | 8.93 | 🟢 Normal | -0.097 |  |
| 2026-07-30 09:07:01 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-30 09:05:52 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-30 09:05:33 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-30 09:05:12 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-07-30 09:05:10 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-30 09:04:42 | Katharagama (Menik Ganga) | 0.35 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-07-30 09:04:36 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-30 09:04:30 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-30 09:04:26 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-30 09:04:07 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-07-30 09:04:06 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-30 09:04:04 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-30 09:03:55 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-30 09:03:46 | Hanwella (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-30 09:03:25 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-07-30 09:03:00 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-30 09:02:59 | Thawalama (Gin Ganga) | 1.14 | 🟢 Normal | -0.042 |  |
| 2026-07-30 09:02:50 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-30 09:02:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | -0.060 |  |
| 2026-07-30 09:02:31 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-30 09:02:17 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-30 09:02:17 | Ellagawa (Kalu Ganga) | 4.63 | 🟢 Normal | -0.032 |  |
| 2026-07-30 09:02:11 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-07-30 09:02:08 | Thanamalwila (Kirindi Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-30 09:02:08 | Putupaula (Kalu Ganga) | 0.34 | 🟢 Normal | -0.072 |  |
| 2026-07-30 09:01:24 | Magura (Kalu Ganga) | 1.06 | 🟢 Normal | -0.022 |  |
| 2026-07-30 09:01:22 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-30 09:00:41 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-30 09:00:38 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-07-30 09:00:35 | Thanthirimale (Malwathu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-07-30 09:00:34 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.010 |  |
| 2026-07-30 09:00:26 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-07-30 09:00:21 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-07-30 09:00:09 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | 0.111 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-30 09:00:09 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-07-30 09:04:42 | Katharagama (Menik Ganga) | 0.35 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-07-30 09:00:26 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-07-30 09:04:26 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-30 09:02:11 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-07-30 09:05:33 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-30 09:01:22 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-30 09:00:38 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-07-30 09:02:17 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-30 09:03:00 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-30 09:02:50 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-30 09:05:52 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-30 09:04:30 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-30 09:04:04 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-30 09:03:46 | Hanwella (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-30 09:02:31 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-30 09:09:50 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-07-30 08:04:35 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-30 09:04:06 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-30 09:00:41 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-30 09:07:01 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-30 09:05:10 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-30 09:05:12 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-07-30 09:04:36 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-30 09:00:35 | Thanthirimale (Malwathu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-07-30 09:03:55 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-30 09:02:08 | Thanamalwila (Kirindi Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-30 09:03:25 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-07-30 09:04:07 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-07-30 09:00:34 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.010 |  |
| 2026-07-30 09:00:21 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-07-30 09:08:20 | Rathnapura (Kalu Ganga) | 0.96 | 🟢 Normal | -0.021 |  |
| 2026-07-30 09:01:24 | Magura (Kalu Ganga) | 1.06 | 🟢 Normal | -0.022 |  |
| 2026-07-30 09:11:16 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.026 |  |
| 2026-07-30 09:02:17 | Ellagawa (Kalu Ganga) | 4.63 | 🟢 Normal | -0.032 |  |
| 2026-07-30 09:02:59 | Thawalama (Gin Ganga) | 1.14 | 🟢 Normal | -0.042 |  |
| 2026-07-30 09:02:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | -0.060 |  |
| 2026-07-30 09:02:08 | Putupaula (Kalu Ganga) | 0.34 | 🟢 Normal | -0.072 |  |
| 2026-07-30 09:07:45 | Glencourse (Kelani Ganga) | 8.93 | 🟢 Normal | -0.097 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)