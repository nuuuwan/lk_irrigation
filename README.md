# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--01_02:12:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **139,586 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-01 02:12:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.97 | 🟢 Normal | -0.012 |  |
| 2026-05-01 02:12:03 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-01 02:11:30 | Rathnapura (Kalu Ganga) | 2.30 | 🟢 Normal | -576.000 |  |
| 2026-05-01 02:11:29 | Rathnapura (Kalu Ganga) | 2.46 | 🟢 Normal | -576.000 |  |
| 2026-05-01 02:10:49 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-05-01 02:09:50 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | -0.046 |  |
| 2026-05-01 02:07:56 | Manampitiya (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.019 |  |
| 2026-05-01 02:07:40 | Ellagawa (Kalu Ganga) | 4.70 | 🟢 Normal | 3.600 | 🔺 Rising |
| 2026-05-01 02:07:36 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-01 02:06:45 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-01 02:06:45 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-01 02:06:43 | Yaka Wewa (Ma Oya) | 1.08 | 🟢 Normal | -0.140 |  |
| 2026-05-01 02:06:12 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-01 02:06:11 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-05-01 02:05:34 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | -0.010 |  |
| 2026-05-01 02:05:27 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-01 02:04:46 | Glencourse (Kelani Ganga) | 8.76 | 🟢 Normal | -0.038 |  |
| 2026-05-01 02:03:39 | Wellawaya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-01 02:03:33 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-05-01 02:03:24 | Moragaswewa (Deduru Oya) | 0.91 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-01 02:03:11 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | -0.012 |  |
| 2026-05-01 02:02:37 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-05-01 02:02:15 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-05-01 02:01:40 | Ellagawa (Kalu Ganga) | 4.34 | 🟢 Normal | 3.600 | 🔺 Rising |
| 2026-05-01 02:01:39 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-01 02:01:24 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-01 02:01:22 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-05-01 02:01:15 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.024 |  |
| 2026-05-01 02:00:20 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-01 02:07:40 | Ellagawa (Kalu Ganga) | 4.70 | 🟢 Normal | 3.600 | 🔺 Rising |
| 2026-05-01 01:00:16 | Peradeniya (Mahaweli Ganga) | 1.92 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-05-01 01:02:55 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-01 02:03:24 | Moragaswewa (Deduru Oya) | 0.91 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-01 02:05:27 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-01 02:01:22 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-05-01 02:03:39 | Wellawaya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-01 01:14:22 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-05-01 01:06:03 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-01 02:02:37 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-05-01 02:01:24 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-01 02:07:36 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-01 02:10:49 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-05-01 02:03:33 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-05-01 02:06:12 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-01 02:01:39 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-01 01:04:56 | Dunamale (Aththanagalu Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-05-01 02:12:03 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-01 02:06:11 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-30 18:02:32 | Thanthirimale (Malwathu Oya) | 3.03 | 🟢 Normal | 0.000 |  |
| 2026-05-01 02:06:45 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-01 02:02:15 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-04-30 23:10:59 | Horowpothana (Yan Oya) | 1.99 | 🟢 Normal | -0.009 |  |
| 2026-05-01 02:05:34 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | -0.010 |  |
| 2026-04-30 18:02:01 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.010 |  |
| 2026-05-01 01:02:14 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-05-01 02:00:20 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-04-30 18:03:14 | Galgamuwa (Mee Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-05-01 02:03:11 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | -0.012 |  |
| 2026-05-01 02:12:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.97 | 🟢 Normal | -0.012 |  |
| 2026-05-01 02:07:56 | Manampitiya (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.019 |  |
| 2026-05-01 01:06:01 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | -0.020 |  |
| 2026-05-01 00:03:12 | Magura (Kalu Ganga) | 1.03 | 🟢 Normal | -0.020 |  |
| 2026-05-01 02:01:15 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.024 |  |
| 2026-05-01 02:04:46 | Glencourse (Kelani Ganga) | 8.76 | 🟢 Normal | -0.038 |  |
| 2026-05-01 00:05:11 | Putupaula (Kalu Ganga) | 0.39 | 🟢 Normal | -0.042 |  |
| 2026-05-01 02:09:50 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | -0.046 |  |
| 2026-05-01 02:06:43 | Yaka Wewa (Ma Oya) | 1.08 | 🟢 Normal | -0.140 |  |
| 2026-05-01 02:11:30 | Rathnapura (Kalu Ganga) | 2.30 | 🟢 Normal | -576.000 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)