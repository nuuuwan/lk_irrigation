# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--22_15:08:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **80,081 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-22 15:08:28 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-02-22 15:07:16 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-22 15:07:07 | Magura (Kalu Ganga) | 2.85 | 🟢 Normal | -0.171 |  |
| 2026-02-22 15:06:56 | Thalgahagoda (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-02-22 15:06:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.12 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-02-22 15:06:24 | Horowpothana (Yan Oya) | 2.13 | 🟢 Normal | -0.018 |  |
| 2026-02-22 15:05:05 | Thanamalwila (Kirindi Oya) | 1.54 | 🟢 Normal | -0.039 |  |
| 2026-02-22 15:04:52 | Panadugama (Nilwala Ganga) | 4.00 | 🟢 Normal | 2.524 | 🔺 Rising |
| 2026-02-22 15:04:36 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | -0.040 |  |
| 2026-02-22 15:04:33 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | -0.010 |  |
| 2026-02-22 15:04:22 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-02-22 15:04:17 | Rathnapura (Kalu Ganga) | 3.25 | 🟢 Normal | -0.162 |  |
| 2026-02-22 15:04:16 | Putupaula (Kalu Ganga) | 1.53 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-02-22 15:04:14 | Glencourse (Kelani Ganga) | 9.80 | 🟢 Normal | -0.147 |  |
| 2026-02-22 15:04:14 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | -0.040 |  |
| 2026-02-22 15:04:13 | Badalgama (Maha Oya) | 3.00 | 🟢 Normal | -0.093 |  |
| 2026-02-22 15:04:12 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | -0.030 |  |
| 2026-02-22 15:03:37 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-22 15:03:20 | Nawalapitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.060 |  |
| 2026-02-22 15:03:16 | Hanwella (Kelani Ganga) | 2.21 | 🟢 Normal | -0.120 |  |
| 2026-02-22 15:03:02 | Moraketiya (Walawe Ganga) | 1.07 | 🟢 Normal | -0.038 |  |
| 2026-02-22 15:02:51 | Pitabeddara (Nilwala Ganga) | 1.03 | 🟢 Normal | -0.128 |  |
| 2026-02-22 15:02:30 | Ellagawa (Kalu Ganga) | 7.78 | 🟢 Normal | 0.000 |  |
| 2026-02-22 15:02:27 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.070 |  |
| 2026-02-22 15:02:27 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | -0.049 |  |
| 2026-02-22 15:02:03 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-02-22 15:01:57 | Giriulla (Maha Oya) | 1.55 | 🟢 Normal | -0.052 |  |
| 2026-02-22 15:01:40 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-22 15:01:39 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | -0.100 |  |
| 2026-02-22 15:01:33 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-22 15:01:29 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.101 |  |
| 2026-02-22 15:01:17 | Wellawaya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-02-22 15:01:17 | Siyambalanduwa (Heda Oya) | 0.77 | 🟢 Normal | -0.021 |  |
| 2026-02-22 15:01:16 | Baddegama (Gin Ganga) | 2.67 | 🟢 Normal | 0.000 |  |
| 2026-02-22 15:01:02 | Thaldena (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-02-22 15:00:46 | Manampitiya (Mahaweli Ganga) | 3.98 | 🟡 Alert | -0.070 |  |
| 2026-02-22 15:00:09 | Weraganthota (Mahaweli Ganga) | -1.36 | 🟢 Normal | -0.050 |  |
| 2026-02-22 15:00:09 | Padiyathalawa (Maduru Oya) | 1.30 | 🟢 Normal | -0.050 |  |
| 2026-02-22 15:00:09 | Nakkala (Kumbukkan Oya) | 1.35 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-22 15:06:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.12 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-02-22 15:00:46 | Manampitiya (Mahaweli Ganga) | 3.98 | 🟡 Alert | -0.070 |  |
| 2026-02-22 15:04:52 | Panadugama (Nilwala Ganga) | 4.00 | 🟢 Normal | 2.524 | 🔺 Rising |
| 2026-02-22 15:08:28 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-02-22 15:02:03 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-02-22 15:04:16 | Putupaula (Kalu Ganga) | 1.53 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-02-22 15:01:40 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-22 15:03:37 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-22 15:01:33 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-22 15:07:16 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-22 15:02:30 | Ellagawa (Kalu Ganga) | 7.78 | 🟢 Normal | 0.000 |  |
| 2026-02-22 15:01:16 | Baddegama (Gin Ganga) | 2.67 | 🟢 Normal | 0.000 |  |
| 2026-02-22 15:01:02 | Thaldena (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-02-22 15:06:56 | Thalgahagoda (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-02-22 15:04:33 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | -0.010 |  |
| 2026-02-22 15:01:17 | Wellawaya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-02-22 15:04:22 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-02-22 15:06:24 | Horowpothana (Yan Oya) | 2.13 | 🟢 Normal | -0.018 |  |
| 2026-02-22 15:00:09 | Nakkala (Kumbukkan Oya) | 1.35 | 🟢 Normal | -0.020 |  |
| 2026-02-22 15:01:17 | Siyambalanduwa (Heda Oya) | 0.77 | 🟢 Normal | -0.021 |  |
| 2026-02-22 15:04:12 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | -0.030 |  |
| 2026-02-22 15:03:02 | Moraketiya (Walawe Ganga) | 1.07 | 🟢 Normal | -0.038 |  |
| 2026-02-22 15:05:05 | Thanamalwila (Kirindi Oya) | 1.54 | 🟢 Normal | -0.039 |  |
| 2026-02-22 15:04:36 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | -0.040 |  |
| 2026-02-22 15:04:14 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | -0.040 |  |
| 2026-02-22 15:02:27 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | -0.049 |  |
| 2026-02-22 15:00:09 | Weraganthota (Mahaweli Ganga) | -1.36 | 🟢 Normal | -0.050 |  |
| 2026-02-22 15:00:09 | Padiyathalawa (Maduru Oya) | 1.30 | 🟢 Normal | -0.050 |  |
| 2026-02-22 15:01:57 | Giriulla (Maha Oya) | 1.55 | 🟢 Normal | -0.052 |  |
| 2026-02-22 15:03:20 | Nawalapitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.060 |  |
| 2026-02-22 15:02:27 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.070 |  |
| 2026-02-22 15:04:13 | Badalgama (Maha Oya) | 3.00 | 🟢 Normal | -0.093 |  |
| 2026-02-22 15:01:39 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | -0.100 |  |
| 2026-02-22 15:01:29 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.101 |  |
| 2026-02-22 15:03:16 | Hanwella (Kelani Ganga) | 2.21 | 🟢 Normal | -0.120 |  |
| 2026-02-22 15:02:51 | Pitabeddara (Nilwala Ganga) | 1.03 | 🟢 Normal | -0.128 |  |
| 2026-02-22 15:04:14 | Glencourse (Kelani Ganga) | 9.80 | 🟢 Normal | -0.147 |  |
| 2026-02-22 15:04:17 | Rathnapura (Kalu Ganga) | 3.25 | 🟢 Normal | -0.162 |  |
| 2026-02-22 15:07:07 | Magura (Kalu Ganga) | 2.85 | 🟢 Normal | -0.171 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)