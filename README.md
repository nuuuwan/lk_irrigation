# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--29_21:11:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **219,731 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-29 21:11:37 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-07-29 21:09:13 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-07-29 21:08:07 | Glencourse (Kelani Ganga) | 8.90 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-07-29 21:07:34 | Rathnapura (Kalu Ganga) | 1.35 | 🟢 Normal | -0.052 |  |
| 2026-07-29 21:06:45 | Putupaula (Kalu Ganga) | 0.46 | 🟢 Normal | -0.085 |  |
| 2026-07-29 21:05:35 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.028 |  |
| 2026-07-29 21:05:28 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-29 21:05:26 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-29 21:05:16 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-07-29 21:04:42 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.315 | 🔺 Rising |
| 2026-07-29 21:04:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.14 | 🟢 Normal | -0.047 |  |
| 2026-07-29 21:04:13 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-29 21:04:05 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-29 21:03:56 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-29 21:03:49 | Hanwella (Kelani Ganga) | 0.73 | 🟢 Normal | -0.030 |  |
| 2026-07-29 21:03:36 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-29 21:03:09 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-29 21:03:03 | Baddegama (Gin Ganga) | 1.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-29 21:02:55 | Kithulgala (Kelani Ganga) | 1.77 | 🟢 Normal | -0.029 |  |
| 2026-07-29 21:02:45 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-07-29 21:02:37 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-29 21:02:36 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-29 21:02:27 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-29 21:02:19 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-29 21:02:10 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | -0.012 |  |
| 2026-07-29 21:01:55 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-29 21:01:47 | Ellagawa (Kalu Ganga) | 4.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-29 21:01:46 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-07-29 21:01:40 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-07-29 21:01:27 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-29 21:01:23 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-29 21:01:19 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-07-29 21:00:59 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-29 21:00:39 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.041 |  |
| 2026-07-29 21:00:39 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-29 20:28:03 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-07-29 20:25:42 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-29 21:04:42 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.315 | 🔺 Rising |
| 2026-07-29 21:05:16 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-07-29 21:09:13 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-07-29 21:08:07 | Glencourse (Kelani Ganga) | 8.90 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-07-29 21:00:39 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-29 21:01:19 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-07-29 21:01:27 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-29 21:03:03 | Baddegama (Gin Ganga) | 1.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-29 21:01:47 | Ellagawa (Kalu Ganga) | 4.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-29 21:01:55 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-29 21:01:23 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-29 21:04:13 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-29 21:03:36 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-29 21:00:59 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-29 18:01:46 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-29 19:05:38 | Magura (Kalu Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-07-29 21:02:36 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-29 21:02:37 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-29 21:04:05 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-29 21:03:09 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-29 21:02:19 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-29 21:05:28 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-29 21:02:27 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-29 21:11:37 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-07-29 21:03:56 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-29 21:05:26 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-29 18:01:01 | Thanthirimale (Malwathu Oya) | 0.84 | 🟢 Normal | -0.005 |  |
| 2026-07-29 21:02:45 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-07-29 21:01:40 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-07-29 21:01:46 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-07-29 21:02:10 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | -0.012 |  |
| 2026-07-29 21:05:35 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.028 |  |
| 2026-07-29 21:02:55 | Kithulgala (Kelani Ganga) | 1.77 | 🟢 Normal | -0.029 |  |
| 2026-07-29 21:03:49 | Hanwella (Kelani Ganga) | 0.73 | 🟢 Normal | -0.030 |  |
| 2026-07-29 18:00:16 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | -0.034 |  |
| 2026-07-29 21:00:39 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.041 |  |
| 2026-07-29 21:04:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.14 | 🟢 Normal | -0.047 |  |
| 2026-07-29 21:07:34 | Rathnapura (Kalu Ganga) | 1.35 | 🟢 Normal | -0.052 |  |
| 2026-07-29 21:06:45 | Putupaula (Kalu Ganga) | 0.46 | 🟢 Normal | -0.085 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)