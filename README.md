# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--19_20:13:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **183,890 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-19 20:13:10 | Glencourse (Kelani Ganga) | 10.31 | 🟢 Normal | -0.009 |  |
| 2026-06-19 20:11:34 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-19 20:10:53 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-19 20:10:44 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-19 20:09:57 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-06-19 20:09:53 | Thawalama (Gin Ganga) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-06-19 20:08:37 | Baddegama (Gin Ganga) | 1.60 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-19 20:08:20 | Peradeniya (Mahaweli Ganga) | 2.16 | 🟢 Normal | 0.341 | 🔺 Rising |
| 2026-06-19 20:07:39 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-19 20:07:35 | Badalgama (Maha Oya) | 2.41 | 🟢 Normal | -0.010 |  |
| 2026-06-19 20:07:31 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-19 20:06:53 | Rathnapura (Kalu Ganga) | 1.83 | 🟢 Normal | -0.020 |  |
| 2026-06-19 20:05:28 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.118 |  |
| 2026-06-19 20:04:53 | Panadugama (Nilwala Ganga) | 2.82 | 🟢 Normal | -0.011 |  |
| 2026-06-19 20:04:32 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-19 20:04:15 | Magura (Kalu Ganga) | 2.37 | 🟢 Normal | -0.010 |  |
| 2026-06-19 20:03:52 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-19 20:03:51 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | -0.138 |  |
| 2026-06-19 20:03:41 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | -0.010 |  |
| 2026-06-19 20:03:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.97 | 🟢 Normal | -0.028 |  |
| 2026-06-19 20:03:35 | Putupaula (Kalu Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-19 20:03:34 | Hanwella (Kelani Ganga) | 2.39 | 🟢 Normal | -0.031 |  |
| 2026-06-19 20:03:26 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-06-19 20:03:23 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.012 |  |
| 2026-06-19 20:03:13 | Deraniyagala (Kelani Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-06-19 20:03:03 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-19 20:03:02 | Ellagawa (Kalu Ganga) | 5.85 | 🟢 Normal | -0.020 |  |
| 2026-06-19 20:02:54 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-19 20:02:54 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | -0.079 |  |
| 2026-06-19 20:02:42 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-19 20:01:58 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | -0.011 |  |
| 2026-06-19 20:01:57 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-19 20:01:42 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-19 20:01:26 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-19 20:01:17 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-19 20:00:55 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-19 20:00:30 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-19 20:08:20 | Peradeniya (Mahaweli Ganga) | 2.16 | 🟢 Normal | 0.341 | 🔺 Rising |
| 2026-06-19 20:01:17 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-19 20:10:44 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-19 20:03:03 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-19 20:08:37 | Baddegama (Gin Ganga) | 1.60 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-19 20:10:53 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-19 18:00:15 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | 0.000 |  |
| 2026-06-19 20:00:30 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-19 20:02:54 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-19 20:11:34 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-19 20:01:42 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-19 20:07:31 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-19 18:02:46 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-19 20:03:13 | Deraniyagala (Kelani Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-06-19 20:07:39 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-19 20:04:32 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-19 20:03:52 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-19 20:03:35 | Putupaula (Kalu Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-19 20:00:55 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-19 20:09:53 | Thawalama (Gin Ganga) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-06-19 20:09:57 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-06-19 20:01:57 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-19 20:02:42 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-19 20:13:10 | Glencourse (Kelani Ganga) | 10.31 | 🟢 Normal | -0.009 |  |
| 2026-06-19 20:04:15 | Magura (Kalu Ganga) | 2.37 | 🟢 Normal | -0.010 |  |
| 2026-06-19 20:07:35 | Badalgama (Maha Oya) | 2.41 | 🟢 Normal | -0.010 |  |
| 2026-06-19 20:03:26 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-06-19 20:03:41 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | -0.010 |  |
| 2026-06-19 18:02:43 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-06-19 20:04:53 | Panadugama (Nilwala Ganga) | 2.82 | 🟢 Normal | -0.011 |  |
| 2026-06-19 20:01:58 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | -0.011 |  |
| 2026-06-19 20:03:23 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.012 |  |
| 2026-06-19 20:03:02 | Ellagawa (Kalu Ganga) | 5.85 | 🟢 Normal | -0.020 |  |
| 2026-06-19 20:06:53 | Rathnapura (Kalu Ganga) | 1.83 | 🟢 Normal | -0.020 |  |
| 2026-06-19 20:03:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.97 | 🟢 Normal | -0.028 |  |
| 2026-06-19 20:03:34 | Hanwella (Kelani Ganga) | 2.39 | 🟢 Normal | -0.031 |  |
| 2026-06-19 20:02:54 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | -0.079 |  |
| 2026-06-19 20:05:28 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.118 |  |
| 2026-06-19 20:03:51 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | -0.138 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)