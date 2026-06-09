# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--09_13:27:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **174,705 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-09 13:27:36 | Dunamale (Aththanagalu Oya) | 1.92 | 🟢 Normal | -0.014 |  |
| 2026-06-09 13:18:39 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-06-09 13:18:24 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-09 13:11:39 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-09 13:11:15 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-06-09 13:10:08 | Magura (Kalu Ganga) | 2.16 | 🟢 Normal | -0.010 |  |
| 2026-06-09 13:08:28 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | -0.009 |  |
| 2026-06-09 13:06:02 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-06-09 13:05:40 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-09 13:05:33 | Rathnapura (Kalu Ganga) | 1.97 | 🟢 Normal | -0.010 |  |
| 2026-06-09 13:05:29 | Badalgama (Maha Oya) | 2.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-09 13:05:25 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-06-09 13:05:13 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-09 13:04:36 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | -0.020 |  |
| 2026-06-09 13:04:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.03 | 🟢 Normal | -0.020 |  |
| 2026-06-09 13:04:27 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-06-09 13:04:21 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.011 |  |
| 2026-06-09 13:03:21 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-09 13:03:19 | Hanwella (Kelani Ganga) | 3.30 | 🟢 Normal | -0.030 |  |
| 2026-06-09 13:03:09 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-09 13:03:01 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-09 13:03:00 | Peradeniya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -0.049 |  |
| 2026-06-09 13:03:00 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-06-09 13:03:00 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-09 13:02:38 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.016 |  |
| 2026-06-09 13:02:34 | Deraniyagala (Kelani Ganga) | 1.26 | 🟢 Normal | -0.020 |  |
| 2026-06-09 13:02:28 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-09 13:02:24 | Glencourse (Kelani Ganga) | 11.17 | 🟢 Normal | -0.010 |  |
| 2026-06-09 13:02:20 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-06-09 13:02:17 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-09 13:02:01 | Putupaula (Kalu Ganga) | 1.30 | 🟢 Normal | -0.030 |  |
| 2026-06-09 13:01:55 | Baddegama (Gin Ganga) | 2.21 | 🟢 Normal | -0.022 |  |
| 2026-06-09 13:01:30 | Panadugama (Nilwala Ganga) | 2.79 | 🟢 Normal | -0.011 |  |
| 2026-06-09 13:01:20 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-09 13:01:13 | Ellagawa (Kalu Ganga) | 6.20 | 🟢 Normal | -0.030 |  |
| 2026-06-09 13:00:58 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-09 13:00:45 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-06-09 13:00:40 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | 0.000 |  |
| 2026-06-09 13:00:31 | Nawalapitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-06-09 12:38:50 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.023 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-09 13:04:27 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-06-09 13:05:25 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-06-09 13:05:29 | Badalgama (Maha Oya) | 2.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-09 13:18:39 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-06-09 13:06:02 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-06-09 13:00:40 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | 0.000 |  |
| 2026-06-09 13:05:40 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-09 13:01:20 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-09 13:02:17 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-09 13:03:09 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-09 13:18:24 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-09 13:02:28 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-09 13:05:13 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-09 13:11:15 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-06-09 13:03:21 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-09 13:11:39 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-09 13:00:45 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-06-09 13:03:01 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-09 13:03:00 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-09 13:00:58 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-09 13:08:28 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | -0.009 |  |
| 2026-06-09 13:10:08 | Magura (Kalu Ganga) | 2.16 | 🟢 Normal | -0.010 |  |
| 2026-06-09 13:03:00 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-06-09 13:05:33 | Rathnapura (Kalu Ganga) | 1.97 | 🟢 Normal | -0.010 |  |
| 2026-06-09 13:02:20 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-06-09 13:00:31 | Nawalapitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-06-09 13:02:24 | Glencourse (Kelani Ganga) | 11.17 | 🟢 Normal | -0.010 |  |
| 2026-06-09 13:01:30 | Panadugama (Nilwala Ganga) | 2.79 | 🟢 Normal | -0.011 |  |
| 2026-06-09 13:04:21 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.011 |  |
| 2026-06-09 13:27:36 | Dunamale (Aththanagalu Oya) | 1.92 | 🟢 Normal | -0.014 |  |
| 2026-06-09 13:02:38 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.016 |  |
| 2026-06-09 13:04:36 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | -0.020 |  |
| 2026-06-09 13:04:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.03 | 🟢 Normal | -0.020 |  |
| 2026-06-09 13:02:34 | Deraniyagala (Kelani Ganga) | 1.26 | 🟢 Normal | -0.020 |  |
| 2026-06-09 13:01:55 | Baddegama (Gin Ganga) | 2.21 | 🟢 Normal | -0.022 |  |
| 2026-06-09 13:02:01 | Putupaula (Kalu Ganga) | 1.30 | 🟢 Normal | -0.030 |  |
| 2026-06-09 13:01:13 | Ellagawa (Kalu Ganga) | 6.20 | 🟢 Normal | -0.030 |  |
| 2026-06-09 13:03:19 | Hanwella (Kelani Ganga) | 3.30 | 🟢 Normal | -0.030 |  |
| 2026-06-09 13:03:00 | Peradeniya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -0.049 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)