# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--17_20:30:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **182,103 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-17 20:30:10 | Moragaswewa (Deduru Oya) | 0.49 | 🟢 Normal | -0.007 |  |
| 2026-06-17 20:16:57 | Ellagawa (Kalu Ganga) | 5.29 | 🟢 Normal | -0.011 |  |
| 2026-06-17 20:16:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-17 20:11:47 | Urawa (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-06-17 20:09:19 | Magura (Kalu Ganga) | 1.84 | 🟢 Normal | -0.019 |  |
| 2026-06-17 20:08:45 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.046 |  |
| 2026-06-17 20:08:42 | Kithulgala (Kelani Ganga) | 2.09 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-06-17 20:08:12 | Panadugama (Nilwala Ganga) | 2.98 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-06-17 20:06:42 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-06-17 20:06:25 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-17 20:05:45 | Hanwella (Kelani Ganga) | 1.84 | 🟢 Normal | -0.019 |  |
| 2026-06-17 20:05:32 | Rathnapura (Kalu Ganga) | 3.20 | 🟢 Normal | 0.259 | 🔺 Rising |
| 2026-06-17 20:05:23 | Thawalama (Gin Ganga) | 1.92 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-06-17 20:04:37 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | -0.054 |  |
| 2026-06-17 20:04:05 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-17 20:03:46 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.058 |  |
| 2026-06-17 20:03:43 | Peradeniya (Mahaweli Ganga) | 1.81 | 🟢 Normal | 0.207 | 🔺 Rising |
| 2026-06-17 20:03:41 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-17 20:03:19 | Baddegama (Gin Ganga) | 1.66 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-17 20:03:16 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-17 20:03:04 | Deraniyagala (Kelani Ganga) | 2.26 | 🟢 Normal | -0.351 |  |
| 2026-06-17 20:02:55 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-17 20:02:51 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-17 20:02:41 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-17 20:02:36 | Dunamale (Aththanagalu Oya) | 1.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-17 20:02:25 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-17 20:02:12 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-17 20:02:03 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-06-17 20:01:51 | Glencourse (Kelani Ganga) | 9.90 | 🟢 Normal | -0.011 |  |
| 2026-06-17 20:01:44 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-17 20:01:43 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-06-17 20:01:30 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-17 20:00:54 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-17 20:00:32 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-17 20:00:19 | Nawalapitiya (Mahaweli Ganga) | 1.99 | 🟢 Normal | 0.087 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-17 20:05:32 | Rathnapura (Kalu Ganga) | 3.20 | 🟢 Normal | 0.259 | 🔺 Rising |
| 2026-06-17 20:03:43 | Peradeniya (Mahaweli Ganga) | 1.81 | 🟢 Normal | 0.207 | 🔺 Rising |
| 2026-06-17 20:11:47 | Urawa (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-06-17 20:08:42 | Kithulgala (Kelani Ganga) | 2.09 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-06-17 20:08:12 | Panadugama (Nilwala Ganga) | 2.98 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-06-17 20:00:19 | Nawalapitiya (Mahaweli Ganga) | 1.99 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-06-17 20:05:23 | Thawalama (Gin Ganga) | 1.92 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-06-17 20:01:43 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-06-17 20:03:19 | Baddegama (Gin Ganga) | 1.66 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-17 20:16:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-17 20:02:25 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-17 20:02:55 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-17 20:02:36 | Dunamale (Aththanagalu Oya) | 1.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-17 18:02:56 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | 0.000 |  |
| 2026-06-17 19:01:52 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-17 20:02:51 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-17 20:01:44 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-17 20:04:05 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-17 20:02:41 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-17 20:06:25 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-17 20:00:54 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-17 20:02:12 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-17 20:03:41 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-17 20:06:42 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-06-17 20:03:16 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-17 20:00:32 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-17 20:30:10 | Moragaswewa (Deduru Oya) | 0.49 | 🟢 Normal | -0.007 |  |
| 2026-06-17 20:02:03 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-06-17 18:05:17 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-06-17 18:01:25 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-06-17 20:16:57 | Ellagawa (Kalu Ganga) | 5.29 | 🟢 Normal | -0.011 |  |
| 2026-06-17 18:01:29 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.011 |  |
| 2026-06-17 20:01:51 | Glencourse (Kelani Ganga) | 9.90 | 🟢 Normal | -0.011 |  |
| 2026-06-17 20:09:19 | Magura (Kalu Ganga) | 1.84 | 🟢 Normal | -0.019 |  |
| 2026-06-17 20:05:45 | Hanwella (Kelani Ganga) | 1.84 | 🟢 Normal | -0.019 |  |
| 2026-06-17 20:08:45 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.046 |  |
| 2026-06-17 20:04:37 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | -0.054 |  |
| 2026-06-17 20:03:46 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.058 |  |
| 2026-06-17 20:03:04 | Deraniyagala (Kelani Ganga) | 2.26 | 🟢 Normal | -0.351 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)