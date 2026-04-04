# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--04_08:05:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **115,748 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-04 08:05:49 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-04 08:05:39 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | -0.020 |  |
| 2026-04-04 08:05:36 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-04 08:05:32 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-04-04 08:05:27 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | -0.029 |  |
| 2026-04-04 08:04:52 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-04-04 08:04:40 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.151 |  |
| 2026-04-04 08:04:15 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-04 08:03:59 | Baddegama (Gin Ganga) | 1.59 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-04-04 08:03:50 | Manampitiya (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-04-04 08:03:31 | Glencourse (Kelani Ganga) | 8.74 | 🟢 Normal | 0.000 |  |
| 2026-04-04 08:03:02 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-04 08:02:52 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | 0.000 |  |
| 2026-04-04 08:02:50 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-04-04 08:02:15 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-04 08:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-04-04 08:02:10 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-04 08:02:10 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.147 |  |
| 2026-04-04 08:02:03 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-04-04 08:01:43 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-04-04 08:01:27 | Nawalapitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-04-04 08:01:20 | Thanthirimale (Malwathu Oya) | 2.51 | 🟢 Normal | -0.020 |  |
| 2026-04-04 08:01:12 | Thanamalwila (Kirindi Oya) | 0.26 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-04 08:01:08 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.092 |  |
| 2026-04-04 08:01:04 | Weraganthota (Mahaweli Ganga) | -1.82 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-04-04 08:00:59 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-04 08:00:54 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-04-04 08:00:18 | Padiyathalawa (Maduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-04 07:27:18 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-04 07:18:05 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.024 |  |
| 2026-04-04 07:18:00 | Horowpothana (Yan Oya) | 1.74 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-04-04 07:17:49 | Rathnapura (Kalu Ganga) | 0.86 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-04-04 07:15:01 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-04 07:14:50 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.017 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-04 08:01:04 | Weraganthota (Mahaweli Ganga) | -1.82 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-04-04 08:02:50 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-04-04 08:03:59 | Baddegama (Gin Ganga) | 1.59 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-04-04 07:02:15 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-04-04 08:04:15 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-04 08:03:50 | Manampitiya (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-04-04 08:01:12 | Thanamalwila (Kirindi Oya) | 0.26 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-04 08:02:10 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-04 08:03:02 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-04 07:17:49 | Rathnapura (Kalu Ganga) | 0.86 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-04-04 07:18:00 | Horowpothana (Yan Oya) | 1.74 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-04-04 08:02:15 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-04 08:05:36 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-04 08:01:27 | Nawalapitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-04-04 07:04:00 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-04-04 08:02:52 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | 0.000 |  |
| 2026-04-04 08:00:18 | Padiyathalawa (Maduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-04 08:03:31 | Glencourse (Kelani Ganga) | 8.74 | 🟢 Normal | 0.000 |  |
| 2026-04-04 08:00:59 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-04 07:02:08 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-04 08:05:49 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-04 08:04:52 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-04-04 08:05:32 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-04-04 07:15:01 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-04 08:02:03 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-04-04 08:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-04-04 08:00:54 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-04-04 08:01:43 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-04-04 07:04:42 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-04-04 07:14:50 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.017 |  |
| 2026-04-04 08:05:39 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | -0.020 |  |
| 2026-04-04 07:09:43 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | -0.020 |  |
| 2026-04-04 08:01:20 | Thanthirimale (Malwathu Oya) | 2.51 | 🟢 Normal | -0.020 |  |
| 2026-04-04 07:18:05 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.024 |  |
| 2026-04-04 08:05:27 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | -0.029 |  |
| 2026-04-04 08:01:08 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.092 |  |
| 2026-04-04 08:02:10 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.147 |  |
| 2026-04-04 08:04:40 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.151 |  |
| 2026-04-04 07:11:12 | Magura (Kalu Ganga) | 2.31 | 🟢 Normal | -0.235 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)