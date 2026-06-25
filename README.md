# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--25_16:30:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **189,126 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-25 16:30:39 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | -0.007 |  |
| 2026-06-25 16:19:39 | Rathnapura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-25 16:16:15 | Galgamuwa (Mee Oya) | 0.42 | 🟢 Normal | -0.005 |  |
| 2026-06-25 16:11:29 | Dunamale (Aththanagalu Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-06-25 16:10:29 | Panadugama (Nilwala Ganga) | 2.63 | 🟢 Normal | 0.000 |  |
| 2026-06-25 16:10:15 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-25 16:10:14 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | -0.018 |  |
| 2026-06-25 16:08:52 | Magura (Kalu Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-06-25 16:07:51 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.009 |  |
| 2026-06-25 16:07:41 | Peradeniya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.027 |  |
| 2026-06-25 16:06:52 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-25 16:06:38 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | -36.000 |  |
| 2026-06-25 16:06:37 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | -36.000 |  |
| 2026-06-25 16:06:27 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-25 16:05:42 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.028 |  |
| 2026-06-25 16:04:50 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.058 |  |
| 2026-06-25 16:04:41 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-25 16:04:33 | Glencourse (Kelani Ganga) | 10.05 | 🟢 Normal | -0.030 |  |
| 2026-06-25 16:04:04 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-25 16:03:46 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.272 | 🔺 Rising |
| 2026-06-25 16:03:42 | Thanthirimale (Malwathu Oya) | 1.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-25 16:03:32 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-06-25 16:03:29 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | -0.010 |  |
| 2026-06-25 16:03:15 | Badalgama (Maha Oya) | 2.44 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-25 16:03:09 | Hanwella (Kelani Ganga) | 2.00 | 🟢 Normal | -0.020 |  |
| 2026-06-25 16:02:59 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-25 16:02:42 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-06-25 16:02:23 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-25 16:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.21 | 🟢 Normal | -0.070 |  |
| 2026-06-25 16:02:08 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-25 16:02:04 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-25 16:02:01 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.070 |  |
| 2026-06-25 16:01:52 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.344 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-25 16:01:52 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.344 | 🔺 Rising |
| 2026-06-25 16:03:46 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.272 | 🔺 Rising |
| 2026-06-25 16:03:15 | Badalgama (Maha Oya) | 2.44 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-25 16:03:42 | Thanthirimale (Malwathu Oya) | 1.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-25 16:06:27 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-25 16:04:41 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-25 16:01:44 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-25 16:01:36 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-25 14:01:19 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-06-25 16:08:52 | Magura (Kalu Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-06-25 16:02:59 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-25 16:10:29 | Panadugama (Nilwala Ganga) | 2.63 | 🟢 Normal | 0.000 |  |
| 2026-06-25 16:10:15 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-25 16:03:32 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-06-25 16:02:04 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-25 16:11:29 | Dunamale (Aththanagalu Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-06-25 16:04:04 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-25 16:06:52 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-25 16:02:08 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-25 16:19:39 | Rathnapura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-25 16:02:23 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-25 16:16:15 | Galgamuwa (Mee Oya) | 0.42 | 🟢 Normal | -0.005 |  |
| 2026-06-25 16:30:39 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | -0.007 |  |
| 2026-06-25 16:07:51 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.009 |  |
| 2026-06-25 16:02:42 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-06-25 16:01:13 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | -0.010 |  |
| 2026-06-25 16:01:41 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-06-25 16:03:29 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | -0.010 |  |
| 2026-06-25 16:10:14 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | -0.018 |  |
| 2026-06-25 16:03:09 | Hanwella (Kelani Ganga) | 2.00 | 🟢 Normal | -0.020 |  |
| 2026-06-25 16:07:41 | Peradeniya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.027 |  |
| 2026-06-25 16:05:42 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.028 |  |
| 2026-06-25 16:04:33 | Glencourse (Kelani Ganga) | 10.05 | 🟢 Normal | -0.030 |  |
| 2026-06-25 16:01:27 | Ellagawa (Kalu Ganga) | 5.38 | 🟢 Normal | -0.031 |  |
| 2026-06-25 16:04:50 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.058 |  |
| 2026-06-25 16:02:01 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.070 |  |
| 2026-06-25 16:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.21 | 🟢 Normal | -0.070 |  |
| 2026-06-25 15:04:28 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | -0.079 |  |
| 2026-06-25 16:06:38 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)