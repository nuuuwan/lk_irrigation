# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--25_19:20:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **189,241 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-25 19:20:21 | Wellawaya (Kirindi Oya) | 0.75 | 🟢 Normal | -0.030 |  |
| 2026-06-25 19:15:34 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-25 19:15:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.04 | 🟢 Normal | -0.049 |  |
| 2026-06-25 19:15:08 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-25 19:13:14 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | -0.019 |  |
| 2026-06-25 19:10:50 | Thawalama (Gin Ganga) | 1.57 | 🟢 Normal | -0.009 |  |
| 2026-06-25 19:09:54 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.028 |  |
| 2026-06-25 19:09:48 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | -0.009 |  |
| 2026-06-25 19:08:49 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | -0.027 |  |
| 2026-06-25 19:08:05 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-06-25 19:07:55 | Ellagawa (Kalu Ganga) | 5.35 | 🟢 Normal | -0.009 |  |
| 2026-06-25 19:06:13 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.016 |  |
| 2026-06-25 19:06:09 | Panadugama (Nilwala Ganga) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-06-25 19:05:55 | Magura (Kalu Ganga) | 1.77 | 🟢 Normal | -0.010 |  |
| 2026-06-25 19:05:20 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | -0.037 |  |
| 2026-06-25 19:04:59 | Badalgama (Maha Oya) | 2.41 | 🟢 Normal | -0.010 |  |
| 2026-06-25 19:04:43 | Rathnapura (Kalu Ganga) | 1.31 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-25 19:04:27 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-25 19:04:14 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-25 19:03:58 | Dunamale (Aththanagalu Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-06-25 19:03:37 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-25 19:03:23 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-25 19:03:10 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-06-25 19:02:36 | Hanwella (Kelani Ganga) | 1.94 | 🟢 Normal | -0.020 |  |
| 2026-06-25 19:02:35 | Glencourse (Kelani Ganga) | 9.97 | 🟢 Normal | -0.052 |  |
| 2026-06-25 19:02:16 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | -0.021 |  |
| 2026-06-25 19:02:14 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.260 | 🔺 Rising |
| 2026-06-25 19:02:05 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.021 |  |
| 2026-06-25 19:01:52 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-06-25 19:01:47 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-25 19:01:28 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-06-25 19:00:54 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-06-25 19:00:46 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-06-25 18:59:59 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-25 19:02:14 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.260 | 🔺 Rising |
| 2026-06-25 19:04:43 | Rathnapura (Kalu Ganga) | 1.31 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-25 19:04:14 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-25 18:59:59 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-25 18:02:31 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-25 19:15:34 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-25 19:00:54 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-06-25 19:01:47 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-25 19:03:23 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-25 19:06:09 | Panadugama (Nilwala Ganga) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-06-25 19:03:37 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-25 19:01:52 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-06-25 19:03:58 | Dunamale (Aththanagalu Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-06-25 19:15:08 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-25 18:02:21 | Thanthirimale (Malwathu Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-25 19:08:05 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-06-25 19:03:10 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-06-25 19:04:27 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-25 19:10:50 | Thawalama (Gin Ganga) | 1.57 | 🟢 Normal | -0.009 |  |
| 2026-06-25 19:07:55 | Ellagawa (Kalu Ganga) | 5.35 | 🟢 Normal | -0.009 |  |
| 2026-06-25 19:09:48 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | -0.009 |  |
| 2026-06-25 18:01:28 | Weraganthota (Mahaweli Ganga) | -3.42 | 🟢 Normal | -0.010 |  |
| 2026-06-25 19:05:55 | Magura (Kalu Ganga) | 1.77 | 🟢 Normal | -0.010 |  |
| 2026-06-25 18:02:25 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-06-25 19:00:46 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-06-25 18:02:39 | Giriulla (Maha Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-06-25 19:04:59 | Badalgama (Maha Oya) | 2.41 | 🟢 Normal | -0.010 |  |
| 2026-06-25 19:01:28 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-06-25 19:06:13 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.016 |  |
| 2026-06-25 19:13:14 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | -0.019 |  |
| 2026-06-25 19:02:36 | Hanwella (Kelani Ganga) | 1.94 | 🟢 Normal | -0.020 |  |
| 2026-06-25 19:02:05 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.021 |  |
| 2026-06-25 19:02:16 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | -0.021 |  |
| 2026-06-25 19:08:49 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | -0.027 |  |
| 2026-06-25 19:09:54 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.028 |  |
| 2026-06-25 19:20:21 | Wellawaya (Kirindi Oya) | 0.75 | 🟢 Normal | -0.030 |  |
| 2026-06-25 19:05:20 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | -0.037 |  |
| 2026-06-25 19:15:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.04 | 🟢 Normal | -0.049 |  |
| 2026-06-25 19:02:35 | Glencourse (Kelani Ganga) | 9.97 | 🟢 Normal | -0.052 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)