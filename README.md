# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--04_07:01:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **224,442 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **8** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-04 07:01:17 | Ellagawa (Kalu Ganga) | 8.50 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-08-04 07:01:08 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | -0.030 |  |
| 2026-08-04 07:01:08 | Thanthirimale (Malwathu Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-08-04 07:00:26 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-04 07:00:19 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-04 07:00:17 | Weraganthota (Mahaweli Ganga) | -2.85 | 🟢 Normal | -0.020 |  |
| 2026-08-04 06:31:26 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | -0.001 |  |
| 2026-08-04 06:15:07 | Magura (Kalu Ganga) | 2.60 | 🟢 Normal | -0.120 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-04 06:05:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.36 | 🟡 Alert | 0.115 | 🔺 Rising |
| 2026-08-04 06:07:51 | Nagalagam Street (Kelani Ganga) | 1.25 | 🟡 Alert | 0.015 | 🔺 Rising |
| 2026-08-04 06:07:20 | Hanwella (Kelani Ganga) | 7.04 | 🟡 Alert | -0.068 |  |
| 2026-08-04 06:01:18 | Rathnapura (Kalu Ganga) | 7.42 | 🟡 Alert | -0.085 |  |
| 2026-08-04 06:07:01 | Peradeniya (Mahaweli Ganga) | 5.40 | 🟡 Alert | -0.201 |  |
| 2026-08-04 06:07:06 | Glencourse (Kelani Ganga) | 15.12 | 🟡 Alert | -0.254 |  |
| 2026-08-04 06:08:21 | Kithulgala (Kelani Ganga) | 2.83 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-08-04 06:01:54 | Thalgahagoda (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-08-04 07:01:17 | Ellagawa (Kalu Ganga) | 8.50 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-08-04 06:01:53 | Manampitiya (Mahaweli Ganga) | 0.03 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-08-04 06:04:44 | Deraniyagala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-04 06:08:24 | Baddegama (Gin Ganga) | 2.63 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-08-04 06:00:34 | Putupaula (Kalu Ganga) | 1.83 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-04 07:00:19 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-04 06:02:28 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-04 07:00:26 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-04 06:00:57 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-04 06:04:54 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-04 06:00:35 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-04 06:05:39 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-04 06:05:32 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-04 07:01:08 | Thanthirimale (Malwathu Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-08-04 06:04:43 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-08-04 06:31:26 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | -0.001 |  |
| 2026-08-04 06:09:23 | Thanamalwila (Kirindi Oya) | 0.09 | 🟢 Normal | -0.009 |  |
| 2026-08-04 06:03:26 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.019 |  |
| 2026-08-04 07:00:17 | Weraganthota (Mahaweli Ganga) | -2.85 | 🟢 Normal | -0.020 |  |
| 2026-08-04 06:02:22 | Dunamale (Aththanagalu Oya) | 1.62 | 🟢 Normal | -0.020 |  |
| 2026-08-04 07:01:08 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | -0.030 |  |
| 2026-08-04 06:11:00 | Norwood (Kelani Ganga) | 1.33 | 🟢 Normal | -0.044 |  |
| 2026-08-04 06:08:51 | Panadugama (Nilwala Ganga) | 4.55 | 🟢 Normal | -0.067 |  |
| 2026-08-04 06:02:35 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.070 |  |
| 2026-08-04 06:05:09 | Nawalapitiya (Mahaweli Ganga) | 2.62 | 🟢 Normal | -0.079 |  |
| 2026-08-04 05:02:55 | Pitabeddara (Nilwala Ganga) | 1.18 | 🟢 Normal | -0.099 |  |
| 2026-08-04 06:09:17 | Holombuwa (Kelani Ganga) | 1.05 | 🟢 Normal | -0.115 |  |
| 2026-08-04 06:15:07 | Magura (Kalu Ganga) | 2.60 | 🟢 Normal | -0.120 |  |
| 2026-08-04 06:09:40 | Thawalama (Gin Ganga) | 2.53 | 🟢 Normal | -0.151 |  |
| 2026-08-04 06:02:58 | Giriulla (Maha Oya) | 2.25 | 🟢 Normal | -0.225 |  |
| 2026-08-04 06:04:24 | Badalgama (Maha Oya) | 4.22 | 🟢 Normal | -0.286 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)