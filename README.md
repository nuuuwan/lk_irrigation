# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--13_00:16:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **44,017 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-13 00:16:00 | Glencourse (Kelani Ganga) | 9.25 | 🟢 Normal | -0.052 |  |
| 2026-01-13 00:13:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-01-13 00:11:33 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-13 00:07:39 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | -0.063 |  |
| 2026-01-13 00:07:37 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-01-13 00:07:23 | Hanwella (Kelani Ganga) | 1.01 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-13 00:06:52 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-13 00:06:11 | Badalgama (Maha Oya) | 2.34 | 🟢 Normal | -0.020 |  |
| 2026-01-13 00:05:42 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | -0.005 |  |
| 2026-01-13 00:05:16 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-13 00:05:13 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-13 00:05:01 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.120 |  |
| 2026-01-13 00:04:58 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-01-13 00:04:53 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-13 00:04:28 | Baddegama (Gin Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-13 00:04:22 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-13 00:03:43 | Siyambalanduwa (Heda Oya) | 1.24 | 🟢 Normal | -0.028 |  |
| 2026-01-13 00:03:39 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-01-13 00:03:27 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-13 00:03:26 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-01-13 00:03:22 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-13 00:03:21 | Yaka Wewa (Ma Oya) | 1.07 | 🟢 Normal | -0.146 |  |
| 2026-01-13 00:03:04 | Ellagawa (Kalu Ganga) | 4.11 | 🟢 Normal | 0.000 |  |
| 2026-01-13 00:02:35 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-01-13 00:02:31 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-01-13 00:02:24 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-13 00:02:24 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-13 00:02:20 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-13 00:02:19 | Dunamale (Aththanagalu Oya) | 1.57 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-01-13 00:02:18 | Padiyathalawa (Maduru Oya) | 1.42 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-01-13 00:01:37 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-01-13 00:01:34 | Manampitiya (Mahaweli Ganga) | 2.07 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-13 00:01:23 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-01-13 00:01:19 | Horowpothana (Yan Oya) | 3.35 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-01-13 00:01:07 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.051 |  |
| 2026-01-13 00:00:53 | Nakkala (Kumbukkan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-01-12 23:45:00 | Nakkala (Kumbukkan Oya) | 1.43 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-13 00:13:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-01-13 00:02:18 | Padiyathalawa (Maduru Oya) | 1.42 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-01-13 00:02:19 | Dunamale (Aththanagalu Oya) | 1.57 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-01-13 00:07:23 | Hanwella (Kelani Ganga) | 1.01 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-13 00:01:19 | Horowpothana (Yan Oya) | 3.35 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-01-13 00:02:20 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-13 00:01:34 | Manampitiya (Mahaweli Ganga) | 2.07 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-13 00:01:37 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-01-13 00:04:22 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-13 00:02:24 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 18:00:10 | Weraganthota (Mahaweli Ganga) | -1.45 | 🟢 Normal | 0.000 |  |
| 2026-01-13 00:02:31 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-01-13 00:00:53 | Nakkala (Kumbukkan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-01-12 18:04:27 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-13 00:11:33 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-13 00:03:04 | Ellagawa (Kalu Ganga) | 4.11 | 🟢 Normal | 0.000 |  |
| 2026-01-13 00:04:28 | Baddegama (Gin Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-12 23:03:17 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-01-13 00:03:22 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-13 00:02:24 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-13 00:05:16 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-13 00:06:52 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-12 18:02:58 | Thanthirimale (Malwathu Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-13 00:04:53 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-13 00:07:37 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-01-13 00:05:42 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | -0.005 |  |
| 2026-01-13 00:02:35 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-01-13 00:03:39 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-01-13 00:03:26 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-01-12 23:01:47 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-01-13 00:01:23 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-01-13 00:04:58 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-01-13 00:06:11 | Badalgama (Maha Oya) | 2.34 | 🟢 Normal | -0.020 |  |
| 2026-01-13 00:03:43 | Siyambalanduwa (Heda Oya) | 1.24 | 🟢 Normal | -0.028 |  |
| 2026-01-13 00:01:07 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.051 |  |
| 2026-01-13 00:16:00 | Glencourse (Kelani Ganga) | 9.25 | 🟢 Normal | -0.052 |  |
| 2026-01-13 00:07:39 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | -0.063 |  |
| 2026-01-13 00:05:01 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.120 |  |
| 2026-01-13 00:03:21 | Yaka Wewa (Ma Oya) | 1.07 | 🟢 Normal | -0.146 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)