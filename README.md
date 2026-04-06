# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--06_13:25:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **117,747 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **22** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-06 13:25:23 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.026 |  |
| 2026-04-06 13:19:16 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 13:12:50 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-06 13:11:08 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | -0.009 |  |
| 2026-04-06 13:11:07 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-04-06 13:09:37 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | -0.009 |  |
| 2026-04-06 13:09:26 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-06 13:09:17 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-06 13:09:15 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-04-06 13:08:50 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-06 13:08:43 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-06 13:07:11 | Peradeniya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.018 |  |
| 2026-04-06 13:07:03 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-06 13:06:49 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-04-06 13:06:20 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-04-06 13:06:19 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 13:05:32 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-04-06 13:05:27 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-06 13:04:44 | Rathnapura (Kalu Ganga) | 0.64 | 🟢 Normal | -0.031 |  |
| 2026-04-06 13:04:33 | Weraganthota (Mahaweli Ganga) | -2.26 | 🟢 Normal | -0.050 |  |
| 2026-04-06 13:04:05 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 13:03:47 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-06 13:02:24 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-04-06 13:06:49 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-04-06 13:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.50 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-06 13:02:21 | Nawalapitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-06 13:06:19 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 13:01:22 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-06 13:00:41 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-06 13:09:26 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-06 13:02:35 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-04-06 13:02:37 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-06 13:08:43 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-06 13:12:50 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-06 13:04:05 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 13:02:37 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-06 13:01:20 | Ellagawa (Kalu Ganga) | 3.97 | 🟢 Normal | 0.000 |  |
| 2026-04-06 13:09:15 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-04-06 13:11:07 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-04-06 13:02:31 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-06 13:01:32 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-06 13:19:16 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 13:07:03 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-06 13:05:32 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-04-06 13:05:27 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-06 13:08:50 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-06 13:11:08 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | -0.009 |  |
| 2026-04-06 13:09:37 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | -0.009 |  |
| 2026-04-06 13:06:20 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-04-06 13:01:47 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-04-06 13:02:22 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | -0.011 |  |
| 2026-04-06 13:07:11 | Peradeniya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.018 |  |
| 2026-04-06 13:03:47 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | -0.020 |  |
| 2026-04-06 13:01:26 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.021 |  |
| 2026-04-06 13:00:58 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | -0.021 |  |
| 2026-04-06 13:25:23 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.026 |  |
| 2026-04-06 13:00:33 | Thanthirimale (Malwathu Oya) | 1.78 | 🟢 Normal | -0.030 |  |
| 2026-04-06 13:04:44 | Rathnapura (Kalu Ganga) | 0.64 | 🟢 Normal | -0.031 |  |
| 2026-04-06 13:02:44 | Glencourse (Kelani Ganga) | 8.26 | 🟢 Normal | -0.042 |  |
| 2026-04-06 13:04:33 | Weraganthota (Mahaweli Ganga) | -2.26 | 🟢 Normal | -0.050 |  |
| 2026-04-06 13:00:52 | Manampitiya (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.050 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)