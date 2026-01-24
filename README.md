# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--24_20:16:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **54,646 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-24 20:16:41 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-24 20:13:55 | Peradeniya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-01-24 20:10:35 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-01-24 20:09:11 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-01-24 20:08:24 | Rathnapura (Kalu Ganga) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-24 20:08:13 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | -0.009 |  |
| 2026-01-24 20:07:52 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | -0.107 |  |
| 2026-01-24 20:07:32 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-24 20:06:31 | Ellagawa (Kalu Ganga) | 3.81 | 🟢 Normal | -0.011 |  |
| 2026-01-24 20:06:06 | Glencourse (Kelani Ganga) | 8.34 | 🟢 Normal | -0.028 |  |
| 2026-01-24 20:05:41 | Dunamale (Aththanagalu Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-01-24 20:05:15 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-24 20:04:40 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-24 20:04:36 | Padiyathalawa (Maduru Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-01-24 20:04:13 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-24 20:03:57 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.268 | 🔺 Rising |
| 2026-01-24 20:03:53 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-01-24 20:03:34 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-24 20:03:30 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-24 20:03:05 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.020 |  |
| 2026-01-24 20:02:59 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-24 20:02:58 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-24 20:02:58 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-24 20:02:36 | Manampitiya (Mahaweli Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-01-24 20:02:32 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-24 20:02:20 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | -0.011 |  |
| 2026-01-24 20:02:16 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-24 20:02:16 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-01-24 20:01:51 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-24 20:01:38 | Horowpothana (Yan Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-01-24 20:01:10 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-24 20:01:07 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-24 20:00:59 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-24 20:00:50 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.061 |  |
| 2026-01-24 20:00:45 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-24 19:26:05 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-24 19:26:04 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-24 20:03:57 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.268 | 🔺 Rising |
| 2026-01-24 20:13:55 | Peradeniya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-01-24 20:10:35 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-01-24 20:01:07 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-24 20:05:15 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-24 20:08:24 | Rathnapura (Kalu Ganga) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-24 20:01:10 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-24 20:02:32 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-24 20:16:41 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-24 20:02:59 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-24 20:01:38 | Horowpothana (Yan Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-01-24 18:03:22 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-01-24 20:02:16 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-24 20:03:53 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-01-24 20:03:34 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-24 20:02:16 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-01-24 20:09:11 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-01-24 20:02:58 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-24 20:03:30 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-24 20:00:45 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-24 20:04:13 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-24 20:07:32 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-24 20:02:58 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-24 19:26:05 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-24 20:01:51 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-24 20:04:40 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-24 19:08:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-01-24 20:08:13 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | -0.009 |  |
| 2026-01-24 18:01:40 | Thanthirimale (Malwathu Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-01-24 20:04:36 | Padiyathalawa (Maduru Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-01-24 20:02:36 | Manampitiya (Mahaweli Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-01-24 20:05:41 | Dunamale (Aththanagalu Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-01-24 20:02:20 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | -0.011 |  |
| 2026-01-24 20:06:31 | Ellagawa (Kalu Ganga) | 3.81 | 🟢 Normal | -0.011 |  |
| 2026-01-24 20:03:05 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.020 |  |
| 2026-01-24 18:00:14 | Weraganthota (Mahaweli Ganga) | -2.33 | 🟢 Normal | -0.020 |  |
| 2026-01-24 20:06:06 | Glencourse (Kelani Ganga) | 8.34 | 🟢 Normal | -0.028 |  |
| 2026-01-24 20:00:50 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.061 |  |
| 2026-01-24 20:07:52 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | -0.107 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)