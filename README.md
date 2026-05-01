# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--01_10:06:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **139,879 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-01 10:06:22 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-05-01 10:06:20 | Ellagawa (Kalu Ganga) | 5.40 | 🟢 Normal | -0.048 |  |
| 2026-05-01 10:06:01 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-01 10:06:00 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.031 |  |
| 2026-05-01 10:05:49 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.029 |  |
| 2026-05-01 10:05:45 | Dunamale (Aththanagalu Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-05-01 10:05:34 | Badalgama (Maha Oya) | 2.20 | 🟢 Normal | -0.010 |  |
| 2026-05-01 10:05:16 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-01 10:04:48 | Rathnapura (Kalu Ganga) | 1.56 | 🟢 Normal | -0.178 |  |
| 2026-05-01 10:04:09 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-01 10:04:07 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-05-01 10:04:00 | Thawalama (Gin Ganga) | 1.81 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-01 10:03:26 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-05-01 10:03:21 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-01 10:03:08 | Hanwella (Kelani Ganga) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-01 10:03:05 | Yaka Wewa (Ma Oya) | 0.86 | 🟢 Normal | -0.040 |  |
| 2026-05-01 10:02:48 | Glencourse (Kelani Ganga) | 8.73 | 🟢 Normal | -0.041 |  |
| 2026-05-01 10:02:25 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.020 |  |
| 2026-05-01 10:02:19 | Thanamalwila (Kirindi Oya) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-05-01 10:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.92 | 🟢 Normal | -0.070 |  |
| 2026-05-01 10:01:57 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | -0.011 |  |
| 2026-05-01 10:01:48 | Manampitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-01 10:01:43 | Panadugama (Nilwala Ganga) | 2.01 | 🟢 Normal | -0.012 |  |
| 2026-05-01 10:01:39 | Baddegama (Gin Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-01 10:01:09 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-05-01 10:01:06 | Moragaswewa (Deduru Oya) | 1.14 | 🟢 Normal | -0.012 |  |
| 2026-05-01 10:01:02 | Thanthirimale (Malwathu Oya) | 2.71 | 🟢 Normal | -0.010 |  |
| 2026-05-01 10:00:43 | Weraganthota (Mahaweli Ganga) | -3.07 | 🟢 Normal | -0.020 |  |
| 2026-05-01 10:00:32 | Horowpothana (Yan Oya) | 1.83 | 🟢 Normal | -0.029 |  |
| 2026-05-01 09:19:20 | Horowpothana (Yan Oya) | 1.85 | 🟢 Normal | -0.029 |  |
| 2026-05-01 09:15:55 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-01 10:06:22 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-05-01 10:04:00 | Thawalama (Gin Ganga) | 1.81 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-01 10:01:48 | Manampitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-01 10:06:01 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-01 10:03:08 | Hanwella (Kelani Ganga) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-01 10:05:16 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-01 10:04:09 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-01 09:04:01 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-01 09:05:52 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-01 09:04:23 | Magura (Kalu Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-05-01 09:15:55 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-05-01 10:01:39 | Baddegama (Gin Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-01 09:09:01 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-05-01 09:03:12 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-01 10:05:45 | Dunamale (Aththanagalu Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-05-01 09:08:11 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-01 10:03:21 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-01 09:02:16 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-01 10:05:34 | Badalgama (Maha Oya) | 2.20 | 🟢 Normal | -0.010 |  |
| 2026-05-01 10:03:26 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-05-01 10:01:09 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-05-01 10:01:02 | Thanthirimale (Malwathu Oya) | 2.71 | 🟢 Normal | -0.010 |  |
| 2026-05-01 10:04:07 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-05-01 10:01:57 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | -0.011 |  |
| 2026-05-01 10:01:06 | Moragaswewa (Deduru Oya) | 1.14 | 🟢 Normal | -0.012 |  |
| 2026-05-01 10:01:43 | Panadugama (Nilwala Ganga) | 2.01 | 🟢 Normal | -0.012 |  |
| 2026-05-01 10:02:25 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.020 |  |
| 2026-05-01 10:02:19 | Thanamalwila (Kirindi Oya) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-05-01 10:00:43 | Weraganthota (Mahaweli Ganga) | -3.07 | 🟢 Normal | -0.020 |  |
| 2026-05-01 09:05:28 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | -0.021 |  |
| 2026-05-01 10:05:49 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.029 |  |
| 2026-05-01 10:00:32 | Horowpothana (Yan Oya) | 1.83 | 🟢 Normal | -0.029 |  |
| 2026-05-01 10:06:00 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.031 |  |
| 2026-05-01 10:03:05 | Yaka Wewa (Ma Oya) | 0.86 | 🟢 Normal | -0.040 |  |
| 2026-05-01 10:02:48 | Glencourse (Kelani Ganga) | 8.73 | 🟢 Normal | -0.041 |  |
| 2026-05-01 10:06:20 | Ellagawa (Kalu Ganga) | 5.40 | 🟢 Normal | -0.048 |  |
| 2026-05-01 09:07:03 | Putupaula (Kalu Ganga) | 0.46 | 🟢 Normal | -0.059 |  |
| 2026-05-01 10:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.92 | 🟢 Normal | -0.070 |  |
| 2026-05-01 10:04:48 | Rathnapura (Kalu Ganga) | 1.56 | 🟢 Normal | -0.178 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)