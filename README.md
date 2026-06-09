# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--09_14:25:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **174,744 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-09 14:25:41 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.018 |  |
| 2026-06-09 14:20:33 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-09 14:16:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.00 | 🟢 Normal | -0.025 |  |
| 2026-06-09 14:08:09 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-09 14:07:52 | Nagalagam Street (Kelani Ganga) | 0.59 | 🟢 Normal | -0.042 |  |
| 2026-06-09 14:07:51 | Rathnapura (Kalu Ganga) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-06-09 14:07:12 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-09 14:06:29 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-06-09 14:06:08 | Magura (Kalu Ganga) | 2.15 | 🟢 Normal | -0.011 |  |
| 2026-06-09 14:05:10 | Baddegama (Gin Ganga) | 2.18 | 🟢 Normal | -0.028 |  |
| 2026-06-09 14:04:44 | Hanwella (Kelani Ganga) | 3.27 | 🟢 Normal | -0.029 |  |
| 2026-06-09 14:04:43 | Dunamale (Aththanagalu Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-06-09 14:04:21 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-09 14:04:03 | Nawalapitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-06-09 14:04:02 | Badalgama (Maha Oya) | 2.67 | 🟢 Normal | 0.000 |  |
| 2026-06-09 14:03:50 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-09 14:03:48 | Peradeniya (Mahaweli Ganga) | 2.03 | 🟢 Normal | -0.020 |  |
| 2026-06-09 14:03:32 | Glencourse (Kelani Ganga) | 11.13 | 🟢 Normal | -0.039 |  |
| 2026-06-09 14:03:28 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-09 14:03:19 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | -0.031 |  |
| 2026-06-09 14:03:14 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-09 14:03:07 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-09 14:03:01 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-06-09 14:02:51 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | -0.020 |  |
| 2026-06-09 14:02:45 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-09 14:02:41 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-06-09 14:02:30 | Deraniyagala (Kelani Ganga) | 1.29 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-09 14:02:26 | Panadugama (Nilwala Ganga) | 2.78 | 🟢 Normal | -0.010 |  |
| 2026-06-09 14:02:21 | Ellagawa (Kalu Ganga) | 6.17 | 🟢 Normal | -0.029 |  |
| 2026-06-09 14:02:18 | Putupaula (Kalu Ganga) | 1.26 | 🟢 Normal | -0.040 |  |
| 2026-06-09 14:02:16 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-09 14:02:11 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-09 14:02:02 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | -0.225 |  |
| 2026-06-09 14:01:57 | Pitabeddara (Nilwala Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-06-09 14:01:53 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-09 14:01:40 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-09 14:01:35 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | -0.034 |  |
| 2026-06-09 14:01:02 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-09 14:02:41 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-06-09 14:02:30 | Deraniyagala (Kelani Ganga) | 1.29 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-09 14:03:28 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-09 14:02:45 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-09 14:08:09 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-09 14:03:07 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-09 14:02:11 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-09 14:04:03 | Nawalapitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-06-09 14:07:12 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-09 14:01:02 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-09 14:04:21 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-09 14:03:50 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-09 14:06:29 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-06-09 14:04:43 | Dunamale (Aththanagalu Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-06-09 14:01:53 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-09 14:04:02 | Badalgama (Maha Oya) | 2.67 | 🟢 Normal | 0.000 |  |
| 2026-06-09 14:03:14 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-09 14:00:11 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-06-09 14:20:33 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-09 14:01:40 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-09 14:02:16 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-09 14:07:51 | Rathnapura (Kalu Ganga) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-06-09 14:02:26 | Panadugama (Nilwala Ganga) | 2.78 | 🟢 Normal | -0.010 |  |
| 2026-06-09 14:03:01 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-06-09 14:01:57 | Pitabeddara (Nilwala Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-06-09 14:06:08 | Magura (Kalu Ganga) | 2.15 | 🟢 Normal | -0.011 |  |
| 2026-06-09 14:25:41 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.018 |  |
| 2026-06-09 14:03:48 | Peradeniya (Mahaweli Ganga) | 2.03 | 🟢 Normal | -0.020 |  |
| 2026-06-09 14:02:51 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | -0.020 |  |
| 2026-06-09 14:16:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.00 | 🟢 Normal | -0.025 |  |
| 2026-06-09 14:05:10 | Baddegama (Gin Ganga) | 2.18 | 🟢 Normal | -0.028 |  |
| 2026-06-09 14:04:44 | Hanwella (Kelani Ganga) | 3.27 | 🟢 Normal | -0.029 |  |
| 2026-06-09 14:02:21 | Ellagawa (Kalu Ganga) | 6.17 | 🟢 Normal | -0.029 |  |
| 2026-06-09 14:03:19 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | -0.031 |  |
| 2026-06-09 14:01:35 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | -0.034 |  |
| 2026-06-09 14:03:32 | Glencourse (Kelani Ganga) | 11.13 | 🟢 Normal | -0.039 |  |
| 2026-06-09 14:02:18 | Putupaula (Kalu Ganga) | 1.26 | 🟢 Normal | -0.040 |  |
| 2026-06-09 14:07:52 | Nagalagam Street (Kelani Ganga) | 0.59 | 🟢 Normal | -0.042 |  |
| 2026-06-09 14:02:02 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | -0.225 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)