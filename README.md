# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--16_00:09:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **46,677 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-16 00:09:23 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-01-16 00:09:14 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-16 00:08:34 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-01-16 00:08:08 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-16 00:08:03 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-16 00:07:28 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-16 00:07:23 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-16 00:06:56 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-01-16 00:05:50 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-01-16 00:05:13 | Siyambalanduwa (Heda Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-16 00:04:48 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.012 |  |
| 2026-01-16 00:04:10 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-01-16 00:03:51 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-01-16 00:03:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-01-16 00:03:44 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-16 00:03:28 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | -1.714 |  |
| 2026-01-16 00:03:25 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.061 |  |
| 2026-01-16 00:03:16 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-01-16 00:03:09 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-16 00:03:07 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | -1.714 |  |
| 2026-01-16 00:03:07 | Putupaula (Kalu Ganga) | 0.69 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-16 00:03:03 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-16 00:02:50 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-16 00:02:49 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.020 |  |
| 2026-01-16 00:02:39 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-01-16 00:02:20 | Magura (Kalu Ganga) | 1.15 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-01-16 00:01:55 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-16 00:01:44 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-16 00:01:18 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-16 00:01:14 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-16 00:01:14 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-16 00:01:09 | Manampitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.020 |  |
| 2026-01-16 00:01:00 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-15 23:26:07 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-01-15 23:23:22 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-01-15 23:19:04 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-16 00:03:51 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-01-16 00:03:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-01-16 00:02:20 | Magura (Kalu Ganga) | 1.15 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-01-16 00:02:39 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-01-16 00:08:34 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-01-16 00:03:07 | Putupaula (Kalu Ganga) | 0.69 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-16 00:03:09 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-16 00:08:08 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-16 00:03:03 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-16 00:01:00 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-16 00:01:14 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-16 00:02:50 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-16 00:01:55 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-15 18:03:50 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-16 00:01:44 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-16 00:07:23 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-16 00:06:56 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-01-16 00:03:44 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-16 00:07:28 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-16 00:05:13 | Siyambalanduwa (Heda Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-15 23:06:05 | Dunamale (Aththanagalu Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-16 00:01:14 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-16 00:09:23 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-01-16 00:05:50 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-01-16 00:09:14 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-15 23:23:22 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-01-16 00:01:18 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-16 00:08:03 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-16 00:03:16 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-01-16 00:04:10 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-01-15 23:00:53 | Horowpothana (Yan Oya) | 2.26 | 🟢 Normal | -0.010 |  |
| 2026-01-16 00:04:48 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.012 |  |
| 2026-01-15 22:05:48 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | -0.019 |  |
| 2026-01-16 00:02:49 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.020 |  |
| 2026-01-16 00:01:09 | Manampitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.020 |  |
| 2026-01-15 18:02:13 | Thanthirimale (Malwathu Oya) | 1.83 | 🟢 Normal | -0.040 |  |
| 2026-01-16 00:03:25 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.061 |  |
| 2026-01-15 18:07:05 | Weraganthota (Mahaweli Ganga) | -2.39 | 🟢 Normal | -0.400 |  |
| 2026-01-16 00:03:28 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | -1.714 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)