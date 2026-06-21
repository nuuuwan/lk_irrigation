# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--21_23:30:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **185,784 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-21 23:30:19 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-21 23:24:15 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-21 23:14:59 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.019 |  |
| 2026-06-21 23:14:17 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.050 |  |
| 2026-06-21 23:08:57 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-21 23:08:12 | Rathnapura (Kalu Ganga) | 1.59 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-06-21 23:07:57 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | -0.040 |  |
| 2026-06-21 23:07:51 | Ellagawa (Kalu Ganga) | 5.12 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-06-21 23:06:14 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-21 23:05:42 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-21 23:05:02 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-06-21 23:04:40 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.021 |  |
| 2026-06-21 23:03:32 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-21 23:03:27 | Panadugama (Nilwala Ganga) | 2.57 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-06-21 23:03:25 | Badalgama (Maha Oya) | 2.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-21 23:03:24 | Glencourse (Kelani Ganga) | 9.97 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-06-21 23:02:58 | Hanwella (Kelani Ganga) | 1.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-21 23:02:45 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-21 23:02:45 | Deraniyagala (Kelani Ganga) | 1.12 | 🟢 Normal | -0.031 |  |
| 2026-06-21 23:02:38 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | -0.011 |  |
| 2026-06-21 23:02:35 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-21 23:02:26 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-21 23:02:20 | Dunamale (Aththanagalu Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-06-21 23:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.66 | 🟢 Normal | 0.000 |  |
| 2026-06-21 23:02:05 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-21 23:01:49 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-06-21 23:01:41 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.033 |  |
| 2026-06-21 23:01:24 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.011 |  |
| 2026-06-21 23:01:15 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-21 23:01:07 | Peradeniya (Mahaweli Ganga) | 2.56 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-06-21 23:01:07 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-06-21 23:00:24 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-21 23:00:18 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-21 22:45:37 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-21 23:03:24 | Glencourse (Kelani Ganga) | 9.97 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-06-21 23:01:07 | Peradeniya (Mahaweli Ganga) | 2.56 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-06-21 23:07:51 | Ellagawa (Kalu Ganga) | 5.12 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-06-21 23:08:12 | Rathnapura (Kalu Ganga) | 1.59 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-06-21 18:01:26 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-21 23:03:32 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-21 23:03:25 | Badalgama (Maha Oya) | 2.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-21 23:02:58 | Hanwella (Kelani Ganga) | 1.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-21 23:03:27 | Panadugama (Nilwala Ganga) | 2.57 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-06-21 23:01:49 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-06-21 22:01:16 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-21 23:02:45 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-21 22:03:24 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-21 23:00:24 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-21 23:02:26 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-21 23:02:35 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-21 23:00:18 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-21 18:07:51 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-21 23:30:19 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-21 23:06:14 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-21 23:02:05 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-21 23:05:02 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-06-21 23:08:57 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-21 23:02:20 | Dunamale (Aththanagalu Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-06-21 23:05:42 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-21 23:01:15 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-21 23:01:07 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-06-21 23:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.66 | 🟢 Normal | 0.000 |  |
| 2026-06-21 21:01:51 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | -0.010 |  |
| 2026-06-21 23:02:38 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | -0.011 |  |
| 2026-06-21 23:01:24 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.011 |  |
| 2026-06-21 23:14:59 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.019 |  |
| 2026-06-21 18:01:51 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-06-21 23:04:40 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.021 |  |
| 2026-06-21 23:02:45 | Deraniyagala (Kelani Ganga) | 1.12 | 🟢 Normal | -0.031 |  |
| 2026-06-21 23:01:41 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.033 |  |
| 2026-06-21 23:07:57 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | -0.040 |  |
| 2026-06-21 23:14:17 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.050 |  |
| 2026-06-21 22:07:26 | Magura (Kalu Ganga) | 1.68 | 🟢 Normal | -0.207 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)