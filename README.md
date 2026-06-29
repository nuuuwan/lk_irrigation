# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--29_19:14:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **192,808 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-29 19:14:02 | Holombuwa (Kelani Ganga) | 0.98 | 🟢 Normal | -0.057 |  |
| 2026-06-29 19:12:18 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-29 19:10:56 | Magura (Kalu Ganga) | 3.10 | 🟢 Normal | -0.086 |  |
| 2026-06-29 19:10:51 | Putupaula (Kalu Ganga) | 1.49 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-06-29 19:10:28 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-29 19:10:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.76 | 🟢 Normal | -1.752 |  |
| 2026-06-29 19:09:58 | Rathnapura (Kalu Ganga) | 6.01 | 🟡 Alert | -0.144 |  |
| 2026-06-29 19:09:30 | Pitabeddara (Nilwala Ganga) | 1.36 | 🟢 Normal | 8.551 | 🔺 Rising |
| 2026-06-29 19:08:30 | Panadugama (Nilwala Ganga) | 4.39 | 🟢 Normal | -0.029 |  |
| 2026-06-29 19:06:49 | Kithulgala (Kelani Ganga) | 2.03 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-06-29 19:06:27 | Glencourse (Kelani Ganga) | 12.34 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-06-29 19:05:56 | Hanwella (Kelani Ganga) | 3.54 | 🟢 Normal | 0.171 | 🔺 Rising |
| 2026-06-29 19:05:41 | Badalgama (Maha Oya) | 2.31 | 🟢 Normal | 0.000 |  |
| 2026-06-29 19:04:46 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | -0.009 |  |
| 2026-06-29 19:04:44 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-29 19:03:55 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 19:03:49 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.066 |  |
| 2026-06-29 19:03:41 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.005 |  |
| 2026-06-29 19:03:11 | Baddegama (Gin Ganga) | 2.95 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-06-29 19:03:06 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-06-29 19:02:54 | Thawalama (Gin Ganga) | 2.29 | 🟢 Normal | -0.010 |  |
| 2026-06-29 19:02:32 | Peradeniya (Mahaweli Ganga) | 3.10 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-06-29 19:02:29 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 8.551 | 🔺 Rising |
| 2026-06-29 19:02:18 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-06-29 19:02:15 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-29 19:02:14 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-06-29 19:02:14 | Deraniyagala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.198 |  |
| 2026-06-29 19:01:51 | Nawalapitiya (Mahaweli Ganga) | 2.04 | 🟢 Normal | -0.088 |  |
| 2026-06-29 19:01:50 | Ellagawa (Kalu Ganga) | 7.46 | 🟢 Normal | 0.198 | 🔺 Rising |
| 2026-06-29 19:01:36 | Dunamale (Aththanagalu Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-06-29 19:01:19 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-29 19:01:12 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | -0.010 |  |
| 2026-06-29 19:01:11 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-29 19:01:08 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-29 19:01:07 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-29 19:00:55 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-29 19:09:58 | Rathnapura (Kalu Ganga) | 6.01 | 🟡 Alert | -0.144 |  |
| 2026-06-29 19:09:30 | Pitabeddara (Nilwala Ganga) | 1.36 | 🟢 Normal | 8.551 | 🔺 Rising |
| 2026-06-29 19:01:50 | Ellagawa (Kalu Ganga) | 7.46 | 🟢 Normal | 0.198 | 🔺 Rising |
| 2026-06-29 19:05:56 | Hanwella (Kelani Ganga) | 3.54 | 🟢 Normal | 0.171 | 🔺 Rising |
| 2026-06-29 18:04:44 | Thalgahagoda (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-06-29 19:03:11 | Baddegama (Gin Ganga) | 2.95 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-06-29 19:02:32 | Peradeniya (Mahaweli Ganga) | 3.10 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-06-29 19:06:49 | Kithulgala (Kelani Ganga) | 2.03 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-06-29 19:06:27 | Glencourse (Kelani Ganga) | 12.34 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-06-29 19:10:51 | Putupaula (Kalu Ganga) | 1.49 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-06-29 19:03:55 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 19:03:41 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.005 |  |
| 2026-06-29 18:03:53 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | 0.000 |  |
| 2026-06-29 19:02:18 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-06-29 19:02:15 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-29 19:01:19 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-29 19:00:55 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-29 18:04:05 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-06-29 19:01:07 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-29 19:01:11 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-29 19:01:36 | Dunamale (Aththanagalu Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-06-29 19:04:44 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-29 19:05:41 | Badalgama (Maha Oya) | 2.31 | 🟢 Normal | 0.000 |  |
| 2026-06-29 18:02:06 | Thanthirimale (Malwathu Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-06-29 19:12:18 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-29 19:01:08 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-29 19:04:46 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | -0.009 |  |
| 2026-06-29 19:03:06 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-06-29 19:02:14 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-06-29 19:01:12 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | -0.010 |  |
| 2026-06-29 18:01:14 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-06-29 19:02:54 | Thawalama (Gin Ganga) | 2.29 | 🟢 Normal | -0.010 |  |
| 2026-06-29 19:08:30 | Panadugama (Nilwala Ganga) | 4.39 | 🟢 Normal | -0.029 |  |
| 2026-06-29 19:14:02 | Holombuwa (Kelani Ganga) | 0.98 | 🟢 Normal | -0.057 |  |
| 2026-06-29 19:03:49 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.066 |  |
| 2026-06-29 19:10:56 | Magura (Kalu Ganga) | 3.10 | 🟢 Normal | -0.086 |  |
| 2026-06-29 19:01:51 | Nawalapitiya (Mahaweli Ganga) | 2.04 | 🟢 Normal | -0.088 |  |
| 2026-06-29 19:02:14 | Deraniyagala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.198 |  |
| 2026-06-29 19:10:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.76 | 🟢 Normal | -1.752 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)