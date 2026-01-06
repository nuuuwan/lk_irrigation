# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--06_15:35:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **38,288 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-06 15:35:32 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-01-06 15:11:33 | Panadugama (Nilwala Ganga) | 2.76 | 🟢 Normal | -0.027 |  |
| 2026-01-06 15:10:54 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-01-06 15:08:01 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-01-06 15:07:28 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-06 15:07:22 | Thanthirimale (Malwathu Oya) | 1.69 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-06 15:07:11 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-01-06 15:06:18 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-06 15:06:03 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-06 15:05:52 | Manampitiya (Mahaweli Ganga) | 3.70 | 🟡 Alert | 0.080 | 🔺 Rising |
| 2026-01-06 15:05:39 | Katharagama (Menik Ganga) | 0.50 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-01-06 15:05:05 | Rathnapura (Kalu Ganga) | 0.95 | 🟢 Normal | -0.030 |  |
| 2026-01-06 15:05:02 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-06 15:04:53 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | -0.030 |  |
| 2026-01-06 15:04:19 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-06 15:04:01 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.041 |  |
| 2026-01-06 15:03:37 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-06 15:02:49 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-01-06 15:02:43 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-06 15:02:42 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-06 15:02:41 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-01-06 15:02:39 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | 0.000 |  |
| 2026-01-06 15:02:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.04 | 🟢 Normal | -0.069 |  |
| 2026-01-06 15:02:19 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-06 15:02:17 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-06 15:02:13 | Horowpothana (Yan Oya) | 2.35 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-01-06 15:02:11 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-01-06 15:02:10 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-01-06 15:01:45 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-01-06 15:01:45 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-06 15:01:41 | Yaka Wewa (Ma Oya) | 0.94 | 🟢 Normal | -0.021 |  |
| 2026-01-06 15:01:28 | Weraganthota (Mahaweli Ganga) | -0.37 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-06 15:01:24 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-06 15:01:19 | Siyambalanduwa (Heda Oya) | 5.19 | 🟡 Alert | -0.120 |  |
| 2026-01-06 15:01:05 | Nakkala (Kumbukkan Oya) | 2.30 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-01-06 15:00:46 | Ellagawa (Kalu Ganga) | 4.45 | 🟢 Normal | 0.000 |  |
| 2026-01-06 15:00:39 | Thaldena (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.098 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-06 15:05:52 | Manampitiya (Mahaweli Ganga) | 3.70 | 🟡 Alert | 0.080 | 🔺 Rising |
| 2026-01-06 15:01:19 | Siyambalanduwa (Heda Oya) | 5.19 | 🟡 Alert | -0.120 |  |
| 2026-01-06 15:02:49 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-01-06 15:08:01 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-01-06 15:01:05 | Nakkala (Kumbukkan Oya) | 2.30 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-01-06 15:05:39 | Katharagama (Menik Ganga) | 0.50 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-01-06 15:01:45 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-01-06 15:02:13 | Horowpothana (Yan Oya) | 2.35 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-01-06 15:06:18 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-06 15:01:24 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-06 15:02:19 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-06 15:01:28 | Weraganthota (Mahaweli Ganga) | -0.37 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-06 15:07:22 | Thanthirimale (Malwathu Oya) | 1.69 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-06 15:35:32 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-01-06 14:01:27 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-01-06 15:02:43 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-06 15:01:45 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-06 15:04:19 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-06 15:07:11 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-01-06 15:05:02 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-06 15:00:46 | Ellagawa (Kalu Ganga) | 4.45 | 🟢 Normal | 0.000 |  |
| 2026-01-06 15:02:39 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | 0.000 |  |
| 2026-01-06 15:02:42 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-06 15:02:17 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-06 15:06:03 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-06 15:03:37 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-06 15:07:28 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-06 15:02:11 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-01-06 15:02:41 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-01-06 15:02:10 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-01-06 15:10:54 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-01-06 15:01:41 | Yaka Wewa (Ma Oya) | 0.94 | 🟢 Normal | -0.021 |  |
| 2026-01-06 15:11:33 | Panadugama (Nilwala Ganga) | 2.76 | 🟢 Normal | -0.027 |  |
| 2026-01-06 15:04:53 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | -0.030 |  |
| 2026-01-06 15:05:05 | Rathnapura (Kalu Ganga) | 0.95 | 🟢 Normal | -0.030 |  |
| 2026-01-06 15:04:01 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.041 |  |
| 2026-01-06 15:02:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.04 | 🟢 Normal | -0.069 |  |
| 2026-01-06 15:00:39 | Thaldena (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.098 |  |
| 2026-01-06 14:03:27 | Padiyathalawa (Maduru Oya) | 2.76 | 🟢 Normal | -0.180 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)