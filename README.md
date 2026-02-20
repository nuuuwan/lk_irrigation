# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--20_17:24:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **78,345 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-20 17:24:53 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-02-20 17:23:50 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-02-20 17:14:24 | Magura (Kalu Ganga) | 1.26 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-02-20 17:13:33 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-20 17:13:06 | Rathnapura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-02-20 17:12:26 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-02-20 17:08:02 | Glencourse (Kelani Ganga) | 8.38 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-02-20 17:06:47 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-02-20 17:06:06 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-20 17:05:30 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-20 17:05:23 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-20 17:05:20 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-20 17:04:45 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-20 17:04:25 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-02-20 17:04:21 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-20 17:04:18 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-02-20 17:04:18 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-20 17:03:53 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.119 |  |
| 2026-02-20 17:03:49 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.030 |  |
| 2026-02-20 17:03:40 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-20 17:03:23 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-02-20 17:03:22 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2026-02-20 17:03:03 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-20 17:03:01 | Weraganthota (Mahaweli Ganga) | -1.27 | 🟢 Normal | -0.068 |  |
| 2026-02-20 17:02:54 | Dunamale (Aththanagalu Oya) | 0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-20 17:02:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.12 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-20 17:02:50 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | -0.052 |  |
| 2026-02-20 17:02:38 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.032 |  |
| 2026-02-20 17:02:33 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-02-20 17:02:32 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.228 | 🔺 Rising |
| 2026-02-20 17:02:22 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-20 17:02:15 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | -0.011 |  |
| 2026-02-20 17:01:50 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.013 |  |
| 2026-02-20 17:01:45 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-20 17:01:35 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-20 17:01:33 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-02-20 17:01:28 | Thanamalwila (Kirindi Oya) | 0.60 | 🟢 Normal | -0.020 |  |
| 2026-02-20 17:01:14 | Padiyathalawa (Maduru Oya) | 1.88 | 🟢 Normal | -0.052 |  |
| 2026-02-20 17:00:47 | Siyambalanduwa (Heda Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-20 17:00:36 | Manampitiya (Mahaweli Ganga) | 2.98 | 🟢 Normal | 0.181 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-20 17:02:32 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.228 | 🔺 Rising |
| 2026-02-20 17:03:22 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2026-02-20 17:00:36 | Manampitiya (Mahaweli Ganga) | 2.98 | 🟢 Normal | 0.181 | 🔺 Rising |
| 2026-02-20 17:03:23 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-02-20 17:23:50 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-02-20 17:08:02 | Glencourse (Kelani Ganga) | 8.38 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-02-20 17:02:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.12 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-20 17:14:24 | Magura (Kalu Ganga) | 1.26 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-02-20 17:03:03 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-20 17:02:54 | Dunamale (Aththanagalu Oya) | 0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-20 17:13:06 | Rathnapura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-02-20 17:01:33 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-02-20 17:06:06 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-20 17:05:20 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-20 17:04:18 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-20 17:13:33 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-20 17:02:22 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-20 17:01:45 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-20 17:05:30 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-20 17:24:53 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-02-20 17:00:47 | Siyambalanduwa (Heda Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-20 17:04:21 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-20 17:04:25 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-02-20 17:05:23 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-20 17:03:40 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-20 17:12:26 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-02-20 17:04:45 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-20 17:06:47 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-02-20 17:04:18 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-02-20 17:02:33 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-02-20 17:02:15 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | -0.011 |  |
| 2026-02-20 17:01:50 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.013 |  |
| 2026-02-20 17:01:28 | Thanamalwila (Kirindi Oya) | 0.60 | 🟢 Normal | -0.020 |  |
| 2026-02-20 17:03:49 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.030 |  |
| 2026-02-20 17:02:38 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.032 |  |
| 2026-02-20 17:02:50 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | -0.052 |  |
| 2026-02-20 17:01:14 | Padiyathalawa (Maduru Oya) | 1.88 | 🟢 Normal | -0.052 |  |
| 2026-02-20 17:03:01 | Weraganthota (Mahaweli Ganga) | -1.27 | 🟢 Normal | -0.068 |  |
| 2026-02-20 17:03:53 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.119 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)