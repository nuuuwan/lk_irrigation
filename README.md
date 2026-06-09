# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--09_20:07:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **174,966 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-09 20:07:17 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | -0.010 |  |
| 2026-06-09 20:07:06 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-09 20:06:44 | Rathnapura (Kalu Ganga) | 1.90 | 🟢 Normal | -0.021 |  |
| 2026-06-09 20:06:27 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-09 20:06:13 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-09 20:05:54 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | -0.021 |  |
| 2026-06-09 20:05:53 | Glencourse (Kelani Ganga) | 11.03 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-06-09 20:04:33 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-09 20:04:21 | Putupaula (Kalu Ganga) | 1.12 | 🟢 Normal | -0.031 |  |
| 2026-06-09 20:04:16 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-06-09 20:04:09 | Baddegama (Gin Ganga) | 2.05 | 🟢 Normal | -0.020 |  |
| 2026-06-09 20:03:55 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | -0.021 |  |
| 2026-06-09 20:03:45 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-09 20:03:25 | Deraniyagala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.089 |  |
| 2026-06-09 20:03:11 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | -0.052 |  |
| 2026-06-09 20:02:51 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-09 20:02:41 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-09 20:02:38 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-09 20:02:30 | Panadugama (Nilwala Ganga) | 2.72 | 🟢 Normal | -0.010 |  |
| 2026-06-09 20:02:27 | Hanwella (Kelani Ganga) | 3.09 | 🟢 Normal | -0.020 |  |
| 2026-06-09 20:02:21 | Dunamale (Aththanagalu Oya) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-06-09 20:02:18 | Ellagawa (Kalu Ganga) | 6.03 | 🟢 Normal | -0.011 |  |
| 2026-06-09 20:02:10 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-09 20:02:08 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-06-09 20:02:08 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-09 20:01:37 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-09 20:01:35 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-09 20:01:10 | Peradeniya (Mahaweli Ganga) | 2.04 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-09 20:01:08 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-09 20:00:22 | Nawalapitiya (Mahaweli Ganga) | 1.76 | 🟢 Normal | -0.052 |  |
| 2026-06-09 20:00:15 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-09 19:35:08 | Moragaswewa (Deduru Oya) | 0.40 | 🟢 Normal | -0.021 |  |
| 2026-06-09 19:18:55 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-09 19:17:12 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-09 20:04:16 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-06-09 20:05:53 | Glencourse (Kelani Ganga) | 11.03 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-06-09 20:01:10 | Peradeniya (Mahaweli Ganga) | 2.04 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-09 20:03:45 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-09 20:00:15 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-09 20:02:08 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-09 20:01:35 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-09 20:02:38 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-09 20:02:08 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-06-09 20:01:37 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-09 18:03:19 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-09 20:06:13 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-09 20:02:51 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-09 19:02:20 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-09 20:06:27 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-09 20:07:06 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-09 20:02:10 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-09 20:02:21 | Dunamale (Aththanagalu Oya) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-06-09 19:01:25 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-09 18:12:11 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-06-09 19:03:49 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-09 20:04:33 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-09 20:02:41 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-09 20:01:08 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-09 19:09:06 | Magura (Kalu Ganga) | 2.08 | 🟢 Normal | -0.009 |  |
| 2026-06-09 20:07:17 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | -0.010 |  |
| 2026-06-09 20:02:30 | Panadugama (Nilwala Ganga) | 2.72 | 🟢 Normal | -0.010 |  |
| 2026-06-09 20:02:18 | Ellagawa (Kalu Ganga) | 6.03 | 🟢 Normal | -0.011 |  |
| 2026-06-09 20:02:27 | Hanwella (Kelani Ganga) | 3.09 | 🟢 Normal | -0.020 |  |
| 2026-06-09 20:04:09 | Baddegama (Gin Ganga) | 2.05 | 🟢 Normal | -0.020 |  |
| 2026-06-09 20:06:44 | Rathnapura (Kalu Ganga) | 1.90 | 🟢 Normal | -0.021 |  |
| 2026-06-09 20:03:55 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | -0.021 |  |
| 2026-06-09 20:05:54 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | -0.021 |  |
| 2026-06-09 20:04:21 | Putupaula (Kalu Ganga) | 1.12 | 🟢 Normal | -0.031 |  |
| 2026-06-09 18:02:14 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | -0.031 |  |
| 2026-06-09 19:07:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.82 | 🟢 Normal | -0.046 |  |
| 2026-06-09 20:03:11 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | -0.052 |  |
| 2026-06-09 20:00:22 | Nawalapitiya (Mahaweli Ganga) | 1.76 | 🟢 Normal | -0.052 |  |
| 2026-06-09 20:03:25 | Deraniyagala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.089 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)