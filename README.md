# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--01_19:21:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **61,805 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-01 19:21:19 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.008 |  |
| 2026-02-01 19:10:46 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-01 19:08:48 | Panadugama (Nilwala Ganga) | 2.56 | 🟢 Normal | -0.019 |  |
| 2026-02-01 19:08:47 | Putupaula (Kalu Ganga) | 0.46 | 🟢 Normal | -0.045 |  |
| 2026-02-01 19:08:35 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-02-01 19:07:53 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-02-01 19:07:49 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-02-01 19:07:17 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | -0.071 |  |
| 2026-02-01 19:06:58 | Thalgahagoda (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-02-01 19:06:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.48 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-02-01 19:05:23 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-01 19:05:01 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.063 |  |
| 2026-02-01 19:04:54 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-01 19:04:37 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-01 19:04:23 | Ellagawa (Kalu Ganga) | 4.36 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-01 19:03:59 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-02-01 19:03:53 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-01 19:03:42 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-01 19:03:30 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-01 19:03:28 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-01 19:03:24 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-01 19:03:18 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-01 19:03:12 | Peradeniya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-01 19:03:09 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-01 19:03:00 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-01 19:02:44 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-01 19:02:38 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-01 19:02:25 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-01 19:02:10 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.349 | 🔺 Rising |
| 2026-02-01 19:02:00 | Yaka Wewa (Ma Oya) | 1.03 | 🟢 Normal | -0.034 |  |
| 2026-02-01 19:01:44 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-01 19:01:35 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-01 19:01:32 | Manampitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-02-01 19:01:26 | Nawalapitiya (Mahaweli Ganga) | 0.06 | 🟢 Normal | -0.573 |  |
| 2026-02-01 19:00:23 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-02-01 19:00:06 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-01 19:02:10 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.349 | 🔺 Rising |
| 2026-02-01 19:08:35 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-02-01 18:00:43 | Thanthirimale (Malwathu Oya) | 2.31 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-02-01 19:03:09 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-01 19:06:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.48 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-02-01 19:06:58 | Thalgahagoda (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-02-01 19:03:30 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-01 19:00:23 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-02-01 19:04:23 | Ellagawa (Kalu Ganga) | 4.36 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-01 19:03:12 | Peradeniya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-01 19:03:18 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-01 19:02:44 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-01 19:00:06 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-01 19:10:46 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-01 19:01:44 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-01 19:03:42 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-01 19:02:38 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-01 19:05:23 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-01 19:03:00 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-01 19:01:35 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-01 19:02:25 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-01 19:03:53 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-01 19:07:49 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-02-01 19:04:54 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-01 18:06:16 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-01 19:03:24 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-01 19:21:19 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.008 |  |
| 2026-02-01 19:03:59 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-02-01 19:07:53 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-02-01 19:01:32 | Manampitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-02-01 18:02:53 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-02-01 19:08:48 | Panadugama (Nilwala Ganga) | 2.56 | 🟢 Normal | -0.019 |  |
| 2026-02-01 18:02:51 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.030 |  |
| 2026-02-01 19:02:00 | Yaka Wewa (Ma Oya) | 1.03 | 🟢 Normal | -0.034 |  |
| 2026-02-01 19:08:47 | Putupaula (Kalu Ganga) | 0.46 | 🟢 Normal | -0.045 |  |
| 2026-02-01 18:01:47 | Weraganthota (Mahaweli Ganga) | -2.15 | 🟢 Normal | -0.050 |  |
| 2026-02-01 19:05:01 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.063 |  |
| 2026-02-01 19:07:17 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | -0.071 |  |
| 2026-02-01 19:01:26 | Nawalapitiya (Mahaweli Ganga) | 0.06 | 🟢 Normal | -0.573 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)