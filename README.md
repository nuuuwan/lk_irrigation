# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--04_10:23:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **115,837 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-04 10:23:55 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | -0.008 |  |
| 2026-04-04 10:18:05 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.078 |  |
| 2026-04-04 10:11:22 | Baddegama (Gin Ganga) | 1.64 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-04 10:11:00 | Padiyathalawa (Maduru Oya) | 0.40 | 🟢 Normal | -0.188 |  |
| 2026-04-04 10:10:46 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-04 10:08:01 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.011 |  |
| 2026-04-04 10:06:58 | Magura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.244 |  |
| 2026-04-04 10:06:56 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.009 |  |
| 2026-04-04 10:06:52 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | -0.040 |  |
| 2026-04-04 10:06:41 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | -0.029 |  |
| 2026-04-04 10:05:24 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | -0.040 |  |
| 2026-04-04 10:05:03 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-04-04 10:05:03 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 10:04:54 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-04 10:04:43 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-04 10:04:36 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-04 10:04:29 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-04 10:04:26 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | -0.010 |  |
| 2026-04-04 10:04:04 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-04 10:03:30 | Putupaula (Kalu Ganga) | 0.25 | 🟢 Normal | -0.030 |  |
| 2026-04-04 10:03:14 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | -0.030 |  |
| 2026-04-04 10:03:08 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 10:03:07 | Weraganthota (Mahaweli Ganga) | -1.84 | 🟢 Normal | -0.029 |  |
| 2026-04-04 10:02:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.20 | 🟢 Normal | -0.030 |  |
| 2026-04-04 10:02:36 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-04 10:02:26 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-04 10:02:17 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-04 10:02:16 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.144 |  |
| 2026-04-04 10:02:07 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-04-04 10:02:07 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-04 10:01:50 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-04 10:01:49 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.011 |  |
| 2026-04-04 10:01:47 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-04-04 10:01:21 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-04 10:01:12 | Thanamalwila (Kirindi Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-04 10:00:52 | Thanthirimale (Malwathu Oya) | 2.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-04 10:00:44 | Manampitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | -0.031 |  |
| 2026-04-04 10:00:23 | Nawalapitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-04 10:01:50 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-04 10:02:07 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-04 10:02:36 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-04 10:04:04 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-04 10:00:52 | Thanthirimale (Malwathu Oya) | 2.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-04 10:10:46 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-04 10:04:43 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-04 10:03:08 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 10:05:03 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 10:11:22 | Baddegama (Gin Ganga) | 1.64 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-04 10:04:29 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-04 10:01:47 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-04-04 10:02:17 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-04 10:01:21 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-04 10:04:54 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-04 09:01:32 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-04 10:02:26 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-04 10:04:36 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-04 10:01:12 | Thanamalwila (Kirindi Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-04 10:23:55 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | -0.008 |  |
| 2026-04-04 10:06:56 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.009 |  |
| 2026-04-04 10:05:03 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-04-04 10:02:07 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-04-04 10:00:23 | Nawalapitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-04-04 10:04:26 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | -0.010 |  |
| 2026-04-04 10:08:01 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.011 |  |
| 2026-04-04 10:01:49 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.011 |  |
| 2026-04-04 10:06:41 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | -0.029 |  |
| 2026-04-04 10:03:07 | Weraganthota (Mahaweli Ganga) | -1.84 | 🟢 Normal | -0.029 |  |
| 2026-04-04 10:03:14 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | -0.030 |  |
| 2026-04-04 10:03:30 | Putupaula (Kalu Ganga) | 0.25 | 🟢 Normal | -0.030 |  |
| 2026-04-04 10:02:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.20 | 🟢 Normal | -0.030 |  |
| 2026-04-04 10:00:44 | Manampitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | -0.031 |  |
| 2026-04-04 10:05:24 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | -0.040 |  |
| 2026-04-04 10:06:52 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | -0.040 |  |
| 2026-04-04 10:18:05 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.078 |  |
| 2026-04-04 10:02:16 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.144 |  |
| 2026-04-04 10:11:00 | Padiyathalawa (Maduru Oya) | 0.40 | 🟢 Normal | -0.188 |  |
| 2026-04-04 10:06:58 | Magura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.244 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)