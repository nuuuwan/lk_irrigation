# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--29_06:20:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **219,145 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-29 06:20:34 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-07-29 06:17:51 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-07-29 06:10:18 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-29 06:10:14 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-29 06:07:45 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | -0.019 |  |
| 2026-07-29 06:07:37 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | -0.011 |  |
| 2026-07-29 06:06:49 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-07-29 06:06:40 | Peradeniya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.099 |  |
| 2026-07-29 06:06:14 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-29 06:05:51 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.105 |  |
| 2026-07-29 06:05:39 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-07-29 06:05:29 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-29 06:05:25 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-29 06:05:13 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-07-29 06:04:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-07-29 06:04:40 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-07-29 06:04:33 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-29 06:04:31 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-29 06:04:29 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-29 06:04:23 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-29 06:04:21 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-07-29 06:04:20 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-07-29 06:04:05 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-29 06:03:35 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-29 06:03:20 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-29 06:02:53 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.062 |  |
| 2026-07-29 06:02:45 | Hanwella (Kelani Ganga) | 0.55 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-07-29 06:02:38 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-29 06:02:34 | Manampitiya (Mahaweli Ganga) | -0.23 | 🟢 Normal | -0.010 |  |
| 2026-07-29 06:02:33 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-29 06:02:27 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-29 06:02:23 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-29 06:01:51 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-29 06:01:24 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-29 06:01:19 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-29 06:01:01 | Rathnapura (Kalu Ganga) | 0.92 | 🟢 Normal | -0.012 |  |
| 2026-07-29 06:00:18 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.001 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-29 06:04:20 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-07-29 06:04:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-07-29 06:05:13 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-07-29 06:02:45 | Hanwella (Kelani Ganga) | 0.55 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-07-29 06:05:39 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-07-29 06:05:25 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-29 06:04:23 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-29 06:04:29 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-29 06:01:51 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-29 06:06:14 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-29 06:03:20 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-29 06:00:18 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.001 |  |
| 2026-07-29 06:02:33 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-29 06:10:18 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-29 06:03:35 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-29 06:01:24 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-29 06:06:49 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-07-28 18:03:13 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-29 06:20:34 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-07-29 06:02:23 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-29 06:04:33 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-29 06:02:38 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-29 05:03:56 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-07-29 06:05:29 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-29 06:10:14 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-29 06:04:40 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-07-28 18:00:50 | Thanthirimale (Malwathu Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-07-29 06:04:05 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-29 06:01:19 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-29 06:02:27 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-29 06:02:34 | Manampitiya (Mahaweli Ganga) | -0.23 | 🟢 Normal | -0.010 |  |
| 2026-07-29 06:04:21 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-07-29 06:07:37 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | -0.011 |  |
| 2026-07-29 06:01:01 | Rathnapura (Kalu Ganga) | 0.92 | 🟢 Normal | -0.012 |  |
| 2026-07-29 06:07:45 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | -0.019 |  |
| 2026-07-29 05:11:29 | Glencourse (Kelani Ganga) | 9.10 | 🟢 Normal | -0.027 |  |
| 2026-07-29 06:02:53 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.062 |  |
| 2026-07-29 06:06:40 | Peradeniya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.099 |  |
| 2026-07-29 06:05:51 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.105 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)