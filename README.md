# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--09_16:08:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **174,817 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-09 16:08:41 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-09 16:07:22 | Peradeniya (Mahaweli Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-06-09 16:07:18 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-09 16:06:27 | Baddegama (Gin Ganga) | 2.14 | 🟢 Normal | -0.028 |  |
| 2026-06-09 16:06:26 | Nagalagam Street (Kelani Ganga) | 0.62 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-09 16:06:09 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-09 16:05:54 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-09 16:05:52 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -0.038 |  |
| 2026-06-09 16:05:21 | Glencourse (Kelani Ganga) | 11.07 | 🟢 Normal | -0.030 |  |
| 2026-06-09 16:05:04 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-09 16:04:42 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-09 16:04:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.94 | 🟢 Normal | -0.040 |  |
| 2026-06-09 16:04:30 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-09 16:04:19 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-06-09 16:04:19 | Magura (Kalu Ganga) | 2.12 | 🟢 Normal | -0.021 |  |
| 2026-06-09 16:04:10 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-06-09 16:03:28 | Putupaula (Kalu Ganga) | 1.20 | 🟢 Normal | -0.029 |  |
| 2026-06-09 16:03:22 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-06-09 16:03:15 | Hanwella (Kelani Ganga) | 3.20 | 🟢 Normal | -0.040 |  |
| 2026-06-09 16:02:54 | Badalgama (Maha Oya) | 2.66 | 🟢 Normal | -0.010 |  |
| 2026-06-09 16:02:41 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-09 16:02:37 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-09 16:02:29 | Ellagawa (Kalu Ganga) | 6.12 | 🟢 Normal | -0.030 |  |
| 2026-06-09 16:02:22 | Deraniyagala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-06-09 16:02:17 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-09 16:01:54 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-09 16:01:38 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-09 16:01:33 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-09 16:01:25 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-06-09 16:01:08 | Nawalapitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-06-09 16:00:57 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-09 16:00:47 | Dunamale (Aththanagalu Oya) | 1.96 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-09 16:00:34 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-06-09 16:00:14 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-09 16:02:22 | Deraniyagala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-06-09 16:04:10 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-06-09 16:01:08 | Nawalapitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-06-09 16:06:26 | Nagalagam Street (Kelani Ganga) | 0.62 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-09 16:02:37 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-09 16:00:47 | Dunamale (Aththanagalu Oya) | 1.96 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-09 16:08:41 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-09 16:02:17 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-09 16:01:38 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-09 16:02:41 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-09 16:01:54 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-09 16:00:57 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-09 16:01:33 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-09 16:03:22 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-06-09 15:05:05 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-09 16:00:14 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-09 16:04:42 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-09 16:05:04 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-09 16:05:54 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-09 16:07:18 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-09 15:03:21 | Rathnapura (Kalu Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-06-09 16:01:25 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-06-09 16:07:22 | Peradeniya (Mahaweli Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-06-09 16:06:09 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-09 15:01:16 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-09 16:04:30 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-09 16:04:19 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-06-09 15:02:57 | Panadugama (Nilwala Ganga) | 2.77 | 🟢 Normal | -0.010 |  |
| 2026-06-09 16:02:54 | Badalgama (Maha Oya) | 2.66 | 🟢 Normal | -0.010 |  |
| 2026-06-09 16:00:34 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-06-09 16:04:19 | Magura (Kalu Ganga) | 2.12 | 🟢 Normal | -0.021 |  |
| 2026-06-09 16:06:27 | Baddegama (Gin Ganga) | 2.14 | 🟢 Normal | -0.028 |  |
| 2026-06-09 16:03:28 | Putupaula (Kalu Ganga) | 1.20 | 🟢 Normal | -0.029 |  |
| 2026-06-09 16:05:21 | Glencourse (Kelani Ganga) | 11.07 | 🟢 Normal | -0.030 |  |
| 2026-06-09 16:02:29 | Ellagawa (Kalu Ganga) | 6.12 | 🟢 Normal | -0.030 |  |
| 2026-06-09 16:05:52 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -0.038 |  |
| 2026-06-09 16:03:15 | Hanwella (Kelani Ganga) | 3.20 | 🟢 Normal | -0.040 |  |
| 2026-06-09 16:04:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.94 | 🟢 Normal | -0.040 |  |
| 2026-06-09 15:05:52 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.075 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)