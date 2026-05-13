# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--13_18:05:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **150,898 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-13 18:05:34 | Magura (Kalu Ganga) | 5.16 | 🟡 Alert | 0.011 | 🔺 Rising |
| 2026-05-13 18:05:03 | Katharagama (Menik Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-13 18:04:59 | Glencourse (Kelani Ganga) | 11.30 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-13 18:04:42 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-05-13 18:03:56 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-13 18:03:44 | Thawalama (Gin Ganga) | 3.14 | 🟢 Normal | -0.218 |  |
| 2026-05-13 18:03:43 | Rathnapura (Kalu Ganga) | 6.10 | 🟡 Alert | -0.069 |  |
| 2026-05-13 18:03:18 | Dunamale (Aththanagalu Oya) | 3.46 | 🟡 Alert | 0.058 | 🔺 Rising |
| 2026-05-13 18:03:14 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | -0.596 |  |
| 2026-05-13 18:03:09 | Hanwella (Kelani Ganga) | 2.67 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-05-13 18:03:05 | Moragaswewa (Deduru Oya) | 2.86 | 🟢 Normal | -0.053 |  |
| 2026-05-13 18:03:00 | Badalgama (Maha Oya) | 2.93 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-05-13 18:02:50 | Deraniyagala (Kelani Ganga) | 1.09 | 🟢 Normal | -0.060 |  |
| 2026-05-13 18:02:29 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-05-13 18:02:23 | Galgamuwa (Mee Oya) | 2.97 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-05-13 18:02:22 | Weraganthota (Mahaweli Ganga) | -2.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-13 18:02:21 | Thanamalwila (Kirindi Oya) | 1.75 | 🟢 Normal | -0.030 |  |
| 2026-05-13 18:02:18 | Putupaula (Kalu Ganga) | 2.21 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-13 18:02:14 | Thanthirimale (Malwathu Oya) | 3.35 | 🟢 Normal | -0.051 |  |
| 2026-05-13 18:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.70 | 🟡 Alert | 0.067 | 🔺 Rising |
| 2026-05-13 18:02:06 | Moraketiya (Walawe Ganga) | 2.16 | 🟢 Normal | -0.029 |  |
| 2026-05-13 18:02:01 | Manampitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.039 |  |
| 2026-05-13 18:01:44 | Giriulla (Maha Oya) | 2.20 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-05-13 18:01:43 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-05-13 18:01:37 | Kuda Oya (Kirindi Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-05-13 18:01:33 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-05-13 18:01:30 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-13 18:01:27 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.098 |  |
| 2026-05-13 18:01:15 | Ellagawa (Kalu Ganga) | 7.96 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-05-13 18:01:14 | Pitabeddara (Nilwala Ganga) | 2.05 | 🟢 Normal | -0.154 |  |
| 2026-05-13 18:01:10 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | -0.022 |  |
| 2026-05-13 18:00:31 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-05-13 18:00:24 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.042 |  |
| 2026-05-13 18:00:13 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.020 |  |
| 2026-05-13 18:00:09 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-13 18:00:09 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | -0.011 |  |
| 2026-05-13 17:21:29 | Baddegama (Gin Ganga) | 3.01 | 🟢 Normal | 0.096 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-13 17:09:00 | Panadugama (Nilwala Ganga) | 5.38 | 🟡 Alert | 0.101 | 🔺 Rising |
| 2026-05-13 18:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.70 | 🟡 Alert | 0.067 | 🔺 Rising |
| 2026-05-13 18:03:18 | Dunamale (Aththanagalu Oya) | 3.46 | 🟡 Alert | 0.058 | 🔺 Rising |
| 2026-05-13 18:05:34 | Magura (Kalu Ganga) | 5.16 | 🟡 Alert | 0.011 | 🔺 Rising |
| 2026-05-13 18:03:43 | Rathnapura (Kalu Ganga) | 6.10 | 🟡 Alert | -0.069 |  |
| 2026-05-13 18:01:15 | Ellagawa (Kalu Ganga) | 7.96 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-05-13 18:03:09 | Hanwella (Kelani Ganga) | 2.67 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-05-13 17:21:29 | Baddegama (Gin Ganga) | 3.01 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-05-13 18:01:44 | Giriulla (Maha Oya) | 2.20 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-05-13 18:03:00 | Badalgama (Maha Oya) | 2.93 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-05-13 18:02:23 | Galgamuwa (Mee Oya) | 2.97 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-05-13 18:04:59 | Glencourse (Kelani Ganga) | 11.30 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-13 18:02:18 | Putupaula (Kalu Ganga) | 2.21 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-13 18:02:22 | Weraganthota (Mahaweli Ganga) | -2.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-13 18:01:30 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-13 18:00:31 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-05-13 18:05:03 | Katharagama (Menik Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-13 18:03:56 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-13 18:04:42 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-05-13 18:00:09 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-13 18:01:37 | Kuda Oya (Kirindi Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-05-13 18:01:33 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-05-13 18:02:29 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-05-13 18:00:09 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | -0.011 |  |
| 2026-05-13 18:00:13 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.020 |  |
| 2026-05-13 18:01:43 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-05-13 18:01:10 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | -0.022 |  |
| 2026-05-13 18:02:06 | Moraketiya (Walawe Ganga) | 2.16 | 🟢 Normal | -0.029 |  |
| 2026-05-13 18:02:21 | Thanamalwila (Kirindi Oya) | 1.75 | 🟢 Normal | -0.030 |  |
| 2026-05-13 17:04:32 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.031 |  |
| 2026-05-13 18:02:01 | Manampitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.039 |  |
| 2026-05-13 18:00:24 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.042 |  |
| 2026-05-13 18:02:14 | Thanthirimale (Malwathu Oya) | 3.35 | 🟢 Normal | -0.051 |  |
| 2026-05-13 18:03:05 | Moragaswewa (Deduru Oya) | 2.86 | 🟢 Normal | -0.053 |  |
| 2026-05-13 18:02:50 | Deraniyagala (Kelani Ganga) | 1.09 | 🟢 Normal | -0.060 |  |
| 2026-05-13 18:01:27 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.098 |  |
| 2026-05-13 18:01:14 | Pitabeddara (Nilwala Ganga) | 2.05 | 🟢 Normal | -0.154 |  |
| 2026-05-13 18:03:44 | Thawalama (Gin Ganga) | 3.14 | 🟢 Normal | -0.218 |  |
| 2026-05-13 18:03:14 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | -0.596 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)