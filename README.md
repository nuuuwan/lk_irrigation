# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--29_20:23:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **192,846 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-29 20:23:20 | Thalgahagoda (Nilwala Ganga) | 1.02 | 🟢 Normal | -0.109 |  |
| 2026-06-29 20:15:30 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-06-29 20:09:32 | Panadugama (Nilwala Ganga) | 4.36 | 🟢 Normal | -0.029 |  |
| 2026-06-29 20:09:10 | Holombuwa (Kelani Ganga) | 0.94 | 🟢 Normal | -0.044 |  |
| 2026-06-29 20:08:56 | Pitabeddara (Nilwala Ganga) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-06-29 20:08:30 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-29 20:08:26 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-29 20:07:36 | Putupaula (Kalu Ganga) | 1.50 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-29 20:07:34 | Baddegama (Gin Ganga) | 2.96 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-29 20:07:21 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-29 20:07:07 | Ellagawa (Kalu Ganga) | 7.55 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-06-29 20:06:52 | Kithulgala (Kelani Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-06-29 20:06:46 | Rathnapura (Kalu Ganga) | 5.89 | 🟡 Alert | -0.127 |  |
| 2026-06-29 20:06:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.81 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-06-29 20:05:51 | Badalgama (Maha Oya) | 2.30 | 🟢 Normal | -0.010 |  |
| 2026-06-29 20:05:39 | Dunamale (Aththanagalu Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-06-29 20:05:38 | Glencourse (Kelani Ganga) | 12.30 | 🟢 Normal | -0.041 |  |
| 2026-06-29 20:04:43 | Hanwella (Kelani Ganga) | 3.70 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-06-29 20:04:36 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-06-29 20:04:02 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-29 20:03:55 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 20:03:54 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.061 |  |
| 2026-06-29 20:03:40 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-29 20:03:15 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-29 20:02:56 | Magura (Kalu Ganga) | 3.02 | 🟢 Normal | -0.092 |  |
| 2026-06-29 20:02:56 | Thawalama (Gin Ganga) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-06-29 20:02:43 | Peradeniya (Mahaweli Ganga) | 3.07 | 🟢 Normal | -0.030 |  |
| 2026-06-29 20:02:42 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-06-29 20:02:42 | Deraniyagala (Kelani Ganga) | 1.48 | 🟢 Normal | -0.089 |  |
| 2026-06-29 20:02:21 | Nawalapitiya (Mahaweli Ganga) | 1.95 | 🟢 Normal | -0.089 |  |
| 2026-06-29 20:02:07 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-29 20:01:26 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-29 20:01:23 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-29 20:01:20 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-29 20:00:59 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-29 20:00:38 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-29 19:45:04 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-29 20:06:46 | Rathnapura (Kalu Ganga) | 5.89 | 🟡 Alert | -0.127 |  |
| 2026-06-29 20:04:43 | Hanwella (Kelani Ganga) | 3.70 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-06-29 20:07:07 | Ellagawa (Kalu Ganga) | 7.55 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-06-29 20:06:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.81 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-06-29 20:07:36 | Putupaula (Kalu Ganga) | 1.50 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-29 20:03:55 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 20:07:34 | Baddegama (Gin Ganga) | 2.96 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-29 20:06:52 | Kithulgala (Kelani Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-06-29 18:03:53 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | 0.000 |  |
| 2026-06-29 20:02:42 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-06-29 20:00:59 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-29 20:15:30 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-06-29 20:01:20 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-29 20:02:07 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-29 18:04:05 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-06-29 20:03:40 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-29 20:01:26 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-29 20:08:30 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-29 20:05:39 | Dunamale (Aththanagalu Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-06-29 20:03:15 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-29 20:07:21 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-29 20:00:38 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-29 18:02:06 | Thanthirimale (Malwathu Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-06-29 20:02:56 | Thawalama (Gin Ganga) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-06-29 20:04:02 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-29 20:01:23 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-29 20:08:26 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-29 20:04:36 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-06-29 20:05:51 | Badalgama (Maha Oya) | 2.30 | 🟢 Normal | -0.010 |  |
| 2026-06-29 20:08:56 | Pitabeddara (Nilwala Ganga) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-06-29 20:09:32 | Panadugama (Nilwala Ganga) | 4.36 | 🟢 Normal | -0.029 |  |
| 2026-06-29 20:02:43 | Peradeniya (Mahaweli Ganga) | 3.07 | 🟢 Normal | -0.030 |  |
| 2026-06-29 20:05:38 | Glencourse (Kelani Ganga) | 12.30 | 🟢 Normal | -0.041 |  |
| 2026-06-29 20:09:10 | Holombuwa (Kelani Ganga) | 0.94 | 🟢 Normal | -0.044 |  |
| 2026-06-29 20:03:54 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.061 |  |
| 2026-06-29 20:02:21 | Nawalapitiya (Mahaweli Ganga) | 1.95 | 🟢 Normal | -0.089 |  |
| 2026-06-29 20:02:42 | Deraniyagala (Kelani Ganga) | 1.48 | 🟢 Normal | -0.089 |  |
| 2026-06-29 20:02:56 | Magura (Kalu Ganga) | 3.02 | 🟢 Normal | -0.092 |  |
| 2026-06-29 20:23:20 | Thalgahagoda (Nilwala Ganga) | 1.02 | 🟢 Normal | -0.109 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)