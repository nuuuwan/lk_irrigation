# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--22_00:20:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **79,509 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-22 00:20:18 | Moraketiya (Walawe Ganga) | 1.55 | 🟢 Normal | -0.146 |  |
| 2026-02-22 00:15:00 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.029 |  |
| 2026-02-22 00:13:23 | Panadugama (Nilwala Ganga) | 4.09 | 🟢 Normal | 0.250 | 🔺 Rising |
| 2026-02-22 00:13:18 | Urawa (Nilwala Ganga) | 2.78 | 🟡 Alert | 0.214 | 🔺 Rising |
| 2026-02-22 00:09:08 | Pitabeddara (Nilwala Ganga) | 2.19 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-02-22 00:08:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-02-22 00:07:37 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-22 00:07:28 | Thalgahagoda (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-22 00:07:17 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-02-22 00:07:13 | Wellawaya (Kirindi Oya) | 3.25 | 🟢 Normal | -0.284 |  |
| 2026-02-22 00:05:58 | Norwood (Kelani Ganga) | 1.30 | 🟢 Normal | -0.018 |  |
| 2026-02-22 00:05:33 | Baddegama (Gin Ganga) | 1.35 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-02-22 00:05:14 | Holombuwa (Kelani Ganga) | 2.30 | 🟢 Normal | -0.172 |  |
| 2026-02-22 00:05:09 | Glencourse (Kelani Ganga) | 11.35 | 🟢 Normal | 0.381 | 🔺 Rising |
| 2026-02-22 00:04:43 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-02-22 00:04:18 | Deraniyagala (Kelani Ganga) | 1.18 | 🟢 Normal | -0.090 |  |
| 2026-02-22 00:04:16 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | 0.297 | 🔺 Rising |
| 2026-02-22 00:03:55 | Rathnapura (Kalu Ganga) | 5.38 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-02-22 00:03:01 | Padiyathalawa (Maduru Oya) | 1.69 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-02-22 00:02:51 | Kuda Oya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.208 | 🔺 Rising |
| 2026-02-22 00:02:43 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-02-22 00:02:42 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-22 00:02:42 | Thanamalwila (Kirindi Oya) | 1.28 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-02-22 00:02:34 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | 0.251 | 🔺 Rising |
| 2026-02-22 00:02:26 | Thaldena (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.150 |  |
| 2026-02-22 00:02:23 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.200 | 🔺 Rising |
| 2026-02-22 00:02:14 | Manampitiya (Mahaweli Ganga) | 3.00 | 🟡 Alert | 0.454 | 🔺 Rising |
| 2026-02-22 00:01:49 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-22 00:01:43 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-02-22 00:01:40 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-22 00:01:38 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-02-22 00:01:28 | Nakkala (Kumbukkan Oya) | 2.26 | 🟢 Normal | -0.226 |  |
| 2026-02-22 00:01:20 | Peradeniya (Mahaweli Ganga) | 4.18 | 🟢 Normal | -0.148 |  |
| 2026-02-22 00:00:55 | Nawalapitiya (Mahaweli Ganga) | 1.75 | 🟢 Normal | -0.054 |  |
| 2026-02-22 00:00:43 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-22 00:00:42 | Magura (Kalu Ganga) | 1.53 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-02-22 00:00:33 | Thawalama (Gin Ganga) | 2.47 | 🟢 Normal | 0.545 | 🔺 Rising |
| 2026-02-21 23:36:02 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-22 00:02:14 | Manampitiya (Mahaweli Ganga) | 3.00 | 🟡 Alert | 0.454 | 🔺 Rising |
| 2026-02-22 00:13:18 | Urawa (Nilwala Ganga) | 2.78 | 🟡 Alert | 0.214 | 🔺 Rising |
| 2026-02-22 00:03:55 | Rathnapura (Kalu Ganga) | 5.38 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-02-22 00:00:33 | Thawalama (Gin Ganga) | 2.47 | 🟢 Normal | 0.545 | 🔺 Rising |
| 2026-02-22 00:05:09 | Glencourse (Kelani Ganga) | 11.35 | 🟢 Normal | 0.381 | 🔺 Rising |
| 2026-02-22 00:04:16 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | 0.297 | 🔺 Rising |
| 2026-02-22 00:02:34 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | 0.251 | 🔺 Rising |
| 2026-02-22 00:13:23 | Panadugama (Nilwala Ganga) | 4.09 | 🟢 Normal | 0.250 | 🔺 Rising |
| 2026-02-22 00:02:51 | Kuda Oya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.208 | 🔺 Rising |
| 2026-02-22 00:02:23 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.200 | 🔺 Rising |
| 2026-02-22 00:03:01 | Padiyathalawa (Maduru Oya) | 1.69 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-02-22 00:00:42 | Magura (Kalu Ganga) | 1.53 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-02-22 00:07:17 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-02-22 00:09:08 | Pitabeddara (Nilwala Ganga) | 2.19 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-02-22 00:02:42 | Thanamalwila (Kirindi Oya) | 1.28 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-02-22 00:05:33 | Baddegama (Gin Ganga) | 1.35 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-02-22 00:04:43 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-02-21 18:05:22 | Thanthirimale (Malwathu Oya) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-22 00:07:37 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-22 00:01:43 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-02-22 00:00:43 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-22 00:01:49 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-22 00:01:38 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-02-21 18:03:47 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-22 00:02:42 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-22 00:07:28 | Thalgahagoda (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-22 00:08:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-02-22 00:02:43 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-02-22 00:05:58 | Norwood (Kelani Ganga) | 1.30 | 🟢 Normal | -0.018 |  |
| 2026-02-21 18:03:01 | Weraganthota (Mahaweli Ganga) | -1.88 | 🟢 Normal | -0.020 |  |
| 2026-02-22 00:15:00 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.029 |  |
| 2026-02-22 00:00:55 | Nawalapitiya (Mahaweli Ganga) | 1.75 | 🟢 Normal | -0.054 |  |
| 2026-02-22 00:04:18 | Deraniyagala (Kelani Ganga) | 1.18 | 🟢 Normal | -0.090 |  |
| 2026-02-22 00:20:18 | Moraketiya (Walawe Ganga) | 1.55 | 🟢 Normal | -0.146 |  |
| 2026-02-22 00:01:20 | Peradeniya (Mahaweli Ganga) | 4.18 | 🟢 Normal | -0.148 |  |
| 2026-02-22 00:02:26 | Thaldena (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.150 |  |
| 2026-02-22 00:05:14 | Holombuwa (Kelani Ganga) | 2.30 | 🟢 Normal | -0.172 |  |
| 2026-02-22 00:01:28 | Nakkala (Kumbukkan Oya) | 2.26 | 🟢 Normal | -0.226 |  |
| 2026-02-22 00:07:13 | Wellawaya (Kirindi Oya) | 3.25 | 🟢 Normal | -0.284 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)