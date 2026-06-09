# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--09_19:09:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **174,930 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-09 19:09:06 | Magura (Kalu Ganga) | 2.08 | 🟢 Normal | -0.009 |  |
| 2026-06-09 19:08:42 | Rathnapura (Kalu Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-06-09 19:08:26 | Glencourse (Kelani Ganga) | 10.99 | 🟢 Normal | -0.010 |  |
| 2026-06-09 19:08:10 | Ellagawa (Kalu Ganga) | 6.04 | 🟢 Normal | -0.027 |  |
| 2026-06-09 19:07:19 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-09 19:07:14 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | -0.019 |  |
| 2026-06-09 19:07:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.82 | 🟢 Normal | -0.046 |  |
| 2026-06-09 19:06:27 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | -0.009 |  |
| 2026-06-09 19:06:26 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-09 19:05:27 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-06-09 19:04:59 | Badalgama (Maha Oya) | 2.64 | 🟢 Normal | -0.010 |  |
| 2026-06-09 19:04:50 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-09 19:04:46 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-06-09 19:04:46 | Baddegama (Gin Ganga) | 2.07 | 🟢 Normal | -0.029 |  |
| 2026-06-09 19:04:06 | Dunamale (Aththanagalu Oya) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-06-09 19:03:49 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-09 19:03:39 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-09 19:03:24 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-09 19:03:20 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-09 19:02:54 | Nawalapitiya (Mahaweli Ganga) | 1.81 | 🟢 Normal | -0.058 |  |
| 2026-06-09 19:02:27 | Deraniyagala (Kelani Ganga) | 1.51 | 🟢 Normal | -0.100 |  |
| 2026-06-09 19:02:20 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-09 19:02:19 | Hanwella (Kelani Ganga) | 3.11 | 🟢 Normal | -0.051 |  |
| 2026-06-09 19:01:42 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-09 19:01:41 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.020 |  |
| 2026-06-09 19:01:36 | Moragaswewa (Deduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-09 19:01:25 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-09 19:01:24 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-09 19:01:04 | Panadugama (Nilwala Ganga) | 2.73 | 🟢 Normal | -0.010 |  |
| 2026-06-09 19:00:37 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-09 19:00:17 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-09 19:00:12 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-09 18:25:41 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-09 18:01:52 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-06-09 19:05:27 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-06-09 19:06:26 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-09 19:04:50 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-09 19:03:20 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-09 19:03:24 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-09 19:00:12 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-09 19:01:36 | Moragaswewa (Deduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-09 19:01:42 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-09 19:04:46 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-06-09 19:00:37 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-09 18:03:19 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-09 19:02:20 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-09 19:07:19 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-09 19:03:39 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-09 19:04:06 | Dunamale (Aththanagalu Oya) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-06-09 19:01:25 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-09 18:05:53 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-09 19:08:42 | Rathnapura (Kalu Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-06-09 18:12:11 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-06-09 19:03:49 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-09 18:25:41 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-09 19:00:17 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-09 19:01:24 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-09 19:09:06 | Magura (Kalu Ganga) | 2.08 | 🟢 Normal | -0.009 |  |
| 2026-06-09 19:06:27 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | -0.009 |  |
| 2026-06-09 19:08:26 | Glencourse (Kelani Ganga) | 10.99 | 🟢 Normal | -0.010 |  |
| 2026-06-09 19:04:59 | Badalgama (Maha Oya) | 2.64 | 🟢 Normal | -0.010 |  |
| 2026-06-09 19:01:04 | Panadugama (Nilwala Ganga) | 2.73 | 🟢 Normal | -0.010 |  |
| 2026-06-09 18:01:42 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-06-09 19:07:14 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | -0.019 |  |
| 2026-06-09 19:01:41 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.020 |  |
| 2026-06-09 19:08:10 | Ellagawa (Kalu Ganga) | 6.04 | 🟢 Normal | -0.027 |  |
| 2026-06-09 19:04:46 | Baddegama (Gin Ganga) | 2.07 | 🟢 Normal | -0.029 |  |
| 2026-06-09 18:02:14 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | -0.031 |  |
| 2026-06-09 19:07:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.82 | 🟢 Normal | -0.046 |  |
| 2026-06-09 19:02:19 | Hanwella (Kelani Ganga) | 3.11 | 🟢 Normal | -0.051 |  |
| 2026-06-09 19:02:54 | Nawalapitiya (Mahaweli Ganga) | 1.81 | 🟢 Normal | -0.058 |  |
| 2026-06-09 19:02:27 | Deraniyagala (Kelani Ganga) | 1.51 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)