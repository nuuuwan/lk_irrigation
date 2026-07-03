# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--03_13:14:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **196,159 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-03 13:14:43 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | -0.009 |  |
| 2026-07-03 13:10:31 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | -0.009 |  |
| 2026-07-03 13:09:02 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | -0.009 |  |
| 2026-07-03 13:08:49 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-07-03 13:07:21 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-03 13:06:17 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-03 13:06:09 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-03 13:05:56 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-03 13:05:49 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | -0.010 |  |
| 2026-07-03 13:05:47 | Glencourse (Kelani Ganga) | 9.60 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-07-03 13:05:38 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-07-03 13:05:33 | Dunamale (Aththanagalu Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-03 13:05:03 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-03 13:04:12 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-03 13:03:35 | Hanwella (Kelani Ganga) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-07-03 13:03:24 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-03 13:03:06 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-07-03 13:02:59 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.031 |  |
| 2026-07-03 13:02:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-07-03 13:02:41 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-07-03 13:02:40 | Deraniyagala (Kelani Ganga) | 0.74 | 🟢 Normal | -0.060 |  |
| 2026-07-03 13:02:40 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-03 13:02:35 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-03 13:02:28 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-07-03 13:02:24 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-03 13:02:09 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-03 13:02:03 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 2.919 | 🔺 Rising |
| 2026-07-03 13:01:49 | Moragaswewa (Deduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-03 13:01:42 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-07-03 13:01:32 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-03 13:01:26 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 2.919 | 🔺 Rising |
| 2026-07-03 13:01:24 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.140 |  |
| 2026-07-03 13:01:20 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-03 13:01:15 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-07-03 13:01:14 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.193 | 🔺 Rising |
| 2026-07-03 13:01:08 | Ellagawa (Kalu Ganga) | 4.90 | 🟢 Normal | 0.000 |  |
| 2026-07-03 13:01:00 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-07-03 13:00:57 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-07-03 13:00:19 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | -3.291 |  |
| 2026-07-03 12:55:48 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-03 13:02:03 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 2.919 | 🔺 Rising |
| 2026-07-03 13:01:14 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.193 | 🔺 Rising |
| 2026-07-03 13:03:06 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-07-03 13:02:28 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-07-03 13:08:49 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-07-03 13:05:47 | Glencourse (Kelani Ganga) | 9.60 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-07-03 13:00:57 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-07-03 13:06:17 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-03 13:01:42 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-07-03 13:01:49 | Moragaswewa (Deduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-03 13:01:00 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-07-03 13:01:20 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-03 13:02:35 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-03 13:01:32 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-03 13:03:24 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-03 13:05:56 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-03 13:02:40 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-03 13:01:08 | Ellagawa (Kalu Ganga) | 4.90 | 🟢 Normal | 0.000 |  |
| 2026-07-03 13:02:41 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-07-03 13:05:38 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-07-03 13:04:12 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-03 13:07:21 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-03 13:05:33 | Dunamale (Aththanagalu Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-03 13:02:09 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-03 13:05:03 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-03 13:01:15 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-07-03 13:06:09 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-03 13:02:24 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-03 13:02:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-07-03 13:10:31 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | -0.009 |  |
| 2026-07-03 13:14:43 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | -0.009 |  |
| 2026-07-03 13:09:02 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | -0.009 |  |
| 2026-07-03 13:05:49 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | -0.010 |  |
| 2026-07-03 13:03:35 | Hanwella (Kelani Ganga) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-07-03 12:09:08 | Rathnapura (Kalu Ganga) | 1.21 | 🟢 Normal | -0.019 |  |
| 2026-07-03 13:02:59 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.031 |  |
| 2026-07-03 13:02:40 | Deraniyagala (Kelani Ganga) | 0.74 | 🟢 Normal | -0.060 |  |
| 2026-07-03 13:01:24 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.140 |  |
| 2026-07-03 13:00:19 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | -3.291 |  |

## River Water Level Charts by Station

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)