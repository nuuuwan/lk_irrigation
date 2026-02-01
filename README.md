# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--01_08:06:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **61,368 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **46** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-01 08:06:49 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-01 08:06:48 | Rathnapura (Kalu Ganga) | 1.01 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-01 08:06:29 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-01 08:05:52 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-02-01 08:05:39 | Pitabeddara (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-02-01 08:05:08 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.102 |  |
| 2026-02-01 08:05:05 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | -0.071 |  |
| 2026-02-01 08:04:48 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.062 |  |
| 2026-02-01 08:04:38 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-01 08:04:27 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 08:04:21 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-02-01 08:03:56 | Dunamale (Aththanagalu Oya) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-02-01 08:03:45 | Padiyathalawa (Maduru Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-01 08:03:38 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-02-01 08:03:37 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-02-01 08:03:36 | Horowpothana (Yan Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-02-01 08:03:22 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.058 |  |
| 2026-02-01 08:03:11 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2026-02-01 08:03:11 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-01 08:03:10 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.051 |  |
| 2026-02-01 08:03:03 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-01 08:02:52 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.022 |  |
| 2026-02-01 08:02:50 | Thanthirimale (Malwathu Oya) | 1.86 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-01 08:02:26 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-01 08:02:22 | Weraganthota (Mahaweli Ganga) | -1.76 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-02-01 08:02:20 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | -0.115 |  |
| 2026-02-01 08:02:15 | Ellagawa (Kalu Ganga) | 4.24 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-01 08:02:06 | Thanamalwila (Kirindi Oya) | 0.54 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-01 08:01:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | -0.061 |  |
| 2026-02-01 08:01:46 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-01 08:01:29 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-02-01 08:01:11 | Manampitiya (Mahaweli Ganga) | 1.49 | 🟢 Normal | -0.060 |  |
| 2026-02-01 08:01:07 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-01 08:00:52 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-01 07:39:51 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | -0.071 |  |
| 2026-02-01 07:30:40 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | -0.071 |  |
| 2026-02-01 07:22:49 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2026-02-01 07:20:52 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-01 07:17:09 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-01 07:16:10 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.051 |  |
| 2026-02-01 07:13:02 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.051 |  |
| 2026-02-01 07:12:39 | Panadugama (Nilwala Ganga) | 2.18 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-01 07:11:39 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-02-01 07:11:21 | Magura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-02-01 07:11:06 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.102 |  |
| 2026-02-01 07:10:06 | Padiyathalawa (Maduru Oya) | 0.69 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-01 08:03:11 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2026-02-01 08:02:22 | Weraganthota (Mahaweli Ganga) | -1.76 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-02-01 08:05:39 | Pitabeddara (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-02-01 08:05:52 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-02-01 08:03:37 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-02-01 08:03:38 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-02-01 08:06:29 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-01 07:12:39 | Panadugama (Nilwala Ganga) | 2.18 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-01 08:06:48 | Rathnapura (Kalu Ganga) | 1.01 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-01 08:02:50 | Thanthirimale (Malwathu Oya) | 1.86 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-01 08:02:15 | Ellagawa (Kalu Ganga) | 4.24 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-01 08:02:06 | Thanamalwila (Kirindi Oya) | 0.54 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-01 08:04:27 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 08:01:29 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-02-01 08:01:46 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-01 08:03:11 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-01 08:06:49 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-01 08:00:52 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-01 08:03:36 | Horowpothana (Yan Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-02-01 07:02:31 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-01 07:11:39 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-02-01 08:03:45 | Padiyathalawa (Maduru Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-01 08:03:03 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-01 08:01:07 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-01 07:02:35 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-01 08:04:38 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-01 07:20:52 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-01 08:02:26 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-01 08:03:56 | Dunamale (Aththanagalu Oya) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-02-01 08:04:21 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-02-01 08:02:52 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.022 |  |
| 2026-02-01 08:03:10 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.051 |  |
| 2026-02-01 08:03:22 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.058 |  |
| 2026-02-01 08:01:11 | Manampitiya (Mahaweli Ganga) | 1.49 | 🟢 Normal | -0.060 |  |
| 2026-02-01 08:01:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | -0.061 |  |
| 2026-02-01 08:04:48 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.062 |  |
| 2026-02-01 08:05:05 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | -0.071 |  |
| 2026-02-01 08:05:08 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.102 |  |
| 2026-02-01 08:02:20 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | -0.115 |  |

## River Water Level Charts by Station

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)