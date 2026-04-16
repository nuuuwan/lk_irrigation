# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--16_08:14:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **126,450 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-16 08:14:49 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | -0.033 |  |
| 2026-04-16 08:12:13 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-16 08:11:52 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-16 08:11:51 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-16 08:09:19 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.022 |  |
| 2026-04-16 08:07:51 | Glencourse (Kelani Ganga) | 9.21 | 🟢 Normal | -0.050 |  |
| 2026-04-16 08:07:16 | Panadugama (Nilwala Ganga) | 2.49 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-16 08:07:10 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-04-16 08:07:10 | Ellagawa (Kalu Ganga) | 4.50 | 🟢 Normal | 0.000 |  |
| 2026-04-16 08:06:32 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-04-16 08:06:28 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-16 08:05:56 | Kithulgala (Kelani Ganga) | 1.11 | 🟢 Normal | -0.086 |  |
| 2026-04-16 08:05:21 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.061 |  |
| 2026-04-16 08:05:17 | Rathnapura (Kalu Ganga) | 1.66 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2026-04-16 08:05:09 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-04-16 08:04:28 | Hanwella (Kelani Ganga) | 0.86 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-16 08:04:21 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-16 08:04:11 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-04-16 08:03:51 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-16 08:03:49 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-04-16 08:03:37 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-16 08:03:28 | Putupaula (Kalu Ganga) | 0.32 | 🟢 Normal | -0.060 |  |
| 2026-04-16 08:02:46 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.020 |  |
| 2026-04-16 08:02:45 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-16 08:02:14 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-16 08:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.01 | 🟢 Normal | -0.100 |  |
| 2026-04-16 08:02:08 | Thanamalwila (Kirindi Oya) | 1.93 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-16 08:02:00 | Kuda Oya (Kirindi Oya) | 1.75 | 🟢 Normal | -0.065 |  |
| 2026-04-16 08:01:42 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-16 08:01:40 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-16 08:01:38 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-16 08:01:34 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-16 08:01:24 | Manampitiya (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-04-16 08:01:16 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-16 08:01:15 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | -0.011 |  |
| 2026-04-16 08:01:05 | Thanthirimale (Malwathu Oya) | 1.90 | 🟢 Normal | -0.020 |  |
| 2026-04-16 08:01:02 | Nawalapitiya (Mahaweli Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-04-16 08:00:13 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-16 08:00:11 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.051 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-16 08:05:17 | Rathnapura (Kalu Ganga) | 1.66 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2026-04-16 08:04:28 | Hanwella (Kelani Ganga) | 0.86 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-16 08:06:32 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-04-16 08:02:08 | Thanamalwila (Kirindi Oya) | 1.93 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-16 08:07:16 | Panadugama (Nilwala Ganga) | 2.49 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-16 07:01:28 | Magura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-16 08:12:13 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-16 08:00:13 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-16 08:01:42 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-16 08:01:40 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-16 08:03:51 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-16 08:01:16 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-16 08:03:37 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-16 08:11:51 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-16 08:07:10 | Ellagawa (Kalu Ganga) | 4.50 | 🟢 Normal | 0.000 |  |
| 2026-04-16 08:04:21 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-16 08:02:45 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-16 08:06:28 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-16 08:01:34 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-16 08:02:14 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-16 08:07:10 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-04-16 08:05:09 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-04-16 08:11:52 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-16 08:04:11 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-04-16 08:01:02 | Nawalapitiya (Mahaweli Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-04-16 08:01:24 | Manampitiya (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-04-16 08:03:49 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-04-16 08:01:15 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | -0.011 |  |
| 2026-04-16 08:02:46 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.020 |  |
| 2026-04-16 08:01:05 | Thanthirimale (Malwathu Oya) | 1.90 | 🟢 Normal | -0.020 |  |
| 2026-04-16 08:09:19 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.022 |  |
| 2026-04-16 08:14:49 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | -0.033 |  |
| 2026-04-16 08:07:51 | Glencourse (Kelani Ganga) | 9.21 | 🟢 Normal | -0.050 |  |
| 2026-04-16 08:00:11 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.051 |  |
| 2026-04-16 08:03:28 | Putupaula (Kalu Ganga) | 0.32 | 🟢 Normal | -0.060 |  |
| 2026-04-16 08:05:21 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.061 |  |
| 2026-04-16 08:02:00 | Kuda Oya (Kirindi Oya) | 1.75 | 🟢 Normal | -0.065 |  |
| 2026-04-16 08:05:56 | Kithulgala (Kelani Ganga) | 1.11 | 🟢 Normal | -0.086 |  |
| 2026-04-16 08:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.01 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)