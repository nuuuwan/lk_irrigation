# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--10_08:03:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **41,594 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-10 08:03:13 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-10 08:02:53 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-01-10 08:02:31 | Thaldena (Mahaweli Ganga) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 08:02:23 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-10 08:02:19 | Yaka Wewa (Ma Oya) | 1.06 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-10 08:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | -0.070 |  |
| 2026-01-10 08:02:04 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-10 08:02:03 | Thanthirimale (Malwathu Oya) | 1.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 08:01:31 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.048 |  |
| 2026-01-10 08:01:24 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-01-10 08:01:23 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-10 08:01:22 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-10 08:01:09 | Moragaswewa (Deduru Oya) | 0.92 | 🟢 Normal | -0.051 |  |
| 2026-01-10 08:00:36 | Manampitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-10 08:00:31 | Horowpothana (Yan Oya) | 2.63 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-01-10 08:00:25 | Weraganthota (Mahaweli Ganga) | -1.27 | 🟢 Normal | -0.004 |  |
| 2026-01-10 07:56:03 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-10 07:25:41 | Moragaswewa (Deduru Oya) | 0.95 | 🟢 Normal | -0.051 |  |
| 2026-01-10 07:25:24 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-10 07:19:56 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-10 07:15:50 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-10 07:14:50 | Horowpothana (Yan Oya) | 2.59 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-01-10 07:14:46 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | -0.008 |  |
| 2026-01-10 07:11:27 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.048 |  |
| 2026-01-10 07:11:04 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.054 |  |
| 2026-01-10 07:10:24 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-10 07:09:34 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.018 |  |
| 2026-01-10 07:07:28 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-10 07:07:21 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-01-10 07:07:08 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-10 07:07:05 | Katharagama (Menik Ganga) | 0.67 | 🟢 Normal | -0.019 |  |
| 2026-01-10 07:06:40 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-01-10 07:06:25 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.028 |  |
| 2026-01-10 07:06:06 | Panadugama (Nilwala Ganga) | 2.40 | 🟢 Normal | -0.028 |  |
| 2026-01-10 07:06:04 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.157 |  |
| 2026-01-10 07:05:50 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-10 07:05:44 | Thanamalwila (Kirindi Oya) | 1.25 | 🟢 Normal | -0.040 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-10 07:01:43 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-01-10 07:07:21 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-01-10 08:00:31 | Horowpothana (Yan Oya) | 2.63 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-01-10 08:01:24 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-01-10 08:00:36 | Manampitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-10 07:05:50 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-10 07:04:32 | Padiyathalawa (Maduru Oya) | 1.43 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-10 07:04:16 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-10 08:02:19 | Yaka Wewa (Ma Oya) | 1.06 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-10 08:02:31 | Thaldena (Mahaweli Ganga) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 08:02:03 | Thanthirimale (Malwathu Oya) | 1.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 08:02:04 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-10 08:02:53 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-01-10 08:01:23 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-10 08:02:23 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-10 07:07:28 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-10 07:05:33 | Galgamuwa (Mee Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-10 07:10:24 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-10 07:19:56 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-10 08:03:13 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-10 07:05:27 | Baddegama (Gin Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-10 08:01:22 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-10 07:04:21 | Siyambalanduwa (Heda Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-01-10 07:06:40 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-01-10 07:15:50 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-10 07:07:08 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-10 07:56:03 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-10 08:00:25 | Weraganthota (Mahaweli Ganga) | -1.27 | 🟢 Normal | -0.004 |  |
| 2026-01-10 07:14:46 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | -0.008 |  |
| 2026-01-10 07:09:34 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.018 |  |
| 2026-01-10 07:07:05 | Katharagama (Menik Ganga) | 0.67 | 🟢 Normal | -0.019 |  |
| 2026-01-10 07:06:06 | Panadugama (Nilwala Ganga) | 2.40 | 🟢 Normal | -0.028 |  |
| 2026-01-10 07:06:25 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.028 |  |
| 2026-01-10 07:05:44 | Thanamalwila (Kirindi Oya) | 1.25 | 🟢 Normal | -0.040 |  |
| 2026-01-10 08:01:31 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.048 |  |
| 2026-01-10 08:01:09 | Moragaswewa (Deduru Oya) | 0.92 | 🟢 Normal | -0.051 |  |
| 2026-01-10 07:11:04 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.054 |  |
| 2026-01-10 08:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | -0.070 |  |
| 2026-01-10 07:06:04 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.157 |  |

## River Water Level Charts by Station

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)