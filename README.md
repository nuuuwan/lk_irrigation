# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--12_07:18:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **122,832 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-12 07:18:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | -0.023 |  |
| 2026-04-12 07:18:23 | Peradeniya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.017 |  |
| 2026-04-12 07:15:28 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.008 |  |
| 2026-04-12 07:15:09 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.009 |  |
| 2026-04-12 07:14:52 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | -0.008 |  |
| 2026-04-12 07:14:25 | Rathnapura (Kalu Ganga) | 0.51 | 🟢 Normal | -0.008 |  |
| 2026-04-12 07:12:47 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-12 07:11:54 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.008 |  |
| 2026-04-12 07:08:40 | Magura (Kalu Ganga) | 1.19 | 🟢 Normal | -0.045 |  |
| 2026-04-12 07:08:38 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | -0.010 |  |
| 2026-04-12 07:08:08 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-04-12 07:07:48 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | -0.009 |  |
| 2026-04-12 07:06:58 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-04-12 07:06:37 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-12 07:05:54 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.448 | 🔺 Rising |
| 2026-04-12 07:05:53 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | -0.056 |  |
| 2026-04-12 07:05:28 | Nawalapitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-12 07:04:22 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-12 07:04:13 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-04-12 07:04:05 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-12 07:04:00 | Thanamalwila (Kirindi Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-12 07:03:59 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-12 07:03:39 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | -0.094 |  |
| 2026-04-12 07:03:29 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-04-12 07:02:47 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-12 07:02:44 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-12 07:02:38 | Weraganthota (Mahaweli Ganga) | -2.50 | 🟢 Normal | 0.276 | 🔺 Rising |
| 2026-04-12 07:02:34 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 07:02:24 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-12 07:01:56 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-12 07:01:47 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-12 07:01:41 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-12 07:01:40 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-12 07:01:23 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 07:01:15 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.020 |  |
| 2026-04-12 07:01:07 | Ellagawa (Kalu Ganga) | 3.83 | 🟢 Normal | -0.031 |  |
| 2026-04-12 07:00:43 | Horowpothana (Yan Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-12 07:00:16 | Thalgahagoda (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-04-12 06:38:14 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-12 07:05:54 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.448 | 🔺 Rising |
| 2026-04-12 07:02:38 | Weraganthota (Mahaweli Ganga) | -2.50 | 🟢 Normal | 0.276 | 🔺 Rising |
| 2026-04-12 07:00:16 | Thalgahagoda (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-04-12 07:06:58 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-04-12 07:03:59 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-12 07:02:44 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-12 07:01:23 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 07:02:34 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 07:01:40 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-12 07:01:47 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-12 07:01:56 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-12 07:05:28 | Nawalapitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-12 07:01:41 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-12 07:04:05 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-12 07:00:43 | Horowpothana (Yan Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-12 07:12:47 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-12 07:02:47 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-12 07:06:37 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-12 07:02:24 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-12 07:04:13 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-04-12 07:04:22 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-12 07:08:08 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-04-12 07:04:00 | Thanamalwila (Kirindi Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-12 07:15:28 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.008 |  |
| 2026-04-12 07:14:25 | Rathnapura (Kalu Ganga) | 0.51 | 🟢 Normal | -0.008 |  |
| 2026-04-12 07:14:52 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | -0.008 |  |
| 2026-04-12 07:11:54 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.008 |  |
| 2026-04-12 07:15:09 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.009 |  |
| 2026-04-12 07:07:48 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | -0.009 |  |
| 2026-04-12 07:08:38 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | -0.010 |  |
| 2026-04-11 18:00:38 | Thanthirimale (Malwathu Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-04-12 07:18:23 | Peradeniya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.017 |  |
| 2026-04-12 07:01:15 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.020 |  |
| 2026-04-12 06:05:15 | Baddegama (Gin Ganga) | 0.86 | 🟢 Normal | -0.021 |  |
| 2026-04-12 07:18:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | -0.023 |  |
| 2026-04-12 07:01:07 | Ellagawa (Kalu Ganga) | 3.83 | 🟢 Normal | -0.031 |  |
| 2026-04-12 07:08:40 | Magura (Kalu Ganga) | 1.19 | 🟢 Normal | -0.045 |  |
| 2026-04-12 07:05:53 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | -0.056 |  |
| 2026-04-12 07:03:39 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | -0.094 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)