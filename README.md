# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--27_09:24:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **136,298 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-27 09:24:17 | Panadugama (Nilwala Ganga) | 2.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 09:16:51 | Ellagawa (Kalu Ganga) | 4.48 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-04-27 09:10:15 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-04-27 09:09:10 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-27 09:08:37 | Rathnapura (Kalu Ganga) | 1.82 | 🟢 Normal | -0.063 |  |
| 2026-04-27 09:08:19 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | -0.019 |  |
| 2026-04-27 09:06:52 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-04-27 09:06:38 | Kithulgala (Kelani Ganga) | 1.06 | 🟢 Normal | -0.045 |  |
| 2026-04-27 09:06:28 | Glencourse (Kelani Ganga) | 8.84 | 🟢 Normal | -0.058 |  |
| 2026-04-27 09:05:23 | Padiyathalawa (Maduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-27 09:05:15 | Giriulla (Maha Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-04-27 09:04:33 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | -1.054 |  |
| 2026-04-27 09:04:10 | Baddegama (Gin Ganga) | 1.75 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-27 09:04:00 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.029 |  |
| 2026-04-27 09:03:15 | Hanwella (Kelani Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-04-27 09:03:14 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | -0.030 |  |
| 2026-04-27 09:03:08 | Katharagama (Menik Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-27 09:03:08 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-04-27 09:03:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.88 | 🟢 Normal | -0.010 |  |
| 2026-04-27 09:02:53 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.020 |  |
| 2026-04-27 09:02:50 | Badalgama (Maha Oya) | 2.19 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-27 09:02:40 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-04-27 09:02:34 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | -0.128 |  |
| 2026-04-27 09:02:31 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.068 |  |
| 2026-04-27 09:02:25 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-04-27 09:02:21 | Thanamalwila (Kirindi Oya) | 0.61 | 🟢 Normal | -0.030 |  |
| 2026-04-27 09:02:20 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-27 09:02:16 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.039 |  |
| 2026-04-27 09:02:14 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-27 09:01:54 | Peradeniya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-04-27 09:01:32 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-27 09:01:32 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | -0.020 |  |
| 2026-04-27 09:01:23 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-04-27 09:01:08 | Moraketiya (Walawe Ganga) | 1.08 | 🟢 Normal | -1.054 |  |
| 2026-04-27 09:01:04 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-27 09:00:33 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-27 09:00:20 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-27 09:00:17 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-27 09:00:17 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.107 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-27 09:00:17 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-04-27 09:16:51 | Ellagawa (Kalu Ganga) | 4.48 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-04-27 09:02:50 | Badalgama (Maha Oya) | 2.19 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-27 09:03:08 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-04-27 09:01:04 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-27 09:04:10 | Baddegama (Gin Ganga) | 1.75 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-27 09:24:17 | Panadugama (Nilwala Ganga) | 2.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 09:00:17 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-27 09:00:33 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-27 09:02:14 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-27 09:01:32 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-27 09:05:15 | Giriulla (Maha Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-04-27 09:05:23 | Padiyathalawa (Maduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-27 09:00:20 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-27 09:02:20 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-27 09:03:08 | Katharagama (Menik Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-27 09:10:15 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-04-27 09:01:54 | Peradeniya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-04-27 09:09:10 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-27 08:09:47 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-27 09:06:52 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-04-27 09:03:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.88 | 🟢 Normal | -0.010 |  |
| 2026-04-27 09:02:40 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-04-27 09:03:15 | Hanwella (Kelani Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-04-27 09:02:25 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-04-27 09:01:23 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-04-27 09:08:19 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | -0.019 |  |
| 2026-04-27 09:02:53 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.020 |  |
| 2026-04-27 09:01:32 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | -0.020 |  |
| 2026-04-27 09:04:00 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.029 |  |
| 2026-04-27 09:02:21 | Thanamalwila (Kirindi Oya) | 0.61 | 🟢 Normal | -0.030 |  |
| 2026-04-27 09:03:14 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | -0.030 |  |
| 2026-04-27 09:02:16 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.039 |  |
| 2026-04-27 09:06:38 | Kithulgala (Kelani Ganga) | 1.06 | 🟢 Normal | -0.045 |  |
| 2026-04-27 09:06:28 | Glencourse (Kelani Ganga) | 8.84 | 🟢 Normal | -0.058 |  |
| 2026-04-27 09:08:37 | Rathnapura (Kalu Ganga) | 1.82 | 🟢 Normal | -0.063 |  |
| 2026-04-27 09:02:31 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.068 |  |
| 2026-04-27 09:02:34 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | -0.128 |  |
| 2026-04-27 09:04:33 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | -1.054 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)