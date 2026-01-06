# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--06_14:29:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **38,251 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-06 14:29:06 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-06 14:16:13 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | -0.008 |  |
| 2026-01-06 14:14:54 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-01-06 14:12:26 | Magura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-06 14:09:58 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -0.027 |  |
| 2026-01-06 14:08:43 | Katharagama (Menik Ganga) | 0.42 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-01-06 14:06:51 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-06 14:06:48 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.009 |  |
| 2026-01-06 14:06:19 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | -0.042 |  |
| 2026-01-06 14:05:52 | Yaka Wewa (Ma Oya) | 0.96 | 🟢 Normal | -0.028 |  |
| 2026-01-06 14:05:52 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.179 | 🔺 Rising |
| 2026-01-06 14:05:49 | Manampitiya (Mahaweli Ganga) | 3.62 | 🟡 Alert | 0.182 | 🔺 Rising |
| 2026-01-06 14:05:49 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-06 14:05:30 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | -0.029 |  |
| 2026-01-06 14:05:29 | Thanamalwila (Kirindi Oya) | 1.31 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-01-06 14:05:21 | Panadugama (Nilwala Ganga) | 2.79 | 🟢 Normal | -0.069 |  |
| 2026-01-06 14:05:21 | Thaldena (Mahaweli Ganga) | 1.49 | 🟢 Normal | -0.039 |  |
| 2026-01-06 14:05:10 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | -0.034 |  |
| 2026-01-06 14:04:57 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | -0.020 |  |
| 2026-01-06 14:03:59 | Peradeniya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -0.031 |  |
| 2026-01-06 14:03:51 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-01-06 14:03:37 | Nawalapitiya (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-06 14:03:27 | Padiyathalawa (Maduru Oya) | 2.76 | 🟢 Normal | -0.180 |  |
| 2026-01-06 14:03:26 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-06 14:02:43 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-06 14:02:37 | Horowpothana (Yan Oya) | 2.29 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-01-06 14:02:18 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-01-06 14:02:14 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-06 14:02:01 | Ellagawa (Kalu Ganga) | 4.45 | 🟢 Normal | 0.000 |  |
| 2026-01-06 14:01:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.11 | 🟢 Normal | -0.081 |  |
| 2026-01-06 14:01:31 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-06 14:01:30 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-01-06 14:01:27 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-01-06 14:01:19 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-06 14:01:15 | Siyambalanduwa (Heda Oya) | 5.31 | 🟡 Alert | -0.094 |  |
| 2026-01-06 14:01:14 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-06 14:01:02 | Thanthirimale (Malwathu Oya) | 1.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 14:01:01 | Nakkala (Kumbukkan Oya) | 2.20 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-01-06 14:00:40 | Weraganthota (Mahaweli Ganga) | -0.39 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-06 13:39:23 | Manampitiya (Mahaweli Ganga) | 3.54 | 🟡 Alert | 0.182 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-06 14:05:49 | Manampitiya (Mahaweli Ganga) | 3.62 | 🟡 Alert | 0.182 | 🔺 Rising |
| 2026-01-06 14:01:15 | Siyambalanduwa (Heda Oya) | 5.31 | 🟡 Alert | -0.094 |  |
| 2026-01-06 14:05:52 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.179 | 🔺 Rising |
| 2026-01-06 14:01:30 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-01-06 14:02:18 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-01-06 14:02:37 | Horowpothana (Yan Oya) | 2.29 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-01-06 14:14:54 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-01-06 14:05:29 | Thanamalwila (Kirindi Oya) | 1.31 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-01-06 14:08:43 | Katharagama (Menik Ganga) | 0.42 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-01-06 14:01:01 | Nakkala (Kumbukkan Oya) | 2.20 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-01-06 14:06:51 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-06 14:00:40 | Weraganthota (Mahaweli Ganga) | -0.39 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-06 14:01:02 | Thanthirimale (Malwathu Oya) | 1.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 14:01:27 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-01-06 14:01:31 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-06 14:01:19 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-06 14:03:37 | Nawalapitiya (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-06 14:05:49 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-06 14:12:26 | Magura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-06 14:01:14 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-06 14:02:01 | Ellagawa (Kalu Ganga) | 4.45 | 🟢 Normal | 0.000 |  |
| 2026-01-06 14:02:14 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-06 14:02:43 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-06 14:03:26 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-06 14:29:06 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-06 14:16:13 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | -0.008 |  |
| 2026-01-06 14:06:48 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.009 |  |
| 2026-01-06 14:03:51 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-01-06 14:04:57 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | -0.020 |  |
| 2026-01-06 14:09:58 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -0.027 |  |
| 2026-01-06 14:05:52 | Yaka Wewa (Ma Oya) | 0.96 | 🟢 Normal | -0.028 |  |
| 2026-01-06 14:05:30 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | -0.029 |  |
| 2026-01-06 14:03:59 | Peradeniya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -0.031 |  |
| 2026-01-06 14:05:10 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | -0.034 |  |
| 2026-01-06 14:05:21 | Thaldena (Mahaweli Ganga) | 1.49 | 🟢 Normal | -0.039 |  |
| 2026-01-06 14:06:19 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | -0.042 |  |
| 2026-01-06 14:05:21 | Panadugama (Nilwala Ganga) | 2.79 | 🟢 Normal | -0.069 |  |
| 2026-01-06 14:01:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.11 | 🟢 Normal | -0.081 |  |
| 2026-01-06 14:03:27 | Padiyathalawa (Maduru Oya) | 2.76 | 🟢 Normal | -0.180 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)