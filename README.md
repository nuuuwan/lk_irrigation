# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--10_05:26:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **147,689 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-10 05:26:30 | Dunamale (Aththanagalu Oya) | 1.62 | 🟢 Normal | -0.180 |  |
| 2026-05-10 05:22:47 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | -0.015 |  |
| 2026-05-10 05:20:20 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | -0.090 |  |
| 2026-05-10 05:19:50 | Dunamale (Aththanagalu Oya) | 1.64 | 🟢 Normal | -0.180 |  |
| 2026-05-10 05:17:30 | Thawalama (Gin Ganga) | 1.53 | 🟢 Normal | -0.016 |  |
| 2026-05-10 05:11:52 | Moragaswewa (Deduru Oya) | 3.28 | 🟢 Normal | -0.211 |  |
| 2026-05-10 05:11:27 | Thanamalwila (Kirindi Oya) | 3.06 | 🟢 Normal | -0.567 |  |
| 2026-05-10 05:10:36 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-05-10 05:10:25 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -0.248 |  |
| 2026-05-10 05:08:39 | Magura (Kalu Ganga) | 1.56 | 🟢 Normal | -0.019 |  |
| 2026-05-10 05:08:08 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-05-10 05:06:49 | Hanwella (Kelani Ganga) | 1.46 | 🟢 Normal | 0.218 | 🔺 Rising |
| 2026-05-10 05:04:44 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | -0.019 |  |
| 2026-05-10 05:04:36 | Rathnapura (Kalu Ganga) | 1.35 | 🟢 Normal | -0.031 |  |
| 2026-05-10 05:04:34 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-05-10 05:04:32 | Glencourse (Kelani Ganga) | 10.19 | 🟢 Normal | -0.392 |  |
| 2026-05-10 05:04:13 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.048 |  |
| 2026-05-10 05:04:12 | Peradeniya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.029 |  |
| 2026-05-10 05:03:53 | Holombuwa (Kelani Ganga) | 0.77 | 🟢 Normal | -0.021 |  |
| 2026-05-10 05:03:50 | Giriulla (Maha Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-05-10 05:03:36 | Katharagama (Menik Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-05-10 05:02:27 | Badalgama (Maha Oya) | 2.54 | 🟢 Normal | -0.010 |  |
| 2026-05-10 05:02:27 | Nakkala (Kumbukkan Oya) | 1.71 | 🟢 Normal | -0.130 |  |
| 2026-05-10 05:02:26 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.020 |  |
| 2026-05-10 05:02:26 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-10 05:02:23 | Ellagawa (Kalu Ganga) | 5.00 | 🟢 Normal | -0.132 |  |
| 2026-05-10 05:01:16 | Horowpothana (Yan Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-05-10 05:01:09 | Kuda Oya (Kirindi Oya) | 2.60 | 🟢 Normal | -0.020 |  |
| 2026-05-10 05:00:59 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-10 05:00:52 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-05-10 05:00:20 | Wellawaya (Kirindi Oya) | 2.10 | 🟢 Normal | -0.340 |  |
| 2026-05-10 04:53:30 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.248 |  |
| 2026-05-10 04:49:04 | Moragaswewa (Deduru Oya) | 3.36 | 🟢 Normal | -0.211 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-10 05:06:49 | Hanwella (Kelani Ganga) | 1.46 | 🟢 Normal | 0.218 | 🔺 Rising |
| 2026-05-09 18:02:49 | Weraganthota (Mahaweli Ganga) | -2.65 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-05-10 05:02:26 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-10 05:00:59 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-10 05:04:34 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-05-10 04:03:49 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-05-10 05:01:16 | Horowpothana (Yan Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-05-10 02:01:34 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-10 05:03:36 | Katharagama (Menik Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-05-10 05:10:36 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-05-10 02:02:31 | Padiyathalawa (Maduru Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-05-10 05:08:08 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-05-10 04:03:34 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-05-10 05:02:27 | Badalgama (Maha Oya) | 2.54 | 🟢 Normal | -0.010 |  |
| 2026-05-10 05:00:52 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-05-10 05:03:50 | Giriulla (Maha Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-05-10 05:22:47 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | -0.015 |  |
| 2026-05-10 05:17:30 | Thawalama (Gin Ganga) | 1.53 | 🟢 Normal | -0.016 |  |
| 2026-05-10 05:08:39 | Magura (Kalu Ganga) | 1.56 | 🟢 Normal | -0.019 |  |
| 2026-05-10 05:04:44 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | -0.019 |  |
| 2026-05-10 05:02:26 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.020 |  |
| 2026-05-10 05:01:09 | Kuda Oya (Kirindi Oya) | 2.60 | 🟢 Normal | -0.020 |  |
| 2026-05-10 05:03:53 | Holombuwa (Kelani Ganga) | 0.77 | 🟢 Normal | -0.021 |  |
| 2026-05-10 05:04:12 | Peradeniya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.029 |  |
| 2026-05-10 05:04:36 | Rathnapura (Kalu Ganga) | 1.35 | 🟢 Normal | -0.031 |  |
| 2026-05-10 05:04:13 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.048 |  |
| 2026-05-10 04:03:32 | Thaldena (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.050 |  |
| 2026-05-09 18:00:42 | Thanthirimale (Malwathu Oya) | 3.25 | 🟢 Normal | -0.051 |  |
| 2026-05-10 04:12:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.80 | 🟢 Normal | -0.062 |  |
| 2026-05-09 18:04:22 | Galgamuwa (Mee Oya) | 2.26 | 🟢 Normal | -0.081 |  |
| 2026-05-10 05:20:20 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | -0.090 |  |
| 2026-05-10 05:02:27 | Nakkala (Kumbukkan Oya) | 1.71 | 🟢 Normal | -0.130 |  |
| 2026-05-10 05:02:23 | Ellagawa (Kalu Ganga) | 5.00 | 🟢 Normal | -0.132 |  |
| 2026-05-10 05:26:30 | Dunamale (Aththanagalu Oya) | 1.62 | 🟢 Normal | -0.180 |  |
| 2026-05-10 05:11:52 | Moragaswewa (Deduru Oya) | 3.28 | 🟢 Normal | -0.211 |  |
| 2026-05-10 05:10:25 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -0.248 |  |
| 2026-05-10 05:00:20 | Wellawaya (Kirindi Oya) | 2.10 | 🟢 Normal | -0.340 |  |
| 2026-05-10 05:04:32 | Glencourse (Kelani Ganga) | 10.19 | 🟢 Normal | -0.392 |  |
| 2026-05-10 05:11:27 | Thanamalwila (Kirindi Oya) | 3.06 | 🟢 Normal | -0.567 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)