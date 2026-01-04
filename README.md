# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--04_21:10:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **36,738 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-04 21:10:45 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-01-04 21:08:54 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.050 |  |
| 2026-01-04 21:08:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.48 | 🟢 Normal | -0.022 |  |
| 2026-01-04 21:07:31 | Peradeniya (Mahaweli Ganga) | 2.15 | 🟢 Normal | 0.464 | 🔺 Rising |
| 2026-01-04 21:07:23 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | -0.009 |  |
| 2026-01-04 21:07:20 | Magura (Kalu Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-04 21:07:16 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | -0.009 |  |
| 2026-01-04 21:06:26 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-04 21:06:23 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-04 21:05:53 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-04 21:05:50 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-04 21:05:37 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | -0.040 |  |
| 2026-01-04 21:05:33 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-04 21:05:07 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | -0.009 |  |
| 2026-01-04 21:04:46 | Panadugama (Nilwala Ganga) | 2.55 | 🟢 Normal | -0.021 |  |
| 2026-01-04 21:04:32 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-04 21:04:24 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-04 21:04:21 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-04 21:03:59 | Manampitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.019 |  |
| 2026-01-04 21:03:59 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-01-04 21:03:30 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-04 21:03:22 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-04 21:03:10 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-01-04 21:02:56 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-01-04 21:02:53 | Thawalama (Gin Ganga) | 1.57 | 🟢 Normal | -0.022 |  |
| 2026-01-04 21:02:29 | Horowpothana (Yan Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-01-04 21:02:24 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-04 21:02:23 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-04 21:02:23 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-04 21:02:17 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-01-04 21:02:08 | Katharagama (Menik Ganga) | 0.04 | 🟢 Normal | -0.010 |  |
| 2026-01-04 21:02:04 | Baddegama (Gin Ganga) | 1.48 | 🟢 Normal | -0.020 |  |
| 2026-01-04 21:01:46 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | -0.010 |  |
| 2026-01-04 21:01:40 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-04 21:01:21 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-01-04 20:20:46 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-04 21:07:31 | Peradeniya (Mahaweli Ganga) | 2.15 | 🟢 Normal | 0.464 | 🔺 Rising |
| 2026-01-04 21:02:56 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-01-04 21:03:22 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-04 18:04:42 | Weraganthota (Mahaweli Ganga) | -1.62 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-01-04 21:03:10 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-01-04 21:05:53 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-04 21:02:24 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-04 21:04:21 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-04 21:02:23 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-04 21:04:32 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-04 21:02:23 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-04 21:01:40 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-04 21:04:24 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-04 21:02:29 | Horowpothana (Yan Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-01-04 21:07:20 | Magura (Kalu Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-04 21:05:33 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-04 21:03:30 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-04 21:06:26 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-04 21:05:50 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-04 21:01:21 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-01-04 21:06:23 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-04 18:02:32 | Thanthirimale (Malwathu Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-01-04 20:03:35 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-04 21:03:59 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-01-04 21:07:16 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | -0.009 |  |
| 2026-01-04 21:07:23 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | -0.009 |  |
| 2026-01-04 21:05:07 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | -0.009 |  |
| 2026-01-04 21:02:17 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-01-04 21:01:46 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | -0.010 |  |
| 2026-01-04 21:02:08 | Katharagama (Menik Ganga) | 0.04 | 🟢 Normal | -0.010 |  |
| 2026-01-04 21:10:45 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-01-04 21:03:59 | Manampitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.019 |  |
| 2026-01-04 21:02:04 | Baddegama (Gin Ganga) | 1.48 | 🟢 Normal | -0.020 |  |
| 2026-01-04 21:04:46 | Panadugama (Nilwala Ganga) | 2.55 | 🟢 Normal | -0.021 |  |
| 2026-01-04 21:08:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.48 | 🟢 Normal | -0.022 |  |
| 2026-01-04 21:02:53 | Thawalama (Gin Ganga) | 1.57 | 🟢 Normal | -0.022 |  |
| 2026-01-04 21:05:37 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | -0.040 |  |
| 2026-01-04 18:15:36 | Galgamuwa (Mee Oya) | 2.40 | 🟢 Normal | -0.048 |  |
| 2026-01-04 21:08:54 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.050 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)